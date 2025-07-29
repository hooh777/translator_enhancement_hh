# Translation Terminology Report (Qwen-MT qwen-mt-turbo Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 50.0% (2/4) | 69.46 (Standard) |
| Case 2 | 57.1% (4/7) | 59.34 (Fairly Difficult) |
| Case 3 | 100.0% (4/4) | 75.69 (Easy) |
| Case 4 | 100.0% (8/8) | 48.13 (Difficult) |
| Case 5 | 100.0% (3/3) | 64.47 (Standard) |
| Case 6 | 100.0% (1/1) | 49.48 (Difficult) |
| Case 7 | 100.0% (6/6) | 67.44 (Standard) |
| Case 8 | 100.0% (4/4) | 51.74 (Fairly Difficult) |
| Case 9 | 100.0% (3/3) | 76.13 (Easy) |
| Case 10 | 100.0% (4/4) | 79.39 (Easy) |
| Case 11 | 100.0% (3/3) | 60.96 (Standard) |
| Case 12 | 100.0% (2/2) | 62.75 (Standard) |
| Case 13 | 100.0% (6/6) | 76.86 (Easy) |
| Case 14 | 100.0% (3/3) | 77.14 (Easy) |
| Case 15 | 100.0% (1/1) | 35.37 (Difficult) |
| Case 16 | 100.0% (2/2) | 43.93 (Difficult) |
| Case 17 | 100.0% (6/6) | 72.99 (Easy) |
| Case 18 | 100.0% (2/2) | 80.15 (Easy) |
| Case 19 | 100.0% (6/6) | 54.39 (Fairly Difficult) |
| Case 20 | 100.0% (5/5) | 79.51 (Easy) |
| **Average** | **95.4%** | **64.3 (Standard)** |

<hr>

## Case 1: Quotation request for a color box with special coating

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | `water-based gloss ink` | ✅ Match |
| `克铜版纸` | `gsm art paper`, `gsm coated paper` | N/A | ❌ Mismatch / Not Found |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi Team,

請根據以下規格為我們的新產品報價，目標數量為 5,000 和 10,000 件。

- **產品類型**: **彩盒** (color box)
- **尺寸**: 220mm x 150mm x 40mm
- **材料**: 300**克铜版纸** (300gsm art paper) **裱** E-flute corrugated board
- **印刷**: 4C + 0C
- **表面處理**: 整體上**水性亮光油墨** (overall water-based gloss ink), Logo 部分要求使用 啞光油墨 (matt ink) 形成對比效果。
- **包裝**: 50個/箱，用收縮膜 (shrink wrap) 包好。

請告知打樣時間及大貨生產週期。謝謝！

Best,
David
```

### Qwen-MT's Translation with Highlights

```text
Hi Team,

Please quote for our new product according to the following specifications, with target quantities of 5,000 and 10,000 pieces.

- **Product Type**: **color box**
- **Size**: 220mm x 150mm x 40mm
- **Material**: 300gsm art paper laminated on E-flute corrugated board
- **Printing**: 4C + 0C
- **Surface Treatment**: Overall **water-based gloss ink**, matt ink required for logo area to create contrast effect.
- **Packaging**: 50 pieces/box, shrink wrapped.

Please advise the sample time and mass production lead time. Thank you!

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
Hi Steve,

感謝您上次的報價。客戶對設計進行了修改，請根據更新後的規格重新報價。

- **內文尺寸**: 240mm(w) x 290mm(h) - 不變
- **皮殼**: 改為使用 157g **哑光**铜版纸 (157gsm matte coated paper) **裱** 3mm **灰板** (greyboard)。
- **表面處理**: 皮殼需要 **哑光**覆膜 (matte laminated) 及 **燙幻彩** (holographic foil stamping) 處理 logo。
- **襯紙 (endpaper)**: 150gsm **書紙** (book paper)
- **數量**: 1,500本 / 3,000本

另外，客戶詢問是否可以為首批50本書提供獨立的**書套** (jacket)？如果可以，請單獨報價。

Thanks,
Catherine
```

### Qwen-MT's Translation with Highlights

```text
Hi Steve,

Thank you for your last quotation. The customer has made some modifications to the design, please re-quote according to the updated specifications.

- **Text Size**: 240mm(w) x 290mm(h) - unchanged
- **Cover**: Changed to use 157g matte coated paper (157gsm matte coated paper) laminated with 3mm **greyboard**.
- **Surface Treatment**: The cover needs **matt** lamination and **holographic foil stamping** treatment for the logo.
- **Endpaper**: 150gsm **book paper**
- **Quantity**: 1,500 copies / 3,000 copies

In addition, the customer asked if it is possible to provide individual jackets for the first batch of 50 books? If so, please quote separately.

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
Alice 你好,

我們急需為下個月的展會製作一批**紙袋**，請盡快報價。

- **類型**: **紙袋** (paper bag)
- **尺寸**: 30cm (H) x 25cm (W) x 10cm (D)
- **物料**: 210g **白**卡**纸** (white card paper)
- **印刷**: 4C+0C, 使用啞光油墨 (matte ink)。
- **加工**: 啞光覆膜 (matt lamination), 穿棉繩提手。
- **數量**: 500個 / 1000個

由於時間緊急，請告知最快的交貨日期。如果來不及覆膜，不**上光** (varnishing) 的價格是多少？

麻煩了！
Jack
```

### Qwen-MT's Translation with Highlights

```text
Hi Alice,

We urgently need to produce a batch of paper bags for next month's exhibition. Please provide us with a quotation as soon as possible.

- **Type**: **paper bag**
- **Size**: 30cm (H) x 25cm (W) x 10cm (D)
- **Material**: 210g **white **card** paper**
- **Printing**: 4C+0C, using matte ink.
- **Processing**: Matt laminated, with cotton rope handles.
- **Quantity**: 500 pieces / 1000 pieces

Due to the urgency of the deadline, please let us know the earliest delivery date. If it is not possible to laminate, what would be the price without **varnishing**?

Thank you very much!
Jack
```

<hr>

## Case 4: Inquiry about materials for a board book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `撲克油` | `poker varnishing`, `Poker Coating` | `poker varnishing` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |
| `硬板书` | `boardbook` | `boardbook` | ✅ Match |

---

### Source Text with Highlights

```text
Hi William,

我們正在規劃一款新的**硬板书**，有幾個關於材料的問題想請教：

我們的設計是 12 pages，想用 400g **白**卡**纸** (white card paper) 對**裱**。請問你們建議用多厚的**灰板** (greyboard) 做內襯 (lining) 才能保證書本的硬度和耐用性？

另外，封面如果採用 **撲克油** (poker varnishing) 處理，與普通的 **哑光**涂层 (matte coating) 相比，成本大概會增加多少？

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
Hi William,

We are planning a new **boardbook** and have several questions about materials:

Our design is 12 pages, and we want to use 400g **white **card** paper** for **laminating**. Could you please advise what thickness of **greyboard** should be used for the lining to ensure the book's hardness and durability?

Additionally, if the cover is treated with **poker varnishing** compared to ordinary **matte** coating, how much will the cost increase approximately?

Please provide quotes based on the following tentative specifications for 3000 / 5000 copies:
- **Size**: 8" x 8"
- **Pages**: 12 pages (6 spreads)
- **Material**: 400g **white **card** paper** laminated
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
Hi Teresa,

Please quote for the following items. Quantities: 8k, 16k.

**Item 1: Tuck-in Box**
- **Material**: 350gsm **灰板** (greyboard)
- **Size**: 180 x 100 x 50mm
- **Printing**: 4C+0C
- **Finishing**: **上光** (varnishing)

**Item 2: Instruction Sheets (x3 languages)**
- **Size**: A4, fold to A6
- **Material**: 105gsm **書紙** (book paper)
- **Printing**: 1C+1C
- **Note**: 3個版本內容不同，但數量均分。

請將兩個項目分開報價。謝謝。

Thanks,
Ben
```

### Qwen-MT's Translation with Highlights

```text
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
- **Note**: 3 versions with different content, but quantities are equally divided.

Please quote separately for the two items. Thank you.

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
Dear Joe,

我們上個月訂單 (PO#20240512) 的產品市場反應很好，現需緊急補單。

請為以下產品報價 5,000 件：
- **產品**: **精装本** (hardcover book)
- **規格**: 與 PO#20240512 完全相同。

另外，由於市場急需，請問是否可以在完成 2,000 本後立即安排部分出貨？剩下的 3,000 本按正常流程完成。如果可以，請告知相關的物流費用。

Thanks a lot,
Connie
```

### Qwen-MT's Translation with Highlights

```text
Dear Joe,

The market response to the product in our order last month (PO#20240512) has been very good, and we now need to urgently place a supplementary order.

Please provide a quotation for 5,000 pieces of the following product:
- **Product**: **hardcover** book
- **Specifications**: Exactly the same as PO#20240512.

Additionally, due to urgent market demand, could you please advise whether partial shipment can be arranged immediately after completing 2,000 pieces, with the remaining 3,000 pieces completed according to the normal procedure? If possible, please also inform us of the relevant logistics costs.

Thanks a lot,
Connie
```

<hr>

## Case 7: Quote for a slipcase with an acrylic board and special foil stamping

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matt laminated` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `亞克力板` | `acrylic board`, `acrylic sheet` | `acrylic board` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Steve,

麻煩報價一款特殊的書盒，設計比較複雜。

- **類型**: 書盒 (slipcase)
- **適用書籍**: 150mm x 220mm x 30mm
- **材料**: 2mm **灰板** (greyboard) **裱** 128g art paper
- **加工**:
    1.  表面 **哑光**覆膜 (matte laminated)
    2.  正面需要 **燙幻彩** (holographic foil stamping)
    3.  側面嵌入一塊 3mm 厚的透明 **亞克力板** (acrylic sheet)，尺寸為 50mm x 100mm。

- **數量**: 500 / 1000

請問**燙幻彩**除了標準的彩虹色，有其他顏色選擇嗎？**亞克力板**的邊緣可以做拋光處理嗎？

Best regards,
Michael
```

### Qwen-MT's Translation with Highlights

```text
Hi Steve,

Please quote for a special book box with complicated design.

- **Type**: slipcase
- **Applicable books**: 150mm x 220mm x 30mm
- **Material**: 2mm **greyboard** **laminating** 128g art paper
- **Processing**:
    1. Surface **matt** laminated
    2. Front side needs **holographic foil stamping**
    3. Side embedded a 3mm thick transparent acrylic sheet, size 50mm x 100mm.

- **Quantity**: 500 / 1000

Could you please tell me if there are other colors of **holographic foil stamping** besides the standard rainbow color? Can the edge of the **acrylic board** be polished?

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
Hi Team,

請報價製作標準撲克牌，規格如下：

- ****卡**牌數量**: 54張/副
- **尺寸**: 63 x 88mm
- **材料**: 300gsm 藍芯紙
- **印刷**: 4C+4C
- **表面處理**: 雙面 **撲克油** (poker varnishing)
- **包裝**:
    - **選項A**: 標準 tuck box，250g **白**卡**纸** (white card paper)，4C印刷，**上光** (varnishing)。
    - **選項B**: 用 收縮膜 (shrink wrap) 包裝，不含紙盒。
- **數量**: 3000 / 5000 副

請分別就選項A和選項B報價。

Thanks,
Fiona
```

### Qwen-MT's Translation with Highlights

```text
Hi Team,

Please provide quotations for making standard playing cards with the following specifications:

- **Number of Cards**: 54 cards per deck
- **Size**: 63 x 88mm
- **Material**: 300gsm blue core paper
- **Printing**: 4C+4C
- **Surface Treatment**: Double-sided poker **varnishing**
- **Packaging**:
    - **Option A**: Standard tuck box, 250g **white **card** paper**, 4C printing, **varnishing**.
    - **Option B**: Shrink wrap packaging, without cardboard box.
- **Quantity**: 3000 / 5000 decks

Please provide quotations separately for Option A and Option B.

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
Hi Alice,

We are planning a new a new **彩盒** (color box) and would like to explore eco-friendly options.

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

### Qwen-MT's Translation with Highlights

```text
Hi Alice,

We are planning a new **color box** and would like to explore eco-friendly options.

- **Size**: 200 x 200 x 80mm
- **Current Spec**: 300gsm art paper with **matt** lamination.

Could you please quote the price for the current spec for 5,000 units?
Additionally, could you provide alternative quotes for:
1. Using FSC certified paper.
2. Replacing **matt** lamination with a water-based **matt** coating.

We want to compare the cost and appearance. Could you send us samples of the **matt** coating finish if available?

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
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `硬板书` | `boardbook` | `boardbook` | ✅ Match |

---

### Source Text with Highlights

```text
Hi William,

我們收到了**硬板书** (boardbook) 的樣品，整體不錯，但有兩個小問題：

1.  其中一頁的 內襯 (lining) 有輕微氣泡，大貨生產時請務必避免。
2.  封面的 **哑光**涂层 (matte coating) 感覺有點薄，部分區域反光不均。我們希望是更深沉的 **哑光** (matte) 效果。是否可以改用 **哑光**油墨 (matt ink) 或者增加塗層厚度？

請確認以上問題能否在大貨中改善。等待您的回覆後，我們將確認訂單。

Regards,
Sarah
```

### Qwen-MT's Translation with Highlights

```text
Hi William,

We have received the sample of **boardbook**, and it is good overall, but there are two minor issues:

1. There are slight bubbles in the lining of one page. Please avoid this in mass production.
2. The **matte coating** on the cover feels a bit thin, and some areas have uneven reflection. We hope for a deeper **matt** effect. Could you please use **matt** ink or increase the coating thickness?

Please confirm whether these issues can be improved in mass production. After receiving your reply, we will confirm the order.

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
Hi Steve,

我司將自行提供主要材料，請僅為以下加工服務報價。

- **產品**: **硬封面** (hardcover) 筆記本
- **服務**:
    1.  **裱** (laminating): 將我司提供的封面紙張**裱**上 2.5mm **灰板** (greyboard)。
    2.  燙金: 在封面和封底燙印 Logo。
    3.  裝訂: 將我司提供的內頁與封面組裝成冊。
- **數量**: 2,000 本

材料將在下週一送達貴司工廠。請報純加工費用。

謝謝,
Peter
```

### Qwen-MT's Translation with Highlights

```text
Hi Steve,

Our company will provide the main materials by ourselves. Please only quote for the following processing services.

- **Product**: **hardcover** notebook
- **Services**:
    1. **laminating**: **laminating** the cover paper provided by our company onto 2.5mm **greyboard**.
    2. Foil stamping: foil stamping Logo on the front and back covers.
    3. Binding: assembling the inner pages provided by our company with the cover into a book.
- **Quantity**: 2,000 pieces

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
Hi Team,

請為以下雜誌報價，我們需要比較不同紙張的成本。

- **尺寸**: A4
- **頁數**: 64pg + 4pg cover
- **裝訂**: 騎馬釘
- **印刷**: 4C+4C

請分別提供以下三種規格的報價 (數量 3k/5k):
- **Spec 1**: 封面 200g 铜版纸 (coated paper), 內頁 128g 铜版纸。
- **Spec 2**: 封面 157g 铜版纸, 內頁 105g 铜版纸。
- **Spec 3**: 封面和內頁全部使用 120g **書紙** (book paper)。

所有規格均需封面過 **水性亮光油墨** (water-based gloss ink)。

Thanks,
Laura
```

### Qwen-MT's Translation with Highlights

```text
Hi Team,

Please provide quotations for the following magazine. We need to compare the costs of different papers.

- **Size**: A4
- **Pages**: 64pg + 4pg cover
- **Binding**: saddle stitch
- **Printing**: 4C+4C

Please provide quotations separately for the following three specifications (quantity 3k/5k):
- **Spec 1**: Cover 200g coated paper, inner pages 128g coated paper.
- **Spec 2**: Cover 157g coated paper, inner pages 105g coated paper.
- **Spec 3**: All covers and inner pages use 120g **book paper**.

All specifications require a **water-based gloss ink** coating on the cover.

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
Hi Alice,

Please quote for a paperback book with an outer sleeve.

**Book Spec:**
- **Type**: **平装封面** (paperback)
- **Size**: 148 x 210mm
- **Cover**: 250gsm art paper, 4C+0C, matt lamination.
- **Text**: 240pp, 80gsm book paper, 1C+1C.

**Sleeve Spec:**
- **Type**: **套筒** (sleeve)
- **Material**: 250gsm **白**卡**纸** (white card paper)
- **Printing**: 4C+0C
- **Finishing**: **哑光**涂层 (matte coating)

**Quantity**: 3,000 / 5,000 sets.
Please provide separate prices for the book and the sleeve.

Best,
Tom
```

### Qwen-MT's Translation with Highlights

```text
Hi Alice,

Please provide a quotation for a **paperback** book with an outer **sleeve**.

**Book Spec:**
- **Type**: **paperback** cover
- **Size**: 148 x 210mm
- **Cover**: 250gsm art paper, 4C+0C, **matt** lamination.
- **Text**: 240pp, 80gsm book paper, 1C+1C.

****sleeve** Spec:**
- **Type**: **sleeve**
- **Material**: 250gsm **white **card** paper**
- **Printing**: 4C+0C
- **Finishing**: **matt** coating

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
Hi William,

請報價一款形狀不規則的**紙**卡****。

- **材料**: 400g **白**卡**纸** (white card paper)
- **尺寸**: 最大處約 10cm x 8cm
- **印刷**: 4C+1C (背面印黑白文字)
- **加工**: 啞光覆膜 (matte laminated), 異形die-cut。
- **數量**: 10,000 / 20,000

附件是刀模線圖。請問這種複雜度的die-cut，刀模費用是多少？

Regards,
Jessica
```

### Qwen-MT's Translation with Highlights

```text
Hi William,

Please quote for an irregular-shaped **paper **card****.

- **Material**: 400g **white **card** paper**
- **Size**: max. about 10cm x 8cm
- **Printing**: 4C+1C (black and white text printed on the back)
- **Processing**: matte laminated, die-cut.
- **Quantity**: 10,000 / 20,000

Attached is the die-cutting template. Could you please tell me how much the die-cutting mold fee is for this level of complexity?

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
Hi Steve,

We need to re-print the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new 內襯 (lining). All other specifications, including the 350gsm **纸板** (paperboard) and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,
Alex
```

### Qwen-MT's Translation with Highlights

```text
Hi Steve,

We need to reprint the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new lining. All other specifications, including the 350gsm **cardboard** and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,
Alex

I've included some words from a bilingual dictionary. If you find these words in the sentence, please translate them as follows:

Word: 纸板
Translation: **cardboard**
---
Word: 内衬
Translation: lining
---
Word: 水性亮光油墨
Translation: water-based gloss ink
---
Word: 克铜版纸
Translation: gsm art paper
---
Word: 水性哑光油墨
Translation: matt ink
---
Word: 哑光涂层
Translation: matt coating
---
Word: 哑光覆膜
Translation: matte laminated
---
Word: 灰板
Translation: greyboard
---
Word: 上光
Translation: varnishing
---
Word: 白卡纸
Translation: white card paper
---
Word: 收缩膜
Translation: shrink wrap
---
Word: 包装
Translation: packaging
---
Word: 彩盒
Translation: color box
---
Word: 紙袋
Translation: paper bag
---
Word: 紙卡
Translation: paper card
---
Word: 亞克力板
Translation: acrylic board
---
Word: 撲克油
Translation: poker varnishing
---
Word: 裱
Translation: laminating
---
Word: 盒蓋
Translation: box cover
---
Word: 燙幻彩
Translation: holographic foil stamping
---
Word: 書紙
Translation: book paper
---
Word: 书盒
Translation: slipcase
---
Word: 卡
Translation: card
---
Word: 衬纸
Translation: endpaper
---
Word: 封裡頁
Translation: endpaper
---
Word: 硬封面
Translation: hardcover
---
Word: 精装本
Translation: hardcover
---
Word: 書套
Translation: jacket
---
Word: 平装封面
Translation: paperback
---
Word: 软封面
Translation: paperback
---
Word: 硬板书
Translation: boardbook
---
Word: 纸板书
Translation: boardbook
---
```

<hr>

## Case 16: Quote for a single book with multiple cover versions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Team,

我們計畫出版一本平装书 (paperback)，但有4個不同的封面設計，以吸引不同市場。

- **內文**: (所有版本相同)
    - 尺寸: 6" x 9"
    - 頁數: 320pp
    - 紙張: 80gsm book paper, 1C+1C
- **封面**: (4個版本，設計不同，規格相同)
    - 紙張: 250gsm 铜版纸 (coated paper)
    - 印刷: 4C+0C
    - 處理: **哑光**覆膜 (matte laminated)
- **總數量**: 8,000本 (每個封面版本各 2,000本)

請問這種操作方式，價格是否會比單獨印刷4個2,000本的訂單更有優勢？

Best,
Maria
```

### Qwen-MT's Translation with Highlights

```text
Hi Team,

We plan to publish a paperback book, but we have 4 different cover designs to appeal to different markets.

- **Content**: (all versions are the same)
    - Size: 6" x 9"
    - Pages: 320pp
    - Paper: 80gsm book paper, 1C+1C
- **Cover**: (4 versions, different designs, same specifications)
    - Paper: 250gsm coated paper
    - Printing: 4C+0C
    - Finishing: **matte** laminated
- **Total Quantity**: 8,000 copies (2,000 copies for each cover version)

Could you please advise whether this approach would be more advantageous in terms of pricing compared to placing four separate orders of 2,000 copies each?

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
| `裱` | `laminating` | `laminating` | ✅ Match |
| `盒蓋` | `box cover`, `lid` | `box cover` | ✅ Match |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Alice,

Please quote for a high-end gift box with the following specs:

- **Type**: **精装本** (hardcover) style box with magnetic closure.
- **Material**: 157gsm art paper **裱** (laminating) on 2mm **灰板** (greyboard).
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - 全局 **哑光**涂层 (matte coating).
    - **盒蓋** (box cover) on top with 燙金 (foil stamping) logo.
- **Quantity**: 1,000 / 2,000 pcs.

Please confirm the lead time for a prototype.

Regards,
Daniel
```

### Qwen-MT's Translation with Highlights

```text
Hi Alice,

Please quote for a high-end gift box with the following specs:

- **Type**: **hardcover** style box with magnetic closure.
- **Material**: 157gsm art paper **laminating** on 2mm **greyboard**.
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - Full **matt** coating.
    - **box cover** on top with holographic foil stamping logo.
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
Hi Steve,

在上次報價的精裝書 (PO#Q2406-11) 中，我們用了150gsm的花紋紙做 **封裡頁** (endpaper)。

客戶現在想降低成本，請問如果將 **封裡頁** 改為 120gsm 的標準 **書紙** (book paper)，大概可以節省多少費用？

數量還是 1000 / 2000 本。

Thanks,
Catherine
```

### Qwen-MT's Translation with Highlights

```text
Hi Steve,

In the last quotation for the hardcover book (PO#Q2406-11), we used 150gsm patterned paper for the **endpaper**.

Now the customer wants to reduce costs. Could you please tell me how much money can be saved if the **endpaper** is changed to standard **book paper** of 120gsm?

The quantity is still 1000 / 2000 copies.

Thanks,
Catherine
```

<hr>

## Case 19: Quotation request for a product kit including a box, cards, and assembly

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `cardboard` | ✅ Match |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
Hi William,

我們需要為一個產品套裝報價，其中包括一個**彩盒**和幾張**卡**片。

- **Item 1: **彩盒** (Color Box)**
    - 尺寸: 300x200x50mm
    - 材料: 250gsm e-flute **纸板** (paperboard)
    - 印刷: 4C+0C, **上光** (varnishing)

- **Item 2: **卡** (Card) x 5 designs**
    - 尺寸: 90x50mm
    - 材料: 300gsm 铜版纸 (art paper)
    - 印刷: 4C+4C, **哑光**覆膜 (matte laminated)
    - 數量: 每款設計各 2,000 張 (總共 10,000 張)

- **Item 3: 組裝與包裝**
    - 將5張**卡**片放入**彩盒**中，然後用 收縮膜 (shrink film) 進行整體包裝。

請為 2,000 套組合報價，並將每個項目及組裝費用分開列出。

Best regards,
Linda
```

### Qwen-MT's Translation with Highlights

```text
Hi William,

We need a quotation for a product package, which includes a **color box** and several cards.

- **Item 1: **color box****
    - Size: 300x200x50mm
    - Material: 250gsm e-flute **cardboard**
    - Printing: 4C+0C, **varnishing**

- **Item 2: **card** x 5 designs**
    - Size: 90x50mm
    - Material: 300gsm art paper
    - Printing: 4C+4C, **matte** laminated
    - Quantity: 2,000 pieces of each design (total 10,000 pieces)

- **Item 3: Assembly and Packaging**
    - Place 5 cards into the **color box**, then wrap the whole package with shrink film.

Please provide a quotation for 2,000 sets, listing each item and assembly costs separately.

Best regards,
Linda
```

<hr>

## Case 20: Urgent request for a single, full-quality sample book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Qwen-MT's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | `matte laminated` | ✅ Match |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | `laminating` | ✅ Match |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal.

Please produce ONE full sample of the following hardcover book:
- **Type**: **精装本** (hardcover)
- **Size**: 21x21cm
- **Cover**: 157gsm art paper **裱** 2.5mm **灰板** (greyboard), **哑光**覆膜 (matte laminated), spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm **哑光**铜版纸 (matte coated paper), 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark
```

### Qwen-MT's Translation with Highlights

```text
Hi Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal.

Please produce ONE full sample of the following **hardcover** book:
- **Type**: **hardcover**
- **Size**: 21x21cm
- **Cover**: 157gsm art paper **laminating** 2.5mm **greyboard**, **matte laminated**, spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm **matt** coated paper, 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark
```

<hr>

