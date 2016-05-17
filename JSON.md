1. JSON is an easier-to-use alternative to XML.

2. JSON use javascript syntax
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
3. Much like XML, But

  * XML has to be parsed with an XML parser, JSON can be parsed by a standard JavaScript function.

4. Syntax
  * rules
    * JSON data in key/value pairs
    
    "firstName":"John"
    
    * JSON data is seperated by comma
    * Curly braces contains object
    * Square brackets contains array
  
