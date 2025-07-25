#!/usr/bin/env python3

import os
import shutil
from pathlib import Path

def demonstrate_symlink_usage():
    """Demonstrate common symlink usage patterns in Python."""
    
    print("Symlink Usage Examples in Python")
    print("=" * 40)
    
    # Example 1: Check if path is a symlink
    def is_symlink(path):
        return os.path.islink(path)
    
    # Example 2: Get symlink target
    def get_symlink_target(path):
        if os.path.islink(path):
            return os.readlink(path)
        return None
    
    # Example 3: Create symlink (Unix-like systems)
    def create_symlink(target, link_name):
        try:
            if os.path.exists(link_name):
                os.remove(link_name)
            os.symlink(target, link_name)
            print(f"Created symlink: {link_name} -> {target}")
        except OSError as e:
            print(f"Error creating symlink: {e}")
    
    # Example 4: Follow symlink to get real path
    def get_real_path(path):
        return os.path.realpath(path)
    
    # Example 5: List all symlinks in directory
    def list_symlinks(directory):
        symlinks = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.islink(item_path):
                target = os.readlink(item_path)
                symlinks.append((item, target))
        return symlinks
    
    print("\n1. Check if path is symlink:")
    print("   os.path.islink('config/current')")
    
    print("\n2. Get symlink target:")
    print("   os.readlink('config/current')")
    
    print("\n3. Create symlink:")
    print("   os.symlink('target', 'link_name')")
    
    print("\n4. Get real path (follow symlinks):")
    print("   os.path.realpath('config/current')")
    
    print("\n5. List symlinks in directory:")
    print("   [item for item in os.listdir('config') if os.path.islink(os.path.join('config', item))]")

if __name__ == "__main__":
    demonstrate_symlink_usage()
