# 🔍 Algoritma Pencarian Jalur: UCS & IDA* dalam Python

Repositori ini berisi implementasi dua algoritma pencarian jalur populer dalam teori graf, yaitu **Uniform Cost Search (UCS)** dan **Iterative Deepening A\* (IDA\*)**. Keduanya digunakan untuk menemukan rute terbaik dari satu titik ke titik lain, terutama pada skenario yang melibatkan peta, rute, dan sistem navigasi.

## 📁 Struktur File

- `ucs.py` – Implementasi algoritma **Uniform Cost Search** menggunakan Python dan `PriorityQueue`.
- `ida.py` – Implementasi algoritma **IDA\*** lengkap dengan heuristik, menggunakan pendekatan rekursif dan iterative thresholding.

---

## 🔧 Fitur

### ✅ Uniform Cost Search (UCS)
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
