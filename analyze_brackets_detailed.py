#!/usr/bin/env python3
import re

with open('/Users/zoe.nguyen/Q2 App Prototype/q2-prototype.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the NoRatingHabitDrawer function
start_line = None
end_line = None
depth = 0
for i, line in enumerate(lines):
    if 'function NoRatingHabitDrawer' in line:
        start_line = i
        break

if start_line is None:
    print("NoRatingHabitDrawer function not found")
    exit(1)

# Track bracket depth from function start
curly_depth = 0
paren_depth = 0
square_depth = 0
in_jsx = False
jsx_depth = 0

print(f"Starting analysis from line {start_line + 1}")
print("=" * 80)

for i in range(start_line, min(start_line + 1000, len(lines))):
    line = lines[i]
    line_num = i + 1

    # Count brackets
    for char in line:
        if char == '{':
            curly_depth += 1
        elif char == '}':
            curly_depth -= 1
            if curly_depth < 0:
                print(f"⚠️  Line {line_num}: Extra closing curly brace (depth={curly_depth})")
                print(f"    {line.rstrip()}")
        elif char == '(':
            paren_depth += 1
        elif char == ')':
            paren_depth -= 1
            if paren_depth < 0:
                print(f"⚠️  Line {line_num}: Extra closing parenthesis (depth={paren_depth})")
                print(f"    {line.rstrip()}")
        elif char == '[':
            square_depth += 1
        elif char == ']':
            square_depth -= 1

    # Check if function ended (closing brace at depth 0)
    if curly_depth == 0 and i > start_line and '}' in line:
        end_line = i
        print(f"\nFunction ends at line {line_num}")
        print(f"Final depths: curly={curly_depth}, paren={paren_depth}, square={square_depth}")
        break

print("\n" + "=" * 80)
print(f"Analysis complete: lines {start_line + 1} to {end_line + 1 if end_line else 'EOF'}")
