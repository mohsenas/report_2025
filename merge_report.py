import os

def merge_html():
    base_dir = r"c:\Users\khali\Desktop\REPORTS\report_2025"
    comp_dir = os.path.join(base_dir, "components")
    output_file = os.path.join(base_dir, "annual_report_2025.html")
    
    # Clean, minimalist component order
    components = [
        "cover.html",
        "header.html",
        "toc.html",
        "executive_summary.html",
        "ai_section.html",
        "erp_modules.html",
        "finance_section.html",
        "infrastructure_section.html",
        "timeline_section.html",
        "footer.html"
    ]
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annual Report 2025 | Obeikan Digital Solutions</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="report-container">
"""
    
    for comp in components:
        comp_path = os.path.join(comp_dir, comp)
        if os.path.exists(comp_path):
            with open(comp_path, "r", encoding="utf-8") as f:
                html_content += f"\n<!-- {comp} -->\n"
                html_content += f.read()
        else:
            print(f"Warning: {comp} not found")
            
    html_content += """
</div>
</body>
</html>
"""
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✓ Report successfully created: {output_file}")

if __name__ == "__main__":
    merge_html()
