#!/usr/bin/env python3
"""
Main entry point for news-image-20261122.
Copies assets/entry.png to $MAKEFUN_OUTPUT_DIR/entry.png (default '/output')
and verifies output file size and SHA256 checksum.
"""

import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "89ef34aebb989816e5676f708a27448532e39b02b775ef174adae531888a8415"
EXPECTED_SIZE = 319424


def verify_output(dest_path: str) -> None:
    """Verifies that the copied file matches expected size and SHA256 checksum strictly."""
    if not os.path.exists(dest_path):
        raise FileNotFoundError(f"Critical error: Destination file missing at {dest_path}")
    
    file_size = os.path.getsize(dest_path)
    if file_size != EXPECTED_SIZE:
        raise ValueError(f"Integrity check failed: size mismatch (expected {EXPECTED_SIZE} bytes, got {file_size} bytes)")

    sha = hashlib.sha256()
    with open(dest_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha.update(chunk)
    file_sha = sha.hexdigest()
    if file_sha != EXPECTED_SHA256:
        raise ValueError(f"Integrity check failed: SHA256 mismatch (expected {EXPECTED_SHA256}, got {file_sha})")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    src_path = os.path.join(os.path.dirname(__file__), "assets", "entry.png")
    dest_path = os.path.join(output_dir, "entry.png")
    
    shutil.copyfile(src_path, dest_path)
    verify_output(dest_path)
    print(f"Successfully generated and verified {dest_path}")


if __name__ == "__main__":
    main()
