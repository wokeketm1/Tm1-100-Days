# Portal Link
 * TM1透過Perspective將Excel頁面上傳至伺服器，End User即可透過類似Excel的頁面查看資料。
 * 單一的頁面是無法解決商業上難題，這裡我們透過Excel本身所提供的Hyperlink來達成頁面切換的效果。
 
# Entity Path
 1. Active Form上傳後會產生實體檔案，路徑如下。
 2. 直接在路徑下點開相對應的Excel，效果同在Perspective中開啟。
  ```
  \\Data Path\}Externals
  ```

# Hyperlink in Excel
  ```
  #Syntax
  Hyperlink(link，friendly_name)
  
  #Example
  Hyperlink(TM1:// [ServerName] /blob/PUBLIC/.\}Externals\ [Filename] ，[friendly_name])
  ```
  
  
  
  
