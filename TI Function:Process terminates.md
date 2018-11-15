#ItemReject
  報錯:O
  
  範例:
  If (vCountry @='taipei');
    ItemReject('來源不能有' | vCountry);
  Endif;
  
  說明:
  略過該筆資料，繼續判向下執行，慣用於調整錯誤訊息的內容。
  
#ItemSkip
  報錯:X

  範例:
  If (vCountry @='taipei');
    ItemSkip;
  Endif;
  
  說明:
  略過該筆資料，繼續判斷下一筆data，慣用於Data tab。
  
#ProcessBreak
  報錯:X
  
#ProcessError
  報錯:O
  
#ProcessQuit
  報錯:O
