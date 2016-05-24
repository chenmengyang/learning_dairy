##### 1. Activity #####
* create java file FirstActivity.java under java folder
* create layout folder and file under src, first_layout.xml
* register the activity at manifest.xml, set it as main activity and
* use setContentView to add a new layout for that activity
* add some action to the button, show the Toast
   * use getViewById to get the button, convert to Button object
   * use button.setOnClickListener() to add action to the button
   * Toast.maketext(this,"...",short).show()

* cannot find the menu key on the virtual machine phone, target >= 15....
* finish() method in activity can destory an activity


##### 2. Intent #####
* Explicit intent, define an intent object at FirstActivity.java's onClick method, and use startActivity to start this ...
  * The constructor has two parameters
  * Intent(FirstActivity.this, SecondActivity.class)
* Implicit intend, define the action and category at manifest.xml
  * follow the **action** and **category**
  * The constructor has one parameter
  * Intent("The action string in manifest")
  * intend.addCategory("category string in manifest")
  * can even start other processes, e.g. open a web browser:
    * 内置动作 ＋ 协议
    * Intent intent = new Intent(Intent.ACTION_VIEW);
    * intent.setData(Uri.parse("http://www.baidu.com"));
  * except the http protocol, it can also used to open many other protocols like geo, tel
    * 内置动作 ＋ 协议
    * Intent intent = new Intent(Intent.ACTION_DIAL);
    * intent.setData(Uri.parse("tel:10086"));
* passing data
  * putExtra(string,string)
    * intent.putExtra("extra_data","Hello Second Act!");
  * getIntent() + getStringExtra()
    * Intent intent = getIntent();
    * String data = intent.getStringExtra("extra_data");
* passing data back to last activity
  * startActivityForResult(intent,1);
  * intent.putExtra(a,b); setResult(RESULT_OK, intent);
  * onActivityResult(int requestCode,int resultCode,Intent data)
  * onBackPressed()

##### 3. Activity Lifecycle#####
* A stack for storing activities (LIFO)
* 7 Lifecycle
  * onCreate()
  * onStart()
  * onResume()
  * onPause()
  * onStop()
  * onDestroy()
  * onRestart()
* onSaveInstanceState()
  * Bundle.putString
  * Bundle.getString

##### 4. Activity StartMode#####
* standard
* singleTop
* singleTask
* **singleInstance?** put *this or next* instance in a new stack?

##### 5. Activity Best Implementation#####
* Define a baseActivity class, all the activity will inhere this class. In which onCreate will show the current instance
* Define a ActivityCollector class, with an ArrayList inside which can collect activities
  * quit function can be defined as clear all the activities in the list.
* define actionStart() function in each sub activities
