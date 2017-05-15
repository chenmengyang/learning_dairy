let http = require('http');
let cheerio = require('cheerio');
let baseUrl = 'http://www.etuovi.com/homes-for-sale?rd=50&page=';

let pageArr = [1,2,3,4,5,6,7,8,9,10];

let idArr = [];
let getId = function(currentPage)
{
    http.get(currentPage, (res) => {
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
        try {
        //   let parsedData = JSON.parse(rawData);
        let htmlCode = rawData;
        let $ = cheerio.load(htmlCode);
        // let arr = [];
        let items = $('section.results.list>ol>li') // .map(function(i,el){arr.push($(this).attr('id')); return $(this).attr('id')});//map((i,el)=>{return $(this).attr('id')});
                    .map(function(i,el){
                        idArr.push($(this).attr('id'));
                        return 1;
                    });
        console.log(idArr);
        //   console.log(rawData);
        } catch (e) {
        console.log(e.message);
        }
    });
    }).on('error', (e) => {
    console.log(`Got error: ${e.message}`);
    });
}

let getFuncArr = function(func,baseUrl,pageArr)
{
    let arr = [];
    pageArr.forEach((e)=>{
        arr.push(func(baseUrl+e));
    });
    return arr;
}

getFuncArr(getId,baseUrl,pageArr);