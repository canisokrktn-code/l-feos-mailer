#!/usr/bin/env python3
"""
Life OS Mailer — GitHub Actions ile otomatik çalışır.
Haziran 2026 takvimi kodlanmış, Temmuz'da güncellenecek.
"""
import smtplib, sys, os
from datetime import date, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# GitHub Secrets'tan al
GMAIL_USER = os.environ.get('GMAIL_USER', 'canisokrktn@gmail.com')
GMAIL_PASS = os.environ.get('GMAIL_PASS', '')
TO         = 'canisokrktn@gmail.com'

# ─── HAZİRAN TAKVİMİ ───────────────────────────────────────
NOBET        = {7,9,14,16,21,23,25,28}
MESAI        = {11,18,30}
NOBET_SONRASI= {8,10,15,17,22,24,26,29}
BOS          = {12,13,19,20,27}
SPOR         = {10:1,11:2,12:3,15:1,18:2,19:3,22:1,24:2,26:3,27:1,29:2,30:3}
HAFIF        = {10,15,22,24,26,29}

PROG = {
    1: "P1 — Göğüs/Arka Kol\n  • Smith Machine Incline Press: 4×12\n  • Chest Press: 4×10\n  • Pec Deck Fly: 4×12\n  • Cable Pushdown: 4×12\n  • Machine Dips: 3×15",
    2: "P2 — Sırt/Ön Kol\n  • Pulldown: 4×12\n  • Low Row: 4×12\n  • Dumbbell Row: 4×10\n  • Scott Curl: 4×12\n  • Cable Biceps Curl: 4×12",
    3: "P3 — Bacak/Omuz\n  • Machine Shoulder Press: 4×12\n  • Lateral Raise: 4×15\n  • Leg Press: 4×12\n  • Lunge: 3×15\n  • Leg Extensions: 4×12"
}

TR_DAYS = ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]

MEYVE = {
    0:"🍒 Kiraz — C vitamini + antioksidan",
    1:"🍓 Çilek — C vitamini + bağışıklık güçlendirici",
    2:"🍑 Kayısı — A vitamini + potasyum",
    3:"🍑 Şeftali — C+A vitamini",
    4:"🍉 Karpuz — Hidrasyon + A+C vitamini",
    5:"🍈 Kavun — C vitamini + B6",
    6:"🍒 Kiraz — C vitamini"
}

YEMEK = {
    0:("Tavuk çorbası+pilav","Zeytinyağlı sebze"),
    1:("Fırın tavuk+pilav+salata","Mercimek çorbası"),
    2:("Ton balıklı makarna","Izgara tavuk+sebze"),
    3:("Izgara balık+pilav","Domates soslu makarna"),
    4:("Tavuk sote+bulgur","Sebze çorbası+tost"),
    5:("Ton balıklı salata","Fırın tavuk+patates"),
    6:("Zeytinyağlı makarna","Izgara et+salata")
}

GELISIM = [
    "📱 Teknoloji: Flutter Riverpod 3.x — state management araştır (15 dk)",
    "🏥 Tıp/Mesleki: DSA görüntü kalitesi optimizasyonu — PubMed'de 1 makale",
    "📈 Ekonomi: Kahneman — Sistem 1 vs Sistem 2 kavramını gözden geçir",
    "⚽ Futbol: Gegenpressing vs blok savunma — taktik analiz (15 dk)",
    "🧠 Kişisel Gelişim: Atomik Alışkanlıklar — 1 bölüm oku",
    "📱 Teknoloji: MCP protokolü — nasıl çalıştığını incele (15 dk)",
    "🏥 Tıp/Mesleki: Anjiyografi radyasyon koruması protokollerini gözden geçir",
]

MINDTECH = {
    7:"📖 Toolkit 4 bileşeni planla: mt_atmosphere_painter, haptic_choreographer, mt_closing_ritual, mt_llm_hint_card",
    9:"📖 WriteAndBurn, AcuteAmygdala, DomesticChaos, SilentTreatment ekranlarını oku. Değişim listesi çıkar.",
    11:"📖 Ev|Mutsuz 9 ekranı incele. DopamineQuest, CoolingChamber ve diğerleri.",
    12:"🔧 GÜN 1: TOOLKIT — mt_atmosphere_painter + haptic_choreographer + mt_closing_ritual + mt_llm_hint_card",
    13:"💻 GÜN 2 — Ev|Öfkeli 8 ekran: WriteAndBurn, AcuteAmygdala, DomesticChaos, SilentTreatment, PassiveAggressive, PastConflict, RoleConflict, AccumulatedExpectations",
    14:"💻 GÜN 3 START — DopamineQuest + CoolingChamber + DigitalAnalgesic 🎂",
    16:"💻 GÜN 3 DEVAM — VisorMode + ConnectionStation + MeaningBud + RoutineDecay",
    18:"💻 GÜN 3 BİTİR — SelfCompassion + SleepRegulation",
    19:"💻 GÜN 4 TAM GÜN — Ev|Nötr(4)+Mutlu(4)+Zinde(5) = 13 ekran",
    21:"💻 GÜN 5 START — TriggerCooldown + InvisibleLabor + AmbiguousExpectation",
    23:"💻 GÜN 5 DEVAM — VigilanceReset + UnfairReward + EvidenceBoard + PsychologicalSiege + BoundaryLine",
    25:"💻 GÜN 6 START — ImposterStealth + AssetManager + DecisionProtocol + MentalDecompression",
    27:"💻 GÜN 6+7 TAM GÜN — İş|Mutsuz kalan(5) + İş|Nötr+Zinde+Mutlu(14)",
    28:"💻 GÜN 8 START — Trafik visual-OFF: TrafficFlowMode + FluidObstacle + TrafficUncontrolledRisk + TrafficTimeTheft",
    30:"💻 GÜN 8 DEVAM + Haziran sonu review — Temmuz planını hazırla",
}

def day_type(d):
    if d.month == 6:
        day = d.day
        if day in NOBET: return 'nobet'
        if day in MESAI: return 'mesai'
        if day in NOBET_SONRASI: return 'nobetSonrasi'
        if day in BOS: return 'bos'
    return 'bos'

def spor_bilgi(d):
    if d.month != 6: return None, False
    p = SPOR.get(d.day)
    return p, (d.day in HAFIF)

def format_sabah(d):
    tip = day_type(d)
    dow = d.weekday()
    gun = TR_DAYS[dow]
    oglen, aksam = YEMEK[dow]
    meyve = MEYVE[dow]
    gelisim = GELISIM[d.day % len(GELISIM)]
    p, hafif = spor_bilgi(d)
    mt = MINDTECH.get(d.day, "")
    dogum = d.month == 6 and d.day == 14

    spor_str = ""
    if p:
        prog = PROG[p]
        if hafif:
            prog += "\n  ⚡ Hafif gün — ağırlığı %20 düşür, 3 set yap"
        spor_str = f"\n🏋️ SPOR\n{prog}\n"

    if tip == 'nobet':
        konu = f"🔴 Nöbet — {gun} {d.day} Haziran{'  🎂' if dogum else ''}"
        govde = f"""GÜN: NÖBET · 08:00 başlıyor · Dayanıklılık modu
{'🎂 DOĞUM GÜNÜN KUTLU OLSUN, CAN!' if dogum else ''}

💧 SU — 2 Litre
Her 2 saatte 1 bardak: 08 · 10 · 12 · 14 · 16 · 18 · 20 · 22

🍽️ Öğle: {oglen}
🍽️ Akşam: {aksam}
{meyve}
💊 Kreatin: 5g öğünle
{spor_str}
🧠 MindTech (nöbet arası)
{mt if mt else '— Hafif tut, planla, not al.'}

📚 Gelişim (20 dk)
{gelisim}

— Life OS 3.0"""

    elif tip == 'mesai':
        konu = f"🟡 Mesai — {gun} {d.day} Haziran · 09:00–16:00"
        govde = f"""GÜN: MESAİ 09:00→16:00 · Akşam serbest

💧 SU — 2 Litre
Sabah evde 2 bardak · Öğlen molası 2 bardak · Akşam 2 bardak

🍽️ Öğle: {oglen}
🍽️ Akşam: {aksam}
{meyve}
💊 Kreatin: 5g öğünle

⚡ 16:00 Sonrası
{spor_str if spor_str else '→ Eve gel. MindTech: 45 dk odaklı çalışma.'}
{mt if mt else ''}
📚 Gelişim (20 dk): {gelisim}

3 Öncelik:
1. {'Spor' if p else 'MindTech'}
2. {'MindTech' if p else 'Gelişim'}
3. Pratik / finans

— Life OS 3.0"""

    elif tip == 'nobetSonrasi':
        konu = f"🟠 Nöbet Sonrası — {gun} {d.day} Haziran"
        govde = f"""GÜN: NÖBET ÇIKIŞI · Önce ye → uyu (4-6 saat)

💧 Eve gelince 500 ml iç. Gün boyunca 2 litre hedef.
🍽️ Hafif: {oglen}
{meyve}
💊 Kreatin: 5g öğünle
{spor_str if spor_str else ''}
📚 Gelişim (10-15 dk hafif): {gelisim}

MindTech: Bugün yok — dinlen.

— Life OS 3.0"""

    else:
        konu = f"{'🎂 Doğum Günün!' if dogum else '🟢 Boş Gün'} — {gun} {d.day} Haziran"
        govde = f"""GÜN: BOŞ · Sistem çalışıyor.
{'🎂 DOĞUM GÜNÜN KUTLU OLSUN, CAN! Kendine iyi bak.' if dogum else ''}

💧 SU — 2 Litre
Uyanınca 2 · Öğle 2 · İkindi 2 · Akşam 2 bardak

🍽️ Öğle: {oglen}
🍽️ Akşam: {aksam}
{meyve}
💊 Kreatin: 5g öğünle
{spor_str}
🧠 MindTech
{mt if mt else '— Odaklı çalışma günü.'}
Min 1 saat · Max 4 saat

📚 Gelişim (30-40 dk)
{gelisim}

3 Öncelik:
1. MindTech
2. {'Spor' if p else 'Gelişim'}
3. Finans / pratik

💰 KK1→5 Haz, KK2→8 Haz ödendi mi?

— Life OS 3.0"""

    return konu, govde

def format_aksam(d):
    yarin = d + timedelta(days=1)
    tip = day_type(yarin)
    dow = yarin.weekday()
    gun = TR_DAYS[dow]
    oglen, aksam = YEMEK[dow]
    meyve = MEYVE[dow]
    p, hafif = spor_bilgi(yarin)
    mt = MINDTECH.get(yarin.day, "")
    dogum = yarin.month == 6 and yarin.day == 14

    spor_str = ""
    if p:
        prog = PROG[p]
        if hafif:
            prog += "\n  ⚡ Hafif gün — ağırlığı %20 düşür"
        spor_str = f"\n🏋️ SPOR\n{prog}\n"

    if tip == 'nobet':
        konu = f"🔴 Yarın Nöbet — {gun} {yarin.day} Haziran"
        govde = f"""YARIN: NÖBET 08:00→ertesi 08:00

GECE HAZIRLIK:
☐ Erken uyu — en geç 23:30
☐ Su matarası hazırla
☐ Kıyafet hazır mı?
☐ Hafif ye, ağır yeme

NÖBET BOYUNCA — SU:
08 · 10 · 12 · 14 · 16 · 18 · 20 · 22 · 00 · 02 · 04 · 06
Her 2 saatte 1 büyük bardak → 3 litre hedef

Nöbet arası: Podcast / makale / MindTech fikir notu

"Nöbet disiplinin en saf halidir."
--- Life OS 3.0"""

    elif tip == 'mesai':
        konu = f"🟡 Yarın Mesai — {gun} {yarin.day} Haziran · 09:00–16:00"
        govde = f"""YARIN: MESAİ 09:00→16:00 · Akşam serbest

SABAH HAZIRLIK:
☐ 08:30 uyan · ☐ Kıyafet+çanta · ☐ Su iç

Öğlen molasında 2 bardak su unutma.

16:00 Sonrası:
{spor_str if spor_str else '→ Eve gel. MindTech: 45 dk odaklı çalışma.'}
{mt if mt else ''}
--- Life OS 3.0"""

    elif tip == 'nobetSonrasi':
        konu = f"🟠 Yarın Nöbet Sonrası — {gun} {yarin.day} Haziran"
        govde = f"""YARIN: NÖBET ÇIKIŞI — DİNLENME
08:00'de nöbetten çıkıyorsun.

→ Eve gel → ye → uyu (4-6 saat hedef)
→ Öğleden sonra: yürüyüş, podcast, hafif okuma

✗ Ağır spor yok  ✗ Büyük karar yok  ✗ Aşırı ekran yok
{spor_str if spor_str else ''}
Su: Eve gelince 500 ml iç.
--- Life OS 3.0"""

    else:
        konu = f"{'🎂 Yarın Doğum Günün!' if dogum else '🟢 Yarın Boş Gün'} — {gun} {yarin.day} Haziran"
        govde = f"""YARIN: BOŞ GÜN — Senindir.
{'🎂 YARIN DOĞUM GÜNÜN! Kendine iyi bak.' if dogum else ''}

{spor_str}
🍽️ Öğle: {oglen} / Akşam: {aksam}
{meyve}
💊 Kreatin: 5g öğünle

💡 MindTech:
{mt if mt else '— Odaklı çalışma günü.'}

Öncelikler:
1. {'Spor' if p else 'MindTech'}
2. {'MindTech' if p else 'Gelişim'}
3. Pratik iş

💰 KK1: 5 Haz · KK2: 8 Haz — ödendi mi?
--- Life OS 3.0"""

    return konu, govde

def send(subject, body):
    msg = MIMEMultipart()
    msg['From']    = GMAIL_USER
    msg['To']      = TO
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    with smtplib.SMTP('smtp.gmail.com', 587, timeout=30) as s:
        s.starttls()
        s.login(GMAIL_USER, GMAIL_PASS)
        s.send_message(msg)
    print(f"✅ Gönderildi: {subject}")

if __name__ == '__main__':
    mode  = sys.argv[1] if len(sys.argv) > 1 else 'sabah'
    today = date.today()
    if mode == 'aksam':
        subj, body = format_aksam(today)
    else:
        subj, body = format_sabah(today)
    send(subj, body)
