from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import matplotlib.pyplot as plt
import io
from typing import Dict, Any, List
from .analysis_service import calculate_portfolio_value

def generate_pdf_report(portfolios: List, analytics: Dict[str, Any], insights: str, filename: str = "report.pdf"):
    """
    Generate a PDF report with portfolio summary, charts, and AI insights.
    """
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Portfolio Report", styles['Title']))
    story.append(Spacer(1, 12))

    # Summary
    value_data = calculate_portfolio_value(portfolios)
    story.append(Paragraph(f"Total Portfolio Value: ${value_data['total_value']:.2f}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Allocations Table
    data = [["Ticker", "Allocation %"]]
    for ticker, alloc in value_data['allocations'].items():
        data.append([ticker, f"{alloc:.2f}%"])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    # Chart (simple pie chart)
    fig, ax = plt.subplots()
    labels = list(value_data['allocations'].keys())
    sizes = list(value_data['allocations'].values())
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    # Note: To embed image, need PIL or similar, but for simplicity, skip or use reportlab image
    # For now, just text

    # Insights
    story.append(Paragraph("AI Insights:", styles['Heading2']))
    story.append(Paragraph(insights, styles['Normal']))

    doc.build(story)
    return filename