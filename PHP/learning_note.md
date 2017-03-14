## Learning note for PHP ##

### Features?
* Dynamic typing, $var1 = ...
* Weak type, auto conversion
* Case sensitive (except null/NULL and predefined constants)
* Loop types: for+while+do..while+foreach($array as $element){...}
* Associative array -> a loopable hashtable
* Understand form data, POST + GET easily, how about cross domain?
* IO -> fopen + fread + fclose + filesize ..... how to scan a file line by line?
* Parameters are passed by value by default, add & before parameter enable passing by reference
* Dynamic function calls are interesting, how about functional programming in PHP?
* Regular Expression: [a-Z] match all lower and upper letters.
* Mysql a lot of built-in functions can be called directly
* OOP class, $this->, new, $instance->memberFunction(para1...), __constructor(arg1...), __destructor(), extends, by default public (can set to private and protected), abstract class, interface, statice, final function cannot be overridden.
* Functional programming: array_filter (the higher order function), array_filter($array, $func)
