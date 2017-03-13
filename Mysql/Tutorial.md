```sql
-- This is the note of reading the official tutorial guide mysql-tutorial-5.7

-- display list of options for command line login....
1. mysql --help

-- connect to mysql
2. mysql -h hostname -u cmy -p
-- if server is installed on local computer, don't need -h option
   mysql -u cmy
   mysql -u root (sometimes we need root privilige to do things, for example:)
   CREATE USER guest@localhost IDENTIFIED BY 'guest123'; (create a new user)
   GRANT ALL PRIVILEGES ON *.* TO guest@localhost; (grant priv....)

-- some simple queries
-- return the version of database, current_date. notice unlike oracle, mysql not need dual table.
3. select version(),current_date;
   select 1+1;
   select sin(pi()/2),cos(pi();
   select user();  -- this clause will show you the current username of database

-- some privilege problems, root cannot access problems solved by the belowed link
-- http://stackoverflow.com/questions/8541115/mysql-password-issues-mac-os-x-lion
4. basic operation on database, create db and view data
   show databases; -- find out which dbs currently on the server
   USE test;       -- change/connect to database test
   show tables;    -- list all the tables in this database;
   grant all on dbname.table_name to username@hostname;
   create database moviedb; -- do it login using root user, if you have privilege problem, chech that link above
   grant all on moviedb.* to cmy;                      -- maybe need to execute this command to ensure privilege
   grant all privileges on moviedb.* to cmy@localhost; -- @localhost is very fucking important, unless failed to connect
   grant usage on *.* to cmy@localhost;                -- the same with last
   create table pet(name varchar(20),owner varchar(20),species varchar(20),sex char(1),birth date,death date);
   describe pet;
   insert into pet values('xx','xx','xx','f','1999-12-12','2222-12-12'); --insert
   -- insert is easy, but how to load a file into table???
   -- when using load command, the seperator by default is tab, but you can sepcify a new one, and on OS the terminator should be assign as '\r'
   show warnings; -- when I load the file, some warnings but not showed on the screen, can use this command.
   load data local infile '/Users/cmy/Documents/database/pet.txt' into table pet lines terminated by '\r';
   update pet set birth='1989-02-03' where name='Brower';
   
   --also support distinct select 
   select distinct owner from pet;
   -- in, not in, order by desc/asc are the same with oracle
   -- date calculation, timestampdiff(year,date1,date2)
   select name,curdate(),birth,timestampdiff(year,curdate(),birth) as age from pet;
   -- month(date1), year(date1), dayofmonth(date1)
   -- like is the same
   select * from pet where name like 'c%'; -- begin with c
   select * from pet where name like '%c'; -- end with
   select * from pet where name like '%c%'; -- contains a c
   select * from pet where name like '_____' -- name contains 5 characters
   -- support regexp match
   select * from pet where name regexp '^c';  -- begin with
   select * from pet where name regexp 'fy$'; -- end with
   select * from pet where name regexp '^.....$'; -- 5 characters
   select * from pet where name regexp '^.{5}$';  -- 5 characters
   -- inner join (what's the difference between these two:)
   select pet.name, event.remark from pet inner join event on pet.name = event.name;
   select pet.name, event.remark from pet,event where pet.name = event.name;
   
5.
6. Batch mode? to run a sql script?
   -- on command line, login server and add < filename
   mysql test < script.sql
   mysql -u root -pxxxxx < script1.sql
   -- can catch output
   mysql test < script.sql >output.txt

7. Common queries
   -- max(column_name) group by ...
   -- select the row with the max price value, it is an popular interview question?
   -- these two are the same, but which one is better?
   select article, dealer, price from shop where price = (select max(price) from shop);
   SELECT article, dealer, price from shop s1 where not exists(select 1 from shop s2 where s2.price>s1.price);
   -- another solution using left join ***** important
   -- because left join makes s1 as base table, so all records with s1 will be select
   -- even there is no corresponding record on s2 which has a high price, and we want that record.
   select s1.article, s1.dealer, s1.price from shop s1 left join shop s2 on s1.price<s2.price where s2.price is null;
   -- another solution using order by + limit
   select article, dealer, price from shop order by price desc limit 1;
   
   -- these three are equal, left join maybe better! import
   select s1.article, s1.dealer, s1.price from shop s1 left join shop s2 on s1.price<s2.price and s1.article=s2.article where s2.price is null;
   select s1.article, s1.dealer, s1.price from shop s1 where s1.price =(select max(s2.price) from shop s2 where s2.article=s1.article);
   select s1.article, s1.dealer, s1.price from shop s1 join (select article,max(price) price from shop group by article) s2 on s1.price=s2.price and s1.article=s2.article;
   
   -- variables in mysql, in oracle 'select xx into vv from table_name'
   select @min_price:=min(price) from shop;
   select * from shop where price=@min_price;
   
   -- union, union all the same
   
   -- AUTO_INCREMENT as a column opiton
   -- create table test1(id int AUTO_INCREMENT,...);
   ```
