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
├── log_analyzer.py    # Script analisis file log
├── infra_monitor.py   # Script monitoring infrastructure
├── sample.log         # File log contoh sebagai input
├── monitor.log        # Output log dari infra_monitor (auto-generated)
└── README.md
```

---

## Cara Kerja

1. Script membaca file log baris per baris
2. Setiap baris dicek apakah mengandung keyword `INFO`, `WARNING`, atau `ERROR`
3. Jumlah kemunculan setiap level dihitung dan ditampilkan sebagai ringkasan
4. Semua baris yang mengandung `ERROR` dikumpulkan dan ditampilkan secara detail

---

## Infrastructure Monitor

### `infra_monitor.py`

Script untuk mengecek apakah service-service infrastruktur (Nginx, WordPress, Grafana, Prometheus) dapat diakses melalui HTTP. Hasil pengecekan ditampilkan di terminal dan dicatat ke file `monitor.log`.

**Cara menggunakan:**

```bash
python infra_monitor.py
```

**Contoh output:**

```
=== Infrastructure Monitor ===
Waktu: 2026-04-14 10:00:00

	[UP]	Nginx (http://localhost:8080) - HTTP 200
	[UP]    WordPress (http://localhost:8081) - HTTP 200
	[UP]    Grafana (http://localhost:3001) - HTTP 200
	[UP]    Prometheus (http://localhost:9090) - HTTP 200

Ringkasan: 4/4 service aktif
Log disimpan di monitor.log
```

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
