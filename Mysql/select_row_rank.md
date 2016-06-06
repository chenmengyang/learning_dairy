* First define a variable i

  `sql
  select @i:=0
  `

* Second define your select/insert/update sql

  `sql
  select (@i:=@i+1) as rank, t.* from table_name t;
  update table_name t set column_name = (@i:=@i+1);
  `

* Or you can do this in one clause

  `sql
  select (@i:=@i+1) as rank, p.* from people p, (select @i:=0) as it;
  `
