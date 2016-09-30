#####  HTTP GET #####
* define: sendRequestWithHttpURLConnection()
  ```java
      new Thread(new Runnable(){
                  public void run(){
                         HttpURLConnection connection = null;
                         try{
                            URL url = new URL("http://10.0.2.2:3000/login");
                            connection = (HttpURLConnection) url.openConnection();
                            connection.setRequestMethod("GET");
                            ...
                         }
                         catch(){}
                         finally{}
                         handler.sendMessage(message);
                     }
                }).start()
  ```

* handler ?
  ```java
    private Handler handler = new Handler() {

        public void handleMessage(Message msg)
        {
            switch(msg.what)
            {
                case SHOW_RESPONSE:
                    String response = (String) msg.obj;
                    responseText.setText(response);
            }
        }
    };
```
