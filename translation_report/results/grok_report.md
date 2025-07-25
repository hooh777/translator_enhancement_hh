# Translation Terminology Report (Grok Analysis)

## Overall Metrics Summary

| Case   | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 50.0% (2/4) | 17.9 (Very Difficult)  |
| Case 2 | 42.9% (3/7) | 36.88 (Difficult) |
| Case 3 | 25.0% (1/4) | 46.55 (Difficult) |
| Case 4 | 25.0% (2/8) | 31.89 (Difficult) |
| Case 5 | 66.7% (2/3) | 13.31 (Very Difficult) |
| Case 6 | 100.0% (1/1) | 39.74 (Difficult) |
| Case 7 | 50.0% (3/6) | 36.17 (Difficult) |
| Case 8 | 50.0% (2/4) | 18.12 (Very Difficult) |
| Case 9 | 100.0% (3/3) | 38.16 (Difficult) |
| Case 10 | 75.0% (3/4) | 70.83 (Fairly Easy) |
| Case 11 | 33.3% (1/3) | 44.48 (Difficult) |
| Case 12 | 50.0% (1/2) | 15.48 (Very Difficult) |
| Case 13 | 66.7% (4/6) | 24.34 (Very Difficult) |
| Case 14 | 66.7% (2/3) | 41.74 (Difficult) |
| Case 15 | 100.0% (1/1) | 62.88 (Standard) |
| Case 16 | 50.0% (1/2) | 14.31 (Very Difficult) |
| Case 17 | 66.7% (4/6) | 24.45 (Very Difficult) |
| Case 18 | 100.0% (2/2) | 52.16 (Fairly Difficult) |
| Case 19 | 66.7% (4/6) | 7.8 (Very Difficult) |
| Case 20 |     40.0% (2/5) | 68.5 (Standard) |
| **Average** | **61.2%** | **35.3 (Easy)** |

<hr>

## Case 1: Quotation request for a color box with special coating

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | N/A | ❌ Mismatch / Not Found |
| `克铜版纸` | `gsm art paper`, `gsm coated paper` | `gsm coated paper` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 1

Case 01: Quotation Request for **color box** with Special Coating

Subject: Quotation Request for New Game **color box**

Dear Team,

Please provide a quotation for our new product based on the following specifications, with target quantities of 5,000 and 10,000 units:

Product Type: **color box**
Dimensions: 220mm x 150mm x 40mm
Material: 300 **gsm coated paper** mounted on E-flute corrugated board
Printing: 4-color process (4C + 0C)
Finishing: Glossy aqueous coating overall, with matte ink on the logo for a contrasting effect
Packaging: 50 units per carton, wrapped in shrink film
Please confirm the lead time for sampling and the production schedule for the full order.

Best regards,

David
```

<hr>

## Case 2: Re-quote request for a hardcover book after specification update

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |
| `書紙` | `book paper` | `book paper` | ✅ Match |
| `書套` | `jacket` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi Steve,

感謝您上次的報價。客戶對設計進行了修改，請根據更新後的規格重新報價。

- **內文尺寸**: 240mm(w) x 290mm(h) - 不變
- **皮殼**: 改為使用 157g **哑光**铜版纸 **裱** 3mm **灰板**。
- **表面處理**: 皮殼需要 **哑光**覆膜 及 **燙幻彩** 處理 logo。
- **襯紙**: 150gsm **書紙**
- **數量**: 1,500本 / 3,000本

另外，客戶詢問是否可以為首批50本書提供獨立的**書套**？如果可以，請單獨報價。

Thanks,
Catherine
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 2

Case 02: Re-quote Request for Hardcover Book After Specification Update

Subject: Re: Hardcover Book Quotation - Specification Update

Dear Steve,

Thank you for your previous quotation. The client has made design revisions, and we kindly request a revised quotation based on the updated specifications:

Text Page Dimensions: 240mm (W) x 290mm (H) - unchanged
Case Material: Changed to 157 gsm **matte** coated paper mounted on 3mm gray board
Finishing: **matte** lamination on the case, with **holographic foil stamping** on the logo
Endpaper: 150 gsm **book paper**
Quantity: 1,500 and 3,000 copies
Additionally, the client has inquired whether an independent slipcase can be provided for the first 50 copies. If feasible, please provide a separate quotation for the slipcase.

Thank you,

Catherine
```

<hr>

## Case 3: Urgent order for paper bags for a trade show

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | N/A | ❌ Mismatch / Not Found |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `紙袋` | `paper bag` | `paper bag` | ✅ Match |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 3

Case 03: Urgent Order for Paper Bags for a Trade Show

Subject: Urgent: **paper bag** Quotation for Trade Show

Dear Alice,

We urgently require paper bags for an upcoming trade show next month. Please provide a quotation as soon as possible:

Product Type: **paper bag**
Dimensions: 30cm (H) x 25cm (W) x 10cm (D)
Material: 210 gsm white cardstock
Printing: 4-color process (4C + 0C), using matte ink
Finishing: Matte lamination, with cotton rope handles
Quantity: 500 and 1,000 units
Given the tight timeline, please confirm the earliest possible delivery date. If lamination is not feasible within the timeline, please provide pricing without lamination.

Thank you,

Jack
```

<hr>

## Case 4: Inquiry about materials for a board book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `撲克油` | `poker varnishing`, `Poker Coating` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |
| `硬板书` | `boardbook` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi William,

我們正在規劃一款新的**硬板书**，有幾個關於材料的問題想請教：

我們的設計是 12 pages，想用 400g **白**卡**纸** 對**裱**。請問你們建議用多厚的**灰板** 做內襯 才能保證書本的硬度和耐用性？

另外，封面如果採用 **撲克油** 處理，與普通的 **哑光**涂层 相比，成本大概會增加多少？

請先基於以下暫定規格報價 3000 / 5000 本：
- **尺寸**: 8" x 8"
- **頁數**: 12 pages (6 spreads)
- **材料**: 400g **白**卡**纸**對**裱**
- **印刷**: 4C/4C

期待您的專業建議。

Regards,
Emily
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 4

Case 04: Inquiry About Materials for a Board Book

Subject: Inquiry Regarding Board Book Material Options

Dear William,

We are planning a new board book and have questions regarding material choices:

For a 12-page design using 400 gsm white cardstock laminated together, what thickness of gray board do you recommend for the inner lining to ensure durability and rigidity?

Additionally, if the cover uses poker oil coating instead of standard **matte** coating, how much would the cost increase compared to the standard option?

Please provide a quotation for 3,000 and 5,000 copies based on the following tentative specifications:

Dimensions: 8" x 8"
Pages: 12 pages (6 spreads)
Material: 400 gsm white cardstock laminated
Printing: 4-color process (4C/4C)
We look forward to your professional recommendations.

Regards,

Emily
```

<hr>

## Case 5: Quote for multi-language instruction sheets and packaging

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `上光` | `varnishing`, `coating` | `coating` | ✅ Match |
| `書紙` | `book paper` | `book paper` | ✅ Match |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 5

Case 05: Quote for Multi-Language Instruction Sheets and Packaging

Subject: Quotation Request: Multi-Language Instruction Sheets and Packaging

Dear Teresa,

Please provide a quotation for the following items with quantities of 8,000 and 16,000 units:

Item 1: Tuck-in Box

Material: 350 gsm gray board
Dimensions: 180mm x 100mm x 50mm
Printing: 4-color process (4C + 0C)
Finishing: Glossy **coating**
Item 2: Instruction Sheets (3 Languages)

Dimensions: A4, folded to A6
Material: 105 gsm **book paper**
Printing: 1-color process (1C + 1C)
Note: Three versions with different content, with quantities evenly distributed
Please provide separate quotations for each item.

Thank you,

Ben
```

<hr>

## Case 6: Re-order request with an inquiry about partial shipment

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Dear Joe,

我們上個月訂單 (PO#20240512) 的產品市場反應很好，現需緊急補單。

請為以下產品報價 5,000 件：
- **產品**: **精装本**
- **規格**: 與 PO#20240512 完全相同。

另外，由於市場急需，請問是否可以在完成 2,000 本後立即安排部分出貨？剩下的 3,000 本按正常流程完成。如果可以，請告知相關的物流費用。

Thanks a lot,
Connie
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 6

Case 06: Re-order Request with Inquiry About Partial Shipment

Subject: Re-order Request and Partial Shipment Inquiry

Dear Joe,

The market response to our previous order (PO#20240512) has been excellent, and we urgently need to place a re-order.

Please provide a quotation for 5,000 units of the following product:

Product: **hardcover** Book
Specifications: Identical to PO#20240512
Additionally, due to urgent market demand, is it possible to arrange partial shipment of 2,000 copies upon completion, with the remaining 3,000 copies following the standard schedule? If feasible, please provide the associated logistics costs.

Thank you,

Connie
```

<hr>

## Case 7: Quote for a slipcase with an acrylic board and special foil stamping

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `亞克力板` | `acrylic board`, `acrylic sheet` | `acrylic board` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Steve,

麻煩報價一款特殊的書盒，設計比較複雜。

- **類型**: 書盒
- **適用書籍**: 150mm x 220mm x 30mm
- **材料**: 2mm **灰板** **裱** 128g art paper
- **加工**:
    1.  表面 **哑光**覆膜
    2.  正面需要 **燙幻彩**
    3.  側面嵌入一塊 3mm 厚的透明 **亞克力板**，尺寸為 50mm x 100mm。

- **數量**: 500 / 1000

請問**燙幻彩**除了標準的彩虹色，有其他顏色選擇嗎？**亞克力板**的邊緣可以做拋光處理嗎？

Best regards,
Michael
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 7

Case 07: Quote for a Slipcase with **acrylic board** and Special Foil Stamping

Subject: Quotation for Slipcase with **acrylic board**

Dear Steve,

Please provide a quotation for a complex slipcase with the following specifications:

Product Type: Slipcase
Book Dimensions: 150mm x 220mm x 30mm
Material: 2mm gray board mounted with 128 gsm art paper
Finishing:
**matte** lamination on the surface
**holographic foil stamping** on the front
A 3mm thick transparent acrylic panel (50mm x 100mm) embedded on the side
Quantity: 500 and 1,000 units
Are there color options for **holographic foil stamping** beyond standard rainbow? Can the edges of the acrylic panel be polished?

Best regards,

Michael
```

<hr>

## Case 8: Quotation request for poker cards with different packaging options

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `coating` | ✅ Match |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `撲克油` | `poker varnishing`, `Poker Coating` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 8

Case 08: Quotation Request for Poker Cards with Different Packaging Options

Subject: Poker **card** Quotation

Dear Team,

Please provide a quotation for standard poker cards with the following specifications:

**card** Quantity: 54 cards per deck
Dimensions: 63mm x 88mm
Material: 300 gsm blue core paper
Printing: 4-color process (4C + 4C)
Finishing: Poker oil **coating** on both sides
Packaging Options:
Option A: Standard tuck box, 250 gsm white cardstock, 4-color printing, glossy **coating**
Option B: Shrink film packaging, no paper box
Quantity: 3,000 and 5,000 decks
Please provide separate quotations for Options A and B.

Thank you,

Fiona
```

<hr>

## Case 9: Inquiry about eco-friendly material options for a color box

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Alice,

We are planning a new a new **彩盒** and would like to explore eco-friendly options.

- **Size**: 200 x 200 x 80mm
- **Current Spec**: 300gsm art paper with matt lamination.

Could you please quote the price for the current spec for 5,000 units?
Additionally, could you provide alternative quotes for:
1.  Using FSC certified paper.
2.  Replacing matt lamination with a water-based matt coating (水性**哑光**涂层).

We want to compare the cost and appearance. Could you send us samples of the matt coating finish if available?

Best,
Leo
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 9

Case 09: Inquiry About Eco-Friendly Material Options for a **color box**

Subject: Inquiry for Eco-Friendly Options for **color box**

Dear Alice,

We are planning a new **color box** and wish to explore eco-friendly material options:

Dimensions: 200mm x 200mm x 80mm
Current Specification: 300 gsm art paper with **matte** lamination
Please provide a quotation for 5,000 units based on the current specification. Additionally, please provide alternative quotations for:

Using FSC-certified paper
Replacing **matte** lamination with water-based **matte** coating
We would like to compare cost and appearance. If available, please send samples of the water-based **matte** coating finish.

Best regards,

Leo
```

<hr>

## Case 10: Feedback on sample quality for a board book order

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光油墨` | `matt ink`, `matte ink` | `matte ink` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `硬板书` | `boardbook` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi William,

我們收到了**硬板书** 的樣品，整體不錯，但有兩個小問題：

1.  其中一頁的 內襯 有輕微氣泡，大貨生產時請務必避免。
2.  封面的 **哑光**涂层 感覺有點薄，部分區域反光不均。我們希望是更深沉的 **哑光** 效果。是否可以改用 **哑光**油墨 或者增加塗層厚度？

請確認以上問題能否在大貨中改善。等待您的回覆後，我們將確認訂單。

Regards,
Sarah
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 10

Case 10: Feedback on Sample Quality for a Board Book Order

Subject: Feedback on Sample for Order #S20240608

Dear William,

We have received the board book sample, and the overall quality is good, but there are two minor issues:

One page has slight air bubbles in the inner lining, which must be avoided in full production.
The cover’s **matte** coating appears thin, with uneven gloss in some areas. We prefer a deeper **matte** effect. Is it possible to use **matte** ink or increase the coating thickness?
Please confirm whether these issues can be resolved in full production. We will confirm the order upon your response.

Regards,

Sarah
```

<hr>

## Case 11: Request for a quote on processing fees only (CMT)

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `硬封面` | `hardcover` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 11

Case 11: Request for a Quote on Processing Fees Only (CMT)

Subject: Quotation Request for Cut, Make, Trim (CMT) Services

Dear Steve,

We will provide the primary materials and request a quotation for the following processing services only:

Product: **hardcover** Notebook
Services:
Mounting: Laminate our provided cover paper onto 2.5mm gray board
Foil Stamping: Apply gold foil stamping to the logo on the front and back cover
Binding: Assemble our provided text pages with the cover
Quantity: 2,000 units
Materials will be delivered to your factory next Monday. Please provide a quotation for processing fees only.

Thank you,

Peter
```

<hr>

## Case 12: Quotation comparison for different paper weights

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | N/A | ❌ Mismatch / Not Found |
| `書紙` | `book paper` | `book paper` | ✅ Match |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 12

Case 12: Quotation Comparison for Different Paper Weights

Subject: Quotation Comparison for Different Paper Weights

Dear Team,

Please provide quotations for a magazine, comparing the costs of different paper weights:

Dimensions: A4
Pages: 64 pages + 4-page cover
Binding: Saddle stitching
Printing: 4-color process (4C + 4C)
Please provide quotations for the following specifications (quantities of 3,000 and 5,000):

Spec 1: Cover: 200 gsm coated paper; Text: 128 gsm coated paper
Spec 2: Cover: 157 gsm coated paper; Text: 105 gsm coated paper
Spec 3: Cover and Text: 120 gsm **book paper**
All specifications require a glossy aqueous coating on the cover.

Thank you,

Laura
```

<hr>

## Case 13: Quote for a paperback book with an outer sleeve

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |
| `平装封面` | `paperback` | `paperback` | ✅ Match |
| `套筒` | `sleeve` | `sleeve` | ✅ Match |

---

### Source Text with Highlights

```text
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
- **Finishing**: **哑光**涂层

**Quantity**: 3,000 / 5,000 sets.
Please provide separate prices for the book and the sleeve.

Best,
Tom
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 13

Case 13: Quote for a **paperback** Book with an Outer **sleeve**

Subject: Quotation for **paperback** with **sleeve**

Dear Alice,

Please provide a quotation for a **paperback** book with an outer **sleeve**:

Book Specifications:

Type: **paperback**
Dimensions: 148mm x 210mm
Cover: 250 gsm art paper, 4-color printing (4C + 0C), **matte** lamination
Text: 240 pages, 80 gsm book paper, 1-color printing (1C + 1C)
**sleeve** Specifications:

Type: Outer **sleeve**
Material: 250 gsm white cardstock
Printing: 4-color process (4C + 0C)
Finishing: **matte** coating
Quantity: 3,000 and 5,000 sets

Please provide separate prices for the book and the **sleeve**.

Best regards,

Tom
```

<hr>

## Case 14: Inquiry about a paper card with a complex die-cut shape

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `紙卡` | `paper card` | `paper card` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
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

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 14

Case 14: Inquiry About a **paper **card**** with a Complex Die-Cut Shape

Subject: Quotation and Die-Cut Inquiry for **paper **card****

Dear William,

Please provide a quotation for an irregularly shaped **paper **card****:

Material: 400 gsm white cardstock
Dimensions: Approximately 10cm x 8cm at the widest points
Printing: 4-color process front, 1-color black text back (4C + 1C)
Finishing: Matte lamination, custom die-cut
Quantity: 10,000 and 20,000 units
The die-cut template is attached. What is the cost for the die-cut mold given this complexity?

Regards,

Jessica
```

<hr>

## Case 15: Re-print request with a size modification

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `cardboard` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Steve,

We need to re-print the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new 內襯. All other specifications, including the 350gsm **纸板** and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,
Alex
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 15

Case 15: Re-print Request with Size Modification

Subject: Re-print Request with Size Modification

Dear Steve,

We need to re-print the color boxes from PO#20231105 with a modification:

The original size was 150mm x 150mm x 150mm. The new size is 160mm x 160mm x 160mm to accommodate a new inner lining. All other specifications, including 350 gsm **cardboard** and UV coating, remain unchanged.

Please provide a quotation for 5,000 units.

Thank you,

Alex
```

<hr>

## Case 16: Quote for a single book with multiple cover versions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi Team,

我們計畫出版一本平装书，但有4個不同的封面設計，以吸引不同市場。

- **內文**: (所有版本相同)
    - 尺寸: 6" x 9"
    - 頁數: 320pp
    - 紙張: 80gsm book paper, 1C+1C
- **封面**: (4個版本，設計不同，規格相同)
    - 紙張: 250gsm 铜版纸
    - 印刷: 4C+0C
    - 處理: **哑光**覆膜
- **總數量**: 8,000本 (每個封面版本各 2,000本)

請問這種操作方式，價格是否會比單獨印刷4個2,000本的訂單更有優勢？

Best,
Maria
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 16

Case 16: Quote for a Single Book with Multiple Cover Versions

Subject: Quotation for a Book with Multiple Cover Versions

Dear Team,

We plan to publish a paperback book with four different cover designs to target various markets:

Text (identical for all versions):
Dimensions: 6" x 9"
Pages: 320 pages
Paper: 80 gsm book paper, 1-color printing (1C + 1C)
Cover (four versions, different designs, same specifications):
Paper: 250 gsm coated paper
Printing: 4-color process (4C + 0C)
Finishing: **matte** lamination
Total Quantity: 8,000 copies (2,000 copies per cover version)
Would this approach be more cost-effective than printing four separate orders of 2,000 copies each?

Best regards,

Maria
```

<hr>

## Case 17: Quote request for a hardcover gift box with a magnetic closure

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `盒蓋` | `box cover`, `lid` | `lid` | ✅ Match |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Alice,

Please quote for a high-end gift box with the following specs:

- **Type**: **精装本** style box with magnetic closure.
- **Material**: 157gsm art paper **裱** on 2mm **灰板**.
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - 全局 **哑光**涂层.
    - **盒蓋** on top with 燙金 logo.
- **Quantity**: 1,000 / 2,000 pcs.

Please confirm the lead time for a prototype.

Regards,
Daniel
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 17

Case 17: Quote Request for a **hardcover** Gift Box with Magnetic Closure

Subject: Quotation Request for **hardcover** Gift Box with Magnetic Closure

Dear Alice,

Please provide a quotation for a high-end gift box with the following specifications:

Type: **hardcover**-style box with magnetic closure
Material: 157 gsm art paper mounted on 2mm gray board
Internal Dimensions: 250mm x 180mm x 60mm
Printing: 1-color Pantone Black 6 C (1C + 0C)
Finishing:
Full **matte** coating
Gold foil stamping on the logo on the **lid**
Quantity: 1,000 and 2,000 units
Please confirm the lead time for a prototype.

Regards,

Daniel
```

<hr>

## Case 18: Inquiry about changing the endpaper material to reduce cost

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `書紙` | `book paper` | `book paper` | ✅ Match |
| `封裡頁` | `endpaper` | `endpaper` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Steve,

在上次報價的精裝書 (PO#Q2406-11) 中，我們用了150gsm的花紋紙做 **封裡頁**。

客戶現在想降低成本，請問如果將 **封裡頁** 改為 120gsm 的標準 **書紙**，大概可以節省多少費用？

數量還是 1000 / 2000 本。

Thanks,
Catherine
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 18

Case 18: Inquiry About Changing **endpaper** Material to Reduce Cost

Subject: Inquiry Regarding **endpaper** Material for Hardcover Book

Dear Steve,

In our previous quotation for the hardcover book (PO#Q2406-11), we used 150 gsm textured paper for the endpapers.

To reduce costs, what savings could be achieved by switching to 120 gsm standard **book paper** for the endpapers? The quantities remain 1,000 and 2,000 copies.

Thank you,

Catherine
```

<hr>

## Case 19: Quotation request for a product kit including a box, cards, and assembly

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `cardboard` | ✅ Match |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `上光` | `varnishing`, `coating` | `coating` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi William,

我們需要為一個產品套裝報價，其中包括一個**彩盒**和幾張**卡**片。

- **Item 1: **彩盒****
    - 尺寸: 300x200x50mm
    - 材料: 250gsm e-flute **纸板**
    - 印刷: 4C+0C, **上光**

- **Item 2: **卡** x 5 designs**
    - 尺寸: 90x50mm
    - 材料: 300gsm 铜版纸
    - 印刷: 4C+4C, **哑光**覆膜
    - 數量: 每款設計各 2,000 張 (總共 10,000 張)

- **Item 3: 組裝與包裝**
    - 將5張**卡**片放入**彩盒**中，然後用 收縮膜 進行整體包裝。

請為 2,000 套組合報價，並將每個項目及組裝費用分開列出。

Best regards,
Linda
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 19

Case 19: Quotation Request for a Product Kit Including Box, Cards, and Assembly

Subject: Quotation Request for Product Kit Packaging

Dear William,

We require a quotation for a product kit that includes a **color box** and cards:

Item 1: **color box**
Dimensions: 300mm x 200mm x 50mm
Material: 250 gsm E-flute **cardboard**
Printing: 4-color process (4C + 0C), glossy **coating**
Item 2: Cards (5 Designs)
Dimensions: 90mm x 50mm
Material: 300 gsm coated paper
Printing: 4-color process (4C + 4C), **matte** lamination
Quantity: 2,000 cards per design (10,000 cards total)
Item 3: Assembly and Packaging
Insert 5 cards into each **color box** and package with shrink film
Please provide a quotation for 2,000 kits, with separate pricing for each item and assembly costs.

Best regards,

Linda
```

<hr>

## Case 20: Urgent request for a single, full-quality sample book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal.

Please produce ONE full sample of the following hardcover book:
- **Type**: **精装本**
- **Size**: 21x21cm
- **Cover**: 157gsm art paper **裱** 2.5mm **灰板**, **哑光**覆膜, spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm **哑光**铜版纸, 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark
```

### Grok's Translation with Highlights

```text
// Grok's Translation for Case 20

Case 20: Urgent Request for a Single, Full-Quality Sample Book

Subject: Urgent Sample Request - **hardcover** Book

Dear Joe,

To finalize a project with a client, we urgently need a physical sample of a **hardcover** book to close the deal:

Type: **hardcover** Book
Dimensions: 21cm x 21cm
Cover: 157 gsm art paper mounted on 2.5mm gray board, **matte** lamination, spot UV on the title
Endpaper: 140 gsm black card paper
Text: 128 pages, 157 gsm **matte** coated paper, 4-color printing (4C + 4C)
As this is a rush job, please provide the cost and the fastest possible turnaround time for this single sample. We can arrange a courier for pickup once ready.

This is critical for us. Thank you for your assistance.

Best regards,

Mark
```

<hr>

