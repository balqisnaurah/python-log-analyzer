# Python Log Analyzer

Script Python sederhana untuk menganalisis file log. Script ini menghitung jumlah setiap level log (INFO, WARNING, ERROR) dan menampilkan detail baris yang mengandung error.

---

## Contoh Output

```
=== Hasil Analisis Log ===
INFO: 2 entries
WARNING: 1 entries
ERROR: 3 entries

=== Detail Error ===
2026-04-10 08:05:33 ERROR Database connection timeout
2026-04-10 08:10:45 ERROR File not found: config.yaml
2026-04-10 08:20:10 ERROR Memory limit exceeded
```

---

## Cara Menggunakan

**1. Clone repository ini**

```bash
git clone https://github.com/balqisnaurah/python-log-analyzer.git
cd python-log-analyzer
```

**2. Jalankan script**

```bash
python log_analyzer.py
```

Script akan membaca file `sample.log` dan menampilkan hasil analisis di terminal.

**3. Menggunakan file log sendiri**

Ganti nama file pada baris terakhir di `log_analyzer.py`:

```python
if __name__ == "__main__":
    analyze_log("nama_file_log_kamu.log")
```

---

## Struktur File

```
python-log-analyzer/
├── log_analyzer.py    # Script utama untuk analisis log
├── sample.log         # File log contoh sebagai input
└── README.md
```

---

## Cara Kerja

1. Script membaca file log baris per baris
2. Setiap baris dicek apakah mengandung keyword `INFO`, `WARNING`, atau `ERROR`
3. Jumlah kemunculan setiap level dihitung dan ditampilkan sebagai ringkasan
4. Semua baris yang mengandung `ERROR` dikumpulkan dan ditampilkan secara detail

---

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| Python 3 | Bahasa pemrograman utama |
| File I/O | Membaca isi file log |
| String Parsing | Mengidentifikasi level log dari setiap baris |

---

## Tentang

Repository ini dibuat sebagai bagian dari proses belajar pengolahan dan analisis log. Analisis log merupakan salah satu aktivitas penting dalam operasional infrastruktur untuk mendeteksi error, memantau performa sistem, dan melakukan troubleshooting.
