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

#####  HTTP POST #####
```java
  //setting
  URL url = new URL("http://10.0.2.2:3000/login");
  connection = (HttpURLConnection) url.openConnection();
  connection.setRequestMethod("POST");
  connection.setConnectTimeout(80000);
  connection.setReadTimeout(80000);
  connection.setUseCaches(false);
  connection.setDoInput(true);
  connection.setDoOutput(true);
  connection.setRequestProperty("Content-Type","application/json");
  
  // sending
  JSONObject jsonParam = new JSONObject();
  jsonParam.put("account","user1");
  jsonParam.put("password","123456");
  DataOutputStream wr = new DataOutputStream(connection.getOutputStream());
  wr.writeBytes(jsonParam.toString());
  wr.flush();
  wr.close();
  
  //get response
  StringBuilder sb = new StringBuilder();
  int HttpResult = connection.getResponseCode();
  if (HttpResult == HttpURLConnection.HTTP_OK)
  {
      BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream(),"utf-8"));
      String line = null;
      while ((line = br.readLine()) != null) {
          sb.append(line + "\n");
      }
      br.close();
      Log.d("response","" + sb.toString());
  }
  
  //debug
  else {
      InputStream in = connection.getErrorStream();
      BufferedReader reader = new BufferedReader(new InputStreamReader(in));
      StringBuilder response = new StringBuilder();
      String line;
      while((line=reader.readLine())!=null)
      {
          response.append(line);
      }
      Log.d("response", response.toString());
  }
```


#####  NodeJS-Express Handle POST from Android #####
* remember to install body-parser!!!
  * npm i body-parser --S
  
