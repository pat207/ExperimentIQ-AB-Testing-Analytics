from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate(
    "reports/executive_report.pdf"
)

styles = getSampleStyleSheet()

content = []

title = Paragraph(
    "A/B Testing Executive Report",
    styles["Title"]
)

content.append(title)
content.append(Spacer(1, 20))

overview = Paragraph(
"""
This report summarizes the results of an A/B experiment
conducted on 10,000 users to evaluate the effectiveness
of Variant B compared to Variant A.
""",
styles["BodyText"]
)

content.append(overview)
content.append(Spacer(1, 20))

metrics = Paragraph(
"""
<b>Key Results</b><br/><br/>

Conversion Rate A: 4.93%<br/>
Conversion Rate B: 6.40%<br/><br/>

Relative Improvement: 29.8%<br/><br/>

P-Value: 0.0015<br/>
Statistical Power: 88.98%<br/><br/>

Monthly Revenue Gain: $146,944<br/>
Annual Revenue Gain: $1.76M
""",
styles["BodyText"]
)

content.append(metrics)
content.append(PageBreak())

recommendation = Paragraph(
"""
<b>Recommendation</b><br/><br/>

The experiment achieved statistical significance and
Variant B demonstrated a meaningful improvement in
conversion rate.

Recommendation:
Deploy Variant B to production.
""",
styles["BodyText"]
)

content.append(recommendation)

doc.build(content)

print("PDF Report Generated Successfully")