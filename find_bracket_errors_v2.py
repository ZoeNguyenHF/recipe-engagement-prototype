#!/usr/bin/env python3
import re

with open('/Users/zoe.nguyen/Q2 App Prototype/q2-prototype.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the script tag
script_start = None
for i, line in enumerate(lines):
    if '<script type="text/babel">' in line:
        script_start = i + 1  # Line after the script tag
        break

if script_start is None:
    print("Script tag not found")
    exit(1)

# Track depth
curly_depth = 0
paren_depth = 0
min_curly = 0
min_paren = 0
error_lines = []

for i in range(script_start, len(lines)):
    line = lines[i]
    if '</script>' in line:
        break

    actual_line_num = i + 1  # 1-indexed line number in the file

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
                error_lines.append(('curly', actual_line_num, line.rstrip(), curly_depth))
        elif char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth -= 1
            if paren_depth < 0 and paren_depth < min_paren:
                min_paren = paren_depth
                error_lines.append(('paren', actual_line_num, line.rstrip(), paren_depth))

print("Bracket balance errors found (showing file line numbers):")
print("=" * 80)
for bracket_type, line_num, line_content, depth in error_lines[-10:]:  # Show last 10 errors
    print(f"File line {line_num} ({bracket_type}): depth={depth}")
    print(f"  {line_content}")
    print()

print(f"\nFinal depths: curly={curly_depth}, paren={paren_depth}")
print(f"Minimum depths reached: curly={min_curly}, paren={min_paren}")
