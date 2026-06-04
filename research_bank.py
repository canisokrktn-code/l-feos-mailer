# ============================================================
# ARAŞTIRMA BANKASI — Life OS Haftalık Gelişim Sistemi
# Pazartesi: Mesleki | Çarşamba: MindTech | Cuma: Sağlık
# ============================================================

MESLEKI = [
    {
        "baslik": "DSA Görüntülemede Görüntü Kalitesi Optimizasyonu",
        "alt": "Digital Substraction Angiography — Temel Parametreler",
        "ozet": """Dijital substraksiyon anjiyografide (DSA) görüntü kalitesi, tanı doğruluğunu doğrudan etkiler.
Görüntü kalitesini belirleyen üç temel parametre vardır: kontrast çözünürlüğü, mekansal çözünürlük ve
sinyal-gürültü oranı (SNR). Bu üç faktörün dengesi, hem tanısal yeterliliği hem de hasta radyasyon
dozunu etkiler.

Kontrast enjeksiyonu sırasında iyot konsantrasyonu (genellikle 300-370 mgI/mL), akış hızı ve enjeksiyon
hacmi görüntü kontrastını belirler. Çok düşük konsantrasyon damar dolumunu yetersiz gösterirken, çok yüksek
doz gereksiz radyasyon ve böbrek yükü yaratır. Klinik pratik: serebral anjiyografide tipik doz 5-7 mL/sn,
total 8-12 mL.

Frame rate seçimi kritiktir. İnme merkezinde akut stroke değerlendirmesinde yüksek frame rate (6-8 fps)
kollateral dolaşımı ve trombus geçiş zamanını doğru gösterir. Rutin periferik çalışmalarda 3-4 fps yeterli
olup dozı azaltır.

Maskeleme kalitesi DSA'nın temel gücüdür. Hasta hareketi maskeyi bozar; modern sistemlerde piksel shifting
ve motion correction algoritmaları bu sorunu büyük ölçüde gidermektedir. Nefes tutma protokollerinin hasta
ile önceden çalışılması görüntü kalitesini %30-40 artırır.""",
        "anahtar": [
            "SNR artırmak için kV'yi optimize et (DSA'da genellikle 70-80 kV)",
            "Matrix boyutu ve görüntü alanı (FOV) çözünürlüğü etkiler — küçük FOV = yüksek çözünürlük",
            "Kontrast gecikmesi (delay) damar dolumunu etkiler, hasta yaşı ve kardiyak output'a göre ayarla",
            "Road mapping fonksiyonu kateter navigasyonunu kolaylaştırır, doz azaltır",
            "Son görüntü tutma (Last Image Hold) fluoroskopi dozunu azaltır — aktif kullan",
        ],
        "pratik": "Bir sonraki işlemde: kontrast protokolünü önceden belirle, nefes tutma talimatını ver, LIH özelliğini aktif kullan.",
        "kaynaklar": [
            "Stacker R. et al. — Optimization of Digital Subtraction Angiography (Eur Radiol 2021)",
            "ACR-SIR Practice Parameter for DSA — acr.org/guidelines",
            "Balter S. — Methods for measuring fluoroscopic skin dose (Pediatr Radiol 2006)",
        ]
    },
    {
        "baslik": "Akut İskemik İnmede Görüntüleme Algoritması",
        "alt": "Trombektomi Kararında Radyoloji Teknisyeninin Rolü",
        "ozet": """Akut iskemik inmede 'zaman beyin demektir' — her geçen dakika 1.9 milyon nöron ölmektedir.
İnme merkezinde radyoloji teknisyeni bu zincirin kritik bir halkasıdır. Görüntüleme protokolünün
doğru ve hızlı uygulanması trombektomi kararını doğrudan etkiler.

Akut dönem görüntüleme üç aşamadan oluşur: 1) Non-kontrastlı BT (NCCT) — kanama dışlamak için,
2) BT Anjiyografi (CTA) — tıkalı damarı görmek için, 3) BT Perfüzyon (CTP) — kurtarılabilir dokuyu
(penumbra) belirlemek için.

NCCT'de erken iskemi bulguları: hipodens lezyon, insular ribbon işareti, bazal ganglion
hipodensite, hiperdans MCA işareti (taze trombüs). Bu bulguları tanımak, teknisyenin
radyologa doğru bilgi aktarımı açısından değerlidir.

CTP post-processing kritiktir. CBF (serebral kan akımı), CBV (serebral kan volümü), MTT ve Tmax
haritaları otomatik yazılımlarla (RapidAI, MIStar) üretilir. Teknisyen artefaktları tanımalı:
hareket artefaktı, metal artefaktı, yetersiz kontrast bolus zamanlaması.

Trombektomi sonrası kontrol anjiyografide TICI skoru belirlenir (0-2b başarısız, 2b-3 başarılı
rekanalizasyon). Bu görüntüleri kaliteli almak prosedürün belgelenmesi açısından zorunludur.""",
        "anahtar": [
            "Door-to-imaging süresi <20 dakika hedefi — hazırlık protokolünü önceden yap",
            "CTA için kontrast timing kritik: test bolus veya bolus tracking kullan",
            "CTP'de hasta kooperasyonu şart — sıralamayı hızlı ve açık anlat",
            "ASPECTS skoru NCCT'de erken iskemi alanını 10 bölgede puanlar — öğren",
            "Endovasküler girişim odasına geçişte cihaz ve steril alan hazırlığı için standart liste yap",
        ],
        "pratik": "İnme protokolünü ezberle: NCCT → CTA → CTP sırası, her biri için prep süresi ve kritik kontrol noktaları.",
        "kaynaklar": [
            "Powers WJ et al. — 2019 AHA/ASA Guidelines for Acute Ischemic Stroke (Stroke 2019)",
            "Wintermark M. et al. — CT perfusion in acute stroke — European consensus (Eur Radiol 2020)",
            "Hacke W. et al. — ECASS III trial — tPA time window (NEJM 2008)",
        ]
    },
    {
        "baslik": "Radyasyon Güvenliği: Anjiyografi Laboraturvarında Korunma",
        "alt": "ALARA Prensibi ve Pratik Dozimetri",
        "ozet": """Anjiyografi laboratuvarında çalışan personel, Türkiye'deki mesleki radyasyon limitleri
kapsamındadır (yıllık efektif doz limiti: 20 mSv/yıl ortalama, 5 yıl için). Gerçek tehlike
çoğunlukla saçılan radyasyondan kaynaklanır.

Saçılan radyasyonun %95'i hastadan kaynaklanır ve ters kare yasasına göre mesafeyle azalır:
mesafeyi 2 katına çıkarmak dozu 4'e böler. Operatörden 1 metre mesafe, girişimci radyologun
aldığı dozun yaklaşık 1/10'una karşılık gelir.

Koruyucu ekipman: kurşun önlük (0.25-0.5 mm Pb eşdeğeri), tiroid koruyucu, kurşun gözlük
(en sık ihmal edilen), tavan askılı kurşun cam. Göz lensinin katarakt eşiği revize edildi
(500 mGy → 0.5 Gy); gözlük kullanımı artık zorunluluk.

Floroskopi optimizasyonu: pulse fluoroskopi (7.5 fps > 15 fps dozu yaklaşık yarıya indirir),
düşük doz mod, kollimasyon (ışın alanını küçültmek hem dozu hem saçılmayı azaltır), hasta
masa yüksekliği ayarı (dedektörü hastaya yaklaştır, tüpü uzaklaştır).

Dozimetre takibi: film/TLD/OSL dozimetreler kurşun önlüğün dışında takılır (vücut dozunu temsil
eder), ikinci dozimetre önlüğün içinde takılıyorsa efektif doz hesabı yapılabilir.""",
        "anahtar": [
            "En etkili koruma: mesafe ve süre — floroskopi süresini aktif takip et",
            "Kollimasyonu küçük tut: görüntü alanı küçülünce hem doz hem saçılma azalır",
            "Hasta gantri açısı: lateral ve LAO pozisyonlarında operatör dozu artar — farkında ol",
            "Dozimetren yerde veya masada bırakma — takılı olmayan dozimetre anlamsız",
            "Yıllık doz değerlendirmeni talep et, kayıt altında tut",
        ],
        "pratik": "Kurşun gözlüğünü her prosedürde kullan. Tavan camı yoksa maksimum mesafede dur. Pulse fluoroskopiyi aktif et.",
        "kaynaklar": [
            "ICRP Publication 135 — Occupational Intakes of Radionuclides (2020)",
            "Castellano IA et al. — Radiation protection in interventional cardiology (Heart 2020)",
            "Türkiye Atom Enerjisi Kurumu — Radyasyon Güvenliği Yönetmeliği (TAEK 2022)",
        ]
    },
    {
        "baslik": "Serebral Vasküler Anatomi: Anjiyografi Perspektifinden",
        "alt": "Willis Poligonu ve Kollateral Dolaşım",
        "ozet": """Serebral vasküler anatomiyi DSA görüntülerinde tanımak, inme merkezinde çalışan
teknisyen için temel bir yetkinliktir. Willis poligonu (Circulus arteriosus cerebri), anterior
ve posterior dolaşımı birbirine bağlayan anastomotik halkadır.

Anterior dolaşım: İnternal karotid arter (ICA) → Orta serebral arter (MCA, M1-M2-M3 segmentleri) +
Ön serebral arter (ACA). MCA M1 tıkanıklığı büyük damar tıkanıklığı (LVO) olup trombektomi endikasyonudur.

Posterior dolaşım: Vertebral arterler → Baziler arter → Posterior serebral arterler (PCA).
Baziler arter tıkanıklığı yüksek mortaliteli olup agresif müdahale gerektirir.

Kollateral dolaşım trombektomi prognozu için kritiktir: iyi kollaterlerde penumbra korunur,
işlem gecikmesine daha fazla tolerans vardır. DSA'da kollaterlerin derecesi görsel olarak
değerlendirilir (kötü-orta-iyi-mükemmel skalası).

İnme merkezinde sık karşılaşılan anatomik varyantlar: fetal tip PCA (ICA'dan köken alır,
CTA'da konfüzyon yaratır), aplastik A1 segmenti, yüksek bifürkasyon. Bu varyantları
tanımak yanlış anlaşılmaları önler.""",
        "anahtar": [
            "MCA M1 tıkanıklığı = LVO = trombektomi çağrısı — hızlı tanıma kritik",
            "DSA'da AP ve lateral projeksiyon birlikte değerlendirilmeli — tek projeksiyon yanıltıcı olabilir",
            "ICA sifon bölgesi ateroskleroz ve diseksiyon için sık bölge — dikkatli bak",
            "Dural sinüsler venöz tıkanıklık için kontrol et: superior sagittal, transvers, sigmoid sinüs",
            "Anatomik çeşitlilik: her hasta aynı değil — standart protokol + dikkatli değerlendirme",
        ],
        "pratik": "Bir sonraki DSA işleminde: her damar segmentini zihinsel etiketle. ICA → MCA → ACA zincirini takip et.",
        "kaynaklar": [
            "Osborn AG — Diagnostic Cerebral Angiography (Lippincott Williams, 2nd ed.)",
            "Berenstein A. et al. — Surgical Neuroangiography (Springer 2004)",
            "Netter FH — Atlas of Human Anatomy, Plate 134-140",
        ]
    },
    {
        "baslik": "Kontrast Madde Kullanımı: Güvenlik ve Protokol",
        "alt": "Nefrotoksisite, Alerji Yönetimi ve Hidrasyon",
        "ozet": """İyotlu kontrast madde (KM) kullanımı anjiyografinin ayrılmaz parçasıdır. Ancak
kontrast ilişkili akut böbrek hasarı (CI-AKI) ve alerjik reaksiyonlar ciddi komplikasyonlar
arasındadır. Teknisyen olarak risk faktörlerini tanımak ve protokollere hakim olmak
hasta güvenliğini artırır.

CI-AKI risk faktörleri: kronik böbrek yetmezliği (eGFR <30 yüksek risk), diyabet, dehidratasyon,
konjestif kalp yetmezliği, nefrotoksik ilaçlar (NSAİ, aminoglikozid). Önlem: hidrasyon (işlem
öncesi 6-12 saat IV %0.9 NaCl), kontrast dozunu minimize et, iso-osmolar KM tercih et.

Kontrast reaksiyonları: hafif (ürtiker, bulantı — antihistaminik), orta (bronkospazm,
hipotansiyon — kortikosteroid + epi hazır), ağır (anafilaksi — epinefrin 0.3 mg IM,
arrest ekipmanı). Premedikasyon protokolü: önceki reaksiyon varsa prednizon 40 mg × 3
(13 saat, 7 saat, 1 saat önce) + difenhidramin 50 mg 1 saat önce.

Kontrast ısıtması: 37°C'ye ısıtılmış KM viskoziteyi düşürür, enjeksiyon kolaylaşır,
hasta konforu artar. Modern sistemlerde ısıtıcı ünite standarttır.""",
        "anahtar": [
            "Her hastada eGFR değerini kontrol et — böbrek fonksiyonunu bil",
            "Metformin: KM sonrası 48 saat kesilmesi gerekir (laktik asidoz riski)",
            "Kontrast reaksiyon seti hazır mı? Epinefrin, antihistaminik, kortikosteroid — her işlem öncesi kontrol",
            "İzoozmolar KM (iodixanol 320) yüksek riskli hastalarda tercih edilmeli",
            "Kontrast miktarını minimize et: gerekenden fazla verme, körükleme",
        ],
        "pratik": "Bir sonraki işlem öncesi: hastanın eGFR değerini, alerji hikayesini ve mevcut ilaçlarını teyit et.",
        "kaynaklar": [
            "ACR Manual on Contrast Media v10.3 — acr.org (güncel versiyon)",
            "Mehran R. et al. — Contrast-associated acute kidney injury (Nat Rev Cardiol 2019)",
            "European Society of Urogenital Radiology — ESUR Guidelines on Contrast Agents",
        ]
    },
    {
        "baslik": "Endovasküler Trombektomi: Prosedür Akışı",
        "alt": "Teknisyen Perspektifinden Cihaz ve Süreç Yönetimi",
        "ozet": """Mekanik trombektomi (MT) akut iskemik inmede altın standart tedavi haline gelmiştir.
Teknisyenin bu prosedürdeki rolü kritiktir: hem görüntüleme kalitesi hem de alet-cihaz
yönetimi hasta sonucunu doğrudan etkiler.

Prosedür akışı: 1) Femoral veya radyal erişim, 2) Aortik arkın DSA ile görüntülenmesi,
3) Hedef karotid/vertebral arterin selektif kateterizasyonu, 4) Mikrokaterter ile tıkanan
damarın geçilmesi, 5) Stent retriever veya aspirasyon kateteri ile trombüs çıkarımı,
6) Kontrol DSA — TICI skoru değerlendirmesi.

Stent retriever sistemleri (Solitaire, Trevo): nitinol kafes yapısı trombüsü yakalar,
5 dakika bekletilip çekilir. Aspirasyon sistemleri (ADAPT tekniği): büyük çaplı kateterle
direkt aspirasyon. İkisinin kombinasyonu (SOLUMBRA) dirençli vakalarda kullanılır.

Teknisyenin dikkat etmesi gerekenler: microcatheter ve microwire eşleşmesi (uyumsuz
kombinasyonlar kıvrılmaya yol açar), kontrast enjeksiyonunun yavaş yapılması (vazospazm
riski), steril alan koruması (uzun prosedürler), saatlik dozimetri takibi.""",
        "anahtar": [
            "TICI 2b-3 başarılı rekanalizasyon olarak kabul edilir — kontrol DSA'yı kaliteli al",
            "Prosedür setini standartlaştır: her sabah kontrol listesi hazırla",
            "Vazospazm görürsen: ısınmış %0.9 NaCl veya nimodipin intraarterial verilebilir",
            "Kontrast volüm takibi: uzun prosedürlerde toplam doz böbrek limitini aşabilir",
            "Prosedür süresi kayıt altında olmalı — her 15 dakikada bir not al",
        ],
        "pratik": "Trombektomi setini oluşturan her cihazı (wire, catheter, stent retriever) tanı ve uyumluluk tablosunu çıkar.",
        "kaynaklar": [
            "Goyal M. et al. — ESCAPE Trial (NEJM 2015) — trombektomi kanıtı",
            "Jovin TG et al. — DAWN Trial (NEJM 2018) — genişletilmiş pencere",
            "Brinjikji W. et al. — Mechanical thrombectomy for stroke — systematic review (AJNR 2017)",
        ]
    },
    {
        "baslik": "Floroskopi Optimizasyonu: Az Işın, Çok Bilgi",
        "alt": "Teknik Parametreler ve Klinik Pratik",
        "ozet": """Floroskopi anjiyografinin gerçek zamanlı gözlem aracıdır. Doz kontrolsüz floroskopi
hem hasta hem personel için en büyük radyasyon kaynağıdır. Teknik optimizasyon ile
görüntü kalitesinden ödün vermeden doz %50-70 azaltılabilir.

Pulse floroskopi: sürekli floroskopi yerine kısa ışın atımları kullanır.
15 fps → 7.5 fps geçiş %50 doz azaltımı sağlar; çoğu vasküler prosedür için
7.5 fps yeterlidir. Statik görüntüleme gerektiren momenlerde floroskopi yerine
spot röntgen kullan.

Geometrinin önemi: x-ışın tüpünü hastadan uzaklaştır, dedektörü yaklaştır.
Masayı yükselterek hasta-dedektör mesafesini azalt. Bu değişiklik tek başına
hasta giriş dozunu %40 azaltabilir.

Kollimasyon: ışın alanını ilgi bölgesiyle sınırla. Daha dar kolimasyon =
daha az saçılan radyasyon = hem hasta hem personel için düşük doz,
hem de kontrast artışı. Sanal kollimasyon (pixel mask) kullanılabilir.

Floroskopi süresi takibi: modern sistemlerde ekranda görünen süreyi aktif takip et.
5 dakikayı geçen prosedürlerde seçici spot çekim stratejisine geç.""",
        "anahtar": [
            "7.5 fps pulse floroskopi ile başla — gerçekten ihtiyacın olduğunda yükselt",
            "Hasta masası pozisyonunu optimize et: tüp uzakta, dedektör yakın",
            "Kollimasyon reflek olmalı — her yeni pozisyonda otomatik küçült",
            "Floroskopi süresini yüksek sesle takip et: '3. dakika...' gibi hatırlatma yap",
            "Floroskopi sırasında kauçuk ped giyme alışkanlığını edin",
        ],
        "pratik": "Bir sonraki prosedürde: sadece 7.5 fps ile başla ve bak, ne kadar fark var? Süreyi kayıt tut.",
        "kaynaklar": [
            "Stecker MS et al. — Guidelines for Patient Radiation Management (JVIR 2009)",
            "ICRP Publication 117 — Radiological protection in fluoroscopically guided procedures (2010)",
            "Wagner LK et al. — Radiation management for interventional radiologists (RadioGraphics 2020)",
        ]
    },
    {
        "baslik": "Yapay Zeka ve Radyoloji: Geleceğin Teknolojileri",
        "alt": "İnme Görüntülemesinde AI Uygulamaları",
        "ozet": """Yapay zeka (YZ) radyoloji pratiğinde hızla yer bulmaktadır. İnme görüntülemesinde
RapidAI, Viz.ai, Brainomix gibi platformlar klinik kullanıma girmiştir. Radyoloji
teknisyeni olarak bu teknolojileri anlamak ve doğru kullanmak rekabet avantajı sağlar.

YZ'nin inme görüntülemesindeki uygulamaları: 1) Otomatik LVO tespiti (CTA'dan),
2) BT perfüzyon haritaları otomatik analizi (infarkt çekirdeği vs penumbra),
3) ASPECTS skoru otomatik hesaplama, 4) Kanama tespiti ve hacim ölçümü.

Bu sistemlerin çalışma prensibi: evrişimli sinir ağları (CNN) binlerce görüntü ile
eğitilir, yeni görüntülerde pattern tanıma yapar. Doğruluk oranları %85-95 arasında
değişir; ancak hatalara karşı dikkatli olmak gerekir (yanlış pozitif/negatif).

Teknisyenin rolü değişiyor: ham veri kalitesi YZ performansını doğrudan etkiler.
Hareket artefaktlı, yetersiz kontrastlı görüntüler YZ'yi yanıltır. Kaliteli
görüntüleme protokolü YZ'yi en iyi çalıştıran temeldir.

Gelecek: MR görüntülemede difüzyon otomatik analizi, tam otonom kateter navigasyonu
(robotik anjiyografi sistemleri), gerçek zamanlı doz optimizasyonu.""",
        "anahtar": [
            "RapidAI / Viz.ai çalışma prensibini anla: giriş kalitesi çıkış kalitesini belirler",
            "YZ bir araçtır, karar verici değil — klinik bağlamı her zaman değerlendir",
            "Hatalı YZ sonuçlarını raporla: sistem geri bildirimi ile gelişir",
            "Dijital sağlık okuryazarlığı: DICOM, HL7, FHIR standartlarına aşina ol",
            "Yapay zeka sertifika programlarına bak: Coursera, edX ücretsiz seçenekler sunar",
        ],
        "pratik": "Çalıştığın merkezde hangi YZ sistemleri var? Bir tanesini seç ve nasıl çalıştığını detaylı öğren.",
        "kaynaklar": [
            "Rajpurkar P. et al. — AI in health and medicine (Nature Medicine 2022)",
            "Kuo W. et al. — Expert-level detection of acute intracranial hemorrhage — AI (PNAS 2019)",
            "Viz.ai — Clinical evidence summary — viz.ai/clinical-evidence",
        ]
    },
]

MINDTECH = [
    {
        "baslik": "JITAI: Doğru Zamanda Doğru Müdahale",
        "alt": "Just-In-Time Adaptive Intervention — Bilimsel Temel",
        "ozet": """MindTech'in kalbinde yatan kavram JITAI — Just-In-Time Adaptive Intervention.
Bu yaklaşım mobil sağlık (mHealth) literatüründe 2014'ten bu yana güçlü bir araştırma
alanı haline gelmiştir.

JITAI'nin temel soruları: 1) Kişi şu an müdahaleye ihtiyaç duyuyor mu (vulnerability)?
2) Müdahaleyi şu an kabul edebilir durumda mı (receptivity)? 3) Hangi müdahale en etkili?
Bu üç sorunun kesişimi optimal müdahale zamanını belirler.

Klasik örnekler: SARA alkol bağımlılığı sistemi (stres ve konum bazlı müdahale),
HeartSteps fiziksel aktivite sistemi (adım sayısı ve uyku bazlı),
Sense2Stop sigara bırakma (fizyolojik stres sinyali bazlı).

MindTech farklılaşması: çoğu JITAI tek bir davranışa (alkol, sigara, egzersiz)
odaklanır. MindTech çoklu duygu durumu ve çoklu bağlam ile çalışır. Bu, sensör
füzyon kalitesini ve karar motoru karmaşıklığını artırır.

Teknik zorluklar: gerçek zamanlı sensör işleme batarya tüketir,
privacy-first yaklaşım server-side işlemeyi kısıtlar, kişiselleşme
cold start problemini getirir (yeni kullanıcıda yeterli veri yok).""",
        "anahtar": [
            "JITAI = doğru şey + doğru zaman + doğru kişi — üçü birden olmazsa etki azalır",
            "Receptivity ölçümü kritik: yanlış zamanda doğru müdahale işe yaramaz",
            "MindTech'te JITAI kararı için minimum: gün tipi, saat, son kullanıcı etkileşimi",
            "Cooldown mekanizması şart: aynı müdahale çok sık → kullanıcı körleşir",
            "A/B testing altyapısı kur: hangi müdahale hangi bağlamda daha etkili?",
        ],
        "pratik": "JITAI decision engine'ini gözden geçir: hangi bağlam → hangi müdahale? Boşluk var mı? 3 senaryo yazıp test et.",
        "kaynaklar": [
            "Nahum-Shani I. et al. — Just-in-Time Adaptive Interventions (JITAI) — SAGE 2018",
            "Tewari A. et al. — Smartphone Sensor Data for JITAI (NIPS 2017)",
            "Liao P. et al. — Personalized HeartSteps (JAMIA 2020)",
        ]
    },
    {
        "baslik": "Sensör Füzyon: Telefon Verisiyle Duygu Tahmini",
        "alt": "IMU, Akustik ve Etkileşim Sinyalleri",
        "ozet": """MindTech'in farklılaşması sensörler üzerine kuruludur. Telefon, takılmaya gerek
kalmadan kullanıcı hakkında şaşırtıcı miktarda bilgi üretir. Bu veriyi anlamlı
psikolojik sinyallere dönüştürmek sensör füzyonunun temelidir.

İvmeölçer (accelerometer): adım sayısı, aktivite seviyesi (durma/yürüme/koşma),
telefon tutma şekli, titreme (stres marker). Jiroskop ile birlikte daha zengin
hareket analizi mümkün.

Akustik sinyal (ambient): arka plan ses seviyesi kalabalık/sessiz ortamı gösterir.
Ses frekans analizi sosyal ortam ipuçları verir. Not: gizlilik için ham ses değil,
sadece özellikler (features) işlenmeli.

Ekran etkileşimi: scroll hızı, dokunma sıklığı, oturum süresi, sabah-gece kullanım
paterni dikkat ve stres ile korelasyon gösterir (Harari et al., 2020).

Konum bağlamı: ev/iş/trafik/doğa sınıflandırması GPS + WiFi ile.
Hareket miktarı circadian rhythm ve depresyon için marker.

Füzyon stratejisi: erken füzyon (ham sinyal birleştirme) vs geç füzyon
(her sinyalden ayrı özellik çıkar, sonra birleştir). MindTech için geç füzyon
daha esnek ve yorumlanabilir.""",
        "anahtar": [
            "Sensör verisi = davranış proxy'si, doğrudan ölçüm değil — yorumda temkinli ol",
            "Batarya optimizasyonu: sürekli sensör yerine event-driven sampling",
            "Privacy-by-design: ham sensör verisi cihazda kalmalı, sadece feature'lar işlenmeli",
            "Kalibrasyon önemli: her kullanıcı için bireysel baseline gerekir",
            "Eksik veri yönetimi: kullanıcı telefonu bıraktığında ne olacak?",
        ],
        "pratik": "sensor_fusion_service.dart'ı aç: hangi sensörler aktif? Hangisi en çok batarya tüketiyor? Bir profiling yap.",
        "kaynaklar": [
            "Harari GM et al. — Smartphone Sensing of Mental Health (Current Opinion Psychology 2020)",
            "Xu X. et al. — Leveraging Smartphone Sensors for Health (NPJ Digital Medicine 2021)",
            "Lane ND et al. — A Survey of Mobile Phone Sensing (IEEE Communications 2010)",
        ]
    },
    {
        "baslik": "Flutter Performans Optimizasyonu",
        "alt": "Mobil Uygulamada Pil Tüketimi ve Bellek Yönetimi",
        "ozet": """MindTech sensör-yoğun bir uygulamadır. Sürekli arka plan işleme, sensör
sorgulama ve bildirim yönetimi batarya ve bellek açısından zorlayıcıdır.
Erken optimizasyon kullanıcı bırakma oranını doğrudan etkiler.

Flutter performans araçları: DevTools profiler, flutter run --profile modu,
Performance Overlay (checkerboard raster/UI thread). Jank (frame drop) 16ms
hedefini aşan frame'lerden kaynaklanır.

Bellek yönetimi: StreamController ve AnimationController dispose edilmezse
bellek sızıntısı olur. MindTech'teki 300+ ekranın her birinde dispose()
kontrolü kritik. Büyük listeler için ListView.builder kullan.

Sensör optimizasyonu: accelerometer'ı 50Hz yerine 10Hz'de dinle,
gerektiğinde artır. Background isolate kullanarak UI thread'i bloke etme.
WorkManager (Android) / BGTaskScheduler (iOS) arka plan görevleri için.

Ağ optimizasyonu: LLM çağrılarını cache et (aynı bağlamda tekrar sorma),
timeout ekle (8-40 sn), offline fallback hazırla. Gemini API çağrısı
gecikmesi UX'i doğrudan etkiler.""",
        "anahtar": [
            "dispose() her ekranda: StreamController, AnimationController, Timer hepsini kapat",
            "Const constructor kullan: rebuild sayısını azaltır, performans artar",
            "Riverpod autoDispose: provider otomatik temizleme için",
            "flutter analyze --fatal-infos: warning'leri de düzelt, sadece error'ları değil",
            "Profile modda çalıştır: debug mod'da performans ölçümü yanıltıcı",
        ],
        "pratik": "flutter run --profile ile çalıştır, Performance Overlay aç. En çok jank yaşanan 2 ekranı belirle.",
        "kaynaklar": [
            "Flutter Team — Performance best practices — flutter.dev/docs/perf",
            "Filiph B. — Pragmatic State Management in Flutter (Google I/O 2019)",
            "Riverpod docs — autoDispose providers — riverpod.dev",
        ]
    },
    {
        "baslik": "Somatik Müdahale Tasarımı: Haptic + Ses + Işık",
        "alt": "Çok Modaliteli Mikro-Müdahale Sistemi",
        "ozet": """MindTech'in güçlü yönlerinden biri somatik orkestrasyon — tek bir ekran
yerine haptic titreşim, ses ve ışık birlikte kullanılır. Bu çok modaliteli
yaklaşımın nörobilimsel temeli vardır.

Haptic geri bildirim: titreşim ritmik uygulandığında amigdala reaktivitesini
azaltır. Yavaş, düzenli titreşim (0.1 Hz, inhalasyon-ekshalasyon ritmi)
parasempatik aktivasyonu teşvik eder. Güçlü, beklenmedik titreşim ise
sempatik tepkiyi artırır.

Ses tasarımı: 40 Hz binaural beats bilişsel performansı artırabilir (sınırlı
kanıt). 4-7 Hz teta ritmi gevşeme ile ilişkili. Doğa sesleri (yağmur,
deniz dalgası) kortizol düşürücü etkisi göstermiştir.

Işık ritmi: ekran parlaklığını nefes ritmiyle senkronize etmek görsel odak
oluşturur. Mavi ışık filtresi gece kullanımında melatonin üretimini korur.

MindTech implementasyon notu: SomaticOrchestrator tüm kanalları koordine etmeli,
tek kanalın diğerini baskılamaması önemli (ör. çok güçlü haptic + yüksek ses
birlikte rahatsız edici olabilir).""",
        "anahtar": [
            "Haptic + ses + ışık birlikte etki güçlendirir ama birbirini bastırmaz — denge kur",
            "Kullanıcı tercih kayıt et: bazıları haptic'i kapatır, sistem buna adapte olmalı",
            "Trafik bağlamı: visual-OFF kuralı hayatta kalma meselesi — ihlal etme",
            "Ofis bağlamı: stealth mod — TTS sustur, sadece discrete haptic",
            "A/B test: sadece haptic vs haptic+ses — hangisi daha iyi sonuç veriyor?",
        ],
        "pratik": "somatic_orchestrator.dart'ı aç. 3 farklı bağlam için (ev/ofis/trafik) payload'ları karşılaştır. Eksik var mı?",
        "kaynaklar": [
            "Schaffer S. et al. — Heartbeat Feedback for Stress Reduction (CHI 2019)",
            "Kramer J. et al. — Biofeedback-based relaxation — review (Appl Psychophysiol 2020)",
            "Apple HIG — Haptic Feedback Guidelines — developer.apple.com",
        ]
    },
    {
        "baslik": "Mental Sağlık Uygulamaları: Pazar Analizi",
        "alt": "Rakip Analizi ve MindTech'in Farklılaşma Noktaları",
        "ozet": """Dijital mental sağlık pazarı 2023'te 5.6 milyar dolar değerindeydi,
2030'a kadar 17 milyar dolara ulaşması bekleniyor. Ancak pazarın %95'i
meditasyon ve içerik tabanlı uygulamalardan oluşuyor.

Önde gelen uygulamalar: Headspace (20M kullanıcı, içerik odaklı),
Calm (100M indirme, uyku/meditasyon), Woebot (CBT chatbot, klinik onaylı),
Noom (davranışsal değişim, koçluk), Happify (pozitif psikoloji oyunları).

Sensör tabanlı uygulamalar (MindTech'in gerçek rakibi):
Moodpath (duygu log + AI), Youper (AI CBT), Bearable (semptom takibi),
Reflectly (AI günlük). Bunların hiçbiri cihaz sensörlerini aktif kullanmıyor.

MindTech'in gerçek farklılaşması: pasif sensör tabanlı bağlam tespiti +
proaktif mikro-müdahale + somatik orkestrasyon. Bu kombinasyon piyasada yok.

Ticari risk: büyük oyuncuların (Apple, Google) sağlık özelliklerini genişletmesi.
Apple Watch'un stres tespiti ve nefes uyarısı MindTech ile doğrudan rekabet ediyor.""",
        "anahtar": [
            "Diferansiyasyon net olmalı: 'sensör tabanlı proaktif müdahale' — bu mesajı tut",
            "Klinik kanıt olmadan ciddi B2B satışı zor — pilot çalışma planı yap",
            "B2C vs B2B: kurumsal satış (hastane, şirket) daha hızlı gelir",
            "Fiyatlandırma: freemium modeli kullanıcı büyümesi için, premium klinik özellikler",
            "Gizlilik sertifikasyonu (ISO 27001, GDPR uyumu) kurumsal satış için şart",
        ],
        "pratik": "App Store'da 'stress detection app' ara. İlk 10 uygulamayı incele. MindTech'ten ne farklı, ne eksik?",
        "kaynaklar": [
            "Grand View Research — Digital Mental Health Market Report 2023",
            "Torous J. et al. — Smartphones, sensors, and machine learning — JMIR 2020",
            "Lagan S. et al. — Evaluation of mental health smartphone apps — Psychiatr Serv 2021",
        ]
    },
    {
        "baslik": "Kişiselleştirme Algoritmaları: Adaptif Sistemler",
        "alt": "Kullanıcı Modellemesi ve Reinforcement Learning",
        "ozet": """MindTech'in uzun vadeli değeri kişiselleşmeden gelir: sistem zamanla kullanıcıyı
tanır, müdahale etkinliğini öğrenir. Bu teknik olarak çözülmesi gereken önemli bir sorundur.

Kişiselleştirme seviyeleri: 1) Kural tabanlı (basit ama esnek değil),
2) Bayesian güncelleme (önceki müdahale sonuçlarını günceller),
3) Contextual bandit (hangi aksiyon hangi bağlamda en iyi sonucu verir?),
4) Deep RL (karmaşık ama veri açısından açgözlü).

MindTech için pratik öneri: Thompson Sampling ile contextual bandit.
Her müdahale bir "kol" (arm), geri bildirim (kullanıcı tamamladı mı?) ödüldür.
Hesaplama hafif, gerçek zamanlı güncelleme mümkün, yorumlanabilir.

Cold start problemi: yeni kullanıcıda veri yok. Çözüm: 1) populasyon geneli
varsayımları ile başla, 2) hızlı onboarding soru seti ile bağlam topla,
3) benzer kullanıcı profilinden transfer learning.

Gizlilik ile kişiselleştirme çelişkisi: sunucu tarafı ML veri toplamayı
gerektirir. Cihaz üzeri federated learning (Google) alternatif ama karmaşık.""",
        "anahtar": [
            "Kişiselleştirme = veri gerektirir — kullanıcıdan ne toplayacağını önceden planla",
            "A/B test altyapısı kurmadan kişiselleştirme anlamlı değil",
            "Geri bildirim döngüsü: müdahale tamamlandı mı? Kullanıcı nasıl hissetti? — bu ölçüm şart",
            "Açıklanabilirlik: 'neden bu müdahale?' sorusuna cevap verebilen sistem daha güvenilir",
            "Başlangıç için: en basit kural tabanlı sistemi mükemmel çalıştır, sonra adaptasyona geç",
        ],
        "pratik": "detector_trust_service.dart'ı incele. Hangi dedektörler güven puanı alıyor? Adaptasyon mantığı doğru mu?",
        "kaynaklar": [
            "Tewari A. et al. — Reinforcement Learning for Just-In-Time Interventions — 2017",
            "Liao P. et al. — Personalization in Mobile Health — JAMIA 2020",
            "McMahan HB et al. — Communication-Efficient Federated Learning (Google 2017)",
        ]
    },
    {
        "baslik": "Monetizasyon Stratejileri: Dijital Sağlık Startup'ları",
        "alt": "B2C, B2B ve Klinik Kanal Modelleri",
        "ozet": """MindTech için sürdürülebilir gelir modeli belirlemek teknik kadar önemlidir.
Dijital sağlık startup'larının %90'ı monetizasyon problemini çözemeden kapanır.

B2C modeli: doğrudan kullanıcıya satış. Freemium (ücretsiz temel + ücretli premium)
pazar girişi için etkili. Aylık 9.99-29.99 TL/dolar bandı yaygın.
Zorluk: kullanıcı edinimi pahalı, churn yüksek.

B2B modeli: şirketlere kurumsal sağlık çözümü olarak sat. Çalışan sağlığı (employee
wellness) bütçeleri büyüktür. Hastaneler, sigorta şirketleri, büyük kurumlar hedef.
Zorluk: satış döngüsü uzun (6-18 ay), klinik kanıt gerekebilir.

Klinik kanal: klinikler için araç olarak sat (terapist/psikolog destekli).
Reimbursement (sigorta geri ödeme) uzun vadeli büyük pazar.
Zorluk: FDA/CE işaretlemesi gerekebilir, mevzuat karmaşık.

Türkiye pazarı için öneri: B2B → kurumsal sağlık ve bankacılık/finans sektörü
stres yönetimi programları. İlk 50 şirkete pilot → vaka çalışması → büyüme.""",
        "anahtar": [
            "İlk gelir kanalını belirle ve ona odaklan — hepsini aynı anda yapma",
            "Fiyat belirleme: maliyet değil, değer bazlı fiyatlandırma (value-based pricing)",
            "Pilot müşteri: ödeme yapan 1 kurumsal müşteri, 1000 ücretsiz bireysel kullanıcıdan değerlidir",
            "KPI'ları tanımla: MAU, retention, NPS, health outcome — hangisi senin için kritik?",
            "Yatırımcı dili: TAM/SAM/SOM hesapla — pazar büyüklüğünü kanıtla",
        ],
        "pratik": "3 potansiyel kurumsal müşteri belirle (Türkiye'de). Her biri için 'MindTech onlara ne çözer?' sorusunu yaz.",
        "kaynaklar": [
            "Rock Health — Digital Health Funding Report 2023",
            "Sequoia Capital — The Digital Health Investment Landscape 2022",
            "Christensen C. — The Innovator's Prescription (health disruption kitabı)",
        ]
    },
    {
        "baslik": "UX Tasarımı: Mental Sağlık Uygulamalarında Empati",
        "alt": "Duygusal Tasarım ve Mikro-Müdahale Arayüzleri",
        "ozet": """Mental sağlık uygulamalarında UX tasarımı standart uygulamalardan farklıdır.
Kullanıcı zor bir anda uygulamaya gelir; arayüzün kendisi stres yaratmamalıdır.

Duygusal tasarım prensipleri: 1) Hız — zor anda kullanıcı beklemez,
<3 saniye yükleme, 2) Basitlik — maksimum 1 CTA (call to action) per ekran,
3) Güvenlik hissi — renk, tipografi, ses tonu güven verici olmalı,
4) Çıkış kolaylığı — zorla tamamlatma yok, istediğinde bırakabilir.

Onboarding tasarımı: mental sağlık uygulamalarında uzun onboarding churn artırır.
Maksimum 3-4 adım, hızlı değer göster (value proposition ilk 30 saniyede).

Erişilebilirlik: font boyutu, renk kontrastı, screen reader uyumu — ihmal edilemez.
Türkiye'de görme engelliler dahil engelli nüfus 8.5 milyon.

Micro-copy önemi: butondaki "Başla" ile "Şimdi Nefes Al" arasında büyük fark.
Empatik dil + aksiyon odaklı = etkili micro-copy.""",
        "anahtar": [
            "Her ekranı tek bir duygu durumu için tasarla — karmaşık ekran = terk",
            "Dark pattern kullanma: zorla bildirim, zorla premium — kullanıcı güveni kaybı",
            "Test et: 5 kişiyle kullanılabilirlik testi 100 analitik metrikten değerlidir",
            "Renk psikolojisi: mavi/yeşil sakinleştirici, kırmızı uyarı — MindTech tutarlı mı?",
            "Animasyon süresi: 200-400ms ideal — çok hızlı kaba, çok yavaş sabırsızlık",
        ],
        "pratik": "Bir kullanıcıya MindTech'i ver, ekrana bakma sadece sesi duyarken ne yaptığını gözlemle. Hangi adımda duraksadı?",
        "kaynaklar": [
            "Norman D. — The Design of Everyday Things (temel UX kitabı)",
            "Torous J. — User Engagement and Retention in Mental Health Apps — JMIR 2021",
            "Apple HIG — Human Interface Guidelines — developer.apple.com/design",
        ]
    },
]

SAGLIK = [
    {
        "baslik": "Alerjik Astım Yönetimi: Günlük Hayatta Kontrol",
        "alt": "Tetikleyicilerden Kaçınma ve Semptom Takibi",
        "ozet": """Alerjik astım, IgE aracılı bronşiyal inflamasyon sonucu gelişen kronik bir
havayolu hastalığıdır. Türkiye'de yaklaşık 3 milyon kişiyi etkiler.
İyi kontrol altında normal bir yaşam mümkündür — yönetim bilgi ve disipline dayanır.

Senin tetikleyicilerin: ev tozu akarları, küf, nem, hamamböceği,
fındık/fıstık (inhale veya temas), yumurta. Bu tetikleyicilerin kontrolü
ilaç tedavisinden bağımsız olarak kritiktir.

Ev tozu akarı önlemleri: yatak kılıfı (akar geçirmez), yatak nevresimlerini
60°C'de haftalık yıkama, halı yerine ahşap/laminat zemin, perdeleri hafif
kumaştan seç, havalandırma düzenli yap. Nem %50'nin altında tutulursa akar
üremesi durur.

Küf ve nem kontrolü: banyo ve mutfak özellikle kritik bölge.
Banyoda duş sonrası havalandır (en az 15 dk), nem alıcı cihaz kullan.
Çamaşırları kapalı alanda kurutma — iç mekan nemi artırır.

Hamamböceği: mutfakta gıda kaçağı bırakma, çöpleri kapatılı tut,
çatlak ve aralıkları kapat. İlaçlama düzenli yap.

Semptom günlüğü tut: sabah PEF (peak expiratory flow) ölçümü
varsa astım kontrolünü takip eder.""",
        "anahtar": [
            "En etkili önlem: yatak örtüsünü her hafta 60°C'de yıka",
            "HEPA filtreli hava temizleyici: yatak odasında sürekli çalışır durumda olmalı",
            "İlaç tedavisi + tetikleyici kontrolü birlikte — biri olmadan diğeri yetmez",
            "Spor öncesi: ısınma egzersizi egzersiz kaynaklı bronkospazmı azaltır",
            "Astım acil planı: sarı/kırmızı zon için ne yapacağını önceden belirle",
        ],
        "pratik": "Bu hafta: yatak nevresimini 60°C'de yıka. Yatak odası nemini ölç (nem ölçer ucuz) — %50 altında mı?",
        "kaynaklar": [
            "GINA — Global Initiative for Asthma (2023 Report) — ginasthma.org",
            "Bousquet J. et al. — Allergic Rhinitis and its Impact on Asthma — ARIA 2020",
            "Türk Toraks Derneği — Astım Tanı ve Tedavi Rehberi 2022",
        ]
    },
    {
        "baslik": "Fındık ve Yer Fıstığı Alerjisi: Beslenme Güvenliği",
        "alt": "Etiket Okuma, Çapraz Kontaminasyon ve Acil Müdahale",
        "ozet": """Fındık ve yer fıstığı alerjisi en ciddi gıda alerjilerinden biridir;
anafilaksiye yol açabilir. Botanik olarak fındık (tree nut) ve yer fıstığı (legume)
farklı gruplar olsa da çapraz reaktivite yaşanabilir.

Etiket okuma: Türkiye'de gıda etiketleme zorunluluğu kapsamında 14 majör alerjen
listelenmek zorundadır. "Üretim hattında fındık/yer fıstığı ile temas edebilir"
uyarısını gör — risk toleransına göre karar ver.

Gizli kaynaklar: bazah soslar (pesto, Satay sosu), çikolata ve çikolatalı ürünler,
ekmek ve pastane ürünleri, Asya mutfağı, bazı vejeteryan ürünleri.
Dışarıda yemekte mutfağı bilgilendirmek hakların.

Çapraz reaktivite: Ağaç fındıklarına alerjin varsa ceviz, badem, kaju, antep fıstığı
da reaksiyon verebilir. Senin profilin için doktor ile konuşulmalı.

Acil durum planı: epipen (epinefrin otomatik enjektör) alerjik kişilerde yanında
bulunmalıdır. Türkiye'de reçeteli olarak mevcuttur. Anafilaksi belirtileri:
boğazda sıkışma hissi, nefes güçlüğü, yaygın ürtiker, tansiyon düşmesi.""",
        "anahtar": [
            "Epipen varsa her zaman yanında taşı — evde bırakma",
            "Dışarıda yerken 'fındık/yer fıstığı alerjim var' açıkça söyle",
            "Alerjin seviyeni bil: hafif (deri reaksiyonu) mu, ağır (anafilaksi riski) mi?",
            "IgE testi veya provokasyon testi ile alerjin ciddiyeti belirlenir — güncel test yaptır",
            "Antihistaminikler hafif reaksiyonlar için — anafilakside epipen şart, antihistaminik yetmez",
        ],
        "pratik": "Mutfağını gözden geçir: fındık/yer fıstığı içeren ürünleri listele. Alternatifleri belirle (ayçiçeği tohumu, kabak çekirdeği).",
        "kaynaklar": [
            "FARE — Food Allergy Research & Education — foodallergy.org",
            "Muraro A. et al. — EAACI guidelines for food allergy (Allergy 2021)",
            "Türkiye Alerji ve İmmünoloji Derneği — TAİD — taid.org.tr",
        ]
    },
    {
        "baslik": "İç Mekan Hava Kalitesi ve Solunum Sağlığı",
        "alt": "VOC, Partiküller ve Ev Ortamı İyileştirme",
        "ozet": """İç mekan havası dış mekandan 2-5 kat daha fazla kirletici içerebilir.
Günümüzde evde ve işyerinde geçirilen süre %90'ı aşmaktadır. Alerjik astımı
olan biri için iç mekan hava kalitesi kritik sağlık belirleyicisidir.

Başlıca iç mekan kirleticileri: PM2.5 ve PM10 (ince partiküller),
VOC-uçucu organik bileşikler (boya, temizlik ürünleri, yeni mobilya),
formaldehit (sunta, halı), CO2 (yetersiz havalandırma), küf sporları.

HEPA filtreli hava temizleyici: 0.3 mikron ve üzeri partikülleri %99.97 oranında
filtreler. Yatak odası için H13 sınıfı önerilir. Oda hacmine uygun CADR (temiz
hava oranı) değerine dikkat et. Marka önerileri: Levoit, Xiaomi, Philips.

Havalandırma: günde en az 10-15 dakika pencere açmak CO2 ve VOC'u temizler.
Sabah trafiği yoğun sokakta yaşıyorsan düşük trafik saatlerinde havalandır.

Ev bitkileri: spider plant, boston fern, pothos — VOC emiciler olarak
sınırlı da olsa katkı sağlar. Ancak toprak küf kaynağı olabilir —
toprak üzerine ince taş koy.""",
        "anahtar": [
            "HEPA hava temizleyici yatak odasında sürekli çalışmalı — özellikle gece",
            "Uyurken pencere kapalı tut: gece trafiği ve nem artışı olumsuz",
            "Sigara — pasif içicilik astımı tetikler: sigara içilen ortamlardan kaçın",
            "Yeni mobilya/boya sonrası 2 hafta yoğun havalandır — formaldehit bırakma süresi",
            "Koku = kimyasal = potansiyel tetikleyici: kuvvetli parfüm, çamaşır suyu, oda spreyi dikkat",
        ],
        "pratik": "Bu hafta: oda nemi ve sıcaklığını ölç (akıllı termometre veya uygulama). Ideal: 18-22°C, %40-50 nem.",
        "kaynaklar": [
            "WHO — Guidelines for Indoor Air Quality (2010) — who.int",
            "EPA — Indoor Air Quality — epa.gov/indoor-air-quality-iaq",
            "Bernstein JA et al. — The indoor allergen burden — JACI 2018",
        ]
    },
    {
        "baslik": "Alerjik Astım ve Spor: Egzersiz Yönetimi",
        "alt": "Egzersiz Kaynaklı Bronkospazm ve Spor Seçimi",
        "ozet": """Alerjik astım sporu bırakmak için bir neden değildir. Olimpiyat sporcularının
%8-10'u astım tanısı taşımaktadır. Doğru yönetim ile yoğun egzersiz mümkündür.

Egzersiz kaynaklı bronkospazm (EIB): egzersiz sırasında veya sonrası nefes
darlığı, öksürük, hışıltı. Soğuk ve kuru hava EIB'yi tetikler (burun nemi
ısıtma işlevini yapar, ağızdan nefes → soğuk hava bronşlara ulaşır).

Önlem stratejileri: 1) Isınma 10-15 dk yavaş tempolu egzersiz ile başla
(refrakter dönem oluşturur), 2) Soğuk havada ağız-burun maskesi,
3) Kuruluğu azaltmak için nazal nefes, 4) Doktor önermesiyle kısa etkili
bronkodilatör (salbutamol) egzersiz öncesi 15 dk.

Spor seçimi: yüzme en az EIB tetikleyen spordur (ılık nemli hava).
Yoga, pilates, bisiklet iyi alternatifler. Kış sporları ve maraton
yüksek EIB riski taşır.

Senin spor programın (P1/P2/P3 gym) için: kapalı ortam avantajlıdır.
Yoğun set aralarında nefes normalizasyonuna izin ver. Spor salonundaki
koku (temizlik ürünleri, toz) alerjeni olabilir — iyi havalandırılmış salon seç.""",
        "anahtar": [
            "Isınma egzersizi EIB için en iyi koruma — atlamadan yap",
            "Bronkodilatör reçeten varsa spor çantanda bulundur",
            "Gym'de ağır temizlik ürünü kokusu varsa o gün dikkatli ol",
            "Egzersiz sonrası semptom varsa: otur, derin nefes, geçmezse bronkodilatör",
            "Düzenli aerobik egzersiz astım kontrolünü uzun vadede iyileştirir — devam et",
        ],
        "pratik": "Bir sonraki spor seansında: ısınmayı tam 12 dakika yap. EIB belirtisi var mı yok mu not al.",
        "kaynaklar": [
            "Parsons JP et al. — Exercise-induced bronchoconstriction — ACCP Guidelines 2013",
            "Boulet LP et al. — Asthma in athletes (Clin Exp Allergy 2019)",
            "Price OJ et al. — Exercise-induced bronchoconstriction in elite athletes — BJSM 2019",
        ]
    },
    {
        "baslik": "Anti-İnflamatuar Beslenme: Alerji ve Astım İçin",
        "alt": "Omega-3, Probiyotikler ve Bağışıklık Sistemi",
        "ozet": """Beslenme alerjik inflamasyonu hem artırabilir hem azaltabilir.
Araştırmalar anti-inflamatuar diyetin astım kontrolünü iyileştirebileceğini
göstermektedir. Senin durumun için özellikle uygun besinler ve kaçınılacaklar var.

Anti-inflamatuar besinler: omega-3 yağ asitleri (somon, sardalya, uskumru,
keten tohumu, ceviz — fındık/yer fıstığına dikkat), zeytinyağı, zerdeçal,
zencefil, koyu yapraklı sebzeler (ıspanak, roka), meyveler (özellikle üzüm,
elma, çilek — C vitamini).

Probiyotikler ve mikrobiyom: bağırsak mikrobiyomu bağışıklık sistemini düzenler.
Probiyotik gıdalar (yoğurt, kefir, tarhana, turşu) Th1/Th2 dengesini etkileyebilir.
Bazı çalışmalar probiyotik kullanımının çocuklarda alerjik hastalık riskini
azalttığını gösteriyor (yetişkin kanıtı daha sınırlı).

Kaçınılacaklar: işlenmiş gıdalar (trans yağlar inflamasyonu artırır),
yüksek şekerli gıdalar, kızartmalar. Senin için ek dikkat: fındık, yer fıstığı,
yumurta içerebilecek işlenmiş gıdalar.

D vitamini eksikliği astım kontrolünü zorlaştırır. Türkiye'de özellikle
kış aylarında D vitamini eksikliği yaygın — düzeyini kontrol ettir.""",
        "anahtar": [
            "Haftada 2-3 kez yağlı balık (somon, uskumru, sardalya) omega-3 için",
            "D vitamini düzeyini yılda bir kontrol et — eksikse takviye al",
            "Kefir veya yoğurt günlük — probiyotik için, yumurta alerjini kışkırtmadan",
            "Zeytinyağı ile pişir — kızartma yağı yerine",
            "Sebze ve meyveyi renkli tut: farklı renk = farklı antioksidan",
        ],
        "pratik": "Bu hafta: omega-3 içeren 2 öğün planla. Somon/uskumru/sardalya — hangisi ulaşılabilir?",
        "kaynaklar": [
            "Calder PC — Omega-3 fatty acids and inflammatory processes (Nutrients 2020)",
            "Bousquet J. et al. — Diet and asthma (Curr Opin Allergy Immunol 2021)",
            "Martineau AR et al. — Vitamin D and asthma — NEJM meta-analysis 2017",
        ]
    },
    {
        "baslik": "Uyku Kalitesi: Astım ve Alerji Etkisi",
        "alt": "Gece Semptomları ve Uyku Hijyeni",
        "ozet": """Astımın gece semptomları (gece uyanma, öksürük, nefes darlığı) uyku kalitesini
doğrudan etkiler. Uyku bozulması bağışıklık sistemini zayıflatır ve astım
kontrolünü daha da güçleştirir — kısır döngü oluşur.

Gece semptom sebepleri: 1) Yatay pozisyonun balgam drenajını güçleştirmesi,
2) Gece kortizol düşüklüğü (anti-inflamatuar etki azalır), 3) Ev tozu akarının
yatak ve yastıklarda yoğun olması, 4) Soğuk hava (ısıtma kapalıysa).

Uyku hijyeni + astım yönetimi birlikte: yastığı akar geçirmez kılıfla kapla,
yatak odasını serin ama nemli tutma (18-20°C, %40-50 nem), HEPA hava
temizleyiciyi gece açık bırak, uyumadan önce burun dekonjesyonu (serum fizyolojik).

Sirkadiyen ritim ve astım: araştırmalar gece 2-4 arası bronş daralmasının
zirveye ulaştığını gösteriyor. Bu sebeple uzun etkili ilaçlar (LABA) gece alınır.

Uyku kalitesi takibi: akıllı saat veya uygulama ile uyku fazlarını kaydet.
Gece uyanma sıklığı astım kontrolünün kötüleştiğinin erken göstergesidir.""",
        "anahtar": [
            "Yatak odasında HEPA cihazı — gece boyunca çalıştır",
            "Yatay pozisyonda nefes güçlüğü varsa: baş tarafını hafif yükselt",
            "Gece semptomu arttıysa: doktora bildirme zamanı — ilaç revizyonu gerekebilir",
            "Burun tıkanıklığı ağız solunumuna yol açar → havayolu kuruluğu → bronkospazm — burun aç",
            "Kafein öğleden sonra kesme + düzenli uyku saati sirkadiyen ritmi güçlendirir",
        ],
        "pratik": "Bu hafta: uyku kalitesini kaydet (kaç kez uyandın, sabah enerji seviyesi 1-10). MindTech'teki uyku ekranını test et.",
        "kaynaklar": [
            "Sutherland ER — Nocturnal asthma (J Allergy Clin Immunol 2005)",
            "Redline S. — Sleep disordered breathing and asthma (Curr Opinion Pulm 2020)",
            "Walker M. — Why We Sleep (kitap — uyku bilimi için kapsamlı kaynak)",
        ]
    },
    {
        "baslik": "Stres Yönetimi ve Bağışıklık: Psikoneuroimmünoloji",
        "alt": "Kortizol, Stres ve Alerjik İnflamasyon",
        "ozet": """Stres ve alerjik hastalıklar arasındaki bağlantı psikoneuroimmünoloji
alanında kapsamlı çalışılmıştır. Kronik stres alerjik semptomları kötüleştirir —
bu sezgi değil, biyolojik bir gerçektir.

Mekanizma: kronik stres kortizol direncine yol açar. Normalde kortizol
anti-inflamatuar etki gösterir; dirençte bu etki azalır ve inflamasyon artar.
Aynı zamanda stres mast hücrelerini aktive eder → histamin salınımı →
alerji belirtileri.

Stresin astım üzerindeki kanıtı: depresyon ve anksiyete astım exacerbasyonunu
%2-3 oranında artırır. Nöbet stresi, iş baskısı, uyku bozukluğu — hepsi
eşzamanlı semptom artışı ile ilişkili.

MindTech bağlantısı: stres azaltma müdahalelerin (nefes egzersizi,
mindfulness, biofeedback) astım üzerinde klinik faydası gösterilmiştir.
Bu senin uygulamanın mesleki sağlık değeri demek.

Pratik stres azaltma: günlük 10 dk diyafram nefesi (4-7-8 tekniği),
haftada 3 kez aerobik egzersiz, sosyal destek, uyku düzeni.
İlaç değil ama ilaç kadar etkili.""",
        "anahtar": [
            "Stres = inflamasyon = daha kötü alerji. Bu döngüyü kır.",
            "Diyafram nefesi günlük 10 dk — sabah veya yatmadan önce",
            "Nöbet sonrası toparlanma süreci sadece fiziksel değil, bağışıklık süreci",
            "MindTech kullanımını kendinde test et — hangi müdahale sana gerçekten iyi geliyor?",
            "HRV (kalp hızı değişkenliği) stres ve toparlanma için objektif ölçüm",
        ],
        "pratik": "Bu hafta: sabah 5 dk 4-7-8 nefes tekniği uygula. Sabah astım semptomu farkı var mı not al.",
        "kaynaklar": [
            "Kiecolt-Glaser JK et al. — Stress, immunity, and health — PNAS 2010",
            "Chen E. et al. — Psychological stress and asthma — Curr Opin Allergy 2019",
            "Weil A. — 4-7-8 breathing technique — drweil.com",
        ]
    },
    {
        "baslik": "Yumurta Alerjisi: Yönetim ve Beslenme Alternatifleri",
        "alt": "Çapraz Reaktivite ve Pişirme Etkileri",
        "ozet": """Yumurta alerjisi çocukluk çağının en yaygın gıda alerjilerinden biridir,
ancak yetişkinlerde de görülür. Senin "yarım alerji" tarif ettiğin tablo
muhtemelen IgE aracılı hafif reaksiyon veya intolerans olabilir.

Yumurta proteini: alerjen genellikle beyaz kısmındaki ovomucoid, ovalbumin
ve ovotransferrin proteinleridir. Yumurta sarısına alerji daha nadir.
Pişirme yumurta alerjisini etkiler: iyi pişmiş yumurta, çiğ veya az pişmişten
daha az reaktif olabilir (proteinler ısıyla denatüre olur).

Gizli yumurta kaynakları: pasta, kek, kurabiye, ekmek (bazı çeşitler),
mayonez, hollandaise sos, bazı et ürünleri (köfte, sosis), yufka, krep.

Alternatifler: çia tohumu jeli (1 yem çia + 3 yem su, 5 dk bek),
keten tohumu jeli, muz (1/4 muz), elma püresi — pişirmede bağlayıcı olarak.
Yemek yerken: protein ihtiyacı için et, baklagil, süt ürünleri.

Yumurta alerjisi ile grip aşısı: bazı grip aşıları yumurta proteini içerir.
Alerjistin onayı ile uygulama veya yumurta proteini içermeyen aşı tercih et.""",
        "anahtar": [
            "İyi pişmiş yumurta tolere edebiliyorsan (fırın ürünleri, haşlanmış) bunu not et",
            "Etiket okuma: 'yumurta', 'albumin', 'lizofilm', 'mayonez', 'globulin' — hepsi yumurta",
            "Reaksiyon ne olduğunda çıkıyor? Miktarla değişiyor mu? — günlük not tut",
            "Oral immunoterapi (OIT) yumurta alerjisinde etkili olabilir — uzman değerlendirmesi",
            "Yumurtasız protein kaynakları: tavuk, balık, baklagil, süt ürünleri, kuru fasulye",
        ],
        "pratik": "Son 2 haftada yumurta yediğin anları düşün. Reaksiyon var mıydı? Miktarı not et — pattern çıkar.",
        "kaynaklar": [
            "Caubet JC et al. — Egg allergy — JACI 2014",
            "Lemon-Mulé H. et al. — Immunologic changes in children with egg allergy (JACI 2008)",
            "EAACI — Guidelines on egg allergy — eaaci.org",
        ]
    },
]
