# Translation Terminology Report (Grok Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 0.0% (0/4) | 54.22 (Fairly Difficult) |
| Case 2 | 0.0% (0/7) | 82.03 (Easy) |
| Case 3 | 0.0% (0/4) | 76.78 (Fairly Easy) |
| Case 4 | 0.0% (0/8) | 62.71 (Standard) |
| Case 5 | 0.0% (0/3) | 72.78 (Fairly Easy) |
| Case 6 | 0.0% (0/1) | 66.94 (Standard) |
| Case 7 | 0.0% (0/6) | 76.54 (Fairly Easy) |
| Case 8 | 50.0% (2/4) | 72.05 (Fairly Easy) |
| Case 9 | 66.7% (2/3) | 64.08 (Standard) |
| Case 10 | 0.0% (0/4) | 81.29 (Easy) |
| Case 11 | 0.0% (0/3) | 67.97 (Standard) |
| Case 12 | 0.0% (0/2) | 50.05 (Fairly Difficult) |
| Case 13 | 50.0% (3/6) | 84.9 (Easy) |
| Case 14 | 100.0% (3/3) | 56.27 (Fairly Difficult) |
| Case 15 | 0.0% (0/1) | 76.02 (Fairly Easy) |
| Case 16 | 0.0% (0/2) | 36.47 (Difficult) |
| Case 17 | 0.0% (0/6) | 76.0 (Fairly Easy) |
| Case 18 | 0.0% (0/2) | 87.77 (Easy) |
| Case 19 | 16.7% (1/6) | 60.5 (Standard) |
| Case 20 | 20.0% (1/5) | 86.28 (Easy) |
| **Average** | **15.2%** | **69.6 (Fairly Difficult)** |

<hr>

## Case 1: Quotation request for a color box with special coating

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | N/A | ❌ Mismatch / Not Found |
| `克铜版纸` | `gsm art paper`, `gsm coated paper` | N/A | ❌ Mismatch / Not Found |
| `彩盒` | `color box` | N/A | ❌ Mismatch / Not Found |
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
**Translated English:**

Dear Team,

Please provide the pricing for your new product, with a target quantity of 5,000 and 10,000 units.

- **Product Category**: Boxes
- **Size**: 220mm x 150mm x 40mm
- **Material**: 300g of copper plate paper coated with E-flute corrugated board
- **Printing**: 4C + 0C
- **Surface Treatment**: The entire box is treated with a water-based high-gloss oil ink, while the logo requires a哑光油墨形成对比效果。
- **Packaging**: 50 boxes/pack, wrapped in a compressed mold.

Please inform the production schedule and the production period. Thank you.

Best,
David

In this translation, I have maintained the original meaning and context of the text while providing a professional and clear English version. I have also preserved the original words, numbers, and abbreviations, and integrated them naturally into the final English sentence structure.
```

<hr>

## Case 2: Re-quote request for a hardcover book after specification update

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | N/A | ❌ Mismatch / Not Found |
| `書紙` | `book paper` | N/A | ❌ Mismatch / Not Found |
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
Hi Steve,

Thank you for your previous feedback. Your project has been refined, and I'd like to re-submit your initial quote based on the updated specifications.

- **纸张尺寸**: 240mm(w) x 290mm(h) - Not changed
- **纸张质量**: 改為使用157g的哑光铜版纸，并覆膜3mm以增加光泽。
- **表面处理**: 需要哑光覆膜及烫彩处理，以保护纸张并提升其视觉效果。
- **衬纸质量**: 150gsm的衬纸
- **数量**: 1500本 / 3000本

另外，您是否可以提供一份50本的独立书套报价？如果可以，请提供单独的报价。

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
| `紙袋` | `paper bag` | N/A | ❌ Mismatch / Not Found |
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
Hello Alice,

I am in need of your assistance in preparing a batch of boxes for our upcoming exhibition. Could you please provide an estimate of the price?

- **Box Type**: Boxes
- **Box Size**: 30cm (H) x 25cm (W) x 10cm (D)
- **Material**: 210g White Cardstock
- **Printing**: 4C+0C, Using哑光印刷墨
- **Processing**: 哑光覆膜, 穿棉绳提手
- **Quantity**: 500 boxes / 1000 boxes

Since time is of the essence, please inform me of the fastest shipping date. If you are unable to apply the覆膜 before the shipping date, what is the price of the boxes without the覆膜?

I am concerned.

Jack
```

<hr>

## Case 4: Inquiry about materials for a board book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
| `哑光涂层` | `matt coating`, `matte coating` | N/A | ❌ Mismatch / Not Found |
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
**Answer:**

Hi William,

We are planning to develop a hard-sided book with 12 pages. We need your advice on the materials we should use for embossing. Could you recommend the thickness of the coated paper needed to ensure the book's hardness and durability?

Additionally, if the cover is processed with powdered kerosene, the cost will be higher than the normal glazing. Could you estimate the cost increase for this process?

Please base your recommendations on the following specifications:

- **Size**: 8 inches x 8 inches
- **Page Count**: 12 pages (6 spreads)
- **Material**: 400g white cardboard embossed
- **Printing**: 4C/4C

Thank you for your expert advice.

Regards,
Emily
```

<hr>

## Case 5: Quote for multi-language instruction sheets and packaging

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `上光` | `varnishing`, `coating` | N/A | ❌ Mismatch / Not Found |
| `書紙` | `book paper` | N/A | ❌ Mismatch / Not Found |

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
Subject: Quote for Items

Dear Ben,

I hope this message finds you well. I would like to request a quote for the items you have provided. Please provide the following details:

* Quantities: 8K, 16K
* Item 1: Tuck-in Box
	+ Material: 350gsm 灰板
	+ Size: 180 x 100 x 50mm
	+ Printing: 4C+0C
	+ Finishing: 上光
* Item 2: Instruction Sheets (x3 languages)
	+ Size: A4, fold to A6
	+ Material: 105gsm 書紙
	+ Printing: 1C+1C
	+ Note: 3 versions contain different content, but all have the same number of sheets.

Please provide the final quote for each item. I appreciate your prompt attention to this matter.

Thank you,

Ben
```

<hr>

## Case 6: Re-order request with an inquiry about partial shipment

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `精装本` | `hardcover`, `hardback` | N/A | ❌ Mismatch / Not Found |

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
Dear Joe,

I am pleased to inform you that the order for the next month has been well received, and we need to expedite the order.

Please provide the price for the following products:
- **Product**:精装本
- **Format**: identical to PO#20240512

Additionally, we are in need of your assistance regarding the following:
- **Market Demand**: We are experiencing a significant market demand for your product.
- **Timeline**: We need to arrange for the shipment of the completed 2,000 products within the next 48 hours.
- **Payment Terms**: The payment terms for the completed 3,000 products are as follows:
  - The payment will be made within 48 hours of the completion of the 2,000 products.
  - The payment will be made at the end of the 3,000 products.

Thank you for your prompt response.

Best regards,
Connie
```

<hr>

## Case 7: Quote for a slipcase with an acrylic board and special foil stamping

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `亞克力板` | `acrylic board`, `acrylic sheet` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | N/A | ❌ Mismatch / Not Found |

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
Hi Steve,

I'm having some concerns about a special book box design that's quite complex.

- **Type**: Book box
- **Applicable books**: 150mm x 220mm x 30mm
- **Materials**: 2mm 灰板 覆膜 128g 彩色纸张
- **Processing**:
    1.  Surface is treated with a holographic覆膜
    2.  Front needs to be shimmery
    3.  Side fabric is embedded with a 3mm thick transparent 亞克力 board, measuring 50mm x 100mm.

- **Quantity**: 500 / 1000

Do you have any color options for the shimmery color? And can the transparent 亞克力 board's edges be treated with shimmering glare?

Best regards,
Michael
```

<hr>

## Case 8: Quotation request for poker cards with different packaging options

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | N/A | ❌ Mismatch / Not Found |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
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
Dear Team,

Please provide the pricing standard for the扑克牌, which includes:

- ****card** Quantity**: 54 cards per pack
- **Size**: 63 x 88mm
- **Material**: 300gsm 蓝色纸张
- **Printing**: 4C+4C
- **Surface Treatment**: 两面扑克油
- **Packaging**:
    - **Pack Option A**: A standard pack with 250g **white **card** paper**, 4C-4C printing, and backlighting.
    - **Pack Option B**: A pack without a **card** box.
- **Quantity**: 3000 / 5000 packs

Please provide your prices for the selected options.

Thank you,
Fiona
```

<hr>

## Case 9: Inquiry about eco-friendly material options for a color box

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matt` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matt coating` | ✅ Match |
| `彩盒` | `color box` | N/A | ❌ Mismatch / Not Found |

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
Here is the final translated English text:

Hi Alice,

We are planning a new packaging box and would like to explore eco-friendly options.

- **Size**: 200 x 200 x 80mm
- **Current Spec**: 300gsm art paper with matte lamination.

Could you please quote the price for the current spec for 5,000 units?
Additionally, could you provide alternative quotes for:
1.  Using FSC certified paper.
2.  Replacing **matt** lamination with a water-based **matt** coating (水性哑光涂层).

We want to compare the cost and appearance. Could you send us samples of the **matt** coating finish if available?

Best,
Leo

This translation maintains the original text's structure and content while accurately translating technical terms and preserving the professional tone.
```

<hr>

## Case 10: Feedback on sample quality for a board book order

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
| `哑光油墨` | `matt ink`, `matte ink` | N/A | ❌ Mismatch / Not Found |
| `哑光涂层` | `matt coating`, `matte coating` | N/A | ❌ Mismatch / Not Found |
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
Hello William,

I am pleased to receive the hard copy of the product, which is of good quality but has a few issues:

1.  One of the pages has a slight air bubbles, which is necessary to be avoided during the production process.
2.  The glare on the front cover is a bit thin, and some areas are not as bright as expected. We would like to have a more deep and opaque glaze effect. Could you recommend a glaze oil or paint? Additionally, if possible, we would like to increase the layer thickness of the glaze?

Please confirm these questions will be addressed in the product. I will make sure to revise and finalize the revised order.

Best regards,
Sarah
```

<hr>

## Case 11: Request for a quote on processing fees only (CMT)

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `硬封面` | `hardcover` | N/A | ❌ Mismatch / Not Found |

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
Hi Peter,

We will provide the primary materials for you. Please provide your order for the following services:

- **Product**: Hard cover and notebook
- **Services**:
    1.  Fitting: We will cover the paper sheets with a 2.5mm matte finish.
    2.  Summing: We will add a gold embellishment to the logo on the paper.
    3.  Packaging: We will package the internal pages of the paper into a book.
- **Quantity**: 2,000 units

Materials will be delivered quarterly to your factory. Please report the cost of the materials.

Thank you,
Peter
```

<hr>

## Case 12: Quotation comparison for different paper weights

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | N/A | ❌ Mismatch / Not Found |
| `書紙` | `book paper` | N/A | ❌ Mismatch / Not Found |

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
**Translation:**

Dear Team,

We need to compare the costs of different paper sheets for your publications.

- **Size**: A4 sheets
- **Page Count**: 64 pages with a +4-page cover and 4 pages with a +4-page cover
- **Glue**: 騎馬钉
- **Printing**: 4C+4C

Please provide the following three different paper format prices (each in 3,000 yuan):
- **Spec 1**: 封面 200g 铜版纸, 内页 128g 铜版纸
- **Spec 2**: 封面 157g 铜版纸, 内页 105g 铜版纸
- **Spec 3**: 封面和內页全部使用 120g 書紙

All sheets must be printed with water-based luminous ink.

Thank you,
Laura

**Note:** The original text provided a mix of Chinese and English, and the translation maintained the original structure and content while adhering to the rules of professional business English.
```

<hr>

## Case 13: Quote for a paperback book with an outer sleeve

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | N/A | ❌ Mismatch / Not Found |
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
Please quote for a **paperback** book with an outer **sleeve**.

**Book Spec:**
- **Type**: **paperback**
- **Size**: 148 x 210mm
- **Cover**: 250gsm art paper, 4C+0C, **matte** lamination.
- **Text**: 240pp, 80gsm book paper, 1C+1C.

****sleeve** Spec:**
- **Type**: **sleeve**
- **Material**: 250gsm 白卡纸
- **Printing**: 4C+0C
- **Finishing**: 哑光涂层.

**Quantity**: 3,000 / 5,000 sets.
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
**Translated English:**

Hi William,

Could you please report the price of this irregularly shaped **paper **card****?

- **Material**: 400g **white **card** paper**
- **Size**: Maximum 10cm x 8cm
- **Printing**: 4C+1C (backing up with black and white text)
- **Cutting**: Hard shell覆膜, custom cutting
- **Quantity**: 10,000 / 20,000

Attachments are provided with the die-cut design. Could you inform me the cost of cutting the die-cut?

Regards,
Jessica

Note: The original Chinese text provided a mix of Chinese and English, and the English translation adheres to the rules of accuracy, mixed language, tone, and output format.
```

<hr>

## Case 15: Re-print request with a size modification

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | N/A | ❌ Mismatch / Not Found |

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
I need to reprint the color boxes from PO#20231105, but with a modification.

The original size was 150x150x150mm. The new size needs to be 160x160x160mm to accommodate a new 內襯. All other specifications, including the 350gsm 纸板 and UV coating, remain the same.

Please quote for 5,000 units.

Thanks,
Alex
```

<hr>

## Case 16: Quote for a single book with multiple cover versions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
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
**Final Translated English:**

Dear Team,

I am pleased to announce that our production plan is to produce a hardcover book, but there are four different design variations to be applied to the book.

- **Dimensions**: (All versions are identical)
    - Dimensions: 6" x 9"
    - Page count: 320 pages
    - Paper type: 80gsm book paper, 1C+1C finish
- **Design Variations**: (Four versions, each with different design variations)
    - Paper type: 250gsm copper-coated paper
    - Printing: 4C+0C
    - Finishing:哑光覆膜
- **Total Quantity**: (Each design variation contains 2,000 copies)

Please inquire about this operation, and whether the price of this method will be superior to the price of producing four copies of a single, 2,000-copy, printed version of the same book.

Best,
Maria
```

<hr>

## Case 17: Quote request for a hardcover gift box with a magnetic closure

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
| `哑光涂层` | `matt coating`, `matte coating` | N/A | ❌ Mismatch / Not Found |
| `灰板` | `greyboard` | N/A | ❌ Mismatch / Not Found |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `盒蓋` | `box cover`, `lid` | N/A | ❌ Mismatch / Not Found |
| `精装本` | `hardcover`, `hardback` | N/A | ❌ Mismatch / Not Found |

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
The final translated English text is:

Dear Alice,

Please quote for a high-end gift box with the following specifications:

- **Format**: High-end精装 box with magnetic closure.
- **Material**: 157gsm art paper - 2mm - 灰板.
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - 全局 哑光涂层.
    - 盒盖上印有烫金 logo.
- **Quantity**: 1,000 / 2,000 pcs.

Please confirm the lead time for a prototype.

Regards,
Daniel
```

<hr>

## Case 18: Inquiry about changing the endpaper material to reduce cost

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `書紙` | `book paper` | N/A | ❌ Mismatch / Not Found |
| `封裡頁` | `endpaper` | N/A | ❌ Mismatch / Not Found |

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
Hi Steve,

In the previous packaging book (PO#Q2406-11), we used 150gsm paper for the seal.

The client is looking to cut costs and would like to change the seal paper from 120gsm to standard paper. Could you estimate how much you would save?

The quantity is 1000 / 2000 books.

Thank you,
Catherine
```

<hr>

## Case 19: Quotation request for a product kit including a box, cards, and assembly

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | N/A | ❌ Mismatch / Not Found |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `上光` | `varnishing`, `coating` | N/A | ❌ Mismatch / Not Found |
| `彩盒` | `color box` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | `card` | ✅ Match |

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
Dear William,

We require a package for a product, which includes a box and several cards.

- **Item 1: Box**
    - Size: 300x200x50mm
    - Material: 250gsm e-flute paper board
    - Printing: 4C+0C, 哑光覆膜
    - Quantity: 2,000 cards per item, totaling 10,000 cards

- **Item 2: **card** x 5 Designs**
    - Size: 90x50mm
    - Material: 300gsm copper-coated paper
    - Printing: 4C+4C, 哑光覆膜
    - Quantity: 2,000 cards per item, totaling 10,000 cards

- **Item 3: Packaging and Packaging**
    - Method: Put 5 cards inside a box, then use a rolling tape to package the entire package.

Please provide the cost for 2,000 sets of packaging, and list each item and its packaging cost separately.

Thank you.

Best regards,
Linda
```

<hr>

## Case 20: Urgent request for a single, full-quality sample book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | N/A | ❌ Mismatch / Not Found |
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
Dear Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal.

Please produce ONE full sample of the following **hardcover** book:
- **Type**:精装本
- **Size**: 21x21cm
- **Cover**: 157gsm art paper 裱 2.5mm 灰板, 哑光覆膜, spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm 哑光铜版纸, 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark
```

<hr>

