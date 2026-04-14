# Python Log Analyzer & Infrastructure Monitor

Kumpulan script Python untuk analisis log dan monitoring infrastruktur.

---

## Daftar Script

### `log_analyzer.py`

Script untuk menganalisis file log. Menghitung jumlah setiap level log (INFO, WARNING, ERROR) dan menampilkan detail baris yang mengandung error.

**Cara menggunakan:**

```bash
python log_analyzer.py
```

**Contoh output:**

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

**Cara kerja:**
1. Script membaca file log baris per baris
2. Setiap baris dicek apakah mengandung keyword `INFO`, `WARNING`, atau `ERROR`
3. Jumlah kemunculan setiap level dihitung dan ditampilkan sebagai ringkasan
4. Semua baris yang mengandung `ERROR` dikumpulkan dan ditampilkan secara detail

---

### `infra_monitor.py`

Script untuk mengecek apakah service-service infrastruktur dapat diakses melalui HTTP. Hasil pengecekan ditampilkan di terminal dan dicatat ke file `monitor.log`.

**Service yang dimonitor:**

| Service | URL |
|---------|-----|
| Nginx | http://localhost:8080 |
| WordPress | http://localhost:8081 |
| Grafana | http://localhost:3001 |
| Prometheus | http://localhost:9090 |

**Cara menggunakan:**

```bash
python infra_monitor.py
```

**Contoh output:**

```
=== Infrastructure Monitor ===
Waktu: 2026-04-14 10:00:00

  [UP]   Nginx (http://localhost:8080) - HTTP 200
  [UP]   WordPress (http://localhost:8081) - HTTP 200
  [UP]   Grafana (http://localhost:3001) - HTTP 200
  [UP]   Prometheus (http://localhost:9090) - HTTP 200

Ringkasan: 4/4 service aktif
Log disimpan di monitor.log
```

**Cara kerja:**
1. Script melakukan HTTP request ke setiap service yang terdaftar
2. Jika response berhasil (HTTP 200), service ditandai UP
3. Jika request gagal (timeout atau connection refused), service ditandai DOWN
4. Semua hasil pengecekan ditulis ke file `monitor.log` dengan timestamp

---

## Struktur File

```
python-log-analyzer/
├── log_analyzer.py    # Script analisis file log
├── infra_monitor.py   # Script monitoring infrastruktur
├── sample.log         # File log contoh sebagai input
├── monitor.log        # Output log dari infra_monitor (auto-generated)
└── README.md
```

---

## Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| Python 3 | Bahasa pemrograman utama |
| File I/O | Membaca dan menulis file log |
| String Parsing | Mengidentifikasi level log dari setiap baris |
| urllib | HTTP request untuk pengecekan service |
| datetime | Generating timestamp untuk log |

---

## Tentang

Repository ini dibuat sebagai bagian dari proses belajar pengolahan log dan monitoring infrastruktur. Kedua aktivitas ini merupakan bagian penting dalam operasional infrastruktur untuk mendeteksi error, memantau ketersediaan service, dan melakukan troubleshooting.
