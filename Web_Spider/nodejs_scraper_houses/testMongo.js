var MongoClient = require('mongodb').MongoClient;

var uri = "mongodb://martti:chen123@cluster0-shard-00-00-squue.mongodb.net:27017,cluster0-shard-00-01-squue.mongodb.net:27017,cluster0-shard-00-02-squue.mongodb.net:27017/houses?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin";
MongoClient.connect(uri, function(err, db) {
  if(err)
  {
    console.log("err:"+err);
  }
  else
  {
    console.log("ok");
    let obj = {"houseId":"7751634",
               "img":"http://d3ls91xgksobn.cloudfront.net:80/x114/etuovimedia/images/property/import/555/730555/0e76b9541118d347871c0e0e51d244c4/503c17998c12dbf393c4ed167b76b3e8/ORIGINAL.jpeg",
               "addr":{"street":"Vahverokatu 23","city":"Taka-Lauttala Nokia"},
               "type":{"houseType":"Detached house","housePlan":"6h, k, rt, khh, ph, s, ask.huone, 3x wc, varastot,"},
               "size":"166.0 m²",
               "price":"346000",
               "year":"1998",
               "url":"http://www.etuovi.com/itempage/7751634",
               "tags":["Published 24h","Video"],
               "_id":"591f4558738c6c34779887dd"
            };
    db.collection('tmp').insertOne(obj,function(err,r){
        if(err)
        {
            console.log("err is "+err);
        }
    });
    db.close();
  }
});
