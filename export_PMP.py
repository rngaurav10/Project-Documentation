from weasyprint import HTML, CSS

# Input and output file paths
input_file = "pmp.html"
output_file = "pmp.pdf"

# Optional: custom CSS for PDF formatting
custom_css = CSS(string="""
    @page {
        size: A4;
        margin: 2cm;
    }
    body {
        font-family: Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.5;
    }
    h1, h2, h3 {
        color: #004080;
    }
    header {
        position: running(header);
        text-align: center;
        font-size: 10pt;
        color: #555;
    }
    footer {
        position: running(footer);
        text-align: right;
        font-size: 9pt;
        color: #777;
    }
    @page {
        @top-center { content: element(header) }
        @bottom-right { content: "Page " counter(page) " of " counter(pages); }
    }
""")

# Generate PDF
HTML(input_file).write_pdf(output_file, stylesheets=[custom_css])

print(f"✅ PDF generated successfully: {output_file}")
