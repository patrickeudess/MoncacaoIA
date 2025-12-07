#!/usr/bin/env python3
"""
Organize repository:
- Create /frontend and move top-level HTML/CSS/JS into it (only moves top-level files)
- Remove .pyc files, some Windows binary files, and zero-byte files
Usage: python organize_repo.py
"""
import os, shutil, glob

ROOT = '.'
FRONTEND = 'frontend'
os.makedirs(FRONTEND, exist_ok=True)

moved = []
# Move top-level HTML/CSS/JS files into frontend/
for ext in ('*.html', '*.css', '*.js'):
    for path in glob.glob(os.path.join(ROOT, ext)):
        if os.path.isfile(path):
            dest = os.path.join(FRONTEND, os.path.basename(path))
            print(f"Moving {path} -> {dest}")
            shutil.move(path, dest)
            moved.append((path, dest))

# Remove .pyc and other cache files
removed = []
for root, dirs, files in os.walk(ROOT):
    for f in files:
        if f.endswith('.pyc') or f.endswith('.pyo') or f in ('python.exe','pythonw.exe','t32.exe','t64.exe','w32.exe','w64.exe'):
            full = os.path.join(root, f)
            try:
                os.remove(full)
                removed.append(full)
                print("Removed:", full)
            except Exception as e:
                print("Cannot remove", full, e)

# Remove empty files
for root, dirs, files in os.walk(ROOT):
    for f in files:
        full = os.path.join(root, f)
        try:
            if os.path.getsize(full) == 0:
                os.remove(full)
                removed.append(full)
                print("Removed empty file:", full)
        except Exception:
            pass

print("Moved files:", moved)
print("Removed files:", removed)
print("Organisation complete.")
