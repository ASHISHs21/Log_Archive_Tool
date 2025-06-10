#!/usr/bin/env python3

import argparse
import os
import tarfile
from datetime import datetime
from pathlib import Path

def create_archive(log_dir):
    # Verify the log directory exists
    log_path = Path(log_dir)
    if not log_path.exists() or not log_path.is_dir():
        print(f"Error: The path {log_dir} does not exist or is not a directory.")
        return

    # Create output directory
    archive_dir = Path.home() / "log_archives"
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Archive filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_filename = f"logs_archive_{timestamp}.tar.gz"
    archive_filepath = archive_dir / archive_filename

    # Create tar.gz archive
    with tarfile.open(archive_filepath, "w:gz") as tar:
        for item in log_path.iterdir():
            if item.is_file():
                tar.add(item, arcname=item.name)

    print(f"✅ Logs archived to: {archive_filepath}")

    # Log the operation
    log_file = archive_dir / "archive_log.txt"
    with open(log_file, "a") as logf:
        logf.write(f"{timestamp} - Archived: {archive_filename}\n")

def main():
    parser = argparse.ArgumentParser(description="Archive and compress logs from a given directory.")
    parser.add_argument("log_directory", help="Path to the log directory (e.g. /var/log)")
    args = parser.parse_args()

    create_archive(args.log_directory)

if __name__ == "__main__":
    main()
