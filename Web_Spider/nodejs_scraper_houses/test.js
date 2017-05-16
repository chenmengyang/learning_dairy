let http = require('http');
let url = 'http://www.etuovi.com/homes-for-sale?rd=50&page=1';
let cheerio = require('cheerio');

http.get(url, (res) => {
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
            let items = $('section.results.list>ol>li') // .map(function(i,el){arr.push($(this).attr('id')); return $(this).attr('id')});//map((i,el)=>{return $(this).attr('id')});
                        .map(function(i,el){
                            arr.push($(this).attr('id'));
                            return 1;
                        });
            console.log(" !done! size is ssss");
            
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