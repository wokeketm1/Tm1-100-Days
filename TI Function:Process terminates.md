# ItemReject
  * 顯示錯誤:O
  ```python
    If (vCountry @='taipei');
      ItemReject( '來源不能有' | vCountry );
    Endif;
  ```
  * 說明:略過該筆資料，繼續向下一筆執行，最後顯示錯誤，慣用於調整錯誤訊息的內容。
  
# ItemSkip
  * 顯示錯誤:X
  ```python
  If (vCountry @='taipei');
    ItemSkip;
  Endif;
  ```
  * 說明:略過該筆資料，繼續向下一筆執行，慣用於Data tab。
  
# ProcessBreak
  * 顯示錯誤:X
  ```python
  If (vCountry @='taipei');
    ProcessBreak;
  Endif;
  ```
  * 說明:略過該筆資料，繼續判斷下一筆data，慣用於Data tab。  
  
# ProcessError
  * 顯示錯誤:O
  ```python
  If (vCountry @='taipei');
    ProcessError;
  Endif;
  ```
  * 說明:略過該筆資料，繼續判斷下一筆data，慣用於Data tab。 
  
# ProcessQuit
  * 顯示錯誤:O
  ```python
  If (vCountry @='taipei');
    ProcessQuit;
  Endif;
  ```
  * 說明:略過該筆資料，繼續判斷下一筆data，慣用於Data tab。
