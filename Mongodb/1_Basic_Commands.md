mongodb

linux path: /etc/mongd.conf
linux start: systemctl start mongodb
linux status: systemctl status mongodb

start db: mongod -config mongod.conf
         mongod -f conf/mongod.conf
connect db: mongo 127.0.0.1:12345/test
binary dir: /usr/local/Cellar/mongodb/3.0.3/bin
close db: use admin
         db.shutdownServer()
注意正确的退出方式！！！
show dbs 
use db_name

*insert (集合+json)
	db.imooc_collection.insert({x:1})
	for(i=4;i<=100;i++) db.imooc_collection.insert({x:i})

*query (find,count,skip.limit,sort)

	db.imooc_collection.find()

	db.imooc_collection.find({x:2})

	count => db.imooc_collection.find().count()

	db.imooc_collection.find().skip(3).limit(2).sort({x:1})

*update ($set操作符->部分更新) (第三个参数为true,不存在则insert) 

	db.imooc_collection.update({x:1},{x:999})

	db.imooc_collection.update({z:100},{$set:{y:99}})

	db.imooc_collection.update({y:100},{y:999},true)

	db.imooc_collection.update({c:1},{$set:{c:2}},false,true)	

	如上，multi-update，第四个参数设置为true, 且必须加上set操作符

*remove 不可不给参数

	db.imooc_collection.remove({c:2})

	db.imooc_collection.drop()



*index

	1.查看表索引 db.imooc_collection.getIndexes()

	2.建立索引 db.imooc_collection.ensureIndex({x:1})

	3.多键索引, 对于有的key有的value为数组的

	4.复合索引, 查询条件不止一个

		db.imooc_2.ensureIndex({x:1,y:1})

	5.TTL索引（过期索引）定时清除数据

		db.imooc_2.ensureIndex({time:1},{expireAfterSeconds:30})



*export a collection into a JSON file

mongoexport -h localhost:12345 -d blog_dev -c logs -o logs.json
