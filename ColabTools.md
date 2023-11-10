# Chiakai's Colab 軍火庫
* 更新至 2023-11-08

## 精心研發各種線上偵查小幫手
* ## 全新改版! [Code Investigater AI 隨身程式碼鑑識小幫手]
  * [![](https://chiakai-chang.github.io/tempHTML/img/Cute_CODE_INVESTIGATOR_AI.png)](https://pse.is/5dt4v2)
  * 為解決執行數位鑑識現場勘查時，遇到「開發人員」相關現場充斥複雜難懂之各種程式碼的問題，該問題令現場查緝人員難以快速瞭解掌握涉案情形或釐清現場人員所言是否真實，特別開發此工具，提供快速分析程式碼並產出報告的功能，協助現場快速掌握涉案狀況。
  * 特色:
    * 1、可以直接將程式文檔上傳(如 .html、.py、.bat、.sh、.ps1等)，不用複製貼上。
    * 2、經歷數個月 N 輪的 Promt Engineering (提示工程)實測，目前可實現分析程式並給出以下報告內容: 
      * (1) 辨識是哪一種程式語言
      * (2) 分析程式功能概要
      * (3) 分析程式執行分析、函數名稱與程式碼出處(區分自動、手動的函數與類別區塊)
      * (4) 分析程式作者撰寫與變數命名之風格/特徵
      * (5) 分析並嘗試找出程式內留之相關聯絡資訊
      * (6) 分析並嘗試找出程式內之登入資訊(如帳號,密碼,Token等數位憑證)
      * (7) 分析並嘗試找出程式內之網路資訊(如IP、Port、路徑):
      * (8) 分析程式有無加密動作
      * (9) 分析程式是否有惡意程式碼
      * (10) 分析程式之網路交互作用(如從何處取得資料或將資料傳輸至何處)
      * (11) 分析程式是否存在資料混淆
      * (12) 分析程式是否有可疑/違法活動並總結出摘要
      * (13) 提供偵查建議
  * 趕快來試用看看吧!!
  * 當前有兩個版本：
    * ### (新!) [Open AI 平臺](https://pse.is/5dt4v2)
      * 基於 GPT-4 turbo 語言模型
    * ### (舊) [POE 平臺](https://poe.com/CodeInvestigate)
      * 基於 Claude2-100k 語言模型
      * 一天只能查詢 5 筆

## 精心研發各種小幫手程式 (Colab 即取即用，點擊程式名稱即可開啟)
* ## [臉書好友整理神器](https://colab.research.google.com/drive/1JCgq0qmmsAtfuICuyk_CciQVjgSfKZ33?usp=sharing)
   * 請參考教學: [使用指引](https://drive.google.com/file/d/1KI8intBMvUYx2rTMgFi2utGGM6oxEH0i/view)
   * 整理大量以往難以人工彙整之臉書留言或按攢者資訊，並用以從事「交集分析」抓出關鍵犯嫌。

* ## [臉書留言整理神器](https://colab.research.google.com/drive/1t4xkYcXG0apHxFmjXqOPpR_cHpKwtfxV?usp=sharing)
   * 最近網路相關案件越來越多，臉書上假消息、恐嚇、不當發文等等也是越發頻繁，若是假帳號或相關資料很少的帳號發文，或者由他人轉 PO 的文章，常常都有需要從該貼文的留言內容，嘗試看看有無其他線索的需求。
   * 手動瀏覽再複製貼上，實在是很費力，所以特別撰寫這個小程式，只要會取得「留言部份」的網頁原始碼，貼給本程式，就會自動幫忙整理出以下資訊：
      * 1、留言者
      * 2、留言者臉書連結
      * 3、留言內容

* ## [IPv6 格式轉換小幫手](https://colab.research.google.com/drive/1we5ASiwmo9hfpVU9fNz0b115R-c0VPL5?usp=sharing)
   * 鑒於 IPv6 位址表示法太長，因此有所謂的以下「省略規則」：
      * 規則1：
         * 為每組數字的第一個0可以省略，若整組皆為0，則以0表示。譬如，「0DB8」可以省略為「DB8」，「0000」則為「0」。
      * 規則2：
         * 為連續出現的0000可以省略成「::」。譬如：「:0000:0000:0000:0000:」可以省略成「:0000:0000:0000::」、「:0:0:0:0:」、「:0::0:」或「::」。
   * 投單調取 IPv6 時，須輸入完整128bits，不可省略「0」，英文部分須為大寫。
      * 範例：2001:B400:E2AD:236A:713E:0BF4:804C:1573
   * 所以特別撰寫這個小程式，幫忙將 IPv6 都轉成符合投單調取的格式

* ## [批量 IP HTTP HEAD 確認小幫手](https://colab.research.google.com/drive/1N559gaAMvCnsKWwK3Y3DPUGDI26JGfNc?usp=sharing)
  * 若您有一批 IP 想了解該 IP 是什麼網站
  * 除了透過 Reverse IP Lookup 查詢 Domain 以外，。
  * 也可以針對該 IP 之 80 (http) 或 443 (https) port 發送 HTTP HEAD 請求。
    * 若該 IP 是 WEB server，就會回應 HTTP Headers，即該網站的 Meta Data，包括：
      * 伺服器類型，如: CloudFlare, Google 等。
      * Location，如： 該網頁的域名。
  * 曾經偵辦案件時取得過某不知身分犯嫌的 IP 連線紀錄，想了解他連線到的 IP 是什麼網站，看有沒有有助於瞭解查明該犯嫌身分的資料，所以撰寫了這個程式。
    * 想到可能對大家也會有幫助，特別釋出給大家使用。

* ## [大量同格式JSON彙整小幫手](https://colab.research.google.com/drive/1w1ApO_p3zh38ocU6jW5di3LXfeQWA3t6?usp=sharing)
  * 現在的網頁大多都基於 MVC 等架構，除了呈現的網頁以外，背後還會用 ajax 等方式用去存取 API 來獲得要更新顯示的資料(大多為 JSON 格式)。
  * 因為前述 JSON 給的資料往往比網頁上肉眼能看到得「更豐富」，且格式也更容易整理，所以有個小幫手可以幫忙將這些 Json 接收下來，一起轉換成更容易操作的 excel 格式，豈不美哉？
  * 本小幫手目前有兩種使用方法，適應不同情境：
    * 用法1: 整理已下載之大量 JSON 檔
    * 用法2: 每次複製貼上1筆，即時換整 JSON 資料再匯出

* ## [視覺化情資網路關聯小幫手](https://colab.research.google.com/drive/1hVI20D5MchN6OuSI8OSC6MVYTDSJclg6?usp=sharing)
  * 現在已有的視覺化分析軟體包括：i2 analyst's notebook、KeyLines 等等，真的非常好用。
  * 但是有以下困擾:
    1. i2 價格實在...門檻太高了。
    2. KeyLines 則需要在公務系統內使用，要比較注意資安稽核等等疑慮。
  * 加上有時候只是單純想要「顯示」情資之間的關聯，用來幫助判斷、分析資料。
  * 所以撰寫了個小程式，讓大家可以隨時隨地「免費的」視覺化自己資料之間的關聯。

* ## [AWS IP 確認小幫手](https://colab.research.google.com/drive/1T7vX0L2gs9VCNzwzSpvsI84rGTFRXl3R?usp=sharing)
   *  若大家有遇到 ip 是 amazon (亞馬遜) 的，可以使用這個小幫手來確認 IP 是 AWS 的什麼雲端服務。
      * 亦可參考 RyanLabs 提供之線上查詢工具：AWS IP Range Checker/Lookup Tool
         * 該工具僅能查詢 IPv4 的資料
   * 本程式係從官方：AWS IP address ranges 下載最新之 IP 資訊 (Json 檔，含 IPv4 與 IPv6) 進行比對，為最即時、最準確之資料

* ## [地址轉經緯度小幫手](https://colab.research.google.com/drive/1BWleXRAN1vM82-k9lz-O78fPMqBZf581?usp=sharing)
  * 借用內政部國土測繪中心「國土測繪圖資服務雲」之電子地圖，查詢任意地址之完整行政區(至村里鄰)及經緯度。 

* ## [User-Agent 解析小幫手](https://colab.research.google.com/drive/1IP1t7yFuIYLnTttwcn_V5fy3XkJASk2d?usp=sharing)
  * 在做 log 分析時，常常都會遇到 User-Agent 這個資料，該資料通常包含了其應用程式類型(瀏覽器)、作業系統、軟體供應商……等等，有時還會包含軟體修訂版本等資訊。
  * 因該字串不容易閱讀，所以特別以小程式幫忙解析重點。

* ## [封包 headers 文字轉 dict 小幫手](https://colab.research.google.com/drive/15auzjfvWt6HICDyKtTDEFfKpoT-TlG7s?usp=sharing)
   * 使用 DevTools 複製找到並複製封包有關 Requests Headers 的文字內容。
   * 貼到程式後，即可整理成方便使用的 dict 格式，並自動將 cookie 分離。

* ## [時間戳轉換小幫手](https://colab.research.google.com/drive/1uzcBbl5EHOn8J5S_UHWQ2_rpfs_Gjttp?usp=sharing)
  * 在做資料清洗、資料探勘時，偶爾會發現有以數字表示的時間(即: 時間戳)。
  * 因為數字的時間戳雖然很方便比較「日期、時間差異」、方便做「時區加減計算」，但是不容易直觀的了解究竟是什麼時間，所以為了方便就寫了個小小小幫手。
  * 本小幫手目前有兩種使用方法，適應不同情境：
    * 用法1: 「時間戳」轉換成「西元日期」
    * 用法2: 「任意日期格式」轉換成「時間戳」

* ## [文字加解密技術](https://colab.research.google.com/drive/1lq6E8jFDKuXveji5zJmzl7m7hT3o3503?usp=sharing)
   * 提供文字有關「凱薩加密」、「二進制轉換」等2種之加解密，尤其是「二進制轉換」時常受資安相關社群隱藏發言所愛用。
   * 包含：
      * 凱撒加密
      * 二進制轉換 (資安社群常用)
