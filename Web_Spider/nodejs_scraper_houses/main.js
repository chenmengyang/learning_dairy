let http = require('http');
let cheerio = require('cheerio');
let rd=process.argv[2]?process.argv[2]:10;
let baseUrl = `http://www.etuovi.com/homes-for-sale?locale=en&rd=${rd}&page=`;
let async = require('async');
let pageArr = [1,2,3,4,5,6,7,8,9,10];
// let pageArr = [0];

// first check how many houses we got from website


// let idArr = [];
// let getId = function(callback=false,currentPage)
// {
//     http.get(currentPage, (res) => {
//         const statusCode = res.statusCode;
//         let error;
//         if (statusCode !== 200)
//         {
//             error = new Error(`Request Failed.\n` + `Status Code: ${statusCode}`);
//         }
//         if (error) {
//             console.log(error.message);
//             // consume response data to free up memory
//             res.resume();
//             return;
//         }

//         res.setEncoding('utf8');
//         let rawData = '';
//         res.on('data', (chunk) => rawData += chunk);
//         res.on('end', () => {
//             try
//             {
//                 let htmlCode = rawData;
//                 let $ = cheerio.load(htmlCode);
//                 let arr = [];
//                 let items = $('section.results.list>ol>li') // .map(function(i,el){arr.push($(this).attr('id')); return $(this).attr('id')});//map((i,el)=>{return $(this).attr('id')});
//                             .map(function(i,el){
//                                 arr.push($(this).attr('id'));
//                                 return 1;
//                             });
//                 console.log(" !done! ");
//                 callback(null,arr);
//                 //   console.log(rawData);
//             }
//             catch (e)
//             {
//                 console.log(e.message);
//             }
//         });
//     })
//     .on('error', (e) => {
//         console.log(`Got error: ${e.message}`);
//     });
// }

let getFuncArr = function(baseUrl,pageArr)
{
    let arr = [];
    pageArr.forEach((e)=>{
        // arr.push(function(){return func(callback,baseUrl+e);});
        // arr.push(func(callback,baseUrl+e));
        let cPage = baseUrl+e;
        arr.push(
            function(callback)
            {
                console.log("cPage is "+cPage);
                http.get(cPage, (res) => {
                    const statusCode = res.statusCode;
                    let error;
                    if (statusCode !== 200)
                    {
                        error = new Error(`Request Failed.\n` + `Status Code: ${statusCode}`);
                    }
                    if (error) {
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
                                            // arr.push($(this).attr('id'));
                                            arr.push(1);
                                            // parse the html page using cheerio, cool man!
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
                                            let tags = [];
                                            $(this).find('ul.tools li>em[title]').map(function(i,el){
                                                if(typeof $(this).text() === "string")
                                                {
                                                    tags.push($(this).text());
                                                }
                                            });
                                            console.log($(this).attr('id') + ' tags is '+tags);
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

//
// async.parallel(getFuncArr(getId,baseUrl,pageArr),
//     ()=>console.log('hello')
// );

let sArr = [1,3,5];

let func10 = function(callback,p2){
    callback(null,p2);
}

let getFuncArr1 = function(sArr)
{
    let arr = [];
    sArr.forEach((e)=>{
        arr.push(()=>{return func10(callback,1001);});
        // function(callback,p2){callback(null,872);}
    });
    return arr;
}

// var xxx = getFuncArr(baseUrl,pageArr);
// console.log("xxx length is "+xxx.length);

// async.parallelLimit(getFuncArr(baseUrl,pageArr), 4,function(err,results){
//     console.log(results.length);
// });

async.series([
    function(){console.log('hello you !!!!! love me');},
    async.parallelLimit(getFuncArr(baseUrl,pageArr), 4,function(err,results){
    console.log(results.length);
    })
],function(err, results) {});

// async.parallel([
//     function(callback){callback(null,1);},
//     function(callback){callback(null,1);},
//     function(callback){callback(null,1);}
//  ], function(err,results){console.log(results);}
// );

// async.parallel(
//     getFuncArr1(sArr),
// // [
// //     function(callback) {
// //         setTimeout(function() {
// //             callback(null, 'one');
// //         }, 2000);
// //     },
// //     function(callback) {
// //         setTimeout(function() {
// //             callback(null, 'two');
// //         }, 100);
// //     }
// // ],
// // optional callback
// function(err, results) {
//     console.log(results);
// });