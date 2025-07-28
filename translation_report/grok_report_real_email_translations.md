# Translation Terminology Report (Grok Analysis)

## Overall Metrics Summary

| Case | Terminology Hit Rate | Readability Score (Interpretation) |
| :--- | :--- | :--- |
| Case 1 | 0.0% (0/0) | 41.03 (Difficult) |
| Case 2 | 100.0% (2/2) | 66.01 (Standard) |
| Case 3 | 66.7% (2/3) | 64.04 (Standard) |
| Case 4 | 0.0% (0/0) | 79.47 (Easy) |
| **Average** | **41.7%** | **62.6 (Fairly Difficult)** |

<hr>

## Case 1: N/A

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |

---

### Source Text with Highlights

```text
  下午好!

    請按附件資料報價，數量300PCS/400PCS/500PCS,5K，要求如下：

  Page count: 24pg + cover

Cover: 16" x 6" white 111# Pacesetter Cover Silk

Text pages: 16" x 6" white 80# Pacesetter Text silk

Finish Size: 8" x 6"

Finishing: DIG collate, SaddleStitch, Trim


  補充資料：

    材質：封面及內頁都是90G 雙銅紙，封面過水油，內頁無表面處理。

2個騎馬釘。

    請提供100PCS/200PCS/300PCS/400PCS/500PCS/5K 報價
```

### Grok's Translation with Highlights

```text
Good afternoon,

Please provide a quotation based on the attached specifications for quantities of 100, 200, 300, 400, 500, and 5,000 units, with the following requirements:

Page count: 24 pages + cover
Cover: 16" x 6", white 111# Pacesetter Cover Silk
Text pages: 16" x 6", white 80# Pacesetter Text Silk
Finished size: 8" x 6"
Finishing: Digital collation, saddle stitching, trimming
Supplementary details:
Material: Both cover and text pages use 90 gsm coated paper; cover with varnishing, text pages without surface treatment.
Binding: Two saddle stitches.
Please provide quotations for 100, 200, 300, 400, 500, and 5,000 units.
```

<hr>

## Case 2: N/A

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `包装` | `packaging` | `Packaging` | ✅ Match |
| `卡` | `card` | `card` | ✅ Match |

---

### Source Text with Highlights

```text
Hi William,

我有套圖書想請貴司報價, 資料如下, 謝謝

點讀圖書（全套12冊）


規格1:

封面: 210G粉咭/4pp/4C+4C/雙面加光油    *封面的圖要加針線(可用手沿線撕開) **12本書的封面設計圖不同

內頁: 157G粉紙/32pp/4C+4C/雙面加光油

尺寸: A4 – 210*297MM/騎馬釘

貼紙頁 : A3/4C+0/可重複貼貼紙    **12本書的貼紙設計圖不同

 

規格2:

封面+內頁: 210G粉咭/4+32pp/4C+4C/雙面加光油    *封面的圖要加針線(可用手沿線撕開) **12本書的封面圖不同

尺寸: A4 – 210*297MM/騎馬釘    **12本書的貼紙設計圖不同

 

規格3:

封面+內頁: 250G粉咭/4+32pp/4C+4C/雙面加光油    *封面的圖要加針線(可用手沿線撕開) **12本書的封面圖不同

尺寸: A4 – 210*297MM/騎馬釘    **12本書的貼紙設計圖不同

 

印刷數量: 3000套

包裝方法:暫定收縮（shrink wrap）

 

Best regards,

Connie


Hi William,

We have updated the details, please quote us the price base on the following:


更正


現祇需報1款規格, 更新資料如下:


騎馬釘直度A4點讀圖書套裝:  

尺寸：210mm (W) x 297mm(H) (打開420mm (W) x 297mm(H))

規格：每款頁數32+4pp，每套12款

物料：封面250g單粉**卡**；內頁157g粉紙
顏色：4C+4C
加工：封面單面光膠、燙金、一條semi diecut 針線(約11x18cm) 

 

另每本中間加可點讀貼紙：

尺寸：210mm (W) x 297mm(H) (打開420mm (W) x 297mm(H))

規格：每本10pp（即A3X5），刀模不同

物料：85gsm 光面貼紙
顏色：4C+0

 

書和貼紙請分開報價, 方便調整貼紙張數. 數量請報3000套，謝謝。

 

Best regards,

Connie
```

### Grok's Translation with Highlights

```text
Dear William,

Please provide a quotation for a set of 12 interactive reading books with the following initial specifications:

Specification 1:

Cover: 210 gsm white **card** paper, 4 pages, 4C+4C, double-sided varnishing; includes perforations for hand-tearing; unique cover designs for each of the 12 books.
Text pages: 157 gsm coated paper, 32 pages, 4C+4C, double-sided varnishing.
Size: A4 (210 x 297 mm), saddle-stitched.
Sticker pages: A3, 4C+0, reusable stickers; unique designs for each of the 12 books.
Specification 2:
Cover + Text: 210 gsm white **card** paper, 4+32 pages, 4C+4C, double-sided varnishing; cover with perforations; unique cover designs.
Size: A4 (210 x 297 mm), saddle-stitched; unique sticker designs.
Specification 3:
Cover + Text: 250 gsm white **card** paper, 4+32 pages, 4C+4C, double-sided varnishing; cover with perforations; unique cover designs.
Size: A4 (210 x 297 mm), saddle-stitched; unique sticker designs.
Print quantity: 3,000 sets.
**Packaging**: Tentatively shrink wrap.
Best regards, Connie
Update:

Please provide a quotation for only one specification, updated as follows:

Saddle-stitched A4 Interactive Reading Book Set:

Size: 210 mm (W) x 297 mm (H) (open: 420 mm (W) x 297 mm (H)).
Specification: 32 pages + 4-page cover per book, 12 unique designs per set.
Material: Cover: 250 gsm white **card** paper; Text: 157 gsm coated paper.
Color: 4C+4C.
Finishing: Cover with single-sided varnishing, gold foil stamping, one semi-diecut perforation (approx. 11 x 18 cm).
Additional Interactive Stickers:
Size: 210 mm (W) x 297 mm (H) (open: 420 mm (W) x 297 mm (H)).
Specification: 10 pages per book (A3 x 5), unique die-cut designs.
Material: 85 gsm gloss sticker paper.
Color: 4C+0.
Please provide separate quotations for the books and stickers to allow adjustments to sticker quantities. Quote for 3,000 sets. Thank you.
Best regards, Connie
```

<hr>

## Case 3: N/A

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |
| `灰板` | `greyboard` | `greyboard` | ✅ Match |
| `裱` | `laminating` | N/A | ❌ Mismatch / Not Found |
| `衬纸` | `endpaper` | `Endpapers` | ✅ Match |

---

### Source Text with Highlights

```text
Hi Steve,

 

麻煩幫忙報做精裝書價錢,

 

內文尺寸 240mm(w) x 290mm(h)

皮殼 興泰行布料 **裱****灰板**3mm 及 燙金 (底面燙字)

內文200gsm花紋紙

襯紙150 gsm花紋紙

運通自來模書鴻興負責做皮殼、燙金及上殼

數量1000本 / 2000本

 

Thanks

Catherine


Dear Joe,


內文128pp, 大約1吋厚


Thanks

Catherine
```

### Grok's Translation with Highlights

```text
Dear Steve,

Please provide a quotation for producing a hardcover book with the following specifications:

Text dimensions: 240 mm (W) x 290 mm (H).
Case: Xingtaihang fabric laminated onto 3 mm **greyboard** with gold foil stamping (text on the spine).
Text pages: 200 gsm textured paper.
**Endpapers**: 150 gsm textured paper.
Production: Yuntong self-mold book, with Hongxing responsible for case-making, gold foil stamping, and case-binding.
Quantities: 1,000 and 2,000 copies.
Thank you, Catherine
Dear Joe,

The text consists of 128 pages, approximately 1 inch thick.

Thank you, Catherine
```

<hr>

## Case 4: N/A

### Terminology Analysis Table

| Source Term (原文字詞) | Approved English (術語庫) | Grok's Translation | Matches Term Base? |
| :--- | :--- | :--- | :--- |

---

### Source Text with Highlights

```text
Alice,


Please quote : 10k, 20k, 30k & 50k


250gsm e-flute tuck in box (FSC)

Size:  380 x 240 x 145mm

4C+UV

 

Inst sheet

A5 size x 4 (FSC)

128gsm artpaper

1C+1C,双面过油

 

Card

250gsm e-flute (FSC)

350x720mm

4C+UV

 

Thanks,

Teresa
```

### Grok's Translation with Highlights

```text
Dear Alice,

Please provide quotations for the following items in quantities of 10,000, 20,000, 30,000, and 50,000 units:

Tuck-in Box:
Material: 250 gsm e-flute (FSC-certified).
Size: 380 x 240 x 145 mm.
Printing: 4C with UV coating.
Instruction Sheet:
Size: A5, 4 pages (FSC-certified).
Material: 128 gsm art paper.
Printing: 1C+1C, double-sided varnishing.
Card:
Material: 250 gsm e-flute (FSC-certified).
Size: 350 x 720 mm.
Printing: 4C with UV coating.
Thank you, Teresa
```

<hr>

