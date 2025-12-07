#!/usr/bin/env python3
"""
Patch HTML files to ensure HEAD_FRAGMENT is present.
Usage: python patch_html_head.py HEAD_FRAGMENT.html [list of html files...]
If no html files passed, script will patch all top-level *.html and frontend/*.html
"""
import sys, glob, os

def read_fragment(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def ensure_head_fragment(html_path, frag_text):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if frag_text.strip() in content:
        print(f"SKIP (already contains fragment): {html_path}")
        return
    # insert right after <head> tag
    idx = content.lower().find('<head')
    if idx == -1:
        print("NO <head> TAG:", html_path)
        return
    # find end of opening head tag
    start = content.lower().find('>', idx)
    if start == -1:
        print("MALFORMED <head> in", html_path)
        return
    new_content = content[:start+1] + '\n' + frag_text + '\n' + content[start+1:]
    backup = html_path + '.bak'
    os.rename(html_path, backup)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Patched:", html_path, " (backup at", backup, ")")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python patch_html_head.py HEAD_FRAGMENT.html [files...]")
        sys.exit(1)
    frag = read_fragment(sys.argv[1])
    files = sys.argv[2:]
    if not files:
        files = glob.glob('*.html') + glob.glob('frontend/*.html')
    for html in files:
        if os.path.exists(html):
            ensure_head_fragment(html, frag)
        else:
            print("File not found:", html)
