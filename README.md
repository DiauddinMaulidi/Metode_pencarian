# 🔍 Algoritma Pencarian Jalur: UCS & IDA* dalam Python

Repositori ini berisi implementasi dua algoritma pencarian jalur populer dalam teori graf, yaitu **Uniform Cost Search (UCS)** dan **Iterative Deepening A\* (IDA\*)**. Keduanya digunakan untuk menemukan rute terbaik dari satu titik ke titik lain, terutama pada skenario yang melibatkan peta, rute, dan sistem navigasi.

## 📁 Struktur File

- `ucs.py` – Implementasi algoritma **Uniform Cost Search** menggunakan `PriorityQueue`.
- `ida.py` – Implementasi algoritma **IDA\*** lengkap dengan heuristik, menggunakan pendekatan rekursif dan iterative thresholding.

---

## 🔧 Fitur

### ✅ Uniform Cost Search (UCS)
Uniform Cost Search adalah salah satu algoritma pencarian buta (Blind Search). Konsepnya hampir sama dengan BFS, bedanya adalah bahwa BFS menggunakan urutan level yang paling rendah sampai yang paling tinggi, sedangkan UCS menggunakan urutan biaya dari yang paling kecil sampai yang terbesar. UCS berusaha menemukan solusi dengan total biaya terendah yang dihitung berdasarkan biaya dari simpul asal menuju ke simpul tujuan. Misal kita punya contoh:<br>

![image](https://github.com/user-attachments/assets/6f303160-e45a-4b7a-a746-20ba01ec4433)

- Inisial State = S,<br>
- Perluasan Simpul = Simpul dengan biaya jalur terendah dihapus dari antrean prioritas. Simpul itu kemudian diperluas dengan mengeksplorasi simpulnya atau biasa disebut anak.
- Menjelajahi Tetangga = Untuk setiap tetangga dari simpul yang diperluas, algoritma menghitung total biaya dari simpul awal ke tetangga melalui simpul saat ini. Jika simpul tetangga tidak berada dalam antrean prioritas, simpul tersebut akan ditambahkan ke antrean dengan biaya yang telah dihitung. Jika tetangga sudah berada dalam antrean tetapi jalur biaya yang lebih rendah ke tetangga ini ditemukan, biaya akan diperbarui dalam antrean.
- Goal Check = Setelah memperluas sebuah simpul, algoritma akan memeriksa apakah simpul tersebut telah mencapai simpul tujuan. Jika tujuan tercapai, algoritma akan menampilkan total biaya untuk mencapai simpul ini dan jalur yang diambil. Tapi jika buka simpul tujuan maka algoritma akan melakukan pengulangan hingga antrian prioritas kosong atau tujuan tercapai.

### ✅ Iterative Deepening A* (IDA*)
- Menggabungkan kekuatan **DFS** dan **heuristik A\***.
- Cocok untuk graf yang besar atau ketika memori terbatas.
- Menggunakan pendekatan iteratif berdasarkan threshold dari fungsi `f(n) = g(n) + h(n)`.

---

## 🚀 Cara Menjalankan

1. **Clone repositori:**
   ```bash
   git clone https://github.com/username/graph-search-algorithms.git
   cd graph-search-algorithms
