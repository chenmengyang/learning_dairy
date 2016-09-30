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
