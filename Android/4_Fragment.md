##### 1. Usage of Fragment #####
  * basic
    * define 2 layout files, left_fragment.xml and right_fragment.xml
    * define 2 new classes extends the base class Fragment
      * override onCreateView method
      * inflater.inflate(R.layout.left_fragment,..,..)
    * add <fragment> in activity_main.xml
      * android:name = "com.example.fragmenttest.LeftFragment"
  * Dynamic Fragment operation
    * create new fragment object (define a new class which extends Fragment)
    * get the FragementManager
    * get the FragmentTransaction
    * replace(current_layout,new_fragment)
    * transaction.commit()
  * Imitate the back stack
    * transaction.addToBackStack(null)
  * Fragments are placed into activity
    * activity can communicate with fragment
      * FragementManager.findFragmentById(R.id.)
