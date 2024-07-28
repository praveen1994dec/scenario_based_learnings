import os
from datetime import datetime

def aggregate_logs(log_dir, output_file):
    with open(output_file, "w") as outfile:
        for log_file in os.listdir(log_dir):
            if log_file.endswith(".log"):
                with open(os.path.join(log_dir, log_file), "r") as infile:
                    for line in infile:
                        outfile.write(line)
    print(f"Logs aggregated to {output_file}")

def analyze_logs(log_file):
    error_count = 0
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
    print(f"Number of errors found: {error_count}")

if __name__ == "__main__":
    log_directory = "/var/log/myapp"
    aggregated_log_file = f"aggregated_logs_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
    aggregate_logs(log_directory, aggregated_log_file)
    analyze_logs(aggregated_log_file)
