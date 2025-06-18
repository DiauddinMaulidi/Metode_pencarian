# 🔍 Algoritma Pencarian Jalur: UCS & IDA* dalam Python

Repositori ini berisi implementasi dua algoritma pencarian jalur populer dalam teori graf, yaitu **Uniform Cost Search (UCS)** dan **Iterative Deepening A\* (IDA\*)**. Keduanya digunakan untuk menemukan rute terbaik dari satu titik ke titik lain, terutama pada skenario yang melibatkan peta, rute, dan sistem navigasi.

## 📁 Struktur File

- `ucs.py` – Implementasi algoritma **Uniform Cost Search** menggunakan `PriorityQueue`.
- `ida.py` – Implementasi algoritma **IDA\*** lengkap dengan heuristik, menggunakan pendekatan rekursif dan iterative thresholding.

---

## 🔧 Fitur

### ✅ Uniform Cost Search (UCS)
Uniform Cost Search adalah salah satu algoritma pencarian buta (Blind Search). Konsepnya hampir sama dengan BFS, bedanya adalah bahwa BFS menggunakan urutan level yang paling rendah sampai yang paling tinggi, sedangkan UCS menggunakan urutan biaya dari yang paling kecil sampai yang terbesar. UCS berusaha menemukan solusi dengan total biaya terendah yang dihitung berdasarkan biaya dari simpul asal menuju ke simpul tujuan. Misal kita punya contoh
![image](https://github.com/user-attachments/assets/6f303160-e45a-4b7a-a746-20ba01ec4433)


- Mencari jalur terpendek berdasarkan **biaya aktual** dari titik awal ke titik tujuan.
- Cocok digunakan saat **semua biaya antar simpul diketahui dan tidak ada heuristik**.

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
