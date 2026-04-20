#!/usr/bin/env python3
import re

with open('/Users/zoe.nguyen/Q2 App Prototype/q2-prototype-backup.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JavaScript from script tag
script_match = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
if script_match:
    js_content = script_match.group(1)

    # Count brackets
    curly_open = js_content.count('{')
    curly_close = js_content.count('}')
    paren_open = js_content.count('(')
    paren_close = js_content.count(')')
    square_open = js_content.count('[')
    square_close = js_content.count(']')

    print("BACKUP FILE Bracket counts:")
    print(f"Curly brackets: open={curly_open}, close={curly_close}, diff={curly_open-curly_close}")
    print(f"Parentheses: open={paren_open}, close={paren_close}, diff={paren_open-paren_close}")
    print(f"Square brackets: open={square_open}, close={square_close}, diff={square_open-square_close}")
