#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def validate_symlinks():
    """Validate that symlinks are properly created and point to valid targets."""
    
    symlinks_to_check = [
        ('config/current', 'config/v1.0.0'),
        ('config/latest', 'config/v2.0.0'),
        ('build/latest', 'build/2024-01-16-14-20-30'),
        ('dist/current', 'dist/release-1.2.4')
    ]
    
    print("Validating symlinks...")
    
    for link_path, expected_target in symlinks_to_check:
        if os.path.exists(link_path):
            if os.path.islink(link_path):
                actual_target = os.readlink(link_path)
                if actual_target == expected_target:
                    print(f"✅ {link_path} -> {actual_target}")
                else:
                    print(f"❌ {link_path} -> {actual_target} (expected: {expected_target})")
            else:
                print(f"❌ {link_path} exists but is not a symlink")
        else:
            print(f"❌ {link_path} does not exist")
    
    print("\nSymlink validation completed!")

if __name__ == "__main__":
    validate_symlinks()
