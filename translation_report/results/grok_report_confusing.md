# Translation Terminology Report (Grok Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 33.3% (1/3) | 38.67 (Difficult) |
| Case 2 | 40.0% (2/5) | 50.47 (Fairly Difficult) |
| Case 3 | 33.3% (1/3) | 69.82 (Standard) |
| Case 4 | 0.0% (0/4) | 55.45 (Fairly Difficult) |
| Case 5 | 0.0% (0/1) | 75.71 (Fairly Easy) |
| Case 6 | 33.3% (2/6) | 15.33 (Very Difficult) |
| Case 7 | 66.7% (2/3) | 48.25 (Difficult) |
| Case 8 | 0.0% (0/2) | 34.5 (Difficult) |
| Case 9 | 0.0% (0/0) | 63.49 (Standard) |
| Case 10 | 33.3% (1/3) | 39.33 (Difficult) |
| **Average** | **24.0%** | **49.1 (Fairly Easy)** |

<hr>

## Case 1: Ambiguous use of a finishing term

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `coating` | ✅ Match |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi, 請為 2000 個新盒子報價，尺寸 15x10x5cm。材質用350g的**白**卡**纸**。我們想要一種保護性塗層，請直接報**上光**的價格，要那種標準的就好。謝謝。
```

### Grok's Translation with Highlights

```text
Subject: Quotation for New Boxes

Dear [Recipient's Name],

Please provide a quotation for 2,000 boxes with the following specifications:

Dimensions: 15 x 10 x 5 cm
Material: 350 gsm white cardstock
Finishing: Standard gloss lamination for protective **coating**
Kindly confirm the cost and production timeline. Thank you.
```

<hr>

## Case 2: Conflating multiple similar 'matte' finishes

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光油墨` | `matt ink`, `matte ink` | N/A | ❌ Mismatch / Not Found |
| `哑光涂层` | `matt coating`, `matte coating` | N/A | ❌ Mismatch / Not Found |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Steve, 關於上次那個**精装本**的報價。封面我們最後決定要啞光效果。所以請用**哑光**油墨印刷，然後再做一层**哑光**涂层。哦對了，為了耐用，還是用**哑光**覆膜吧。請更新價格。
```

### Grok's Translation with Highlights

```text
Subject: Updated Quotation for **hardcover** Book

Dear Steve,

Regarding the quotation for the **hardcover** book, we have finalized the cover finish. Please use **matte** lamination for the cover to achieve a non-glossy, durable finish. Kindly update the quotation based on this specification and confirm the revised cost and timeline.

Thank you,
```

<hr>

## Case 3: Using a book term to describe a box

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `精装本` | `hardcover`, `hardback` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Alice, we need a quote for 500 high-end gift boxes. They need to be very rigid, basically like a **精装本**. The outside should be 157gsm art paper **裱** 3mm **灰板**. Let me know the cost ASAP.
```

### Grok's Translation with Highlights

```text
Subject: Urgent Quotation for High-End Gift Boxes

Dear Alice,

We urgently require a quotation for 500 high-end gift boxes. The boxes should be rigid, constructed with 157 gsm art paper mounted on 3 mm **greyboard** for a sturdy, premium structure. Please provide the cost and delivery timeline as soon as possible.

Best regards,
```

<hr>

## Case 4: Contradictory product descriptions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | N/A | ❌ Mismatch / Not Found |
| `平装封面` | `paperback` | N/A | ❌ Mismatch / Not Found |
| `硬板书` | `boardbook` | N/A | ❌ Mismatch / Not Found |
| `纸板书` | `boardbook` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
你好，我想做一款给小孩子的**纸板**书，要非常厚实耐用。规格如下：
- 尺寸: 6x6英寸
- 封面: 250g铜版纸，**平装封面**
- 内页: 105g书纸，32页
- 数量: 5000本
请问这样做一本**硬板书**要多少钱？
```

### Grok's Translation with Highlights

```text
Subject: Quotation Request for Children’s Board Book

Dear [Recipient's Name],

We are seeking a quotation for 5,000 children’s board books designed for durability. Please provide pricing based on the following specifications:

Dimensions: 6 x 6 inches
Cover: 250 gsm coated paper, mounted on thick board for a hardcover board book format
Inner Pages: 32 pages, 105 gsm coated paper, mounted on thick board
Binding: Board book binding
Please confirm the cost per unit and the production timeline. Let us know if you need further clarification.

Best regards,
```

<hr>

## Case 5: Vague instructions for a core process

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi, 我司會提供一批印刷好的157g铜版纸。尺寸是A3。請幫我們把它**裱**在2mm的板上。請報5000張的加工費。謝謝。
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Mounting Process

Dear [Recipient's Name],

We will provide 5,000 sheets of pre-printed 157 gsm coated paper in A3 size. Please quote the cost for mounting these sheets onto 2 mm thick board. Kindly include the processing fee and confirm the production timeline.

Thank you,
```

<hr>

## Case 6: Jumbled request for multiple different products

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | N/A | ❌ Mismatch / Not Found |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `紙袋` | `paper bag` | `paper bag` | ✅ Match |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |
| `書套` | `jacket` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Connie, 麻煩報幾個價。我們要做一個**彩盒**，20x20x8cm，用e-flute。還有一批**紙袋**，大概30cm高，用**白**卡**纸**。最後還需要一個**書套**，給我們現有的書用的，尺寸是15x22x3cm。封面都要**上光**。數量都先報1000個。
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Multiple Products

Dear Connie,

Please provide quotations for the following products, each with a quantity of 1,000 units:

**color box**:
Dimensions: 20 x 20 x 8 cm
Material: E-flute corrugated board
Finishing: Gloss lamination
**paper bag**:
Height: Approximately 30 cm
Material: White cardstock
Finishing: Gloss lamination
Book Slipcase:
Dimensions: 15 x 22 x 3 cm
Material: Suitable for existing books
Finishing: Gloss lamination
Please provide individual costs and the production timeline for each item.

Best regards,
```

<hr>

## Case 7: Informal language and typos obscuring technical needs

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | N/A | ❌ Mismatch / Not Found |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |
| `套筒` | `sleeve` | `sleeve` | ✅ Match |

---

### Source Text with Highlights

```text
hey, 之前說的那個書盒，想改一下。外面那個殼...就是那個**套筒**，我們想用好一點的**纸板**。表面處理...弄個**燙幻彩**，要閃一點的。數量不變，快點報個新價錢plz。
```

### Grok's Translation with Highlights

```text
Subject: Updated Quotation for Book Slipcase

Dear [Recipient's Name],

We would like to revise the specifications for the book slipcase discussed previously. Please use a high-quality, sturdy cardstock for the outer **sleeve** and apply a **holographic foil stamping** finish for a vibrant, reflective effect. The quantity remains unchanged. Kindly provide an updated quotation and confirm the production timeline.

Thank you,
```

<hr>

## Case 8: Contradictory material and aesthetic request

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `白卡纸` | `white card paper` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
Hi Team, Please quote for 5,000 tuck-in boxes, size 10x10x10cm. For the material, please use a thick **白**卡**纸**, maybe 400gsm. But for the look, we want a very natural, brown, recycled paper aesthetic. What can you suggest?
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Eco-Friendly Packaging

Dear [Recipient's Name],

We are requesting a quotation for 5,000 tuck-in boxes with the following specifications:

Dimensions: 10 x 10 x 10 cm
Material: 400 gsm kraft paper to achieve a natural, brown, recycled aesthetic
Note: Please recommend a material that balances thickness with an eco-friendly, recycled paper appearance.
Kindly provide the cost, material recommendations, and production timeline.

Best regards,
```

<hr>

## Case 9: Using non-standard units for a technical spec

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |

---

### Source Text with Highlights

```text
William, 我們想印一批傳單，A5尺寸，雙面彩色。紙張請用150克的铜版纸。就是那種...感覺像80磅text weight那樣的，你懂吧？報價3000和5000張。
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Flyers

Dear William,

We require a quotation for printing A5-sized flyers, double-sided, in full color (CMYK). Please use 150 gsm coated paper, equivalent to approximately 80 lb text weight. Provide pricing for quantities of 3,000 and 5,000 units, along with the production timeline.

Thank you,
```

<hr>

## Case 10: Using two different glossary terms for the same item

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `套筒` | `sleeve` | N/A | ❌ Mismatch / Not Found |

---

### Source Text with Highlights

```text
您好，我們有一批精裝書需要配一個外盒。請為這個書盒報價。書本尺寸21x30x4cm。這個**套筒**需要用硬度高的**灰板**來做，外面**裱**有紋路的紙。請報1000個的價格。
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Book Slipcase

Dear [Recipient's Name],

We need a quotation for 1,000 slipcases for hardcover books with the following specifications:

Dimensions: 21 x 30 x 4 cm
Material: High-rigidity **greyboard**, wrapped with textured paper
Please provide the cost and confirm the production timeline.

Best regards,
```

<hr>

