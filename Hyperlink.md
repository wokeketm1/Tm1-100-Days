# Tm1 Web 介面
 * TM1透過Perspective將Excel頁面上傳至伺服器後，End User即可透過類似Excel的頁面查看資料，  
 但是單一的頁面是無法解決商業上難題，我們可透過Excel本身所提供的Hyperlink來達成頁面切換的效果。
 
# 實體檔案路徑
 1. Active Form上傳後會產生實體檔案，路徑如下。
   ```
  \\[Data Path]\}Externals\[Filename]
  ```
 2. 可嘗試在路徑下點開相對應的Excel，效果同在Perspective中開啟。


# Hyperlink 範例
* 當我們得知TM1存放頁面的原理時，只要在Portal上添加HyperLink儲存格即可達成頁面切換的效果。  
  ```
  #Syntax
  Hyperlink(link，friendly_name)
  
  #Example
  Hyperlink(TM1:// [ServerName] /blob/PUBLIC/.\}Externals\ [Filename] ，[friendly_name])
  ```
  
  
  
  
