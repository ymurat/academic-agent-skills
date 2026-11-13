#!/usr/bin/env python3
"""Find duplicate files across skill folders by SHA256 hash."""

import hashlib
import os
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


def compute_sha256(filepath: Path) -> str:
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def find_duplicates(skills_dir: Path) -> Tuple[Dict[str, List[Path]], int]:
    """
    Find duplicate files across skill folders.
    
    Returns:
        Tuple of (hash_to_files mapping, total duplicate bytes)
    """
    hash_to_files: Dict[str, List[Path]] = defaultdict(list)
    
    # Find all files in resources, references, scripts subdirectories
    for skill_folder in skills_dir.iterdir():
        if not skill_folder.is_dir():
            continue
        
        for subdir in ['resources', 'references', 'scripts']:
            subdir_path = skill_folder / subdir
            if subdir_path.exists():
                for filepath in subdir_path.rglob('*'):
                    if filepath.is_file() and not filepath.name.startswith('.'):
                        file_hash = compute_sha256(filepath)
                        hash_to_files[file_hash].append(filepath)
    
    # Filter to only duplicates (2+ files with same hash)
    duplicates = {h: files for h, files in hash_to_files.items() if len(files) > 1}
    
    # Calculate duplicate bytes
    duplicate_bytes = 0
    for files in duplicates.values():
        file_size = files[0].stat().st_size
        # Count (n-1) * size since we keep one copy
        duplicate_bytes += (len(files) - 1) * file_size
    
    return duplicates, duplicate_bytes


def main():
    """Find and report duplicate files."""
    repo_root = Path(__file__).parent.parent
    skills_dir = repo_root / 'skills'
    
    print("Scanning for duplicate files...")
    duplicates, duplicate_bytes = find_duplicates(skills_dir)
    
    if not duplicates:
        print("No duplicates found.")
        return
    
    print(f"\nFound {len(duplicates)} sets of duplicate files")
    print(f"Potential space savings: {duplicate_bytes:,} bytes ({duplicate_bytes / 1024:.1f} KB)")
    print("\nDuplicate file groups:\n")
    
    for file_hash, files in sorted(duplicates.items(), 
                                   key=lambda x: x[1][0].stat().st_size, 
                                   reverse=True):
        file_size = files[0].stat().st_size
        print(f"Hash: {file_hash[:12]}... ({file_size:,} bytes)")
        for filepath in sorted(files):
            rel_path = filepath.relative_to(repo_root)
            print(f"  - {rel_path}")
        print()


if __name__ == '__main__':
    main()
