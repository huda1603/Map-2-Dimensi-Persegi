# Map-2-Dimensi-Persegi
Membuat Sebuah Map 2D Dengan Titik Mulai(Y) Dan Titik Tujuan(Z) Lalu Menghitung Total Langkahnya Dari Gerakan Secara Horizontal Dan Secara Vertikal Dengan X Sebagai Backgroundnya

# Contoh Input Dan Output
**Input 5x5**
```bash
XXXYX,XXXXX,XXXXX,XZXXX,XXXXX
```
Apabila Dipetakan Menjadi Seperti Ini
```bash
XXXYX
XXXXX
XXXXX
XZXXX
XXXXX
```
Bergerak 2 Langkah Ke Kiri
```bash
XYXXX
XXXXX
XXXXX
XZXXX
XXXXX
```
Lalu Bergerak 3 Langkah Ke Bawah
```bash
XXXXX
XXXXX
XXXXX
XYZXXX
XXXXX
```
**Output**
```bash
Total 5 Langkah
2 Langkah Ke Kiri
3 Langkah Ke Bawah
```

**Contoh Input 4x4**
```bash
XXZX,XXXX,XXXX,XYXX
```
Apabila Dipetakan Menjadi Seperti Ini
```bash
XXZX
XXXX
XXXX
XYXX
```
Bergerak 1 Langkah Ke Kanan
```bash
XXZX
XXXX
XXXX
XXYX
```
Lalu Bergerak 3 Langkah Ke Atas
```bash
XXYZX
XXXX
XXXX
XXXX
```
**Output**
```bash
Total 4 Langkah
1 Langkah Ke Kanan
3 Langkah Ke Atas
```
