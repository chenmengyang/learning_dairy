##### 1. Common UI #####
* TextView
  * android:gravity 指定对齐方式
    * center, top, bottom, left, right
    * center = center_vertical|center_horizontal
  * android:textSize 字体大小
  * android:textColor 字体颜色

* button
  * b = (Button) findViewById(R.id.button)
  * b.setOnClickListener(new OnClickListener(){ public void onClick(View v){} });

* EditText
  * android:hint = "you can put hint text here"
  * android:maxLines = "2"
  * e.getText().toString()

* ImageView
  * imageView = (ImageView) findViewById(R.id.image_view);
  * imageView.setImageResource(R.drawable.pic_name);

* ProgressBar
  * android:visibility 所有控件都有该属性 (visible, invisible, gone)
  * ProgressBar.setVisibility(View.GONE);
  * 有多种样式，默认为圆形

* AlertDialog
  * AlertDialog.Builder dialog = new AlertDialog.Builder(MainActivity.this);
  * dialog.setPositiveButton();
  * dialog.setNegativeButton();

* ProgressDialog
  * setTitle()
  * setMessage()
  * setCancelable(true); // then it can be quit using back key.
  * setProgressStyle();

##### 2. 4 types of basic layout UI#####
* LinearLayout
  * android:orientation = "vertical"|"horizontal"
  * android:layout_gravity
    * top
    * center_vertical
    * bottom
  * android:layout_weight

* RelativeLayout
  * android:layout_centerInParent="true"
    * android:layout_alignParentLeft
    * android:layout_alignParentRight
    * android:layout_alignParentTop
    * android:layout_alignParentBottom
  * android:layout_above="@+id/button3"
    * android:layout_toLeftOf
    * android:layout_toRightOf
    * android:layout_below
  * 边缘对其
    * android:layout_alignLeft
    * android:layout_alignRight
    * android:layout_alignTop
    * android:layout_alignBottom

* FrameLayout

* TableLayout
  * android:stretchColumns="1"
  * android:layout_span = "2"

##### 3. Custom UI #####
  * Include Layout
    * <include layout="@layout/filename"
  * Create Custom UI
    * public class TitleLayout extends LinearLayout
    * LayoutInflater.from(context).inflate(title,this)
    * button1.setOnClickListener(new OnClickListener(){ public void onClick(){......}});

##### 4. ListView #####
*One of the most common UI in android*
  * listview.setAdapter(adapter);
  * ArrayAdapter<T>
  * override getView() method 需加在布局和数据
   * getView(int position,View convertView,ViewGroup parent)
   * T t1 = getItem(position)
   * convertView is 布局缓存, is can be used to improve efficiency
   * View.setTag() + View.getTag() => 存储数据+取出数据, 进一步优化，ListView数据缓存
  * click
   * ListView.setOnItemClickListener(new OnItemClickListener(){ public void onItemClick()})
   * position 定位点击的是哪个子项
  * sizes
    * px and pt are old-fashion
    * sp and dp are better choices for fonts and UIs
