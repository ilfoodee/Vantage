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

    # Revert logo in header
    content = re.sub(
        r'<div class="flex items-center gap-3">\s*<img alt="Vantage Heating Logo" class="h-12 md:h-16 w-auto object-contain"[^>]*>\s*</div>',
        logo_html,
        content
    )
    
    content = re.sub(
        r'<div class="flex justify-center">\s*<img alt="Vantage Heating Logo" class="h-10 w-auto object-contain hidden" src="https://lh3[^>]*>\s*</div>',
        '',
        content
    )
    
    # Change emails
    content = content.replace('info@vantageheating.com', 'hello@vantageheating.co.uk')
    content = content.replace('support@vantageheating.com', 'hello@vantageheating.co.uk')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated logo and emails successfully.")
