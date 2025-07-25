# Translation Terminology Report (Grok Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 100.0% (3/3) | 70.63 (Fairly Easy) |
| Case 2 | 80.0% (4/5) | 42.94 (Difficult) |
| Case 3 | 66.7% (2/3) | 66.74 (Standard) |
| Case 4 | 25.0% (1/4) | 42.44 (Difficult) |
| Case 5 | 0.0% (0/1) | 72.62 (Fairly Easy) |
| Case 6 | 83.3% (5/6) | 68.15 (Standard) |
| Case 7 | 100.0% (3/3) | 53.22 (Fairly Difficult) |
| Case 8 | 100.0% (2/2) | 56.66 (Fairly Difficult) |
| Case 9 | 0.0% (0/0) | 66.97 (Standard) |
| Case 10 | 33.3% (1/3) | 58.79 (Fairly Difficult) |
| **Average** | **58.8%** | **59.9 (Standard)** |

<hr>

## Case 1: Ambiguous use of a finishing term

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
Hi, 請為 2000 個新盒子報價，尺寸 15x10x5cm。材質用350g的**白**卡**纸**。我們想要一種保護性塗層，請直接報**上光**的價格，要那種標準的就好。謝謝。
```

### Grok's Translation with Highlights

```text
Subject: Quotation - New Boxes

Dear [Recipient],

Please provide a quotation for 2,000 new boxes with dimensions of 15 x 10 x 5 cm. The material should be 350 gsm **white **card** paper**. We require a protective coating; please include the cost for standard **varnishing** in the quotation. Thank you.
```

<hr>

## Case 2: Conflating multiple similar 'matte' finishes

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `哑光` | `matt`, `matte` | `matte` | ✅ Match |
| `哑光油墨` | `matt ink`, `matte ink` | `matte ink` | ✅ Match |
| `哑光涂层` | `matt coating`, `matte coating` | `matte coating` | ✅ Match |
| `哑光覆膜` | `matte laminated`, `matt laminated` | N/A | ❌ Mismatch / Not Found |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Steve, 關於上次那個**精装本**的報價。封面我們最後決定要啞光效果。所以請用**哑光**油墨印刷，然後再做一层**哑光**涂层。哦對了，為了耐用，還是用**哑光**覆膜吧。請更新價格。
```

### Grok's Translation with Highlights

```text
Subject: Re: Quotation Inquiry

Dear Steve,

Regarding the previous quotation for the **hardcover** book, we have finalized our decision to use a **matte** finish for the cover. Please print using **matte** ink, followed by an additional **matte** coating. For enhanced durability, please apply **matte** lamination instead. Kindly update the pricing accordingly.
```

<hr>

## Case 3: Using a book term to describe a box

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `精装本` | `hardcover`, `hardback` | `hardcover` | ✅ Match |

---

### Source Text with Highlights

```text
Alice, we need a quote for 500 high-end gift boxes. They need to be very rigid, basically like a **精装本**. The outside should be 157gsm art paper **裱** 3mm **灰板**. Let me know the cost ASAP.
```

### Grok's Translation with Highlights

```text
Subject: URGENT - High-End Box Quotation

Dear Alice,

We urgently require a quotation for 500 high-end gift boxes. These boxes should be highly rigid, comparable to a **hardcover** book. The exterior should consist of 157 gsm art paper laminated onto 3 mm **greyboard**. Please provide the cost as soon as possible.
```

<hr>

## Case 4: Contradictory product descriptions

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | N/A | ❌ Mismatch / Not Found |
| `平装封面` | `paperback` | `paperback` | ✅ Match |
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
Dear [Recipient],
We are interested in producing a board book for young children, designed to be highly durable and robust. The specifications are as follows:
Dimensions: 6 x 6 inches
Cover: 250 gsm coated paper, **paperback**
Interior pages: 105 gsm book paper, 32 pages
Quantity: 5,000 copies
Please provide the cost for producing a board book with these specifications.
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
Subject: Processing Fee Quotation

Dear [Recipient's Name],

Dear [Recipient],

Our company will supply a batch of pre-printed 157 gsm coated paper in A3 size. Please laminate this onto 2 mm board. Kindly provide the processing fee for 5,000 sheets. Thank you.
```

<hr>

## Case 6: Jumbled request for multiple different products

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `上光` | `varnishing`, `coating` | `varnishing` | ✅ Match |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `彩盒` | `color box` | `color box` | ✅ Match |
| `紙袋` | `paper bag` | N/A | ❌ Mismatch / Not Found |
| `卡` | `card` | `card` | ✅ Match |
| `書套` | `jacket` | `jacket` | ✅ Match |

---

### Source Text with Highlights

```text
Connie, 麻煩報幾個價。我們要做一個**彩盒**，20x20x8cm，用e-flute。還有一批**紙袋**，大概30cm高，用**白**卡**纸**。最後還需要一個**書套**，給我們現有的書用的，尺寸是15x22x3cm。封面都要**上光**。數量都先報1000個。
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Multiple Products

Dear Connie,

Please provide quotations for the following products:

A **color box** with dimensions of 20 x 20 x 8 cm, made from e-flute material.
A batch of paper bags, approximately 30 cm in height, made from **white **card** paper**.
A book **jacket** for our existing books, with dimensions of 15 x 22 x 3 cm.
All products require **varnishing** on the exterior. Please quote for 1,000 units of each.
```

<hr>

## Case 7: Informal language and typos obscuring technical needs

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `纸板` | `cardboard`, `paperboard` | `cardboard` | ✅ Match |
| `燙幻彩` | `holographic foil stamping` | `holographic foil stamping` | ✅ Match |
| `套筒` | `sleeve` | `sleeve` | ✅ Match |

---

### Source Text with Highlights

```text
hey, 之前說的那個書盒，想改一下。外面那個殼...就是那個**套筒**，我們想用好一點的**纸板**。表面處理...弄個**燙幻彩**，要閃一點的。數量不變，快點報個新價錢plz。
```

### Grok's Translation with Highlights

```text
Subject: Quotation Update for Slipcase

Dear [Recipient],

Regarding the previously discussed slipcase, we would like to make the following changes: the outer shell (i.e., **sleeve**) should be made from high-quality **cardboard**. For surface treatment, please apply **holographic foil stamping** to achieve a vibrant, reflective effect. The quantity remains unchanged. Please provide an updated quotation promptly.
```

<hr>

## Case 8: Contradictory material and aesthetic request

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `白卡纸` | `white card paper` | `white card paper` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Team, Please quote for 5,000 tuck-in boxes, size 10x10x10cm. For the material, please use a thick **白**卡**纸**, maybe 400gsm. But for the look, we want a very natural, brown, recycled paper aesthetic. What can you suggest?
```

### Grok's Translation with Highlights

```text
Subject: Quotation for Eco-Friendly Packaging

Dear Team,

Please provide a quotation for 5,000 tuck-in boxes with dimensions of 10 x 10 x 10 cm. The material should be thick **white **card** paper**, approximately 400 gsm. However, we prefer a natural, brown, recycled paper aesthetic. Please suggest suitable material options to achieve this look.
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
Subject: Inquiry About Paper Thickness

Dear William,

We plan to print a batch of A5 flyers, double-sided in full color. Please use 150 gsm coated paper, equivalent to approximately 80 lb text weight. Kindly provide quotations for 3,000 and 5,000 sheets.
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
Subject: Quotation for Protective Box

Dear [Recipient],

We require a protective slipcase for a batch of hardcover books. Please provide a quotation for this slipcase, designed for books measuring 21 x 30 x 4 cm. The slipcase should be constructed from high-rigidity **greyboard**, laminated with textured paper on the exterior. Please quote for 1,000 units.
```

<hr>

