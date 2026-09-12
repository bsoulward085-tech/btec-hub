import os
import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ورد البصول' not in content:
        # We replace the closing </p> of the footer-copy paragraph
        new_content = re.sub(
            r'(<p class="footer-copy">.*?)<\/p>',
            r'\1 <br><span style="font-size: 0.9em; opacity: 0.9; margin-top: 5px; display: inline-block; color: var(--primary-light);">تم التطوير بواسطة <strong>ورد البصول</strong></span></p>',
            content,
            flags=re.DOTALL
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file} (already contains name)")
