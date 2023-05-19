# Chiakai's 成果展示區

## 精心研發各種小幫手程式 (打包 exe 提供使用)
* ## [AI智慧程式碼識別小幫手](https://github.com/Chiakai-Chang/CodeForensicsOnScene)
  * 為解決現場勘查時，遇到屬「程式開發」相關現場，充斥複雜難懂之各種程式碼，令現場查緝人員難以快速瞭解掌握涉案情形或釐清現場人員所言是否真實之情形。
  * 特別開發此工具，藉由 AI 提供快速分析程式碼並產出報告的功能，協助現場快速掌握可疑程式碼作用、可能違法情形與關鍵資訊擷取。
  * ![](https://chiakai-chang.github.io/tempHTML/img/CFOS.jpg)

* ## [ATM交易資料自動查詢彙整小幫手](https://github.com/Chiakai-Chang/varityTask/tree/main/atmDataWash)
  * 為解決金流分析時，大量金流資料要逐筆查對 ATM 提領位置傷眼又考驗耐心的煩惱，特別受委託開發此小程式協助自動批次比對 ATM 提領地點。
  * ![](https://chiakai-chang.github.io/tempHTML/img/AtmDataWash.jpg)

## 小幫手程式 (Colab 即取即用)
* ## [臉書好友整理神器](https://colab.research.google.com/drive/1JCgq0qmmsAtfuICuyk_CciQVjgSfKZ33?usp=sharing)
   * 請參考教學: [使用指引](https://drive.google.com/file/d/1KI8intBMvUYx2rTMgFi2utGGM6oxEH0i/view)

* ## [大量同格式JSON彙整小幫手](https://colab.research.google.com/drive/1w1ApO_p3zh38ocU6jW5di3LXfeQWA3t6?usp=sharing)
   *  現在的網頁大多都基於 MVC 等架構，除了呈現的網頁以外，背後還會有 API 去存取資料(大多為 JSON 格式)來更新顯示內容。
   *  因為前述 JSON 給的資料往往比網頁上肉眼能看到得「更豐富」，且格式也更容易整理，所以有個小幫手可以幫忙將這些 Json 接收下來，一起轉換成更容易操作的 excel 格式，豈不美哉？

* ## [AWS IP 確認小幫手](https://colab.research.google.com/drive/1T7vX0L2gs9VCNzwzSpvsI84rGTFRXl3R?usp=sharing)
   *  若大家有遇到 ip 是 amazon (亞馬遜) 的，可以使用這個小幫手來確認 IP 是 AWS 的什麼雲端服務
      * 亦可參考 RyanLabs 提供之線上查詢工具：AWS IP Range Checker/Lookup Tool
         * 該工具僅能查詢 IPv4 的資料
   * 本程式係從官方：AWS IP address ranges 下載最新之 IP 資訊 (Json 檔，含 IPv4 與 IPv6) 進行比對，為最即時、最準確之資料

* ## [地址轉經緯度小幫手](https://colab.research.google.com/drive/1BWleXRAN1vM82-k9lz-O78fPMqBZf581?usp=sharing)
  * 借用內政部國土測繪中心「國土測繪圖資服務雲」之電子地圖，查詢任意地址之完整行政區(至村里鄰)及經緯度。 

* ## [UserAgent 解析小幫手](https://colab.research.google.com/drive/1IP1t7yFuIYLnTttwcn_V5fy3XkJASk2d?usp=sharing)
  * 在做 log 分析時，常常都會遇到 UserAgent 這個資料，該資料通常包含了其應用程式類型(瀏覽器)、作業系統、軟體供應商……等等，有時還會包含軟體修訂版本等資訊。
  * 因該字串不容易閱讀，所以特別以小程式幫忙解析重點。

* ## [封包 headers 文字轉 dict 小幫手](https://colab.research.google.com/drive/15auzjfvWt6HICDyKtTDEFfKpoT-TlG7s?usp=sharing)
   * 使用 DevTools 複製找到並複製封包有關 Requests Headers 的文字內容
   * 貼到程式後，即可整理成方便使用的 dict 格式，並自動將 cookie 分離

* ## [文字加解密技術](https://colab.research.google.com/drive/1lq6E8jFDKuXveji5zJmzl7m7hT3o3503?usp=sharing)
   * 整理曾經遇到的文字加密技術與解密方法
   * 包含：
      * 凱撒加密
      * 二進制轉換 (資安社群常用)


## 資料分析成果展示

<details> 

* ## 模擬「臺中地區博奕熱區變化趨勢」地圖 (可篩選)
   ### [https://chiakai-chang.github.io/tempHTML/GBplaceVarifyMap(201601~202012).html](https://chiakai-chang.github.io/tempHTML/GBplaceVarifyMap(201601~202012).html)

* ## 模擬「臺中地區博奕熱區變化趨勢」地圖 (純看變化)
   ### [https://chiakai-chang.github.io/tempHTML/GBplaceVarifyMap(201601~202012).html](https://chiakai-chang.github.io/tempHTML/GBplaceVarifyMap(201601~202012).html)

* ## 模擬「疫調個案活動軌跡」地圖 (可篩叢集)
   ### [https://chiakai-chang.github.io/tempHTML/demo1.html](https://chiakai-chang.github.io/tempHTML/demo1.html)

* ## 「110報案關鍵字」詞雲 (By 戰隊長:徐思勤)
   ### [https://chiakai-chang.github.io/tempHTML/key110.html](https://chiakai-chang.github.io/tempHTML/key110.html)

* ## 「e化報案」關鍵字詞雲 (By 戰隊長:徐思勤)
   ### [https://chiakai-chang.github.io/tempHTML/keyE.html](https://chiakai-chang.github.io/tempHTML/keyE.html)
</details> 

# Chiakai's 筆記區

<details> 

* ## 資安事件調查處理 (20211206~20211208)
   ### Day 1：[https://hackmd.io/@chiakai/SecurityCLass_1](https://hackmd.io/@chiakai/SecurityCLass_1)
   ### Day 2：[https://hackmd.io/@chiakai/SecurityCLass_2](https://hackmd.io/@chiakai/SecurityCLass_2)
   ### Day 3：[https://hackmd.io/@chiakai/SecurityCLass_3](https://hackmd.io/@chiakai/SecurityCLass_3)

* ## [讓 Colab 執行時永不斷線的秘密](https://colab.research.google.com/drive/1AypPlaUj0Ysz0H8YG6Op1XZ8nhfOi-Qn?usp=sharing) 
 
* ## [解決分母、分子超大導致分數無法進行四維運算問題](https://colab.research.google.com/drive/1z1pmV2sEoMo-Hhlc9JTnLApYuCLS4veC?usp=sharing)
</details> 

### site is published at https://chiakai-chang.github.io/tempHTML/
