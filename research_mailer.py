#!/usr/bin/env python3
"""
Life OS Araştırma Maili
Pazartesi: Mesleki | Çarşamba: MindTech | Cuma: Sağlık
PDF ekiyle birlikte gönderir.
"""
import smtplib, os, sys, io
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Kütüphane kurulumu
try:
    from fpdf import FPDF
except ImportError:
    os.system(f"{sys.executable} -m pip install fpdf2 -q")
    from fpdf import FPDF

from research_bank import MESLEKI, MINDTECH, SAGLIK

GMAIL_USER = os.environ.get('GMAIL_USER', 'canisokrktn@gmail.com')
GMAIL_PASS = os.environ.get('GMAIL_PASS', '')
TO = 'canisokrktn@gmail.com'

KATEGORILER = {
    0: ("Mesleki", MESLEKI, "🏥", "Anjiyografi · DSA · İnme Merkezi"),
    2: ("MindTech", MINDTECH, "💡", "Uygulama Geliştirme · JITAI · Flutter"),
    4: ("Sağlık", SAGLIK, "💚", "Alerji · Astım · Yaşam Kalitesi"),
}

def hafta_indeksi():
    """Yılın kaçıncı haftası — rotasyon için"""
    return date.today().isocalendar()[1]

def pdf_olustur(kategori_adi, ikon, alt_baslik, arastirma):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 20, 20)

    # Başlık bloğu
    pdf.set_fill_color(20, 20, 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 14, f"LIFE OS — {kategori_adi.upper()} ARASTIRMASI", ln=True, fill=True, align="C")

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 8, alt_baslik, ln=True, align="C")
    pdf.ln(4)

    # Araştırma başlığı
    pdf.set_fill_color(230, 57, 70)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 16)
    pdf.multi_cell(0, 10, arastirma["baslik"], fill=True, align="L")
    pdf.ln(2)

    pdf.set_text_color(100, 100, 100)
    pdf.set_font("Helvetica", "I", 11)
    pdf.multi_cell(0, 7, arastirma["alt"])
    pdf.ln(6)

    # Özet
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 9, "OZET", ln=True)
    pdf.set_draw_color(230, 57, 70)
    pdf.set_line_width(0.8)
    pdf.line(20, pdf.get_y(), 100, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    for para in arastirma["ozet"].strip().split("\n\n"):
        pdf.multi_cell(0, 6, para.strip())
        pdf.ln(3)

    # Anahtar noktalar
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 9, "ANAHTAR NOKTALAR", ln=True)
    pdf.line(20, pdf.get_y(), 100, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 10)
    for nokta in arastirma["anahtar"]:
        pdf.set_text_color(230, 57, 70)
        pdf.cell(8, 7, chr(149))
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 7, nokta.strip())

    # Pratik uygulama
    pdf.ln(4)
    pdf.set_fill_color(245, 245, 245)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 9, "BU HAFTA UYGULA", ln=True, fill=True)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 7, arastirma["pratik"].strip(), fill=True)

    # Kaynaklar
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 9, "KAYNAKLAR", ln=True)
    pdf.line(20, pdf.get_y(), 100, pdf.get_y())
    pdf.ln(3)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    for kaynak in arastirma["kaynaklar"]:
        pdf.multi_cell(0, 6, f"  {chr(8226)}  {kaynak}")

    # Footer
    pdf.set_y(-20)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 8, f"Life OS 3.0  |  {date.today().strftime('%d.%m.%Y')}  |  Can Korkutan", align="C")

    return pdf.output()

def send_research(kategori_adi, ikon, alt_baslik, banka):
    indeks = hafta_indeksi() % len(banka)
    arastirma = banka[indeks]

    # PDF oluştur
    pdf_bytes = pdf_olustur(kategori_adi, ikon, alt_baslik, arastirma)

    # Mail
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = TO
    msg['Subject'] = f"{ikon} {kategori_adi}: {arastirma['baslik']}"

    body = f"""{ikon} LIFE OS — {kategori_adi.upper()} ARAŞTIRMASI

{arastirma['baslik']}
{arastirma['alt']}

━━━━━━━━━━━━━━━━━━━━━
BU HAFTAKİ KONU
━━━━━━━━━━━━━━━━━━━━━
{arastirma['ozet'][:400]}...

Detaylı araştırma ekteki PDF dosyasında.

━━━━━━━━━━━━━━━━━━━━━
BU HAFTA UYGULA
━━━━━━━━━━━━━━━━━━━━━
{arastirma['pratik']}

— Life OS 3.0"""

    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # PDF ekle
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(pdf_bytes)
    encoders.encode_base64(attachment)
    dosya_adi = f"LifeOS_{kategori_adi}_{date.today().strftime('%d%m%Y')}.pdf"
    attachment.add_header('Content-Disposition', f'attachment; filename="{dosya_adi}"')
    msg.attach(attachment)

    with smtplib.SMTP('smtp.gmail.com', 587, timeout=30) as s:
        s.starttls()
        s.login(GMAIL_USER, GMAIL_PASS)
        s.send_message(msg)

    print(f"✅ {kategori_adi} araştırması gönderildi: {arastirma['baslik']}")

if __name__ == '__main__':
    # Argüman verilmişse o kategoriyi gönder (test için)
    # python research_mailer.py mesleki / mindtech / saglik / test
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else ''

    if arg == 'mesleki':
        send_research(*KATEGORILER[0][::1])
    elif arg in ('mindtech', 'mt'):
        send_research(*KATEGORILER[2][::1])
    elif arg in ('saglik', 'sağlık'):
        send_research(*KATEGORILER[4][::1])
    elif arg == 'test':
        # Test modunda Mesleki gönder
        kat, banka, ikon, alt = KATEGORILER[0]
        send_research(kat, ikon, alt, banka)
    else:
        bugun = date.today().weekday()
        if bugun in KATEGORILER:
            kat, banka, ikon, alt = KATEGORILER[bugun]
            send_research(kat, ikon, alt, banka)
        else:
            print(f"Bugün ({bugun}) araştırma günü değil.")
