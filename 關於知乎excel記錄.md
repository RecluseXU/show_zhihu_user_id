# 信息  

知乎用戶名與主頁地址均可被用户修改，不確定的信息會造成一些麻煩  
一旦用户改名或者改域名，就又要花时间去核查  

|改知乎用戶路由修改|改知乎用戶名|
|--|--|
|![知乎改路由修改](https://i.loli.net/2020/10/16/eMu3zG8jW95IaHn.png)  |![知乎用戶名修改](https://i.loli.net/2020/10/16/xqTeC5Yf1MmJ3V2.png)  |

我想到了兩種方式可以解決這個問題：  
* 弄一個公司專用賬號，來關注需要收集數據的用戶  
    >天寳說并沒有賬戶，故不可使用此方式  
* 抛棄用戶名與用戶頁域名，用另外的信息來標注每一個用戶  

在對網頁分析的過程中，找到`id`數據信息可以用來唯一確定用戶  

考慮到并非所有人都懂程序，我編寫了一個 `油猴脚本` 來方便的顯示這個信息  

# 脚本概述  

在使用脚本后  
知乎用戶頁(鏈接樣式類似於`https://www.zhihu.com/people/用戶名`)的用戶名下會顯示用戶`ID`信息  
![SHJ_KQ__M4HXVNLJZE7_~FL.png](https://i.loli.net/2020/10/16/GMPCr8igHnBmucJ.png)  

點擊這個信息，能將内容直接複製ID到粘貼面板  
尋找其它地方粘貼即可記錄下這個信息  
![1.gif](https://i.loli.net/2020/10/16/4ebK6Ls9R2NQcJm.gif)  

是一个非常简单的脚本  

# 脚本安裝與使用  
## 安裝  
### Step1 油猴插件安裝  
>安裝過程與安裝普通的瀏覽器插件無異  
>若是已經知道如何安裝瀏覽器插件，可以直接尋找油猴來安裝  

如果不知道如何安裝，我收集了一些安裝的方法，可以對應查看  
* 360瀏覽器  
[B站教程](https://www.bilibili.com/read/cv6423309/)  
* Chrome  
[谷歌應用商店](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?utm_source=chrome-ntp-icon)(需要梯子)  
* 火狐瀏覽器  
[火狐應用商店](https://addons.mozilla.org/zh-CN/firefox/addon/tampermonkey/)  


### Step2 安裝顯示知乎用戶ID脚本  
#### 訪問 https://greasyfork.org/zh-CN/scripts/413419-%E7%9F%A5%E4%B9%8E%E7%94%A8%E6%88%B6%E9%A0%81%E5%B1%95%E7%A4%BA%E7%94%A8%E6%88%B6id  
點擊安裝脚本（這裏我已經安裝，所以有些不同）
![點擊安裝](https://i.loli.net/2020/10/16/wYAvnkR91biJxN3.png)  

#### 點擊安裝  
![](https://i.loli.net/2020/10/16/fv7EcTglO8qHwPt.png)  
如此一來就安裝完成了  

## 使用  
### 脚本管理頁  
![Q`F_UQK6B8DP80BNCXEY5T4.png](https://i.loli.net/2020/10/16/k53nsJ7wD1jdoXO.png)
你可以在油猴脚本管理頁面看到它  
若脚本是尚未啓動，則點擊啓動即可  

### 訪問一個知乎用戶页来驗證效果  
比如说：https://www.zhihu.com/people/hx202047  

![](https://i.loli.net/2020/10/16/GMPCr8igHnBmucJ.png)  
點擊即可複製ID，并且此按鈕的樣貌會改變  

這個id應該被記錄到excel中，如果希望使用excel來記錄  


<br><br><br><br><br><br>


# 其它优秀脚本  

实际上，你可以在 https://greasyfork.org/zh-CN/scripts?q=&sort=total_installs 获取到非常多优秀的脚本  
![1.gif](https://i.loli.net/2020/10/16/AlMpB3oqITSz5fb.gif)

比如 `百度重定向`，`視頻網站去廣告`，`解除網站複製限制`，`電商網站比價` 之類的  


## AC百度重定向
在工作之外，推荐一个[AC百度重定向](https://greasyfork.org/zh-CN/scripts/14178-ac-baidu-%E9%87%8D%E5%AE%9A%E5%90%91%E4%BC%98%E5%8C%96%E7%99%BE%E5%BA%A6%E6%90%9C%E7%8B%97%E8%B0%B7%E6%AD%8C%E5%BF%85%E5%BA%94%E6%90%9C%E7%B4%A2-favicon-%E5%8F%8C%E5%88%97)脚本  

|原本|AC脚本|
|--|--|
| ![](https://i.loli.net/2020/10/16/M9frITbR67y4oKG.png) | ![](https://i.loli.net/2020/10/16/83deAOiWUJjTtFY.png) |

顯示位置，樣式均可以自己定義    