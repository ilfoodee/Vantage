import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'info@vantageheating.com' in content:
            content = content.replace('info@vantageheating.com', 'hello@vantageheating.co.uk')
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
