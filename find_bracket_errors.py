#!/usr/bin/env python3
import re

with open('/Users/zoe.nguyen/Q2 App Prototype/q2-prototype.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JavaScript from script tag
script_match = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
if not script_match:
    print("No script tag found")
    exit(1)

js_content = script_match.group(1)
lines = js_content.split('\n')

# Track depth as we go through the file
curly_depth = 0
paren_depth = 0
min_curly = 0
min_paren = 0
error_lines = []

for i, line in enumerate(lines, 1):
    # Skip lines that are mostly comments
    stripped = line.strip()
    if stripped.startswith('//'):
        continue

    for j, char in enumerate(line):
        if char == '{':
            curly_depth += 1
        elif char == '}':
            curly_depth -= 1
            if curly_depth < 0 and curly_depth < min_curly:
                min_curly = curly_depth
                error_lines.append(('curly', i, line.rstrip(), curly_depth))
        elif char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth -= 1
            if paren_depth < 0 and paren_depth < min_paren:
                min_paren = paren_depth
                error_lines.append(('paren', i, line.rstrip(), paren_depth))

print("Bracket balance errors found:")
print("=" * 80)
for bracket_type, line_num, line_content, depth in error_lines[-10:]:  # Show last 10 errors
    print(f"Line {line_num} ({bracket_type}): depth={depth}")
    print(f"  {line_content}")
    print()

print(f"\nFinal depths: curly={curly_depth}, paren={paren_depth}")
print(f"Minimum depths reached: curly={min_curly}, paren={min_paren}")
