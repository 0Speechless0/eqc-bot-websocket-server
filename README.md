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
virtualenv .venv
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
