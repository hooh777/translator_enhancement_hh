# Translation Terminology Report (Grok Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 75.0% (3/4) | 61.28 (Standard) |
| Case 2 | 85.7% (6/7) | 51.32 (Fairly Difficult) |
| Case 3 | 100.0% (4/4) | 68.09 (Standard) |
| Case 4 | 75.0% (6/8) | 38.24 (Difficult) |
| Case 5 | 100.0% (3/3) | 55.98 (Fairly Difficult) |
| Case 6 | 100.0% (1/1) | 44.06 (Difficult) |
| Case 7 | 83.3% (5/6) | 55.69 (Fairly Difficult) |
| Case 8 | 100.0% (4/4) | 50.9 (Fairly Difficult) |
| Case 9 | 100.0% (3/3) | 61.09 (Standard) |
| Case 10 | 75.0% (3/4) | 70.67 (Fairly Easy) |
| Case 11 | 100.0% (3/3) | 56.55 (Fairly Difficult) |
| Case 12 | 100.0% (2/2) | 59.63 (Fairly Difficult) |
| Case 13 | 100.0% (6/6) | 68.52 (Standard) |
| Case 14 | 100.0% (3/3) | 56.51 (Fairly Difficult) |
| Case 15 | 100.0% (1/1) | 69.11 (Standard) |
| Case 16 | 100.0% (2/2) | 40.41 (Difficult) |
| Case 17 | 83.3% (5/6) | 29.15 (Very Difficult) |
| Case 18 | 100.0% (2/2) | 65.47 (Standard) |
| Case 19 | 83.3% (5/6) | 49.52 (Difficult) |
| Case 20 | 80.0% (4/5) | 77.13 (Fairly Easy) |
| **Average** | **92.0%** | **56.5 (Standard)** |

<hr>

## Case 1: Quotation request for a color box with special coating

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | `water-based gloss ink` | ✅ Match |
| `克铜版纸` | `gsm art paper`, `gsm coated paper` | `gsm art paper` | ✅ Match |
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
Subject: Quote Request: New Game **color box**

Body:

Hi Team,

Please provide a quotation for our new product based on the following specifications, with target quantities of 5,000 and 10,000 units.

Product Type: **color box**
Dimensions: 220mm x 150mm x 40mm
Material: 300 **gsm art paper** laminated onto E-flute corrugated board
Printing: 4C + 0C
Surface Finishing: Overall **water-based gloss ink**, with the logo area using matte ink for a contrasting effect.
Packaging: 50 units per carton, packed with shrink wrap.
Please advise on the lead time for sampling and the production cycle for bulk orders. Thank you!

Best,

David
```

<hr>

## Case 2: Re-quote request for a hardcover book after specification update

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |
| `書紙` | `book paper` | `book paper` | ✅ Match |
| `書套` | `jacket` | `jacket` | ✅ Match |

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
Subject: RE: Hardcover Book Quotation - Specification Update

Body:

Hi Steve,

Thank you for your previous quotation. The client has made design changes, so please provide a revised quotation based on the updated specifications.

Text Block Dimensions: 240mm (W) x 290mm (H) - unchanged
Case: Changed to 157 gsm **matte** coated paper laminated onto 3mm **greyboard**.
Surface Finishing: The case requires **matte** laminated finish and **holographic foil stamping** for the logo.
Endpaper: 150 gsm **book paper**
Quantity: 1,500 / 3,000 copies
Additionally, the client is inquiring whether an independent book **jacket** can be provided for the first 50 copies. If feasible, please provide a separate quotation for this.

Thanks,

Catherine
```

<hr>

## Case 3: Urgent order for paper bags for a trade show

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `紙袋` | `paper bag` | `paper bag` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

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
Subject: URGENT: **paper bag** Quotation - Urgent for Trade Show

Body:

Hi Alice,

We urgently need a batch of paper bags for next month’s trade show. Please provide a quotation as soon as possible.

Type: **paper bag**
Dimensions: 30cm (H) x 25cm (W) x 10cm (D)
Material: 210 gsm **white **card** paper**
Printing: 4C + 0C, using matte ink.
Finishing: Matte laminated, with cotton rope handles.
Quantity: 500 / 1,000 units
Due to the tight timeline, please confirm the earliest possible delivery date. If lamination is not feasible within the timeline, what would be the cost without **varnishing**?

Thank you!

Jack
```

<hr>

## Case 4: Inquiry about materials for a board book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `撲克油` | `poker varnishing`, `Poker Coating` | `poker varnishing` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | `card` | ✅ Match |
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
Subject: Inquiry Regarding Board Book Material

Body:

Hi William,

We are planning a new board book and have some questions about materials:

Our design consists of 12 pages, using 400 gsm **white **card** paper** laminated together. What thickness of **greyboard** do you recommend for the lining to ensure the book’s rigidity and durability?

Additionally, if the cover is treated with **poker varnishing** compared to a standard **matte** coating, approximately how much would the cost increase?

Please provide a quotation for 3,000 / 5,000 copies based on the following tentative specifications:

Dimensions: 8" x 8"
Pages: 12 pages (6 spreads)
Material: 400 gsm **white **card** paper** laminated together
Printing: 4C/4C
We look forward to your professional recommendations.

Regards,

Emily
```

<hr>

## Case 5: Quote for multi-language instruction sheets and packaging

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
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
Subject: Quote Request: Multi-language Instruction Sheet & Packaging

Body:

Hi Teresa,

Please provide a quotation for the following items. Quantities: 8,000 and 16,000 units.

Item 1: Tuck-in Box

Material: 350 gsm **greyboard**
Size: 180 x 100 x 50mm
Printing: 4C + 0C
Finishing: **varnishing**
Item 2: Instruction Sheets (x3 languages)

Size: A4, folded to A6
Material: 105 gsm **book paper**
Printing: 1C + 1C
Note: Three versions with different content, with quantities evenly distributed.
Please provide separate quotations for the two items. Thank you.

Thanks,

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
Subject: Re-order Request & Partial Shipment Inquiry

Body:

Dear Joe,

The market response to our last order (PO#20240512) has been excellent, and we urgently need to place a re-order.

Please provide a quotation for 5,000 units of the following product:

Product: **hardcover** book
Specifications: Identical to PO#20240512
Additionally, due to urgent market demand, is it possible to arrange partial shipment of 2,000 copies upon completion, with the remaining 3,000 copies completed per the standard process? If feasible, please provide the associated logistics costs.

Thanks a lot,

Connie
```

<hr>

## Case 7: Quote for a slipcase with an acrylic board and special foil stamping

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `亞克力板` | `acrylic board`, `acrylic sheet` | `acrylic sheet` | ✅ Match |
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
Subject: Quote: Slipcase with **acrylic sheet**

Body:

Hi Steve,

Please provide a quotation for a complex slipcase design.

Type: Slipcase
Book Dimensions: 150mm x 220mm x 30mm
Material: 2mm **greyboard** laminated with 128 gsm art paper
Finishing:
**matte** laminated surface
**holographic foil stamping** on the front
A 3mm thick transparent **acrylic sheet** (50mm x 100mm) embedded on the side.
Quantity: 500 / 1,000 units
Are there color options for **holographic foil stamping** beyond the standard rainbow effect? Can the edges of the **acrylic sheet** be polished?

Best regards,

Michael
```

<hr>

## Case 8: Quotation request for poker cards with different packaging options

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `撲克油` | `poker varnishing`, `Poker Coating` | `poker varnishing` | ✅ Match |
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
Subject: Poker Cards Quote

Body:

Hi Team,

Please provide a quotation for standard poker cards with the following specifications:

**card** Quantity: 54 cards per deck
Dimensions: 63 x 88mm
Material: 300 gsm blue core paper
Printing: 4C + 4C
Surface Finishing: Poker **varnishing** on both sides
Packaging:
Option A: Standard tuck box, 250 gsm **white **card** paper**, 4C printing, **varnishing**.
Option B: Shrink wrap packaging, without a paper box.
Quantity: 3,000 / 5,000 decks
Please provide separate quotations for Options A and B.

Thanks,

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
Subject: Inquiry for Eco-Friendly Options for **color box**

Body:

Hi Alice,

We are planning a new **color box** and would like to explore eco-friendly options.

Size: 200 x 200 x 80mm
Current Specification: 300 gsm art paper with **matte** laminated finish.
Could you please quote the price for the current specification for 5,000 units?

Additionally, please provide alternative quotations for:

Using FSC-certified paper.
Replacing **matte** lamination with a water-based **matte** coating.
We want to compare the cost and appearance. Could you send samples of the **matte** coating finish if available?

Best,

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
Subject: Feedback on Sample for Order #S20240608

Body:

Hi William,

We have received the board book sample, and the overall quality is good, but there are two minor issues:

One page’s lining has slight air bubbles, which must be avoided in bulk production.
The cover’s **matte** coating feels slightly thin, with uneven reflection in some areas. We prefer a deeper **matte** effect. Is it possible to use **matte** ink or increase the coating thickness?
Please confirm whether these issues can be resolved in bulk production. We will confirm the order upon your response.

Regards,

Sarah
```

<hr>

## Case 11: Request for a quote on processing fees only (CMT)

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
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
Subject: Quote Request: CMT (Cut, Make, Trim) Processing

Body:

Hi Steve,

Our company will supply the primary materials. Please provide a quotation for the following processing services only.

Product: **hardcover** notebook
Services:
**laminating**: Mount our supplied cover paper onto 2.5mm **greyboard**.
Foil Stamping: Apply foil stamping for the logo on the front and back covers.
Binding: Assemble our supplied text pages with the cover.
Quantity: 2,000 units
The materials will be delivered to your factory next Monday. Please quote the processing fees only.

Thank you,

Peter
```

<hr>

## Case 12: Quotation comparison for different paper weights

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | `water-based gloss ink` | ✅ Match |
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
Subject: Quotation Comparison: Different Paper Weights for **book paper**

Body:

Hi Team,

Please provide quotations for a magazine, comparing the costs of different paper weights.

Dimensions: A4
Pages: 64 pages + 4-page cover
Binding: Saddle stitch
Printing: 4C + 4C
Please provide quotations for the following three specifications (quantities: 3,000 / 5,000):

Spec 1: Cover: 200 gsm coated paper; Text: 128 gsm coated paper.
Spec 2: Cover: 157 gsm coated paper; Text: 105 gsm coated paper.
Spec 3: Cover and Text: 120 gsm **book paper**.
All specifications require the cover to be finished with **water-based gloss ink**.

Thanks,

Laura
```

<hr>

## Case 13: Quote for a paperback book with an outer sleeve

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |
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
Subject: Quote: **paperback** with **sleeve**

Body:

Hi Alice,

Please provide a quotation for a **paperback** book with an outer **sleeve**.

Book Specifications:

Type: **paperback**
Size: 148 x 210mm
Cover: 250 gsm art paper, 4C + 0C, **matte** laminated.
Text: 240 pages, 80 gsm book paper, 1C + 1C.
**sleeve** Specifications:

Type: **sleeve**
Material: 250 gsm **white **card** paper**
Printing: 4C + 0C
Finishing: **matte** coating
Quantity: 3,000 / 5,000 sets.

Please provide separate prices for the book and the **sleeve**.

Best,

Tom
```

<hr>

## Case 14: Inquiry about a paper card with a complex die-cut shape

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
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
Subject: **paper **card**** Quotation and Die-cut Inquiry

Body:

Hi William,

Please provide a quotation for an irregularly shaped **paper **card****.

Material: 400 gsm **white **card** paper**
Dimensions: Approximately 10cm x 8cm at the widest point
Printing: 4C + 1C (back printed with black-and-white text)
Finishing: Matte laminated, irregular die-cut.
Quantity: 10,000 / 20,000 units
The die-cut template is attached. What is the cost for a die-cut mold of this complexity?

Regards,

Jessica
```

<hr>

## Case 15: Re-print request with a size modification

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `paperboard` | ✅ Match |

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
Subject: Re-print Request with Size Modification

Body:

Hi Steve,

We need to re-print the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new lining. All other specifications, including the 350 gsm **paperboard** and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,

Alex
```

<hr>

## Case 16: Quote for a single book with multiple cover versions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |

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
Subject: Quote: Single Book with Multiple Cover Versions

Body:

Hi Team,

We plan to publish a paperback book with four different cover designs to target different markets.

Text Block (identical for all versions):
Dimensions: 6" x 9"
Pages: 320 pages
Paper: 80 gsm book paper, 1C + 1C
Cover (4 versions with different designs, same specifications):
Paper: 250 gsm coated paper
Printing: 4C + 0C
Finishing: **matte** laminated
Total Quantity: 8,000 copies (2,000 copies per cover version)
Would this approach be more cost-effective than printing four separate orders of 2,000 copies each?

Best,

Maria
```

<hr>

## Case 17: Quote request for a hardcover gift box with a magnetic closure

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `盒蓋` | `box cover`, `lid` | `box cover` | ✅ Match |
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
Subject: Quote Request: **hardcover** Gift Box with Magnetic Closure

Body:

Hi Alice,

Please provide a quotation for a high-end gift box with the following specifications:

Type: **hardcover** style box with magnetic closure
Material: 157 gsm art paper laminated onto 2mm **greyboard**
Size (Internal): 250 x 180 x 60mm
Printing: 1C (Pantone Black 6 C) + 0C
Finishing:
Overall **matte** coating
Foil stamping logo on the **box cover**
Quantity: 1,000 / 2,000 units
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
Subject: Hardcover Book **endpaper** Material Inquiry

Body:

Hi Steve,

In our previous quotation for the hardcover book (PO#Q2406-11), we used 150 gsm textured paper for the **endpaper**.

The client now wishes to reduce costs. How much could we save by switching the **endpaper** to 120 gsm standard **book paper**?

The quantity remains 1,000 / 2,000 copies.

Thanks,

Catherine
```

<hr>

## Case 19: Quotation request for a product kit including a box, cards, and assembly

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `paperboard` | ✅ Match |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
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
Subject: Quote Request: Product Kit Packaging

Body:

Hi William,

We need a quotation for a product kit that includes a **color box** and several cards.

Item 1: **color box**
Dimensions: 300 x 200 x 50mm
Material: 250 gsm E-flute **paperboard**
Printing: 4C + 0C, **varnishing**
Item 2: Cards (5 designs)
Dimensions: 90 x 50mm
Material: 300 gsm art paper
Printing: 4C + 4C, **matte** laminated
Quantity: 2,000 cards per design (total 10,000 cards)
Item 3: Assembly and Packaging
Insert 5 cards into the **color box**, then package the kit with shrink film.
Please provide a quotation for 2,000 kits, with separate pricing for each item and the assembly cost.

Best regards,

Linda
```

<hr>

## Case 20: Urgent request for a single, full-quality sample book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
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
Subject: URGENT Sample Request - **hardcover** Book

Body:

Hi Joe,

We are finalizing a project with a client and urgently need a physical sample to close the deal.

Please produce ONE full sample of the following **hardcover** book:

Type: **hardcover**
Size: 21 x 21cm
Cover: 157 gsm art paper laminated onto 2.5mm **greyboard**, **matte** laminated, with spot UV on the title.
Endpaper: 140 gsm black card paper
Text: 128 pages, 157 gsm **matte** coated paper, 4C + 4C
We understand this is a rush job. Please provide the cost and the fastest possible turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Thank you for your help.

Thanks,

Mark
```

<hr>

