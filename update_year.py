import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('© 2025 BTEC HUB', '© 2026 BTEC HUB')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated year in {file}")
