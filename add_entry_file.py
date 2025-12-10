from datetime import datetime

entry = input("Enter log entry: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("mission_log.txt", "a") as file:
    file.write(f"\n{timestamp} User entered: {entry}")

