# Translation Terminology Report (Qwen-MT qwen-mt-plus Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 75.0% (3/4) | 67.53 (Standard) |
| Case 2 | 57.1% (4/7) | 59.48 (Fairly Difficult) |
| Case 3 | 100.0% (4/4) | 72.26 (Easy) |
| Case 4 | 100.0% (8/8) | 48.64 (Difficult) |
| Case 5 | 100.0% (3/3) | 60.56 (Standard) |
| Case 6 | 100.0% (1/1) | 66.01 (Standard) |
| Case 7 | 83.3% (5/6) | 63.96 (Standard) |
| Case 8 | 100.0% (4/4) | 55.45 (Fairly Difficult) |
| Case 9 | 100.0% (3/3) | 74.89 (Easy) |
| Case 10 | 100.0% (4/4) | 80.35 (Easy) |
| Case 11 | 100.0% (3/3) | 53.97 (Fairly Difficult) |
| Case 12 | 100.0% (2/2) | 58.08 (Fairly Difficult) |
| Case 13 | 100.0% (6/6) | 79.51 (Easy) |
| Case 14 | 100.0% (3/3) | 71.28 (Easy) |
| Case 15 | 100.0% (1/1) | 71.7 (Easy) |
| Case 16 | 100.0% (2/2) | 42.37 (Difficult) |
| Case 17 | 83.3% (5/6) | 69.86 (Standard) |
| Case 18 | 100.0% (2/2) | 63.39 (Standard) |
| Case 19 | 100.0% (6/6) | 53.53 (Fairly Difficult) |
| Case 20 | 80.0% (4/5) | 79.01 (Easy) |
| **Average** | **93.9%** | **64.6 (Standard)** |

<hr>

## Case 1: Quotation request for a color box with special coating

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | `water-based gloss ink` | ✅ Match |
| `克铜版纸` | `gsm art paper`, `gsm coated paper` | `gsm art paper` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
報價請求：新款遊戲**彩盒**

Hi Team,

請根據以下規格為我們的新產品報價，目標數量為 5,000 和 10,000 件。

- **產品類型**: **彩盒**
- **尺寸**: 220mm x 150mm x 40mm
- **材料**: 300**克铜版纸** **裱** E-flute corrugated board
- **印刷**: 4C + 0C
- **表面處理**: 整體上**水性亮光油墨**, Logo 部分要求使用 啞光油墨 形成對比效果。
- **包裝**: 50個/箱，用收縮膜 包好。

請告知打樣時間及大貨生產週期。謝謝！

Best,
David
```

### Qwen-MT's Translation with Highlights

```text
Quotation request: New game **color box**

Hi Team,

Please quote for our new product according to the following specifications, with target quantities of 5,000 and 10,000 pieces.

- **Product Type**: **Color box**
- **Size**: 220mm x 150mm x 40mm
- **Material**: 300gsm art paper laminated with E-flute corrugated board
- **Printing**: 4C + 0C
- **Surface Treatment**: Overall **water-based gloss ink**, logo part requires matt ink to form a contrast effect.
- **Packaging**: 50 per carton, shrink wrapped.

Please advise on the sample time and bulk production lead time. Thank you!

Best,
David
```

<hr>

## Case 2: Re-quote request for a hardcover book after specification update

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |
| `書紙` | `book paper` | `book paper` | ✅ Match |
| `書套` | `jacket` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
RE: 精裝書報價 - **規格更新**

Hi Steve,

感謝您上次的報價。客戶對設計進行了修改，請根據更新後的規格重新報價。

- **內文尺寸**: 240mm(w) x 290mm(h) - 不變
- **皮殼**: 改為使用 157g **哑光**铜版纸 **裱** 3mm **灰板**。
- **表面處理**: 皮殼需要 ****哑光**覆膜** 及 **燙幻彩** 處理 logo。
- **襯紙**: 150gsm **書紙**
- **數量**: 1,500本 / 3,000本

另外，客戶詢問是否可以為首批50本書提供獨立的**書套**？如果可以，請單獨報價。

Thanks,
Catherine
```

### Qwen-MT's Translation with Highlights

```text
RE: Hardcover Quotation - **Specification Update**

Hi Steve,

Thanks for your last quotation. The client has made some changes to the design, please re-quote according to the updated specifications.

- **Inside dimensions**: 240mm(w) x 290mm(h) - unchanged
- **Cover**: changed to use 157g **matt** coated paper laminated with 3mm **greyboard**.
- **Surface treatment**: cover needs matte lamination and **holographic foil stamping** logo.
- **Lining**: 150gsm **book paper**
- **Quantity**: 1,500 / 3,000

Also, the client asked if it is possible to provide independent sleeves for the first batch of 50 books? If yes, please quote separately.

Thanks,
Catherine
```

<hr>

## Case 3: Urgent order for paper bags for a trade show

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `紙袋` | `paper bag` | `paper bag` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
URGENT: **紙袋**報價 - 展會急用

Alice 你好,

我們急需為下個月的展會製作一批**紙袋**，請盡快報價。

- **類型**: **紙袋**
- **尺寸**: 30cm (H) x 25cm (W) x 10cm (D)
- **物料**: 210g **白**卡**纸**
- **印刷**: 4C+0C, 使用啞光油墨。
- **加工**: 啞光覆膜, 穿棉繩提手。
- **數量**: 500個 / 1000個

由於時間緊急，請告知最快的交貨日期。如果來不及覆膜，不**上光** 的價格是多少？

麻煩了！
Jack
```

### Qwen-MT's Translation with Highlights

```text
URGENT: Quotation for paper bags - Exhibition use

Hi Alice,

We urgently need to make a batch of paper bags for next month's exhibition, please quote as soon as possible.

- **Type**: **Paper bag**
- **Size**: 30cm (H) x 25cm (W) x 10cm (D)
- **Material**: 210g **white **card** paper**
- **Printing**: 4C+0C, using matt ink.
- **Processing**: Matt laminated, cotton rope handle.
- **Quantity**: 500 / 1000

Due to the tight schedule, please advise the earliest delivery date. If it is too late to laminate, what is the price without **varnishing**?

Thank you!
Jack
```

<hr>

## Case 4: Inquiry about materials for a board book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matt coating` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `撲克油` | `poker varnishing`, `Poker Coating` | `poker varnishing` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |
| `硬板书` | `boardbook` | `boardbook` | ✅ Match |

---

### Source Text with Highlights

```text
關於**硬板书**材料問題

Hi William,

我們正在規劃一款新的**硬板书**，有幾個關於材料的問題想請教：

我們的設計是 12 pages，想用 400g **白**卡**纸** 對**裱**。請問你們建議用多厚的**灰板** 做內襯 才能保證書本的硬度和耐用性？

另外，封面如果採用 **撲克油** 處理，與普通的 ****哑光**涂层** 相比，成本大概會增加多少？

請先基於以下暫定規格報價 3000 / 5000 本：
- **尺寸**: 8" x 8"
- **頁數**: 12 pages (6 spreads)
- **材料**: 400g **白**卡**纸**對**裱**
- **印刷**: 4C/4C

期待您的專業建議。

Regards,
Emily
```

### Qwen-MT's Translation with Highlights

```text
About **boardbook** material issue

Hi William,

We are planning a new **boardbook**, and have several questions about the materials:

Our design is 12 pages, and we want to laminate with 400g **white **card** paper**. Could you please advise how thick **greyboard** should be used as lining to ensure the book's hardness and durability?

Also, if the cover uses **poker varnishing**, compared to ordinary **matt coating**, how much will the cost increase approximately?

Please quote based on the following tentative specifications for 3000 / 5000 books:
- **Size**: 8" x 8"
- **Pages**: 12 pages (6 spreads)
- **Material**: 400g **white **card** paper** **laminating**
- **Printing**: 4C/4C

Looking forward to your professional advice.

Regards,
Emily
```

<hr>

## Case 5: Quote for multi-language instruction sheets and packaging

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `書紙` | `book paper` | `book paper` | ✅ Match |

---

### Source Text with Highlights

```text
Quote Request: Multi-language instruction sheet & packaging

Hi Teresa,

Please quote for the following items. Quantities: 8k, 16k.

**Item 1: Tuck-in Box**
- **Material**: 350gsm **灰板**
- **Size**: 180 x 100 x 50mm
- **Printing**: 4C+0C
- **Finishing**: **上光**

**Item 2: Instruction Sheets (x3 languages)**
- **Size**: A4, fold to A6
- **Material**: 105gsm **書紙**
- **Printing**: 1C+1C
- **Note**: 3個版本內容不同，但數量均分。

請將兩個項目分開報價。謝謝。

Thanks,
Ben
```

### Qwen-MT's Translation with Highlights

```text
Quote Request: Multi-language instruction sheet & packaging

Hi Teresa,

Please quote for the following items. Quantities: 8k, 16k.

**Item 1: Tuck-in Box**
- **Material**: 350gsm **greyboard**
- **Size**: 180 x 100 x 50mm
- **Printing**: 4C+0C
- **Finishing**: **varnishing**

**Item 2: Instruction Sheets (x3 languages)**
- **Size**: A4, fold to A6
- **Material**: 105gsm **book paper**
- **Printing**: 1C+1C
- **Note**: 3 versions have different content, but quantities are equal.

Please quote the two items separately. Thanks.

Thanks,
Ben
```

<hr>

## Case 6: Re-order request with an inquiry about partial shipment

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
補單請求 & Partial Shipment Inquiry

Dear Joe,

我們上個月訂單 (PO#20240512) 的產品市場反應很好，現需緊急補單。

請為以下產品報價 5,000 件：
- **產品**: **精装本**
- **規格**: 與 PO#20240512 完全相同。

另外，由於市場急需，請問是否可以在完成 2,000 本後立即安排部分出貨？剩下的 3,000 本按正常流程完成。如果可以，請告知相關的物流費用。

Thanks a lot,
Connie
```

### Qwen-MT's Translation with Highlights

```text
Reorder request & Partial Shipment Inquiry

Dear Joe,

The products from our last month's order (PO#20240512) are doing well in the market, and we need to reorder urgently.

Please quote for 5,000 pieces of the following product:
- **Product**: **hardcover**
- **Specification**: exactly same as PO#20240512.

Also, due to the urgent demand in the market, can you arrange partial shipment after completing 2,000 pieces? The remaining 3,000 pieces will be completed as normal. If yes, please advise the related logistics cost.

Thanks a lot,
Connie
```

<hr>

## Case 7: Quote for a slipcase with an acrylic board and special foil stamping

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `亞克力板` | `acrylic board`, `acrylic sheet` | `acrylic board` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |

---

### Source Text with Highlights

```text
報價：帶**亞克力板**的書盒

Hi Steve,

麻煩報價一款特殊的書盒，設計比較複雜。

- **類型**: 書盒
- **適用書籍**: 150mm x 220mm x 30mm
- **材料**: 2mm **灰板** **裱** 128g art paper
- **加工**:
    1.  表面 ****哑光**覆膜**
    2.  正面需要 **燙幻彩**
    3.  側面嵌入一塊 3mm 厚的透明 **亞克力板**，尺寸為 50mm x 100mm。

- **數量**: 500 / 1000

請問**燙幻彩**除了標準的彩虹色，有其他顏色選擇嗎？**亞克力板**的邊緣可以做拋光處理嗎？

Best regards,
Michael
```

### Qwen-MT's Translation with Highlights

```text
Quotation: slipcase with **acrylic board**

Hi Steve,

Please quote a special slipcase, the design is quite complicated.

- **Type**: slipcase
- **Applicable books**: 150mm x 220mm x 30mm
- **Material**: 2mm **greyboard** **laminating** 128g art paper
- **Processing**:
    1.  **matt** coated
    2.  **holographic foil stamping** on the front
    3.  3mm thick transparent **acrylic board** embedded in the side, size 50mm x 100mm.

- **Quantity**: 500 / 1000

Is there any other color option for **holographic foil stamping** besides the standard rainbow color? Can the edge of the **acrylic board** be polished?

Best regards,
Michael
```

<hr>

## Case 8: Quotation request for poker cards with different packaging options

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `撲克油` | `poker varnishing`, `Poker Coating` | `poker varnishing` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
撲克牌報價

Hi Team,

請報價製作標準撲克牌，規格如下：

- ****卡**牌數量**: 54張/副
- **尺寸**: 63 x 88mm
- **材料**: 300gsm 藍芯紙
- **印刷**: 4C+4C
- **表面處理**: 雙面 **撲克油**
- **包裝**:
    - **選項A**: 標準 tuck box，250g **白**卡**纸**，4C印刷，**上光**。
    - **選項B**: 用 收縮膜 包裝，不含紙盒。
- **數量**: 3000 / 5000 副

請分別就選項A和選項B報價。

Thanks,
Fiona
```

### Qwen-MT's Translation with Highlights

```text
Poker **card** quotation

Hi Team,

Please quote for the production of standard poker cards, specifications as follows:

- **Number of cards**: 54 cards/pack
- **Size**: 63 x 88mm
- **Material**: 300gsm blue core paper
- **Printing**: 4C+4C
- **Surface treatment**: double-sided **poker varnishing**
- **Packaging**:
    - **Option A**: standard tuck box, 250g **white **card** paper**, 4C printing, **varnishing**.
    - **Option B**: shrink wrap packaging, no cardboard box.
- **Quantity**: 3000 / 5000 packs

Please quote separately for Option A and Option B.

Thanks,
Fiona
```

<hr>

## Case 9: Inquiry about eco-friendly material options for a color box

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matt coating` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |

---

### Source Text with Highlights

```text
Inquiry for Eco-Friendly Options for Color Box

Hi Alice,

We are planning a new a new **彩盒** and would like to explore eco-friendly options.

- **Size**: 200 x 200 x 80mm
- **Current Spec**: 300gsm art paper with matt lamination.

Could you please quote the price for the current spec for 5,000 units?
Additionally, could you provide alternative quotes for:
1.  Using FSC certified paper.
2.  Replacing matt lamination with a water-based matt coating (水性****哑光**涂层**).

We want to compare the cost and appearance. Could you send us samples of the matt coating finish if available?

Best,
Leo
```

### Qwen-MT's Translation with Highlights

```text
Inquiry for Eco-Friendly Options for **Color Box**

Hi Alice,

We are planning a new 彩盒 and would like to explore eco-friendly options.

- **Size**: 200 x 200 x 80mm
- **Current Spec**: 300gsm art paper with **matt** lamination.

Could you please quote the price for the current spec for 5,000 units?
Additionally, could you provide alternative quotes for:
1.  Using FSC certified paper.
2.  Replacing **matt** lamination with a water-based **matt coating** (水性哑光涂层).

We want to compare the cost and appearance. Could you send us samples of the **matt coating** finish if available?

Best,
Leo
```

<hr>

## Case 10: Feedback on sample quality for a board book order

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光油墨` | `matt ink`, `matte ink` | `matt ink` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matt coating` | ✅ Match |
| `硬板书` | `boardbook` | `boardbook` | ✅ Match |

---

### Source Text with Highlights

```text
Feedback on sample for Order #S20240608

Hi William,

我們收到了**硬板书** 的樣品，整體不錯，但有兩個小問題：

1.  其中一頁的 內襯 有輕微氣泡，大貨生產時請務必避免。
2.  封面的 ****哑光**涂层** 感覺有點薄，部分區域反光不均。我們希望是更深沉的 **哑光** 效果。是否可以改用 ****哑光**油墨** 或者增加塗層厚度？

請確認以上問題能否在大貨中改善。等待您的回覆後，我們將確認訂單。

Regards,
Sarah
```

### Qwen-MT's Translation with Highlights

```text
Feedback on sample for Order #S20240608

Hi William,

We received the **boardbook** sample, overall it's good, but there are two small issues:

1. One of the pages has slight bubble in the lining, please avoid this in mass production.
2. The **matt coating** on the cover feels a bit thin, some areas have uneven reflection. We want a deeper **matt** effect. Can we use **matt ink** or increase the thickness of the coating?

Please confirm if these issues can be improved in mass production. After your reply, we will confirm the order.

Regards,
Sarah
```

<hr>

## Case 11: Request for a quote on processing fees only (CMT)

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `硬封面` | `hardcover` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
報價請求：來料加工

Hi Steve,

我司將自行提供主要材料，請僅為以下加工服務報價。

- **產品**: **硬封面** 筆記本
- **服務**:
    1.  **裱**: 將我司提供的封面紙張**裱**上 2.5mm **灰板**。
    2.  燙金: 在封面和封底燙印 Logo。
    3.  裝訂: 將我司提供的內頁與封面組裝成冊。
- **數量**: 2,000 本

材料將在下週一送達貴司工廠。請報純加工費用。

謝謝,
Peter
```

### Qwen-MT's Translation with Highlights

```text
Request for quotation: contract manufacturing

Hi Steve,

Our company will provide the main materials, please quote only for the following processing services.

- **Product**: **hardcover** notebook
- **Services**:
    1. **Laminating**: **laminating** the cover paper provided by our company onto 2.5mm **greyboard**.
    2. Foil stamping: foil stamping the logo on the cover and back cover.
    3. Binding: assembling the inner pages provided by our company with the cover into a book.
- **Quantity**: 2,000 copies

The materials will be delivered to your factory next Monday. Please quote the pure processing fee.

Thank you,
Peter
```

<hr>

## Case 12: Quotation comparison for different paper weights

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | `water-based gloss ink` | ✅ Match |
| `書紙` | `book paper` | `book paper` | ✅ Match |

---

### Source Text with Highlights

```text
報價比較：不同克重的**書紙**

Hi Team,

請為以下雜誌報價，我們需要比較不同紙張的成本。

- **尺寸**: A4
- **頁數**: 64pg + 4pg cover
- **裝訂**: 騎馬釘
- **印刷**: 4C+4C

請分別提供以下三種規格的報價 (數量 3k/5k):
- **Spec 1**: 封面 200g 铜版纸, 內頁 128g 铜版纸。
- **Spec 2**: 封面 157g 铜版纸, 內頁 105g 铜版纸。
- **Spec 3**: 封面和內頁全部使用 120g **書紙**。

所有規格均需封面過 **水性亮光油墨**。

Thanks,
Laura
```

### Qwen-MT's Translation with Highlights

```text
Price comparison: different grammage of **book paper**

Hi Team,

Please quote the following magazine, we need to compare the cost of different papers.

- **Size**: A4
- **Pages**: 64pg + 4pg cover
- **Binding**: saddle stitch
- **Printing**: 4C+4C

Please provide the quotation for the following three specifications (quantity 3k/5k) respectively:
- **Spec 1**: Cover 200gsm art paper, inner pages 128gsm art paper.
- **Spec 2**: Cover 157gsm art paper, inner pages 105gsm art paper.
- **Spec 3**: All cover and inner pages use 120g **book paper**.

All specifications require varnishing on the cover with **water-based gloss ink**.

Thanks,
Laura
```

<hr>

## Case 13: Quote for a paperback book with an outer sleeve

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matt coating` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |
| `平装封面` | `paperback` | `paperback` | ✅ Match |
| `套筒` | `sleeve` | `sleeve` | ✅ Match |

---

### Source Text with Highlights

```text
Quote: Paperback with Sleeve

Hi Alice,

Please quote for a paperback book with an outer sleeve.

**Book Spec:**
- **Type**: **平装封面**
- **Size**: 148 x 210mm
- **Cover**: 250gsm art paper, 4C+0C, matt lamination.
- **Text**: 240pp, 80gsm book paper, 1C+1C.

**Sleeve Spec:**
- **Type**: **套筒**
- **Material**: 250gsm **白**卡**纸**
- **Printing**: 4C+0C
- **Finishing**: ****哑光**涂层**

**Quantity**: 3,000 / 5,000 sets.
Please provide separate prices for the book and the sleeve.

Best,
Tom
```

### Qwen-MT's Translation with Highlights

```text
Quote: **Paperback** with **Sleeve**

Hi Alice,

Please quote for a **paperback** book with an outer **sleeve**.

**Book Spec:**
- **Type**: **paperback**
- **Size**: 148 x 210mm
- **Cover**: 250gsm art paper, 4C+0C, **matt** lamination.
- **Text**: 240pp, 80gsm book paper, 1C+1C.

**Sleeve Spec:**
- **Type**: **sleeve**
- **Material**: 250gsm **white **card** paper**
- **Printing**: 4C+0C
- **Finishing**: **matt coating**

**Quantity**: 3,000 / 5,000 sets.
Please provide separate prices for the book and the **sleeve**.

Best,
Tom
```

<hr>

## Case 14: Inquiry about a paper card with a complex die-cut shape

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `紙卡` | `paper card` | `paper card` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
**紙**卡****報價及Die-cut問題

Hi William,

請報價一款形狀不規則的**紙**卡****。

- **材料**: 400g **白**卡**纸**
- **尺寸**: 最大處約 10cm x 8cm
- **印刷**: 4C+1C (背面印黑白文字)
- **加工**: 啞光覆膜, 異形die-cut。
- **數量**: 10,000 / 20,000

附件是刀模線圖。請問這種複雜度的die-cut，刀模費用是多少？

Regards,
Jessica
```

### Qwen-MT's Translation with Highlights

```text
**Paper card** quotation and die-cutting problem

Hi William,

Please quote a **paper card** with irregular shape.

- **Material**: 400g **white **card** paper**
- **Size**: Max. about 10cm x 8cm
- **Printing**: 4C+1C (backside printed in black and white text)
- **Processing**: Matt laminated, special-shaped die-cut.
- **Quantity**: 10,000 / 20,000

Attached is the die-cutting drawing. What is the cost of the die-cutting mold for this kind of complexity?

Regards,
Jessica
```

<hr>

## Case 15: Re-print request with a size modification

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `cardboard` | ✅ Match |

---

### Source Text with Highlights

```text
Re-print request with size modification

Hi Steve,

We need to re-print the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new 內襯. All other specifications, including the 350gsm **纸板** and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,
Alex
```

### Qwen-MT's Translation with Highlights

```text
Re-print request with size modification

Hi Steve,

We need to re-print the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new lining. All other specifications, including the 350gsm **cardboard** and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,
Alex
```

<hr>

## Case 16: Quote for a single book with multiple cover versions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matt laminated` | ✅ Match |

---

### Source Text with Highlights

```text
報價：一書多封面版本

Hi Team,

我們計畫出版一本平装书，但有4個不同的封面設計，以吸引不同市場。

- **內文**: (所有版本相同)
    - 尺寸: 6" x 9"
    - 頁數: 320pp
    - 紙張: 80gsm book paper, 1C+1C
- **封面**: (4個版本，設計不同，規格相同)
    - 紙張: 250gsm 铜版纸
    - 印刷: 4C+0C
    - 處理: ****哑光**覆膜**
- **總數量**: 8,000本 (每個封面版本各 2,000本)

請問這種操作方式，價格是否會比單獨印刷4個2,000本的訂單更有優勢？

Best,
Maria
```

### Qwen-MT's Translation with Highlights

```text
Quotation: multiple cover versions for one book

Hi Team,

We plan to publish a paperback book, but with 4 different cover designs to appeal to different markets.

- **Text**: (same for all versions)
    - Size: 6" x 9"
    - Pages: 320pp
    - Paper: 80gsm book paper, 1C+1C
- **Cover**: (4 versions, different design, same specifications)
    - Paper: 250gsm art paper
    - Printing: 4C+0C
    - Finish: **matt laminated**
- **Total quantity**: 8,000 copies (2,000 copies per cover version)

Would this operation be more advantageous in price than printing 4 separate orders of 2,000 copies each?

Best,
Maria
```

<hr>

## Case 17: Quote request for a hardcover gift box with a magnetic closure

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matt coating` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `盒蓋` | `box cover`, `lid` | `box cover` | ✅ Match |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Quote Request: Hardcover Gift Box with Magnetic Closure

Hi Alice,

Please quote for a high-end gift box with the following specs:

- **Type**: **精装本** style box with magnetic closure.
- **Material**: 157gsm art paper **裱** on 2mm **灰板**.
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - 全局 ****哑光**涂层**.
    - **盒蓋** on top with 燙金 logo.
- **Quantity**: 1,000 / 2,000 pcs.

Please confirm the lead time for a prototype.

Regards,
Daniel
```

### Qwen-MT's Translation with Highlights

```text
Quote Request: **Hardcover** Gift Box with Magnetic Closure

Hi Alice,

Please quote for a high-end gift box with the following specs:

- **Type**: **hardcover** style box with magnetic closure.
- **Material**: 157gsm art paper laminated on 2mm **greyboard**.
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - Global **matt coating**.
    - **Box cover** on top with holographic foil stamping logo.
- **Quantity**: 1,000 / 2,000 pcs.

Please confirm the lead time for a prototype.

Regards,
Daniel
```

<hr>

## Case 18: Inquiry about changing the endpaper material to reduce cost

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `書紙` | `book paper` | `book paper` | ✅ Match |
| `封裡頁` | `endpaper` | `endpaper` | ✅ Match |

---

### Source Text with Highlights

```text
精裝書 **封裡頁** 材料諮詢

Hi Steve,

在上次報價的精裝書 (PO#Q2406-11) 中，我們用了150gsm的花紋紙做 **封裡頁**。

客戶現在想降低成本，請問如果將 **封裡頁** 改為 120gsm 的標準 **書紙**，大概可以節省多少費用？

數量還是 1000 / 2000 本。

Thanks,
Catherine
```

### Qwen-MT's Translation with Highlights

```text
Hardcover **endpaper** material consultation

Hi Steve,

In the last quotation of hardcover (PO#Q2406-11), we used 150gsm textured paper for the **endpaper**.

The client now wants to reduce costs. If we change the **endpaper** to 120gsm standard **book paper**, how much can we save approximately?

The quantity is still 1000/2000 books.

Thanks,
Catherine
```

<hr>

## Case 19: Quotation request for a product kit including a box, cards, and assembly

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `cardboard` | ✅ Match |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matt laminated` | ✅ Match |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
報價請求：產品組合包裝

Hi William,

我們需要為一個產品套裝報價，其中包括一個**彩盒**和幾張**卡**片。

- **Item 1: **彩盒****
    - 尺寸: 300x200x50mm
    - 材料: 250gsm e-flute **纸板**
    - 印刷: 4C+0C, **上光**

- **Item 2: **卡** x 5 designs**
    - 尺寸: 90x50mm
    - 材料: 300gsm 铜版纸
    - 印刷: 4C+4C, ****哑光**覆膜**
    - 數量: 每款設計各 2,000 張 (總共 10,000 張)

- **Item 3: 組裝與包裝**
    - 將5張**卡**片放入**彩盒**中，然後用 收縮膜 進行整體包裝。

請為 2,000 套組合報價，並將每個項目及組裝費用分開列出。

Best regards,
Linda
```

### Qwen-MT's Translation with Highlights

```text
Quotation request: product packaging set

Hi William,

We need a quotation for a product set, which includes a **color box** and several cards.

- **Item 1: Color box**
    - Size: 300x200x50mm
    - Material: 250gsm e-flute **cardboard**
    - Printing: 4C+0C, **varnishing**

- **Item 2: **Card** x 5 designs**
    - Size: 90x50mm
    - Material: 300gsm art paper
    - Printing: 4C+4C, **matt laminated**
    - Quantity: 2,000 each design (total 10,000)

- **Item 3: Assembly and packaging**
    - Insert 5 cards into the **color box**, then wrap the whole with shrink wrap.

Please quote for 2,000 sets, and list each item and assembly cost separately.

Best regards,
Linda
```

<hr>

## Case 20: Urgent request for a single, full-quality sample book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
URGENT Sample Request - Hardcover Book

Hi Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal.

Please produce ONE full sample of the following hardcover book:
- **Type**: **精装本**
- **Size**: 21x21cm
- **Cover**: 157gsm art paper **裱** 2.5mm **灰板**, ****哑光**覆膜**, spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm **哑光**铜版纸, 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark
```

### Qwen-MT's Translation with Highlights

```text
URGENT Sample Request - **Hardcover** Book

Hi Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal.

Please produce ONE full sample of the following **hardcover** book:
- **Type**: **hardcover**
- **Size**: 21x21cm
- **Cover**: 157gsm art paper **laminating** 2.5mm **greyboard**, **matt** coated, spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm **matt** coated paper, 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark
```

<hr>

