# Translation Terminology Report (MiniCPM openbmb/MiniCPM4-0.5B Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 25.0% (1/4) | 62.58 (Standard) |
| Case 2 | 14.3% (1/7) | 81.54 (Easy) |
| Case 3 | 50.0% (2/4) | 81.71 (Easy) |
| Case 4 | 0.0% (0/8) | 63.02 (Standard) |
| Case 5 | 0.0% (0/3) | 73.44 (Easy) |
| Case 6 | 0.0% (0/1) | 54.75 (Fairly Difficult) |
| Case 7 | 0.0% (0/6) | 105.05 (Very Easy) |
| Case 8 | 50.0% (2/4) | 64.09 (Standard) |
| Case 9 | 66.7% (2/3) | 74.05 (Easy) |
| Case 10 | 0.0% (0/4) | 88.38 (Easy) |
| Case 11 | 33.3% (1/3) | 67.16 (Standard) |
| Case 12 | 0.0% (0/2) | 75.47 (Easy) |
| Case 13 | 50.0% (3/6) | 85.75 (Easy) |
| Case 14 | 66.7% (2/3) | 52.05 (Fairly Difficult) |
| Case 15 | 0.0% (0/1) | 74.98 (Easy) |
| Case 16 | 0.0% (0/2) | 48.78 (Difficult) |
| Case 17 | 0.0% (0/6) | 66.01 (Standard) |
| Case 18 | 0.0% (0/2) | 90.51 (Very Easy) |
| Case 19 | 33.3% (2/6) | 66.4 (Standard) |
| Case 20 | 20.0% (1/5) | 70.51 (Easy) |
| **Average** | **20.5%** | **72.3 (Difficult)** |

<hr>

## Case 1: Quotation request for a color box with special coating

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `水性亮光油墨` | `water-based gloss ink` | `water-based gloss ink` | ✅ Match |
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

### MiniCPM's Translation with Highlights

```text

```json
{
    "Hi Team": "Hello Team,",
    "Requirement": "Please provide the pricing for our new product, with a target quantity of 5,000 and 10,000 items.",
    "Product Class": "Box",
    "Dimensions": [
        "220mm x 150mm x 40mm",
        "220mm x 150mm x 40mm"
    ],
    "Material": [
        "300g copper plate paper",
        "Laminated E-flute board"
    ],
    "Printing": [
        "4C + 0C",
        "**water-based gloss ink**"
    ],
    "Surface Treatment": [
        "**water-based gloss ink**",
        "Sensitive ink"
    ],
    "Packaging": [
        "50 boxes/pack",
        "Laminated box"
    ],
    "Packing": [
        "50 boxes/pack",
        "Laminated box"
    ],
    "Purchase Date": "Please inform the production schedule for a week.",
    "Thank You": "Thank you!"
}
```
```

<hr>

## Case 2: Re-quote request for a hardcover book after specification update

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
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

### MiniCPM's Translation with Highlights

```text

```json
{
    "顾客": "Steve",
    "感謝您上次的報價": "Thank you for your previous order.",
    "客戶對設計進行了修改": "Your design team has made some modifications to your order.",
    "請根據更新後的規格重新報價": "Please re-report your order based on the updated specifications.",
    "內文尺寸": "240mm(w) x 290mm(h)",
    "皮殼": "The wood panel has been updated to a 157g silky-hung copper plate.",
    "表面處理": "The surface of the panel will be treated with a silky-hung silky-hung copper plate and a **matte** finish.",
    "襯紙": "The water-based silky-hung copper plate has a 150gsm water-based silk-hung paper.",
    "數量": "1,500 books / 3,000 books",
    "詢問是否可以為首批50本書提供獨立的書套": "Could you provide the price for a set of 50 books, specifically a set of a single book package?",
    "請單獨報價": "Please provide a specific price for a set of a single book package."
}
```
```

<hr>

## Case 3: Urgent order for paper bags for a trade show

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | N/A | ❌ Mismatch / Not Found |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `紙袋` | `paper bag` | N/A | ❌ Mismatch / Not Found |
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

### MiniCPM's Translation with Highlights

```text

```json
{
    "Alice": [
        "Hello Alice,",
        "I am seeking to order a batch of paper bags for our upcoming exhibition.",
        "Please provide a price for this.",
        "The size is 30cm (H) x 25cm (W) x 10cm (D).",
        "The material is 210g of **white **card** paper**.",
        "The ink is 4C+0C, and the printing is哑光油墨.",
        "The materials include 210g of **white **card** paper**.",
        "The printing process includes a哑光覆膜 and a cotton handling hand.",
        "The quantity is 500.",
        "If you are unable to provide the delivery date, please let me know.",
        "If you are not available for the printing, the price is not available."
    ]
}
```
```

<hr>

## Case 4: Inquiry about materials for a board book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

**Translation:**

Hi William,

I'm planning to develop a hard-cover book with 12 pages. I'm asking you for advice on the type of paper used for the cover and the thickness of the grey coating to ensure the book's durability.

For the cover, I'm considering using 扑克纸处理，而普通哑光涂层的成本大约会增加多少？

Based on the given specifications, the cost of the grey coating over the 4C/4C printing method is expected to be higher than the哑光涂层. Could you please provide me with your expert advice?

Thank you.

Regards,
Emily

**Note:** The provided glossary terms are used in the translation to ensure the text remains professional and accurate.
```

<hr>

## Case 5: Quote for multi-language instruction sheets and packaging

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

Here is the translated text:

Hi Teresa,

Please quote for the following items. Quantities: 8k, 16k.

**Item 1: Tuck-in Box**
- **Material**: 350gsm 灰板
- **Size**: 180 x 100 x 50mm
- **Printing**: 4C+0C
- **Finishing**: 上光

**Item 2: Instruction Sheets (x3 languages)**
- **Size**: A4, fold to A6
- **Material**: 105gsm 書紙
- **Printing**: 1C+1C
- **Note**: 3個版本內容不同，但數量均分。

Please let me know the prices for these two items. I appreciate your assistance.

Thanks,
Ben

Note: The term "paperback" is used here as a general term to refer to a book that is folded to make a single-page format. It is not a specific term used in the glossary, but it is a common term in the printing industry.
```

<hr>

## Case 6: Re-order request with an inquiry about partial shipment

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

Dear Joe,

We are pleased to announce that the product market response is positive. We need to expedite our order.

Please provide the price of the product:精装本，与 PO#20240512 完全相同。

We are also in need of expedited shipping for the following products:
- **Product**:精装本
- **Size**: 与 PO#20240512 完全相同。

Please inform us if it is possible to arrange expedited shipping for the following products:
- **Product**:精装本
- **Quantity**: 2,000 units
- **Timeframe**: Immediately after completion of 2,000 units
- **Cost**: The cost of shipping will be calculated accordingly.

Thank you,
Connie
```

<hr>

## Case 7: Quote for a slipcase with an acrylic board and special foil stamping

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

```json
{
    "中文原文": "Hi Steve,

麻煩報價一款特殊的書盒，設計比較複雜。

- **類型**: 書盒
- **適用書籍**: 150mm x 220mm x 30mm
- **材料**: 2mm 灰板 裱 128g art paper
- **加工**:
    1.  表面 哑光覆膜
    2.  正面需要 燙幻彩
    3.  側面嵌入一塊 3mm 厚的透明 亞克力板，尺寸為 50mm x 100mm。

- **數量**: 500 / 1000

請問燙幻彩除了標準的彩虹色，有其他顏色選擇嗎？亞克力板的邊緣可以做拋光處理嗎？

Best regards,
Michael
"
}
```
```

<hr>

## Case 8: Quotation request for poker cards with different packaging options

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

### Translated Text:

Hi Team,

Please rate the standard tuck boxes, specifications:

- **Cardboard quantity**: 54 cards/pack
- **Size**: 63 x 88mm
- **Material**: 300gsm blue core paper
- **Printing**: 4C+4C
- **Surface treatment**: Double-sided 扑克油
- **Packaging**:
    - **Item A**: Standard tuck box, 250g **white **card** paper**, 4C printing, glazing.
    - **Item B**: Compressed paper package, no cardboard box.
- **Quantity**: 3000 / 5000 cards

Please rate the selected items.

Thanks,
Fiona
```

<hr>

## Case 9: Inquiry about eco-friendly material options for a color box

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

### Translated Text

Hi Alice,

We are planning a new 彩盒 and would like to explore eco-friendly options.

- **Size**: 200 x 200 x 80mm
- **Current Spec**: 300gsm art paper with **matt** lamination.

Could you please quote the price for the current spec for 5,000 units?
Additionally, could you provide alternative quotes for:
1.  Using FSC certified paper.
2.  Replacing **matt** lamination with a water-based **matt** coating (水性哑光涂层).

We want to compare the cost and appearance. Could you send us samples of the **matt** coating finish if available?

Best,
Leo

### Explanation

1.  **Size**: 200 x 200 x 80mm
   - This is the dimensions of the new 彩盒.

2.  **Current Spec**: 300gsm art paper with **matt** lamination.
   - This specifies the current specifications for the art paper used in the new 彩盒.

3.  **Price**:
   - The price for the current spec for 5,000 units is not provided in the glossary.

4.  **Alternative Quotes**:
   - **Using FSC certified paper**: This term is not listed in the glossary.
   - **Replacing **matt** lamination with a water-based **matt** coating (水性哑光涂层)**: This is a term that refers to the process of applying a coating to the paper to improve its durability and appearance.

5.  **Samples**:
   - The glossary does not provide sample images or descriptions of the **matt** coating finish.

6.  **Best,
   - Leo
```

<hr>

## Case 10: Feedback on sample quality for a board book order

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

Hi William,

I am receiving the sample of hard-sided book, the whole is fine but there are two problems:

1.  The front of one page has a slightly faint foam, and when it is produced, it is recommended to avoid it.
2.  The satin coating on the cover is a bit thin, some areas have not as much reflection. We hope to have a more deep-dive glaze effect. Can you use a glaze ink or increase the thickness of the coating?

Please confirm these problems can be improved in the book. Wait for your reply to confirm, and we will make sure to revise the design.

Best regards,
Sarah
```

<hr>

## Case 11: Request for a quote on processing fees only (CMT)

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

Hi Peter,

We are pleased to provide you with a list of materials that you can use. Please do not hesitate to contact us for any further details.

- **Product**: **hardcover** Notebook
- **Service**:
    1.  Fabrication: We will fabricate the cover of the notebook at a cost of 2.5mm gray paper.
    2.  Decoration: We will decorate the cover and the back of the notebook with the logo.
    3.  Binding: We will bind the paper and notebook together into a book.
- **Quantity**: 2,000

Materials will be delivered to your factory every week. Please report any details about the processing cost.

Thank you,
Peter
```

<hr>

## Case 12: Quotation comparison for different paper weights

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

### Translated Text:

Hi Team,

Please provide the price estimates for the following volume of paper:

- **Size**: A4
- **Page Count**: 64pg + 4pg cover
- **Booklet**: 騎馬钉
- **Printing**: 4C+4C

Please specify the three different paper formats you would like to compare:

- **Spec 1**: 封面 200g 铜版纸, 內頁 128g 铜版纸.
- **Spec 2**: 封面 157g 铜版纸, 內頁 105g 铜版纸.
- **Spec 3**: 封面和內頁全部使用 120g 书紙.

All three formats must be water-based and have the following specifications:

- **Spec 1**: The paper is water-based and the print is 4C+4C.
- **Spec 2**: The paper is water-based and the print is 4C+4C.
- **Spec 3**: The paper is water-based and the print is 4C+4C.

Thank you,
Laura

This text adheres to the provided guidelines and uses the approved English translations of the specified terms.
```

<hr>

## Case 13: Quote for a paperback book with an outer sleeve

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

**Answer:**

Hi Alice,

Please quote for a **paperback** book with an outer **sleeve**.

**Book Spec:**
- **Type**: 平装封面
- **Size**: 148 x 210mm
- **Cover**: 250gsm art paper, 4C+0C, **matte** lamination.
- **Text**: 240pp, 80gsm book paper, 1C+1C.

****sleeve** Spec:**
- **Type**: 套筒
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

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `紙卡` | `paper card` | N/A | ❌ Mismatch / Not Found |
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

### MiniCPM's Translation with Highlights

```text

```json
{
    "paper": [
        "**white **card** paper**",
        "paper"
    ],
    "paper_size": [
        "10cm x 8cm"
    ],
    "printing": [
        "4C+1C",
        "backing"
    ],
    "cutting": [
        "silicone cut",
        "die-cut"
    ],
    "material_cost": "10,000 / 20,000"
}
```
```

<hr>

## Case 15: Re-print request with a size modification

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

```json
{
    "标题": "Color Boxes from PO#20231105 Modification",
    "描述": "We need to reprint the color boxes from PO#20231105, but with a modification.",
    "原尺寸": {
        "宽度": "150mm",
        "高度": "150mm",
        "厚度": "150mm"
    },
    "新尺寸": {
        "宽度": "160mm",
        "高度": "160mm",
        "厚度": "160mm"
    },
    "其他规格": {
        "纸板": "350gsm",
        "UV coating": "no change"
    },
    "数量": "5000 units"
}
```
```

<hr>

## Case 16: Quote for a single book with multiple cover versions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

### Translated Text:

Hi Team,

I am pleased to announce the publication of a hardcover book in a paper format. The book is designed to appeal to a diverse range of markets, and we have four different design options to cater to various tastes.

- **Contents**: (All versions are identical)
    - Dimensions: 6" x 9"
    - Page Count: 320 pages
    - Paper Margin: 80 gsm book paper, 1C+1C
- **Design**: (Four versions, each with unique design options)
    - Paper Margin: 250 gsm copper-plated paper
    - Printing: 4C+0C
    - Coating:哑光覆膜
- **Total Quantity**: 8,000 copies (Each version contains 2,000 copies)

Please inquire about the operation method, price, and the advantageousness of this method compared to a single-print book with 4,000 copies.

Best,
Maria
```

<hr>

## Case 17: Quote request for a hardcover gift box with a magnetic closure

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

**Translation:**

Hi Alice,

Please quote for a high-end gift box with the following specifications:

- **Type**: High-end精装本 style box with magnetic closure.
- **Material**: 157gsm art paper - 裱 on 2mm 灰板.
- **Size (internal)**: 250 x 180 x 60mm.
- **Printing**: 1C (Pantone Black 6 C) + 0C.
- **Finishing**:
    - 全局 哑光涂层.
    - 盒蓋 on top with 燙金 logo.
- **Quantity**: 1,000 / 2,000 pcs.

Please confirm the lead time for a prototype.

Regards,
Daniel

**Explanation:**

The provided text is a business English translation of a document. The translation follows the given glossary and adheres to the rules of mixed language and output format. The text is professional, clear, and accurate, and it meets the requirements of the critical instruction.
```

<hr>

## Case 18: Inquiry about changing the endpaper material to reduce cost

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

Hi Steve,

In the last book price of my document (P#Q2406-11), I used 150gsm paper for the seal page.

Do you think changing the seal page to 120gsm paper will save you a certain amount of cost?

The quantity is 1000 / 2000 books.

Thanks,
Catherine
```

<hr>

## Case 19: Quotation request for a product kit including a box, cards, and assembly

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | N/A | ❌ Mismatch / Not Found |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
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

### MiniCPM's Translation with Highlights

```text

Here is the translated text:

Hi William,

I need to package a product that includes a box and several cards.

- **Item 1: Box**
    - Size: 300x200x50mm
    - Material: 250gsm E-flute paper板
    - Printing: 4C+0C, coated

- **Item 2: **card** Designs**
    - Size: 90x50mm
    - Material: 300gsm copper-coated paper
    - Printing: 4C+4C, **matte**
    - Quantity: 2,000 cards each

- **Item 3: Packaging and Packaging**
    - Method: Use a roll of 2,000-packing paper to package the cards.

Please provide the cost of 2,000 sets of these packages, and list the cost of each item and the total cost of the package.

Thank you,
Linda
```

<hr>

## Case 20: Urgent request for a single, full-quality sample book

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | MiniCPM's Translation | Matches Term Base? |
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

### MiniCPM's Translation with Highlights

```text

**Translation:**

Hi Joe,

We are finalizing a project with a client and need a physical sample urgently to close the deal. Please produce ONE full sample of the following **hardcover** book:

- **Type**: 精装本
- **Size**: 21x21cm
- **Cover**: 157gsm art paper 裱 2.5mm 哑光覆膜, spot UV on title.
- **Endpaper**: 140gsm black card paper.
- **Text**: 128pp, 157gsm 哑光铜版纸, 4C+4C.

We understand this is a rush job. Please let us know the cost and the absolute fastest turnaround time for this single sample. We can arrange a courier to pick it up once ready.

This is critical for us. Appreciate your help.

Thanks,
Mark

**Note:** The provided glossary is not directly applicable to the provided text, as it does not contain any Chinese terms or specific vocabulary related to the business industry. The text appears to be a general business communication document.
```

<hr>

