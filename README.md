# Proyek Pembelajaran Struktur Data

🎯 **Implementasi Interaktif Struktur Data Menggunakan Python & Web (Flask)**

Proyek ini menyediakan implementasi lengkap dari struktur data dasar dengan antarmuka web interaktif berbasis Flask untuk pembelajaran dan eksperimen.

## 📁 Struktur Proyek

```
├── models/                     # Implementasi Python berbasis console
│   ├── array.py                # Operasi array/list
│   ├── graph.py                # Algoritma graf (DFS, BFS, dll)
│   ├── linked_list.py          # Linked list (singly/doubly)
│   ├── pointer.py              # Konsep pointer dan referensi
│   ├── queue.py                # Implementasi antrian (FIFO)
│   ├── record.py               # Tipe data record/struct
│   ├── recursion.py            # Algoritma rekursif
│   ├── stack.py                # Implementasi stack (LIFO)
│   └── tree.py                 # Struktur dan operasi pohon
├── templates/                  # Template HTML Flask
│   ├── index.html              # Halaman navigasi utama
│   └── sections/               # Template HTML per struktur data
│       ├── array.html          # Visualisasi array interaktif
│       ├── graph.html          # Visualisasi graf & algoritma
│       ├── linked_list.html    # Simulasi linked list
│       ├── pointer.html        # Demo referensi pointer
│       ├── queue.html          # Visualisasi operasi antrian
│       ├── record.html         # Demo struktur record
│       ├── recursion.html      # Visualisasi rekursi
│       ├── stack.html          # Demo operasi stack
│       ├── tree.html           # Visualisasi struktur pohon
├── Procfile/                   # Gunicorn
├── app.py                      # Web server Flask utama
├── requirements.txt            # Dependensi Python
└── README.md                   # Dokumentasi proyek (file ini)
```

## 🚀 Memulai Proyek

### Prasyarat

* Python 3.7 atau lebih tinggi
* Browser web modern (Chrome, Firefox, Edge)

### Instalasi

1. **Clone repositori**

   ```bash
   git clone https://github.com/Anang-Programmer/structify.git
   cd structify
   ```

2. **Install dependensi Python**

   ```bash
   pip install -r requirements.txt
   ```

## 💻 Menjalankan Aplikasi Berbasis Console

Setiap file dalam folder `models/` dapat dijalankan secara mandiri:

Contoh:

```bash
python models/stack.py
```

## 🌐 Menjalankan Aplikasi Web (Flask)

1. Jalankan aplikasi Flask:

   ```bash
   python app.py
   ```

2. Buka browser dan akses:

   ```
   http://localhost:5000
   ```

3. Navigasi halaman utama (`index.html`) akan menampilkan menu struktur data interaktif.

## 🎮 Fitur Interaktif (Web)

* **Visualisasi Langkah-per-Langkah**: Operasi struktur data divisualisasikan secara real-time.
* **Kontrol Interaktif**: Tambah, hapus, dan cari elemen langsung di browser.
* **Contoh Kode**: Cuplikan kode ditampilkan untuk membantu pemahaman.

## 📚 Jalur Belajar yang Direkomendasikan

1. **Array** (`models/array.py` → `templates/array.html`)
2. **Stack** (`models/stack.py` → `templates/stack.html`)
3. **Queue** (`models/queue.py` → `templates/queue.html`)
4. **Linked List** (`models/linked_list.py` → `templates/linked_list.html`)
5. **Tree** (`models/tree.py` → `templates/tree.html`)
6. **Graph** (`models/graph.py` → `templates/graph.html`)
7. **Recursion** (`models/recursion.py` → `templates/recursion.html`)
8. **Topik Lanjutan** (Pointer, Record)

## 🔧 Kustomisasi

### Menambahkan Struktur Data Baru:

1. Tambahkan file Python ke dalam folder `models/`
2. Buat tampilan HTML interaktif di `templates/`
3. Tambahkan rute Flask di `app.py`
4. Perbarui navigasi di `index.html`

### Modifikasi Kode:

* File Python modular dan mudah diubah
* Template HTML menggunakan JavaScript vanilla
* CSS dapat dikustomisasi melalui file `static/`

## 🆘 Troubleshooting

**Masalah umum:**

* Jika file Python tidak jalan:

  * Cek versi Python dengan `python --version`
  * Pastikan dependensi sudah diinstal: `pip install -r requirements.txt`

* Jika web tidak tampil dengan benar:

  * Pastikan menjalankan server Flask, bukan buka HTML langsung
  * Gunakan browser modern dan aktifkan JavaScript

## 📝 Lisensi

Proyek ini dibuat oleh Kelompok 1 untuk memenuhi tugas UAS dan Project Mata Kuliah Struktur Data.

---

**Selamat Belajar! 🎓**

*Proyek ini dirancang untuk membuat pembelajaran struktur data lebih seru dan interaktif. Mulailah dengan versi console untuk memahami logika, lalu jelajahi antarmuka web untuk memperkuat pemahaman Anda.*
