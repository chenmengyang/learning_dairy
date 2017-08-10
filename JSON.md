##### 1. JSON is an easier-to-use alternative to XML. #####

##### 2. JSON use javascript syntax #####
```javascript
<!DOCTYPE html>
<html>
<body>

<h2>JSON Object Creation in JavaScript</h2>

<p id="demo"></p>

<script>
var text = '{"name":"John Johnson","street":"Oslo West 16","phone":"555 1234567"}';

var obj = JSON.parse(text);

document.getElementById("demo").innerHTML =
obj.name + "<br>" +
obj.street + "<br>" +
obj.phone;
</script>

</body>
</html>
```

##### 3. Much like XML, But #####

 * XML has to be parsed with an XML parser, JSON can be parsed by a standard JavaScript function.

##### 4. Syntax #####
 * rules
   * JSON data in key/value pairs
     * "firstName":"John"
   
   * JSON data is seperated by comma
   * Curly braces contains object
     * {"firstName":"John", "lastName":"Doe"}
   
   * Square brackets contains array
     * JSON array can contain multiple objects
     * E.g.
     ```JSON
       "employees":[
      {"firstName":"John", "lastName":"Doe"}, 
      {"firstName":"Anna", "lastName":"Smith"}, 
      {"firstName":"Peter","lastName":"Jones"}
      ]
     ```
  * Using javascript syntax, an array of objects
  ```javascript
  var employees = [{"firstname":"Men","lastname":"Young"},{"firstname":"Men","lastname":"Old"},{"firstname":"Men","lastname":"Suck"}];
  
  employees[0].firstname
  employees[0]["firstname"]
  ```
  
##### 5. Object from string #####
```javascript
var text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}';

var obj = JSON.parse();
```

##### 6. HttpRequest #####

xmlhttp

```html
<!DOCTYPE html>
<html>

<head>
<style>
h1 {
    border-bottom: 3px solid #cc9900;
    color: #996600;
    font-size: 30px;
}
table, th , td  {
    border: 1px solid grey;
    border-collapse: collapse;
    padding: 5px;
}
table tr:nth-child(odd)	{
    background-color: #f1f1f1;
}
table tr:nth-child(even) {
    background-color: #ffffff;
}
</style>
</head>

<body>

<h1>Customers</h1>
<div id="id01"></div>

<script>
var xmlhttp = new XMLHttpRequest();
var url = "http://www.w3schools.com/website/Customers_MYSQL.php";

xmlhttp.onreadystatechange=function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        myFunction(xmlhttp.responseText);
    }
}
xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(response) {
    var arr = JSON.parse(response);
    var i;
    var out = "<table>";

    for(i = 0; i < arr.length; i++) {
        out += "<tr><td>" + 
        arr[i].Name +
        "</td><td>" +
        arr[i].City +
        "</td><td>" +
        arr[i].Country +
        "</td></tr>";
    }
    out += "</table>";
    document.getElementById("id01").innerHTML = out;
}
</script>

</body>
</html>

```

##### 7. JSON FILE #####
```html
<div id="001"> </div>

<script>
function myFunction(arr)
{
  var out="";
  var i;
  for(i=0;i<=arr.length();i++)
  {
    out += '<a href="' + arr[i].url + '">' + arr[i].display + '</a><br>';
  }
}
</script>

<script src="xxx.js"> </script>
```

This is the xxx.js:
```javascript
myFunction([
{
"display": "JavaScript Tutorial",
"url": "http://www.w3schools.com/js/default.asp"
},
{
"display": "HTML Tutorial",
"url": "http://www.w3schools.com/html/default.asp"
},
{
"display": "CSS Tutorial",
"url": "http://www.w3schools.com/css/default.asp"
}
]);
```
