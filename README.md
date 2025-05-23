# 📘TW_DID_Student 數位學生證

本專案是一個基於 Vue 3 + Node.js 架構的全台大專院校通用**數位學生證**申請與驗證系統，整合 Email 驗證、數位憑證發行、錢包導入 QR Code 以及**匿名留言板**等功能。  
本專案除了驗證學生身份的 email 外，完全不會儲存您的其他個人資料，所有資料都由您個人的數位皮夾自行託管。

本專案基於「數位發展部」開發之「數位憑證皮夾」沙盒環境，僅供學習及參考使用，非正式用途。  
希望這項技術未來能普及，「數位憑證皮夾」透過 DID 技術可實現個人資料的去中心化存儲與自主管理。

---

## 🚀 功能特色

- ✅ **學生信箱驗證**（支援所有 `.edu.tw` 結尾與常見子網域）  
- ✅ **自動識別學校中文名稱**（如 `@ntu.edu.tw` → 國立臺灣大學）  
- ✅ **自動填入學號與學校名稱**  
- ✅ **VC 數位學生證**（姓名、學號、學校）  
- ✅ **QR Code 與深層連結** → 一鍵導入錢包  
- ✅ **學生證驗證與身份比對流程**  
- ✅ **新增：匿名留言板**  
  - 使用 DID 驗證學校身分後，可匿名或實名發表意見  
  - 可對貼文按讚、回覆  
  - 搜尋貼文、標籤（`#標籤`）篩選、依時間或按讚數排序  

---

## 🧱 技術架構

### 前端
- **Vue 3（Composition API）**  
- **Tailwind CSS**  
- **Axios**

### 後端
- **Node.js + Express**  
- **MySQL**（儲存學生驗證記錄、留言板資料）  
- **Nodemailer**（寄送驗證信）  
- **自訂 VC API**：發卡 / 授權 / 驗證

---

## 📦 安裝與啟動

### 🔧 安裝依賴
```bash
npm install
```
### ▶️ 啟動前端開發伺服器
```bash
npm run dev
```
### ▶️啟動後端（假設你有 backend server）
```bash
node server.js
```
## 📮 API 說明（簡要）

### 1. 學生身分驗證

- **POST** `/verify-email`  
  傳入 `{ email }`  
  驗證格式、寄出驗證信  
  回傳：`{ success, message, school_name }`

- **GET** `/check-verification`  
  傳入 `email`  
  查詢信箱是否已完成驗證  
  回傳：`{ verified: true/false, student_id, school_name }`

- **POST** `/vc-item-data`  
  發行數位學生證（VC）

- **GET** `/verify-qr` / `/verify-result`  
  DID 驗證的 QR Code 與查詢結果

### 2. 匿名留言板

- **GET** `/board-with-replies`  
  - 參數：`page`, `pageSize`, `search`, `sort`(可選)  
  - 回傳：含主貼文、回覆、按讚數的完整列表

- **POST** `/board-message`  
  - 發表新的留言（需攜帶學校、內容、可選 author_name）

- **POST** `/board-reply`  
  - 對指定留言回覆

- **POST** `/board-like`  
  - 對留言按讚

> 內部亦可支援搜尋 (`search=xxx`) 與排序 (`sort=likes_desc` / `time_desc` / etc.)。

---

## 📄 數位學生證欄位格式

| 欄位名稱 | 類型   | 英文代碼  | 規則說明                   |
| -------- | ------ | --------- | -------------------------- |
| 姓名     | BASIC  | name      | 中英文與 _ 組成            |
| 學號     | CUSTOM | number    | 英文/數字組成              |
| 學校     | CUSTOM | school_CN | 中文名稱，系統自動判別填入 |

---

## 👨‍💻 開發者資訊

作者：Mengxiaozhi（劉訊志）  
聯絡方式：me@xiaozhi.moe  

---

## 📢 貢獻與授權

本專案採用 MIT 授權，歡迎開發者進行二次開發或分享。

---

## ⚠️ 用戶須知與免責聲明

本平台「數位學生證」為學生自主開發之技術展示專案，目的在於探索分散式身份識別技術（DID）於教育領域的應用，並無任何學校或教育機構之官方授權或背書。  

- 本系統所顯示之學校名稱係根據您提供之學術信箱網域自動推論，僅供技術驗證與識別用途，不具備任何法律效力。  
- 本系統未與任何學校資料庫或資訊系統連接，亦不模擬或破解任何學校登入機制。  
- 所產生之數位學生證為模擬性質，僅用於展示憑證技術格式與樣式，不得作為正式學生證使用。  
- 本平台不蒐集、處理或儲存除信箱驗證必要資訊外的個人資料，所有資料僅用於即時驗證與憑證產生，不另作他用。  
- 本平台所生成的學校名稱、憑證資訊，均為使用者自行提供，若造成任何誤解、冒用或第三方損害，本平台概不負責。  
- 若您為教育機構代表，有合作意願或欲提出下架通知，請聯繫本站開發者：me@xiaozhi.moe  

---

## 關於作者想說的話

我叫劉訊志，就讀於致理科技大學資訊管理系一年級。  

在初期版本中，我曾使用學校的 logo 與名稱作為展示頁視覺，未經正式授權，這是我在設計判斷上的疏忽。我已於第一時間主動修正，並不斷調整以符合合規性。

但在事件過程中，我也遭遇了大量無建設性的攻擊，例如：
- 嘲諷此專案「毫無用處」
- 質疑我「騙人」、「裝官方」
- 否定我作為學生創作者的正當性

你可以批評我的設計，但否定一個學生創作者的動機與人格，對於整個技術創作環境毫無幫助

- 我尊重法律，所以我修正項目
- 我堅持理念，所以我不刪文、不道歉