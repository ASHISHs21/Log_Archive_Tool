"""
log_archive.py - Log Archiving CLI Tool

Copyright (c) 2025 Ashish Singh
License: MIT (see LICENSE file for full text)
"""

#!/usr/bin/env python3

import argparse
import os
import tarfile
from datetime import datetime
from pathlib import Path

def create_archive(log_dir):
    log_path = Path(log_dir)
    if not log_path.exists() or not log_path.is_dir():
        print(f"❌ Error: The path {log_dir} does not exist or is not a directory.")
        return

    archive_dir = Path.home() / "log_archives"
    archive_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_filename = f"logs_archive_{timestamp}.tar.gz"
    archive_filepath = archive_dir / archive_filename

    with tarfile.open(archive_filepath, "w:gz") as tar:
        for item in log_path.iterdir():
            if item.is_file() and item.suffix == ".log":
                try:
                    tar.add(item, arcname=item.name)
                    print(f"✅ Added: {item.name}")
                except PermissionError:
                    print(f"⚠️ Skipped (Permission denied): {item}")
                except Exception as e:
                    print(f"⚠️ Skipped {item} due to error: {e}")

    print(f"\n🎉 Archive created: {archive_filepath}")

    # Log the operation
    log_file = archive_dir / "archive_log.txt"
    with open(log_file, "a") as logf:
        logf.write(f"{timestamp} - Archived: {archive_filename}\n")

def main():
    parser = argparse.ArgumentParser(description="Compress and archive .log files from a directory.")
    parser.add_argument("log_directory", help="Path to the log directory (e.g. /var/log)")
    args = parser.parse_args()

    create_archive(args.log_directory)

if __name__ == "__main__":
    main()
