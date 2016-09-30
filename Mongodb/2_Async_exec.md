#### Problem!! This code not working ####
Can not execute a insert base on a query:
```javascript
   Table1.find({}).exec(function(err,results){
       results.forEach(r=>{
          let xx = new Table2({...});
          xx.save();
       })
   })
```

Seems like promise is not work as this, the async operation is not executed
```javascript
   Table1.find({}).exec().then(xx=>xx.save(function(){}))
```

#### sadly, both of them works, I failed because I add mongoose.connection.close() at the end of the program ####
#### which will cause the aysnc operations can not connect to mongodb ####
