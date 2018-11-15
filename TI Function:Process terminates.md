# ItemReject

  ```python
    If (vCountry @='taipei');
      ItemReject( '來源不能有' | vCountry );
    Endif;
  ```
  * 顯示錯誤:O
  * 說明:略過該筆資料，繼續向下一筆執行，最後顯示錯誤，慣用於調整錯誤訊息的內容。
  
  
# ItemSkip

  ```python
  If (vCountry @='taipei');
    ItemSkip;
  Endif;
  ```
  * 顯示錯誤:X
  * 說明:略過該筆資料，繼續向下一筆執行，慣用於Data tab。
  
  
# ProcessBreak

  ```python
  If (vCountry @='taipei');
    ProcessBreak;
  Endif;
  ```
  * 顯示錯誤:X
  * 說明:直接跳至結尾，慣用於來源有誤，搭配**ItemSkip**記錄錯誤內容。  
  
  
# ProcessError

  ```python
  If (vCountry @='taipei');
    ProcessError;
  Endif;
  ```
  * 顯示錯誤:O
  * 說明:直接終止TI並產生Error Log.error。 
  
  
# ProcessQuit

  ```python
  If (vCountry @='taipei');
    ProcessQuit;
  Endif;
  ```
  * 顯示錯誤:O
  * 說明:直接終止TI**不**產生Error Log.error。 
