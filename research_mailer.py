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

def temizle(metin):
    """Unicode karakterleri ASCII'ye cevir"""
    return (metin
        .replace('—', '-').replace('–', '-')
        .replace('•', '*').replace('’', "'")
        .replace('‘', "'").replace('“', '"')
        .replace('”', '"').replace('…', '...')
        .replace('─', '-').replace('━', '=')
        .replace('┃', '|').replace('●', '*')
        .replace('✔', '+').replace('✘', 'x')
        .replace('ı', 'i').replace('ş', 's')
        .replace('ğ', 'g').replace('ü', 'u')
        .replace('ö', 'o').replace('ç', 'c')
        .replace('İ', 'I').replace('Ş', 'S')
        .replace('Ğ', 'G').replace('Ü', 'U')
        .replace('Ö', 'O').replace('Ç', 'C')
        .replace('̇', '').encode('latin-1', 'ignore').decode('latin-1')
    )

def pdf_olustur(kategori_adi, ikon, alt_baslik, arastirma):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 20, 20)

    baslik_txt = temizle(f"LIFE OS - {kategori_adi.upper()} ARASTIRMASI")
    alt_txt    = temizle(alt_baslik)
    ar_baslik  = temizle(arastirma["baslik"])
    ar_alt     = temizle(arastirma["alt"])
    ar_ozet    = temizle(arastirma["ozet"])
    ar_pratik  = temizle(arastirma["pratik"])

    # Başlık
    pdf.set_fill_color(20, 20, 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 14, baslik_txt, new_x="LMARGIN", new_y="NEXT", fill=True, align="C")

    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 8, alt_txt, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(4)

    # Araştırma başlığı
    pdf.set_fill_color(230, 57, 70)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 15)
    pdf.multi_cell(0, 10, ar_baslik, fill=True, align="L")
    pdf.ln(2)

    pdf.set_text_color(100, 100, 100)
    pdf.set_font("Helvetica", "I", 11)
    pdf.multi_cell(0, 7, ar_alt)
    pdf.ln(6)

    # Özet
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 9, "OZET", new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(230, 57, 70)
    pdf.set_line_width(0.8)
    pdf.line(20, pdf.get_y(), 100, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    for para in ar_ozet.strip().split("\n\n"):
        pdf.multi_cell(0, 6, para.strip())
        pdf.ln(3)

    # Anahtar noktalar
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 9, "ANAHTAR NOKTALAR", new_x="LMARGIN", new_y="NEXT")
    pdf.line(20, pdf.get_y(), 100, pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    for nokta in arastirma["anahtar"]:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(0, 7, ">> " + temizle(nokta.strip()))
        pdf.ln(1)

    # Pratik
    pdf.ln(4)
    pdf.set_fill_color(245, 245, 245)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 9, "BU HAFTA UYGULA", new_x="LMARGIN", new_y="NEXT", fill=True)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(0, 7, ar_pratik.strip(), fill=True)

    # Kaynaklar
    pdf.ln(4)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 9, "KAYNAKLAR", new_x="LMARGIN", new_y="NEXT")
    pdf.line(20, pdf.get_y(), 100, pdf.get_y())
    pdf.ln(3)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    for kaynak in arastirma["kaynaklar"]:
        pdf.set_x(pdf.l_margin)
        txt = temizle(f"* {kaynak}")
        pdf.multi_cell(0, 6, txt)
        pdf.ln(1)

    # Footer
    pdf.set_y(-20)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 8, f"Life OS 3.0  |  {date.today().strftime('%d.%m.%Y')}  |  Can Korkutan", align="C")

    return pdf.output()

def send_research(kategori_adi, ikon, alt_baslik, banka):
    indeks = hafta_indeksi() % len(banka)
    a = banka[indeks]

    anahtar_str = "\n".join(f"  >> {n}" for n in a["anahtar"])
    kaynak_str  = "\n".join(f"  [{i+1}] {k}" for i, k in enumerate(a["kaynaklar"]))

    body = f"""{ikon} LIFE OS - {kategori_adi.upper()} ARASTIRMASI
{alt_baslik}
{'='*60}

{a['baslik'].upper()}
{a['alt']}

{'='*60}
OZET
{'='*60}
{a['ozet'].strip()}

{'='*60}
ANAHTAR NOKTALAR
{'='*60}
{anahtar_str}

{'='*60}
BU HAFTA UYGULA
{'='*60}
{a['pratik'].strip()}

{'='*60}
KAYNAKLAR
{'='*60}
{kaynak_str}

{'='*60}
Life OS 3.0 | {date.today().strftime('%d.%m.%Y')} | Can Korkutan
"""

    msg = MIMEMultipart()
    msg['From']    = GMAIL_USER
    msg['To']      = TO
    msg['Subject'] = f"{ikon} {kategori_adi} Arastirmasi: {a['baslik']}"
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    with smtplib.SMTP('smtp.gmail.com', 587, timeout=30) as s:
        s.starttls()
        s.login(GMAIL_USER, GMAIL_PASS)
        s.send_message(msg)

    print(f"✅ {kategori_adi} arastirmasi gonderildi: {a['baslik']}")

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
