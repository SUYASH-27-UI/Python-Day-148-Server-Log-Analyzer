from collections import Counter

def analyze_logs():
    log_counts = Counter()
    error_messages = []

    try:
        with open("server.log", "r") as file:
            for line in file:
                parts = line.strip().split(" ", 3)

                if len(parts) < 4:
                    continue

                log_type = parts[2]
                message = parts[3]

                log_counts[log_type] += 1

                if log_type == "ERROR":
                    error_messages.append(message)

        print("\n===== SERVER LOG REPORT =====")
        print("Total Logs:", sum(log_counts.values()))

        for log_type, count in log_counts.items():
            print(log_type, ":", count)

        print("\n===== ERROR MESSAGES =====")

        if error_messages:
            for error in error_messages:
                print("-", error)
        else:
            print("No errors found.")

        with open("log_report.txt", "w") as report:
            report.write("SERVER LOG REPORT\n")
            report.write("=================\n")
            report.write(
                f"Total Logs: {sum(log_counts.values())}\n"
            )

            for log_type, count in log_counts.items():
                report.write(f"{log_type}: {count}\n")

            report.write("\nERROR MESSAGES:\n")

            for error in error_messages:
                report.write(error + "\n")

        print("\nReport saved to log_report.txt")

    except FileNotFoundError:
        print("server.log file not found!")


analyze_logs()
