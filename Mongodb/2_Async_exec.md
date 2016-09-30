## Problem ##
Can not execute a insert base on a query:
`   Table1.find({}).exec(function(err,results){
       results.forEach(r=>{
          let xx = new Table2({...});
          xx.save();
       })
   })
