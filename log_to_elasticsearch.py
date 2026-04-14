"""
Script untuk mengirim data log dari file ke Elasticsearch.
Membaca file log, memparsing setiap baris, dan mengirimnya
sebagai dokumen JSON ke index Elasticsearch.
"""

import urllib.request
import json
import re

ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "server-logs"
LOG_FILE = "sample.log"

def parse_log_line(line):
    """Memparsing satu baris log menjadi dictionary."""
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
    match = re.match(pattern, line.strip())
    if match:
        return {
            "timestamp": match.group(1).replace(" ", "T"),
            "level": match.group(2),
            "message": match.group(3),
        }
    return None

def send_to_elasticsearch(doc):
    """Mengirim satu dokumen ke Elasticsearch."""
    url = f"{ELASTICSEARCH_URL}/{INDEX_NAME}/_doc"
    data = json.dumps(doc).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        response = urllib.request.urlopen(req)
        return response.getcode()
    except Exception as e:
        return str(e)

def main():
    print(f"Membaca file {LOG_FILE}...")
    success = 0
    failed = 0

    with open(LOG_FILE, "r") as f:
        for line in f:
            doc = parse_log_line(line)
            if doc:
                result = send_to_elasticsearch(doc)
                if result == 201:
                    success += 1
                    print(f"  [OK] {doc['timestamp']} {doc['level']} - {doc['message']}")
                else:
                    failed += 1
                    print(f"  [GAGAL] {line.strip()} - {result}")

    print(f"\nSelesai: {success} berhasil, {failed} gagal")
    print(f"Cek data di Kibana: http://localhost:5601")

if __name__ == "__main__":
    main()
