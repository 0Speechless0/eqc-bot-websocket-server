### 環境需求
1. python11 以上
2. virtualenv ，安裝完python 後執行
```cmd
pip install virtualenv 
```

--------------------

### 套件安裝(可避免套件衝突)
1.
```cmd
virtualenv .venv
```
2.
for windows :
```cmd
.\.venv\Scripts\activate
```
for linux
```cmd
source .venv/bin/activate
```
3. (注意指令位置 在 `./.venv/bin/activate`)
```cmd
pip install -r requirements.txt
```

--------------------

### 套件安裝(全域)

```cmd
pip install -r requirements.txt
```

--------------------

### 啟動伺服器
```cmd
python start.py
```

#### 有兩個伺服器分別為 : 
| port      | 說明 |
| --------- | :-----|
| 5000       | 用於串接line channel，必須到以下連結註冊網址: https://account.line.biz/login?redirectUri=https%3A%2F%2Fdevelopers.line.biz%2Fconsole%2Fchannel%2Fnew%3Ftype%3Dmessaging-api，請先登入 |
| 5001       | websocket 伺服器|


5001 路由說明  :
| path      | 說明 |
| --------- | :---------------------------------|
| /chat | websocket訊息測試網頁 |
| / | websocket位址 |

### 發佈檔案(位置:./dist)
``` cmd
pyinstaller _Main.spec
```
### 部屬 (windows 10 + IIS)
1. 安裝必要程式 :  
   1. URL ReWrite  
   2. Application Request Routing

   

   [https://blog.alanwei.com/blog/2021/04/11/iis-reverse-proxy/](https://blog.alanwei.com/blog/2021/04/11/iis-reverse-proxy/)

2. IIS 設定(詳情於1.的連結) :  
   1. 左鍵點介面主機名稱
      
      ![image](https://github.com/user-attachments/assets/cc484103-969d-47d6-83fd-7213ea02e2c8)
        
   3. 中間點ARR 設置 (Application Request Routing Cache)  
   4. 點擊 Server Proxy Settings  
   5. 勾選 Enable Proxy  
        
3. 網站上建立反向代理路由節點(詳情於1.的連結) :  
     
   1. 點擊EQC系統網站名稱，建立子應用程式 命名 websocket，路徑選擇任一目錄作為建立反向代理config位置  
        
   2. 左鍵點擊EQC系統網站名稱，中間視窗中找到URL Write  
   3. 點擊 URL Write，出現右視窗，點新增規則  
   4. 視窗中點 “反向 Proxy ”  
   5. 依照圖片設定
  
      
      ![image](https://github.com/user-attachments/assets/9cd8b0bd-9641-4e66-8ab3-d674d7dff2cc)

     
     
4. 部屬訊息伺服器 

   1. 啟動服務 ，Main.exe

5. 伺服器自動開機設定  
   1. 建立Main.exe 捷徑  
        
   2. 鍵盤 windows \+ R 或搜尋  " 執行 "，在出現的視窗輸入 : **shell:Startup**
      
    ![image](https://github.com/user-attachments/assets/b9f09218-3b3f-46b1-8b22-c4ce4f5f1dde)


   4. 按確定後，出現檔案總管，將剛剛建立的捷徑移到檔案總管中 :  
 
