```mermaid
	graph TB
	A[首頁<br>https://www.zhihu.com/ ]--Step1 302 <br>set_Cookies: _zap, _xsrf, KLBRSID-->B[302頁]--Step2 200<br>del_Cookies:KLBRSID-->C[登錄頁<br>https://www.zhihu.com/signin?next=%2F ]
	
```