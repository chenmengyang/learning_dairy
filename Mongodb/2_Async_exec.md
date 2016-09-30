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
