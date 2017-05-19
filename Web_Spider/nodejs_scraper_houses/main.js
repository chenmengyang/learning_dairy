let http = require('http');
var MongoClient = require('mongodb').MongoClient;
var uri = "mongodb://martti:chen123@cluster0-shard-00-00-squue.mongodb.net:27017,cluster0-shard-00-01-squue.mongodb.net:27017,cluster0-shard-00-02-squue.mongodb.net:27017/houses?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin";
let cheerio = require('cheerio');
let rd=process.argv[2]?process.argv[2]:10;
let homePage = 'http://www.etuovi.com/?locale=en';
let baseUrl = `http://www.etuovi.com/homes-for-sale?locale=en&rd=${rd}&page=`;
let async = require('async');
let pageCount = 10;
// let pageArr = [0];

MongoClient.connect(uri, function(err, db) {
  if(!err)
  {
      // define a function which can return a list of functions
      let getFuncArr = function(baseUrl,pageArr)
      {
          let arr = [];
          pageArr.forEach((e)=>{
              let cPage = baseUrl+e;
              arr.push(
                  function(callback)
                  {
                      http.get(cPage, (res) => {
                          const statusCode = res.statusCode;
                          let error;
                          if (statusCode !== 200)
                          {
                              error = new Error(`Request Failed.\n` + `Status Code: ${statusCode}`);
                          }
                          if (error)
                          {
                              console.log(error.message);
                              // consume response data to free up memory
                              res.resume();
                              return;
                          }
                          res.setEncoding('utf8');
                          let rawData = '';
                          res.on('data', (chunk) => rawData += chunk);
                          res.on('end', () => {
                              try
                              {
                                  let htmlCode = rawData;
                                  let $ = cheerio.load(htmlCode);
                                  let arr = [];
                                  let items = $('section.results.list>ol>li.residental') // .map(function(i,el){arr.push($(this).attr('id')); return $(this).attr('id')});//map((i,el)=>{return $(this).attr('id')});
                                              .map(function(i,el){
                                                  arr.push(1);
                                                  // parse the html page using cheerio, cool man!
                                                  let houseId = $(this).attr('id');
                                                  let img = $(this).find('a.thumb img').attr('src')?$(this).find('a.thumb img').attr('src'):'';
                                                  let addr = {
                                                      "street":$(this).find('div.address strong').text(),
                                                      "city":$(this).find('div.address span').text()
                                                  };
                                                  let type = {
                                                      "houseType":$(this).find('div.type label').text(),
                                                      "housePlan":$(this).find('div.type span').text()
                                                  };
                                                  let size = $(this).find('div.size span').text();
                                                  let price = $(this).find('div.price span').text().replace(/[^0-9]/g,'');
                                                  let year = $(this).find('div.year span').text();
                                                  let url = 'http://www.etuovi.com/itempage/'+houseId;
                                                  let tags = [];
                                                  $(this).find('ul.tools li>em[title]').map(function(i,el){
                                                      if(typeof $(this).text() === "string")
                                                      {
                                                          tags.push($(this).text());
                                                      }
                                                  });
                                                //   console.log($(this).attr('id') + ' tags is '+tags);
                                                  let obj = {houseId,img,addr,type,size,price,year,url,tags};
                                                //   console.log("obj is "+JSON.stringify(obj));
                                                  db.collection('eduovi_houses').insertOne(obj,function(err, r){
                                                    if(err)
                                                    {
                                                        console.log("failed to insert into mongodb, err "+err + "  obj is "+JSON.stringify(obj));
                                                    }
                                                  });
                                                  return 1;
                                              });
                                  //console.log(currentPage + " !done! size is " + idArr.length);
                                  console.log('length of arr is '+arr.length);
                                  callback(null,arr);
                                  //   console.log(rawData);
                              }
                              catch (e)
                              {
                                  console.log(e.message);
                              }
                          });
                      })
                      .on('error', (e) => {
                          console.log(`Got error: ${e.message}`);
                      });
                  }
              );
          });
          return arr;
      }
      
      async.series([
          // first empty the 
          function(callback) {
              db.collection('eduovi_houses').remove({},function(err,results){
                if(!err)
                {
                    console.log(`collection cleared successful, ${results.n} records removed`);
                }
              });
              callback(null,0);
          },
          // fetch page count, then ,,,
          function(callback) {
              http.get(homePage, (res) => {
                  res.setEncoding('utf8');
                  let rawData = '';
                  res.on('data', (chunk) => rawData += chunk);
                  res.on('end', () => {
                      try
                      {
                          let htmlCode = rawData;
                          let $ = cheerio.load(htmlCode);
                          let count = $('form#searchForm div.submit a.submit em').text().replace(/[^0-9]/g,'');
                          pageCount = Math.round(count/rd);
                          callback(null,1);
                      }
                      catch (e)
                      {
                          console.log(e.message);
                      }
                  });
              });
          }
          ,
          // then run jobs in parallel, set concurrent parameter to 4
          function(callback)
          {
              // console.log('pageCount is '+pageCount);
              let pages = Array.from(Array(pageCount).keys()).map(e=>e+1);
              async.parallelLimit(getFuncArr(baseUrl,pages), 10, function(err,results){
                  callback(null,2);
              });
          }
          ,
          // close the connection to mongo cloud
          function(callback)
          {
            db.close();
            console.log("connection closed");
          }
      ],function(err, results) {console.log(results);});
  }
  else
  {
      console.log("connection to cloud error: "+err);
  }
});