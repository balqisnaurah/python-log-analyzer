"""
Script sederhana untuk menganalisis file log.
Menghitung jumlah level log (INFO, WARNING, ERROR)
dan menampilkan semua baris yang mengandung ERROR.
"""

def analyze_log(file_path):
	log_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}
	error_lines = []

	with open(file_path, "r") as file:
		for line in file:
			for level in log_count:
				if level in line:
					log_count[level] += 1
					if level == "ERROR":
						error_lines.append(line.strip())

	print("=== Hasil Analisis Log ===")
	for level, count in log_count.items():
		print(f"{level}: {count} entries")

	print("\n=== Detail Error ===")
	for error in error_lines:
		print(error)

if __name__ == "__main__":
	analyze_log("sample.log")
