import sys
with open(r'C:\Users\bsoul\.gemini\antigravity\brain\5552011b-04fd-4345-8d1e-5a1b1b107242\scratch\rebuild_proper.py', 'r', encoding='utf-8') as f:
    code = f.read()
code = code.replace("print(f'\\u2705  {filename}')", "open('rebuild_log.txt','a').write(f'OK: {filename}\\n')")
exec(code)
