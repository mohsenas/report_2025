import os

def merge_html():
    base_dir = r"c:\Users\khali\Desktop\REPORTS\report_2025"
    comp_dir = os.path.join(base_dir, "components")
    output_file = os.path.join(base_dir, "annual_report_2025.html")
    
    # Define the order of components
    components = [
        "header.html",
        "hero.html",
        "ai_innovation.html",
        "finance.html",
        "supply_chain_production.html",
        "infrastructure.html",
        "timeline.html",
        "footer.html"
    ]
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nawras ERP Annual Report 2025 | Obeikan Digital Solutions</title>
    <link rel="stylesheet" href="style.css">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
"""
    
    for comp in components:
        comp_path = os.path.join(comp_dir, comp)
        if os.path.exists(comp_path):
            with open(comp_path, "r", encoding="utf-8") as f:
                html_content += f"\n<!-- {comp} -->\n"
                html_content += f.read()
        else:
            print(f"Warning: {comp} not found.")
            
    html_content += """
</body>
</html>
"""
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Report successfully merged into {output_file}")

if __name__ == "__main__":
    merge_html()
