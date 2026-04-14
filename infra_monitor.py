"""
Script untuk monitoring infrastruktur sederhana.
Mengecek apakah service tertentu bisa diaksesmelalui HTTP
dan mencatat hasilnya ke file log.
"""

import urllib.request
import datetime
import json

SERVICES = [
	{"name": "Nginx", "url": "http://localhost:8080"},
	{"name": "WordPress", "url": "http://localhost:8081"},
	{"name": "Grafana", "url": "http://localhost:3001"},
	{"name": "Prometheus", "url": "http://localhost:9090"},
]

LOG_FILE = "monitor.log"

def check_service(name, url, timeout=5):
	"""Mengecek apakah service bisa diakses."""
	try:
		response = urllib.request.urlopen(url, timeout=timeout)
		return {
			"name": name,
			"url": url,
			"status": "UP",
			"http_code": response.getcode(),
		}
	except Exception as e:
		return {
			"name": name,
                        "url": url,
                        "status": "DOWN",
                        "error": str(e),
		}

def write_log(results):
	"""Menulis hasil monitoring ke file log."""
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open(LOG_FILE, "a") as f:
		for result in results:
			status = result["status"]
			name = result["name"]
			f.write(f"{timestamp} | {name} | {status}\n")

def main():
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"=== Infrastructure Monitor ===")
	print(f"Waktu: {timestamp}")
	print()

	results = []
	for service in SERVICES:
		result = check_service(service["name"], service["url"])
		results.append(result)

		if result["status"] == "UP":
			print(f"	[UP]	{result['name']} ({result['url']}) - HTTP {result['http_code']}")
		else:
			print(f"	[DOWN]	{result['name']} ({result['url']}) - {result.get('error', 'Unknown')}")

	write_log(results)

	up_count = sum(1 for r in results if r["status"] == "UP")
	total = len(results)
	print()
	print(f"Ringkasan: {up_count}/{totak} service aktif")
	print(f"Log disimpan di {LOG_FILE}")

if __name__ == "__main__":
	main()
