

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Step 1: Read CSV file
data = pd.read_csv("data.csv")

# Step 2: Data Analysis
total_employees = len(data)
average_salary = data["Salary"].mean()
max_salary = data["Salary"].max()
min_salary = data["Salary"].min()

department_summary = data.groupby("Department")["Salary"].mean().reset_index()

# Step 3: Create PDF
pdf = SimpleDocTemplate("Employee_Report.pdf", pagesize=A4)
elements = []

styles = getSampleStyleSheet()

elements.append(Paragraph("Employee Salary Report", styles["Heading1"]))
elements.append(Spacer(1, 20))

elements.append(Paragraph(f"Total Employees: {total_employees}", styles["Normal"]))
elements.append(Paragraph(f"Average Salary: ₹{average_salary:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Salary: ₹{max_salary}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Salary: ₹{min_salary}", styles["Normal"]))
elements.append(Spacer(1, 20))

# Table Data
table_data = [["Department", "Average Salary"]]

for _, row in department_summary.iterrows():
    table_data.append([row["Department"], f"₹{row['Salary']:.2f}"])

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)

pdf.build(elements)

print("PDF Report Generated Successfully!")
