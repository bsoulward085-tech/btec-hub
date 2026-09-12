import glob
import re
import base64

html_files = glob.glob('*.html')
new_text = base64.b64decode("wqkgMjAyNiBCVEVDIEhVQi4g2KzZhdmK2Lkg2KfZhNit2YLZiNmCINmF2K3ZgdmI2LjYqS4gPGJyPjxzcGFuIHN0eWxlPSJmb250LXNpemU6IDAuOWVtOyBvcGFjaXR5OiAwLjk7IG1hcmdpbi10b3A6IDVweDsgZGlzcGxheTogaW5saW5lLWJsb2NrOyBjb2xvcjogdmFyKC0tcHJpbWFyeS1saWdodCk7Ij7YqtmFINin2YTYqNi32YjZitixINio2YjYp9iz2LfZqSA8c3Ryb25nPtmI2LHYryDYp9mE2KjYtdmI2YQ8L3N0cm9uZz48L3NwYW4+").decode('utf-8')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the contents of <p class="footer-copy">...</p>
    content = re.sub(r'<p class="footer-copy">.*?</p>', f'<p class="footer-copy">{new_text}</p>', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Successfully fixed encoding and added the name.")
