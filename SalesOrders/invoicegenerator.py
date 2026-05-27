from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os
import subprocess
import sys
from db_connector import get_connection


COMPANY_NAME = "PT. Sejahtera Maju Diesel"
COMPANY_ADDRESS = "Jl.Krekot Bunder 5 no 35 A"
COMPANY_PHONE = "021438331578"
COMPANY_EMAIL = "Sejahteramajudiesel@gmail.com"

DATE_FORMAT = '%d/%m/%Y %H:%i:%s'  # ← define once, reuse everywhere


def open_pdf(filepath):
    if sys.platform == "win32":
        os.startfile(filepath)
    elif sys.platform == "darwin":
        subprocess.run(["open", filepath])
    else:
        subprocess.run(["xdg-open", filepath])

def generate_so_invoice(sales_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Get sales order info
        cursor.execute("""
            SELECT so.SalesID, c.CustomerName, c.Phone, c.Email, c.Address,
                   DATE_FORMAT(so.SalesDate, %s),
                   so.TotalAmount, so.Status
            FROM SalesOrders so
            JOIN Customers c ON so.CustomerID = c.CustomerID
            WHERE so.SalesID = %s
        """, (DATE_FORMAT, sales_id))
        order = cursor.fetchone()

        if not order:
            return False, "Sales Order not found"

        # Get sales detail
        cursor.execute("""
            SELECT p.ProductName, sd.Quantity, sd.UnitPrice, sd.Discount, sd.Subtotal
            FROM SalesDetail sd
            JOIN Products p ON sd.ProductID = p.ProductID
            WHERE sd.SalesID = %s
        """, (sales_id,))
        items = cursor.fetchall()

        # Get payment info
        cursor.execute("""
            SELECT COALESCE(SUM(Amount), 0)
            FROM Payments
            WHERE SalesID = %s
        """, (sales_id,))
        paid_amount = float(cursor.fetchone()[0])

        cursor.close()
        conn.close()

        # Generate PDF
        filename = f"Invoice_SO_{sales_id:04d}.pdf"
        filepath = os.path.join(os.path.expanduser("~"), "Documents", filename)

        doc = SimpleDocTemplate(
            filepath,
            pagesize=A4,
            rightMargin=20*mm,
            leftMargin=20*mm,
            topMargin=20*mm,
            bottomMargin=20*mm
        )

        styles = getSampleStyleSheet()
        story = []

        # Company Header
        company_style = ParagraphStyle(
            'CompanyStyle',
            parent=styles['Normal'],
            fontSize=18,
            fontName='Helvetica-Bold',
            alignment=TA_CENTER,
            spaceAfter=2*mm
        )
        subtitle_style = ParagraphStyle(
            'SubtitleStyle',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            spaceAfter=1*mm
        )

        story.append(Paragraph(COMPANY_NAME, company_style))
        story.append(Paragraph(COMPANY_ADDRESS, subtitle_style))
        story.append(Paragraph(
            f"Phone: {COMPANY_PHONE}  |  Email: {COMPANY_EMAIL}",
            subtitle_style
        ))
        story.append(Spacer(1, 4*mm))

        # Divider line
        divider = Table([['']], colWidths=[170*mm], rowHeights=[1])
        divider.setStyle(TableStyle([
            ('LINEABOVE', (0, 0), (-1, 0), 1.5, colors.black),
        ]))
        story.append(divider)
        story.append(Spacer(1, 4*mm))

        # Invoice Title
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Normal'],
            fontSize=16,
            fontName='Helvetica-Bold',
            alignment=TA_CENTER,
            spaceAfter=5*mm
        )
        story.append(Paragraph("SALES INVOICE", title_style))

        # Invoice Info + Customer Info
        info_style = ParagraphStyle(
            'InfoStyle',
            parent=styles['Normal'],
            fontSize=10,
            leading=16
        )

        # Status color
        status = order[7]
        if status == 'Completed':
            status_text = f'<font color="green"><b>{status}</b></font>'
        elif status == 'Cancelled':
            status_text = f'<font color="red"><b>{status}</b></font>'
        else:
            status_text = f'<font color="orange"><b>{status}</b></font>'

        invoice_info = [
            [
                Paragraph(f"<b>Invoice No :</b> SO-{order[0]:04d}", info_style),
                Paragraph(f"<b>Customer :</b> {order[1]}", info_style)
            ],
            [
                Paragraph(f"<b>Date :</b> {order[5]}", info_style),
                Paragraph(f"<b>Phone :</b> {order[2] or '-'}", info_style)
            ],
            [
                Paragraph(f"<b>Status :</b> {status_text}", info_style),
                Paragraph(f"<b>Email :</b> {order[3] or '-'}", info_style)
            ],
            [
                Paragraph("", info_style),
                Paragraph(f"<b>Address :</b> {order[4] or '-'}", info_style)
            ],
        ]

        info_table = Table(invoice_info, colWidths=[85*mm, 85*mm])
        info_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9FA')),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),
            ('PADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(info_table)
        story.append(Spacer(1, 5*mm))

        # Items Table
        header = ['No', 'Product Name', 'Qty', 'Unit Price', 'Discount', 'Subtotal']
        data = [header]

        for i, item in enumerate(items, 1):
            data.append([
                str(i),
                item[0],
                str(item[1]),
                f"Rp. {float(item[2]):,.2f}",
                f"Rp. {float(item[3]):,.2f}",
                f"Rp. {float(item[4]):,.2f}"
            ])

        items_table = Table(
            data,
            colWidths=[10*mm, 60*mm, 15*mm, 30*mm, 25*mm, 35*mm]
        )
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [
                colors.white,
                colors.HexColor('#ECF0F1')
            ]),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (1, 1), (1, -1), 'LEFT'),
            ('ALIGN', (3, 1), (3, -1), 'RIGHT'),
            ('ALIGN', (4, 1), (4, -1), 'RIGHT'),
            ('ALIGN', (5, 1), (5, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
        ]))
        story.append(items_table)
        story.append(Spacer(1, 5*mm))

        # Total Section
        remaining = float(order[6]) - paid_amount
        total_data = [
            ['', 'Total Amount :', f"Rp. {float(order[6]):,.2f}"],
            ['', 'Paid Amount :', f"Rp. {paid_amount:,.2f}"],
            ['', 'Remaining :', f"Rp. {remaining:,.2f}"],
        ]

        total_table = Table(total_data, colWidths=[95*mm, 40*mm, 40*mm])
        total_table.setStyle(TableStyle([
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (1, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('LINEABOVE', (1, 0), (-1, 0), 0.5, colors.grey),
            ('LINEBELOW', (1, -1), (-1, -1), 1.5, colors.black),
            ('BACKGROUND', (1, -1), (-1, -1), colors.HexColor('#2C3E50')),
            ('TEXTCOLOR', (1, -1), (-1, -1), colors.white),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(total_table)
        story.append(Spacer(1, 15*mm))

        # Signature Section
        sig_data = [
            ['Cashier', '', 'Customer'],
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
            ['_______________', '', '_______________'],
            [COMPANY_NAME, '', order[1]],
        ]
        sig_table = Table(sig_data, colWidths=[55*mm, 60*mm, 55*mm])
        sig_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ]))
        story.append(sig_table)

        doc.build(story)
        open_pdf(filepath)
        return True, filepath

    except Exception as e:
        return False, str(e)
