# ItemReject

  ```python
    If (vCountry @='taipei');
      ItemReject( '來源不能有' | vCountry );
    Endif;
  ```
  * 程序失敗
  * 略過該筆資料，繼續向下一筆執行，最後顯示錯誤，慣用於調整錯誤訊息的內容。
  
  
# ItemSkip

  ```python
  If (vCountry @='taipei');
    ItemSkip;
  Endif;
  ```
  * 程序成功
  * 略過該筆資料，繼續向下一筆執行，慣用於Data tab。
  * 在Prolog使用會跳至Data tab。
  
  * Sub Ti中請勿放在Prolog及Epilog，否則會程序失敗。
  
# ProcessBreak

  ```python
  If (vCountry @='taipei');
    ProcessBreak;
  Endif;
  ```
  * 程序成功
  * 直接跳至結尾，慣用於來源有誤，可搭配*AsciiOutput*記錄錯誤內容。  
  
  
# ProcessError

  ```python
  If (vCountry @='taipei');
    ProcessError;
  Endif;
  ```
  * 程序失敗
  * 直接終止TI並產生TM1ProcessError.txt。 
  
  
# ProcessQuit

  ```python
  If (vCountry @='taipei');
    ProcessQuit;
  Endif;
  ```
  * 程序失敗
  * 直接終止TI*不*產生TM1ProcessError.txt。 
