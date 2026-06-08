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
TATIL        = {1,2,3,4,5,6}   # Adana/Tufanbeyli — 1-5 tatil, 6 dönüş
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
        if day in TATIL: return 'tatil'
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

    if tip == 'tatil':
        donus = d.day == 6
        konu = f"{'🔙 Dönüş Günü' if donus else '🏖️ Tatil'} — {gun} {d.day} Haziran"
        govde = f"""GÜN: {'DÖNÜŞ — Adana→İstanbul' if donus else 'TATİL — Bozgüney Köyü 🏡'}

{'⚠️ Bugün dönüş ve nöbet var — hazırlıklarını yap.' if donus else 'Dinlen, şarj ol. Sistem seni bekliyor.'}

💧 Bol su iç — yolculukta sıvı kaybedersin
🍽️ Hafif ye, yol yemeği abartma
{meyve}

📱 Telefona bakma zorunluluğun yok — gerçekten izin al.
{'🔴 Gece nöbet başlıyor — erken uyu!' if donus else ''}

Haziran {6 if d.day < 6 else 7}\'de sistem devreye giriyor.

— Life OS 3.0"""
        return konu, govde

    if tip == 'nobet':
        konu = f"🔴 Nöbet — {gun} {d.day} Haziran{'  🎂' if dogum else ''}"
        govde = f"""{'🎂 DOĞUM GÜNÜN KUTLU OLSUN, CAN!' if dogum else ''}
━━━━ NÖBET · 08:00→ertesi 08:00 ━━━━━━━━━━━━━━━━

07:30  🌅  Uyanış + hazırlık
       📍 Ev — 2 bardak su · Kreatin 5g kahvaltıyla

08:00  🏥  NÖBET BAŞLIYOR
       📍 Hastane

12:00  🍽️  Öğle: {oglen}
       📍 Hastane kantini · {meyve}
       💧 2 bardak su

14:00  🧠  MindTech (nöbet arası, kısa)
       📍 Nöbet odası
       {mt if mt else '— Planla, not al, hafif oku.'}

18:00  🍽️  Akşam: {aksam}
       💧 2 bardak su

20:00  📱  Ara oku / podcast (20 dk)
       {gelisim}

00:00  💧  Gece suyu — 1 bardak
02:00  💧  Gece suyu — 1 bardak

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam su hedefi: 3 litre (her 2 saatte 1 bardak)
— Life OS 3.0"""

    elif tip == 'mesai':
        konu = f"🟡 Mesai — {gun} {d.day} Haziran · 09:00–16:00"
        if p:
            spor_blok = f"""16:30  🏋️  SPOR — Mesai çıkışı direkt git
       📍 Spor salonu
       {PROG[p]}"""
            mt_blok = f"""19:30  🧠  MindTech — Odaklı çalışma
       📍 Ev — çalışma masası
       {mt if mt else '— Akşam seansı, 45 dk–1 saat.'}"""
        else:
            spor_blok = f"""16:30  🧠  MindTech — Mesai çıkışı direkt başla
       📍 Ev — çalışma masası
       {mt if mt else '— Akşam odaklı seans, 1–2 saat.'}"""
            mt_blok = ""

        govde = f"""━━━━ MESAİ · 09:00–16:00 ━━━━━━━━━━━━━━━━━━━━━

08:30  🌅  Uyanış + hazırlık
       📍 Ev — 2 bardak su · Kreatin 5g kahvaltıyla

09:00  🏥  MESAİ BAŞLIYOR
       📍 Hastane

12:00  🍽️  Öğle: {oglen}
       📍 Hastane kantini · {meyve}
       💧 2 bardak su

16:00  🏥  Mesai bitiyor

{spor_blok}

{'18:30' if p else '19:00'}  🍽️  Akşam: {aksam}
       💧 2 bardak su

{mt_blok}

22:00  📚  Kişisel Gelişim (30 dk)
       📍 Ev — sessiz ortam / yatak odası
       {gelisim}

23:30  💤  Uyku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
— Life OS 3.0"""

    elif tip == 'nobetSonrasi':
        konu = f"🟠 Nöbet Sonrası — {gun} {d.day} Haziran"
        if p:
            spor_blok = f"""14:30  🏋️  SPOR — Hafif antrenman
       📍 Spor salonu
       {PROG[p]}
       ⚡ Ağırlığı %20 düşür · 3 set yap"""
            aksam_saati = "16:30"
        else:
            spor_blok = f"""14:00  🚶  Yürüyüş veya dinlenme
       📍 Dışarı çık, hava al (30 dk)"""
            aksam_saati = "17:00"

        govde = f"""━━━━ NÖBET ÇIKIŞI · Dinlenme öncelik ━━━━━━━━━━━━

08:00  🏥  Nöbetten çıkış
       📍 Hastane → Eve geç

08:30  🍽️  Hafif öğle: {oglen}
       📍 Ev — {meyve} · Kreatin 5g
       💧 Eve gelince 500 ml iç

09:00  💤  UYKU — 4–5 saat
       📍 Yatak odası

{spor_blok}

{aksam_saati}  🍽️  Akşam: {aksam}
       💧 2 bardak su

21:00  📺  Serbest zaman — hafif içerik

22:00  📚  Kişisel Gelişim (15 dk, hafif)
       📍 Ev — yatmadan önce
       {gelisim}

23:00  💤  Uyku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
— Life OS 3.0"""

    else:
        konu = f"{'🎂 Doğum Günün!' if dogum else '🟢 Boş Gün'} — {gun} {d.day} Haziran"
        if p:
            spor_blok = f"""14:30  🏋️  SPOR — Öğleden sonra git
       📍 Spor salonu
       {PROG[p]}"""
            mt_sure = "10:00–13:30"
            aksam_saati = "16:30"
            mt_blok = f"""17:30  🧠  MindTech — İkinci seans (isteğe bağlı)
       📍 Ev — çalışma masası
       Devam et veya hafif not al."""
        else:
            spor_blok = ""
            mt_sure = "10:00–14:00"
            aksam_saati = "14:30"
            mt_blok = f"""19:30  🧠  MindTech — Akşam seansı (isteğe bağlı)
       📍 Ev — çalışma masası
       Devam et veya hafif not al."""

        govde = f"""{'🎂 DOĞUM GÜNÜN KUTLU OLSUN, CAN!' if dogum else ''}
━━━━ BOŞ GÜN · Tamamen senindir ━━━━━━━━━━━━━━━

08:30  🌅  Uyanış + sabah rutini
       📍 Ev — 2 bardak su · Kreatin 5g kahvaltıyla

{mt_sure}  🧠  MindTech — Ana seans
       📍 Ev — çalışma masası
       {mt if mt else '— Odaklı çalışma. Min 1 saat, max 4 saat.'}

{'13:30' if p else '14:30'}  🍽️  Öğle: {oglen}
       {meyve} · 💧 2 bardak su

{spor_blok}

{aksam_saati}  ☕  Kısa mola / dinlenme

19:00  🍽️  Akşam: {aksam}
       💧 2 bardak su

{mt_blok}

22:00  📚  Kişisel Gelişim (30–40 dk)
       📍 Ev — sessiz ortam / yatak odası
       {gelisim}

23:30  💤  Uyku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 KK ödemeleri kontrolü — yapıldı mı?
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

    if tip == 'tatil':
        donus = yarin.day == 6
        konu = f"{'🔙 Yarın Dönüş' if donus else '🏖️ Yarın Tatil'} — {gun} {yarin.day} Haziran"
        govde = f"""YARIN: {'DÖNÜŞ GÜNÜ — Adana→İstanbul' if donus else 'TATİL — Bozgüney Köyü 🏡'}

{'⚠️ Yarın dönüş var ve gece nöbet başlıyor! Erken yola çık, erken uyu.' if donus else 'Dinlenmeye devam. Telefonu bırak, insanlarla ol.'}

{'🔴 Nöbet hazırlığı: su matarası, kıyafet, hafif ye.' if donus else ''}

--- Life OS 3.0"""
        return konu, govde

    if tip == 'nobet':
        konu = f"🔴 Yarın Nöbet — {gun} {yarin.day} Haziran"
        govde = f"""━━━━ YARIN NÖBET · Şimdi hazırlan ━━━━━━━━━━━━━━

GECE HAZIRLIK (bu gece):
  ☐ En geç 23:30 uyu
  ☐ Su matarası hazırla
  ☐ Kıyafet + çanta hazır mı?
  ☐ Hafif ye, ağır yeme

NÖBET BOYUNCA:
  08:00  🏥  Başlıyor
  12:00  🍽️  Öğle — hafif ye
  14:00  🧠  Ara — not al, oku, MindTech fikir
  18:00  🍽️  Akşam
  Su: 08·10·12·14·16·18·20·22·00·02·04·06
  Her 2 saatte 1 bardak → 3 litre hedef

"Nöbet disiplinin en saf halidir."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--- Life OS 3.0"""

    elif tip == 'mesai':
        konu = f"🟡 Yarın Mesai — {gun} {yarin.day} Haziran · 09:00–16:00"
        if p:
            aksam_plan = f"""  16:30  🏋️  Spor — direkt git
           {PROG[p]}
  19:30  🧠  MindTech — {mt if mt else 'akşam seansı'}
  22:00  📚  Gelişim (30 dk)"""
        else:
            aksam_plan = f"""  16:30  🧠  MindTech — {mt if mt else 'akşam seansı'}
  22:00  📚  Gelişim (30 dk)"""
        govde = f"""━━━━ YARIN MESAİ · 09:00–16:00 ━━━━━━━━━━━━━━━

SABAH HAZIRLIK (bu gece):
  ☐ Kıyafet + çanta hazır mı?
  ☐ 08:30 alarm kur

YARIN PROGRAM:
  08:30  Uyanış + hazırlık
  09:00  🏥  Mesai başlıyor
  12:00  🍽️  Öğlen — 💧 2 bardak su
  16:00  Mesai bitiyor
{aksam_plan}
  23:30  💤  Uyku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--- Life OS 3.0"""

    elif tip == 'nobetSonrasi':
        konu = f"🟠 Yarın Nöbet Sonrası — {gun} {yarin.day} Haziran"
        if p:
            spor_notu = f"""  14:30  🏋️  Spor — hafif antrenman
           {PROG[p]}
           ⚡ %20 düşür, 3 set"""
        else:
            spor_notu = "  14:00  🚶  Yürüyüş / hava al (30 dk)"
        govde = f"""━━━━ YARIN NÖBET ÇIKIŞI · Dinlen ━━━━━━━━━━━━━━

  08:00  🏥  Nöbetten çıkış
  08:30  🍽️  Hafif öğle → Eve gel
  09:00  💤  Uyku — 4–5 saat
{spor_notu}
  17:00  🍽️  Akşam
  22:00  📚  Hafif gelişim (15 dk)
  23:00  💤  Uyku

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
--- Life OS 3.0"""

    else:
        konu = f"{'🎂 Yarın Doğum Günün!' if dogum else '🟢 Yarın Boş Gün'} — {gun} {yarin.day} Haziran"
        if p:
            spor_satir = f"""  14:30  🏋️  Spor — Öğleden sonra git
           {PROG[p]}"""
            mt_satir = f"""  17:30  🧠  MindTech — {mt if mt else 'Odaklı çalışma'}"""
            aksam_saati2 = "16:30"
        else:
            spor_satir = ""
            mt_satir = f"""  10:00  🧠  MindTech — Ana seans
           {mt if mt else 'Odaklı çalışma, min 1 saat'}"""
            aksam_saati2 = "14:30"

        govde = f"""{'🎂 YARIN DOĞUM GÜNÜN! Kendine iyi bak.' if dogum else ''}
━━━━ YARIN BOŞ GÜN · Program ━━━━━━━━━━━━━━━━

  08:30  🌅  Uyanış — 2 bardak su · Kreatin 5g
{mt_satir}
  {'13:30' if p else aksam_saati2}  🍽️  Öğle: {oglen}
           {meyve}
{spor_satir}
  19:00  🍽️  Akşam: {aksam}
  22:00  📚  Kişisel Gelişim (30–40 dk)
  23:30  💤  Uyku

💊 Kreatin 5g öğünle unutma.
💰 Yarın KK ödemesi var mı?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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
