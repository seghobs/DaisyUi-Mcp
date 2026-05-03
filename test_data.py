import re
import sys

# Set output encoding to UTF-8 to handle any special characters
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_component_extraction(target="button"):
    with open("component_content.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    sections = content.split("\n---\n")
    found = False
    
    for section in sections:
        match = re.search(r"##\s*(.*)", section)
        if match:
            title = match.group(1).strip()
            clean_title = re.sub(r" [-–] daisyUI.*", "", title).lower()
            
            if target in clean_title:
                print(f"FOUND: {title}")
                print("-" * 50)
                # Show first 1000 chars
                print(section[:1000])
                print("\n...\n")
                if "class=" in section:
                    print("SUCCESS: CODE EXAMPLES EXIST")
                found = True
                break
    
    if not found:
        print(f"ERROR: {target} not found!")

print("--- DaisyUI MCP Data Verification Test ---")
test_component_extraction("button")
