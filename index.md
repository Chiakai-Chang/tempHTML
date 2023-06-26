# Chiakai's 成果展示區

## 精心研發各種小幫手程式 (Colab 即取即用，點擊程式名稱即可開啟)
* ## [臉書好友整理神器](https://colab.research.google.com/drive/1JCgq0qmmsAtfuICuyk_CciQVjgSfKZ33?usp=sharing)
   * 請參考教學: [使用指引](https://drive.google.com/file/d/1KI8intBMvUYx2rTMgFi2utGGM6oxEH0i/view)
   * 整理大量以往難以人工彙整之臉書留言或按攢者資訊，並用以從事「交集分析」抓出關鍵犯嫌。

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

* ## [時間戳轉換小幫手]([https://colab.research.google.com/drive/15auzjfvWt6HICDyKtTDEFfKpoT-TlG7s?usp=sharing](https://colab.research.google.com/drive/1uzcBbl5EHOn8J5S_UHWQ2_rpfs_Gjttp?usp=sharing))
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

## 精心研發各種小幫手程式 (打包 exe 提供使用)
* ## [AI智慧程式碼識別小幫手](https://github.com/Chiakai-Chang/CodeForensicsOnScene)
  * 為解決現場勘查時，遇到屬「程式開發」相關現場，充斥複雜難懂之各種程式碼，令現場查緝人員難以快速瞭解掌握涉案情形或釐清現場人員所言是否真實之情形。
  * 特別開發此工具，藉由 AI 提供快速分析程式碼並產出報告的功能，協助現場快速掌握可疑程式碼作用、可能違法情形與關鍵資訊擷取。
  * [![](https://chiakai-chang.github.io/tempHTML/img/CFOS.jpg)](https://github.com/Chiakai-Chang/CodeForensicsOnScene)

* ## [IPwhois好好查](https://github.com/Chiakai-Chang/CheckIP)
  * 為解決 log 分析時，裡面出現多達千萬、甚至上兆行的資料與IP，由此程式自動化從任意文本資料中，逐行抽取 IP 進行整理，再自動進行 IP Whois 查詢，若係臺灣 IP 就再進一步自動前往 TWNIC 進行 IP Whois 查詢，最後將結果整理成 excel 表格，大量節約同仁查詢耗時與精力。
  * [![](https://chiakai-chang.github.io/tempHTML/img/IPwhoisTool.jpg)](https://github.com/Chiakai-Chang/CheckIP)

* ## [PTT_Crawler](https://github.com/Chiakai-Chang/PTT_Crawler_ByUser)
  * PTT 作為臺灣網路消息最大的集散地之一，不少同仁遇到妨害名譽、恐嚇、假消息等案件發生在該站，雖網路上有不少 OSINT 工具可協助查詢資料，但均無保存跡證功能。
  * 遂特別研發此程式，除一鍵可保存所查詢 ID 之基本資要、相關文章、留言、暱稱等資料，並擷取該 ID 所使用 IP 紀錄以外，亦整合網上 OSINT 資源，提供該 ID 最後10筆上站 IP 紀錄，更會自動完成 IP whois 查詢工作，大量節約同仁查詢耗時與精力。
  * [![](https://chiakai-chang.github.io/tempHTML/img/PTT_Crawler_ByUser.jpg)](https://github.com/Chiakai-Chang/PTT_Crawler_ByUser)

* ## [經緯度/地址好好查](https://github.com/Chiakai-Chang/location_to_html)
  * 視覺化的資料是最容易分析的資料，以往同仁有大量的監視器位置、車行紀錄、IP 通聯、戶籍/現住地址等資整合後，往往因資料太過龐大，導致需耗費大量時間分析，才能找出關鍵交集位置。尤其疫情期間更是有大量需分析疫調個案活動軌跡需求。
  * 遂特別研發此程式，除幫同仁將相關經緯度標註於地圖上以外，還供批次地址轉經緯度功能，最後還能產出可攜式的地圖 HTML 檔，方便情資分享與分析。
  * [![](https://chiakai-chang.github.io/tempHTML/img/location_to_html.jpg)](https://github.com/Chiakai-Chang/location_to_html)

* ## [ATM交易資料自動查詢彙整小幫手](https://github.com/Chiakai-Chang/varityTask/tree/main/atmDataWash)
  * 為解決金流分析時，大量金流資料要逐筆查對 ATM 提領位置傷眼又考驗耐心的煩惱，特別受委託開發此小程式協助自動批次比對 ATM 提領地點。
  * [![](https://chiakai-chang.github.io/tempHTML/img/AtmDataWash.jpg)](https://github.com/Chiakai-Chang/varityTask/tree/main/atmDataWash)

* ## [巨量關鍵比對案件好好查](https://github.com/Chiakai-Chang/BigKeywordsMatcher)
  * 為解決同仁有一批關鍵ID，要在一批案件中比對符合的個案，往往都需耗費巨大的心力手動整理的困擾，特別受委託開發此小程式，協助自動批次以大量關鍵 ID 去篩選、比對大量案件，節省大量人力與心力。
  * 請參考教學: [操作教學](https://drive.google.com/file/d/1YeoV7mjYXlExavfmFpZu_emsYBqrIzWC/view?usp=sharing)
  * [![](https://chiakai-chang.github.io/tempHTML/img/BigKeywordsMatcher.jpg)](https://github.com/Chiakai-Chang/BigKeywordsMatcher)

* ## [臉書外洩資訊整理好好查](https://github.com/Chiakai-Chang/2019_FB_Leak_Parser)
  * 2019年傳超過 2.67 億臉書用戶的帳號、電話號碼和姓名在網路上曝光，此程式協助以關鍵字方式，提供檢索該外洩之個資。
  * 為防止濫用，此程式設計需於臺中市警局內網，且需登入科偵平臺方可使用，且查詢會留下log。
  * [![](https://chiakai-chang.github.io/tempHTML/img/fbLeakDataParser.jpg)](https://github.com/Chiakai-Chang/2019_FB_Leak_Parser)

* ## [臺中地區監視器過濾下載器](https://github.com/Chiakai-Chang/AutoCamDownloader)
  * 為解決調閱路口監視器時，要瀏覽或下載監視器必須要安裝很多網頁元件；以網頁觀看歷史影像都需緩存，不便加速回退；看完一段再載下一段，許多時間消耗在空等待；大批調閱時，仍需至GIS地圖查找監視器。
  且重大案件或歹徒不知行向時，要調閱周遭全部監視器就需消耗警力專責調閱等問題。
  * 特別開發可選定案發地點，選擇調閱範圍、時間區段，即可大規模自動批次排程下載監視器影像之程式，為同仁分憂解勞。
  * [![](https://chiakai-chang.github.io/tempHTML/img/AutoCamDownloader.jpg)](https://github.com/Chiakai-Chang/AutoCamDownloader)

* ## [取簿報報小記者](https://github.com/Chiakai-Chang/autoFindAccountTaker)
  * 查緝收簿手依以往被動查緝方式，難有成果。分局本身轄區特性，導致查緝困難，且全臺都在同一小池子，抓數量不多的取簿手。靠警示戶報案太慢，監視器已覆蓋。等警示戶到案也慢，監視器已覆蓋。本地警示戶大多寄到外地，需要聯繫外地警示戶較有機會查緝本地案件。結論：掌握取簿情資與查緝處理速度要「快」！
  * 遂特別開發此程式，盡可能盡速(民間影像保存期限內)找出開戶人聯繫電話，分工由同仁輪值第一時間與開戶人聯繫詢問存簿寄往何處，並立即把握時機前往調閱查緝，頗具成效。
  * [![](https://chiakai-chang.github.io/tempHTML/img/findAccTakenCase.jpg)](https://github.com/Chiakai-Chang/autoFindAccountTaker)

* ## [審核165案件小幫手](https://github.com/Chiakai-Chang/check165case)
  * 受理詐欺案要注意的「眉角」細節極多！就算是承辦人也不一定每次全部都記得。每日165都會稽核受理詐欺案件填輸是否出錯。常常同仁深夜受理後，分局、警察局、165稽核發現需更補正時，不得已往往要將深夜勤同仁自睡窩中吵醒，甚至還要聯繫被害人盡速再度回到受理單位來補正資料，實在擾民傷神。
  * 特別開發此程式，提供同仁受理詐欺前提供相關教學、受理時提供填輸參考、受理後即時審核並回饋應更補正問題，修改完成後，並自動將審核結果傳送供單位主管與業務人員知悉，為大家分憂解勞。
  * [![](https://chiakai-chang.github.io/tempHTML/img/check165case.jpg)](https://github.com/Chiakai-Chang/check165case)

* ## [自動開獎小幫手](https://github.com/Chiakai-Chang/CarHandDataManager)
  * 每周二、四刑事局固定提供詐欺提領情資，提供後分局承辦人需立即整理車手資料、分析轄區提領變化情形與熱時熱點變化趨勢，更要即時繕打調閱函搶時效供同仁儘速前往調閱監錄影像，相當燒腦費時。
  * 特別開發此程式，於接獲情資後，僅需將情資檔匯入程式，即可自動記錄分析轄區提領變化情形與熱時熱點變化趨勢，並自動產出每個處所監視器調閱函參考範本，極大化地分憂解勞。
  * [![](https://chiakai-chang.github.io/tempHTML/img/CarHandDataManager.jpg)](https://github.com/Chiakai-Chang/CarHandDataManager)

## 精心研發各種小幫手程式 (個別任務使用)
* ## [全網/FB社群科偵關鍵情資蒐報局](https://github.com/Chiakai-Chang/FacebookCrawler)
  * 適逢選舉、大型活動或有危安情資時，往往需調用大量人力輪番關注全網與各社群網路有關情資，造成大家身心俱疲。
  * 遂特別開發此爬蟲程式，業已實際協助於各大小選舉期間或經典賽等大型活動期間，協助自動化以關鍵字過濾全網情資，發現選舉賭盤或敏感資訊，提供同仁即時應對偵處。
  * [![](https://chiakai-chang.github.io/tempHTML/img/Crawler.jpg)](https://github.com/Chiakai-Chang/FacebookCrawler)

* ## [Youtube廣告自動爬搜](https://github.com/Chiakai-Chang/AutoParseYoutubeAD)
  * 近年來Youtube廣告遭詐騙集團濫用猖獗，導致不少民眾因而受騙，但要蒐集詐騙廣告檢舉，卻無一便捷方式可供快速搜尋，僅能憑運氣及等待演算法推薦蒐集到1則，就需再度等待運氣及等待演算法推薦才能繼續蒐集，毫無效率可言。
  * 遂特別開發此爬蟲程式，協助以最可能出現詐騙廣告之關鍵字搜尋，並以最小輪播廣告時間，自動化快速蒐集相關廣告資訊，並按檢舉所需資訊整理成表，至今已成功蒐獲數千則廣告。
  * [![](https://chiakai-chang.github.io/tempHTML/img/YT_AD.jpg)](https://github.com/Chiakai-Chang/AutoParseYoutubeAD)

# Chiakai's 混合實境小作品
* ## 第一人稱視角模擬訓練-執行博弈/詐欺犯罪搜索現場調查
  * [下載連結](https://drive.google.com/file/d/1JnpmDLWOaB8Fd9oq5cz4DAi-PKE2bhEJ/view?usp=sharing)
  * 特色：
    * 全國首創「第一人稱視角-搜索詐欺犯罪現場模擬訓練」，融入遊戲元素並透過第一人稱視角的操作方式，有別於傳統的訓練型態，讓同仁身歷其境且邊玩邊學，就算是新進人員，透過這個模擬訓練，就可以學習調查犯罪現場、尋找線索、詢問外語犯嫌、臨場反應、分析證據等項目，最重要的是，未來不只博弈/詐欺案件適用，更可導入不同案件犯罪現場的相關內容，以及所擔任的不同角色任務，綜合訓練偵查人員的執行技巧和應變能力，強化整體偵查體質。
    * 另外遊戲中可配合運用基於 AI 人工智慧技術所開發設計「AI程式碼識別小幫手」，率先全國首創讓程式告訴你程式在做什麼、可能涉及什麼不法行為等內容，提供刑事人員快速辨別可疑程式，協助分析隱藏在程式內的不法行為、加密貨幣錢包位址及網站網址等資訊，強化犯罪現場數位取證能力。
  * 目前可體驗項目：
    * 基於真實經驗而設計的現場環境與人物互動
      * ![image](https://chiakai-chang.github.io/tempHTML/img/always_smoke.gif)
      * ![image](https://chiakai-chang.github.io/tempHTML/img/always_firstday.gif)  
    * 現場小線索之尋找與拼湊
      * ![image](https://chiakai-chang.github.io/tempHTML/img/little_clue.gif)  
      * ![image](https://chiakai-chang.github.io/tempHTML/img/burnt_paper.gif)  
    * 可真實英語對話之 AI 人物
      * 串接 GPT 模型，自然真實的透過語音(英語)來對話
      * 該人物掌握關鍵資訊，需由玩家模擬警方以偵訊技巧來獲取
      * ![](https://chiakai-chang.github.io/tempHTML/img/challenge_2.gif)
    * 模擬實際取得程式碼，該如何從中獲取獲取跡證，並即時藉以進一步突破
      * 精心設計過的真實程式碼
      * 超脫遊戲以外的真實互動  
      * [![](https://chiakai-chang.github.io/tempHTML/img/CFOS.jpg)](https://github.com/Chiakai-Chang/CodeForensicsOnScene)
  * 截圖：
      * ![](https://chiakai-chang.github.io/tempHTML/img/challenge_1.gif)

# Chiakai's 資料分析成果展示
* ## 模擬「臺中地區博奕熱區變化趨勢」地圖
  * ### [2016~2020 點位叢集加熱度變化趨勢](https://chiakai-chang.github.io/tempHTML/GBplaceVarifyMap(201601~202012).html) (可按年度篩選、可播放每年變化情形、可加速)
    * [![](https://chiakai-chang.github.io/tempHTML/img/GBplaceVarifyMap(201601~202012).jpg)](https://chiakai-chang.github.io/tempHTML/GBplaceVarifyMap(201601~202012).html)
  * ### [2015/01/01~2021/02/09 熱度變化趨勢](https://chiakai-chang.github.io/tempHTML/GBMapTaichung(2020~2021).html) (可播放每日變化情形、可加速)
    * [![](https://chiakai-chang.github.io/tempHTML/img/GBMapTaichung(2020~2021).jpg)](https://chiakai-chang.github.io/tempHTML/GBMapTaichung(2020~2021).html)
* ## 模擬「疫調個案活動軌跡」地圖 (可篩叢集)
  * ### [模擬個案活動軌跡移動情形](https://chiakai-chang.github.io/tempHTML/demo1.html) (可篩裝置、可播放按每日變化情形、可加速)
    * [![](https://chiakai-chang.github.io/tempHTML/img/demo1.jpg)](https://chiakai-chang.github.io/tempHTML/demo1.html)
* ## 額外分享：
  * ### [「110報案關鍵字」詞雲 (By 戰隊長:徐思勤)](https://chiakai-chang.github.io/tempHTML/key110.html)
  * ### [「e化報案」關鍵字詞雲 (By 戰隊長:徐思勤)](https://chiakai-chang.github.io/tempHTML/keyE.html)

# Chiakai's 筆記區
* ## 資安事件調查處理 (20211206~20211208)
   * ### Day 1：[https://hackmd.io/@chiakai/SecurityCLass_1](https://hackmd.io/@chiakai/SecurityCLass_1)
   * ### Day 2：[https://hackmd.io/@chiakai/SecurityCLass_2](https://hackmd.io/@chiakai/SecurityCLass_2)
   * ### Day 3：[https://hackmd.io/@chiakai/SecurityCLass_3](https://hackmd.io/@chiakai/SecurityCLass_3)
* ## 程式筆記 (點標題即可開啟)：
  * ### [讓 Colab 執行時永不斷線的秘密](https://colab.research.google.com/drive/1AypPlaUj0Ysz0H8YG6Op1XZ8nhfOi-Qn?usp=sharing) 
  * ### [解決分母、分子超大導致分數無法進行四維運算問題](https://colab.research.google.com/drive/1z1pmV2sEoMo-Hhlc9JTnLApYuCLS4veC?usp=sharing)

### site is published at https://chiakai-chang.github.io/tempHTML/
