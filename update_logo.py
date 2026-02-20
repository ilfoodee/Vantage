import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

logo_html = '''<div class="flex items-center gap-3">
          <div class="flex items-center justify-center w-10 h-10 rounded-full bg-primary/10 text-primary">
            <span class="material-symbols-outlined text-[24px]">hvac</span>
          </div>
          <h2 class="text-secondary dark:text-white text-xl font-extrabold leading-tight tracking-tight">Vantage Heating</h2>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert all img logo tags
    # The header one contains "h-12 md:h-16" or "h-10 w-auto object-contain hidden"
    content = re.sub(
        r'<img alt="Vantage Heating Logo" class="[^"]*" src="https://lh3\.googleusercontent\.com/[^"]*"[^>]*>',
        '',
        content
    )
    
    # We also might have empty <div class="flex justify-center mb-16"></div> now.
    content = re.sub(
        r'<div class="flex justify-center mb-16">\s*</div>',
        '',
        content
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated logo successfully.")
