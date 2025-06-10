# Log_Archive_Tool
https://roadmap.sh/projects/log-archive-tool

# 📦 Log Archive Tool

A simple command-line tool to compress and archive log files from a specified directory.  
It helps you clean up old logs and store them in a compressed format for future reference.

---

## 🔧 Features

- Compresses all log files in a specified directory (`.tar.gz` format)
- Stores the archive in a dedicated `log_archives/` directory
- Automatically timestamps the archive
- Logs all archive operations to a log file (`archive_log.txt`)

---

## 🧰 Installation Requirements

✅ This tool is written in Python and uses only standard libraries — **no additional packages required**!

Make sure Python 3 is installed:

```bash
python3 --version
If Python is not installed, you can install it:

On Ubuntu/Debian:
sudo apt update
sudo apt install python3

On CentOS/RHEL:
sudo yum install python3

On macOS (with Homebrew):
brew install python

🚀 How to Use
Clone the repository or download the script:

git clone https://github.com/ASHISHs21/Log_Archive_Tool
cd Log_Archive_Tool

Run the script:
python3 log_archive.py <log-directory>

For example:
python3 log_archive.py /var/log


📁 Example Output

~/log_archives/
├── logs_archive_20250610_113012.tar.gz
└── archive_log.txt


⏰ Automate with Cron (Optional)
To schedule the archive job (e.g., daily at midnight), use cron:
crontab -e

Add a line like this (update the path):
0 0 * * * /usr/bin/python3 /path/to/log_archive.py /var/log
