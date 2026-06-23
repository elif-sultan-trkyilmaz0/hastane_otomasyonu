#23100011055
#ELİF SULTAN TÜRKYILMAZ
klinikler = {1: "Aile Hekimliği", 2: "Amatem(Alkol ve Madde Bağımlılığı)", 3: "Anezteziyoloji ve Reanimasyon",4: "Beyin ve Sinir Cerrahisi", 5: "Çocuk Cerrahisi",
6: "Çocuk Endokrinolojisi", 7: "Çocuk Enfeksiyon Hastalıkları", 8: "Çocuk Nörolojisi",9: "Çocuk Sağlığı ve Hastalıkları", 10: "Deri ve Zührevi Hastalıkları",
11: "Diş Hekimliği (Genel Diş)", 12: "Endodonti", 13: "Endokrinoloji ve Metabolizma Hastalıkları",15: "Enfeksiuon Hastalıkları ve Klinik Mikrobiyoloji",
16: "Fiziksel Tıp ve Rehabilitasyon", 17: "Gastroenteroloji", 18: "Gastroenteroloji Cerrahisi",19: "Genel Cerrahi", 20: "Geriatri",21: "Göğüs Cerrahisi",
22: "Göğüs Hastalıkları", 23: "Göz Hastalıkları", 24: "Hematoloji",25: "İç Hastalıkları(Dahiliye)", 26: "İmmünoloji ve Alerji Hastalıkları",
27: "Jinekolojik Onkoloji Cerrahisi",28: "Kadın Hastalıkları ve Doğum", 29: "Kalp ve Damar Cerrahisi", 30: "Kardiyoloji",31: "Kulak Burun Boğaz Hastalıkları",
32: "Nefroloji ", 33: "Nöroloji", 34: "Ortadonti",35: "Ortopedi ve Travmatoloji",36: "Perinatoloji", 37: "Periodontoloji",
38: "Plastik,Rekonstrüktif ve Estetik Cerrahisi",39: "Protetik Diş Tedavisi", 40: "Restoratif Diş Tedavisi",41: "Ruh Sağlığı ve Hastalıkları(Psikiyatri)",
42: "Sağlık Kurulu Erişkin",43: "Sağlık Kurulu ÇÖZGER(Çocuk Özel Gereksinim Raporu)",44: "Sigarayı Bırakma Kliniği", 45: "Spor Hekimliği",
46: "Tıbbi Onkoloji", 47: "Üroloji",48: "Ağız ,Diş ve Çene Cerrahisi", 49: "Radyoloji"}
doktorlar = {1: [" Dr Ali Yılmaz", " Dr Ayşe Duman"], 2: [" Dr Ahmet Kara", "Dr Elif Kaya", "Dr Eylül Erdem"],3: ["Dr Mehmet Yaman", "Dr Eylem Arslan", "Dr Öykü Kaya"],
4: ["Dr Mehmet Arık", "Dr Hayat Aydın", "Dr Rüzgar Kara"], 5: ["Dr Hayal Aydın", "Dr Hakan Karaman"], 6: ["Dr Ayla Yılmaz", "Dr Asya Enli", "Dr Enver kara"],
7: ["Dr Hayati Çetin", "Dr Harun", "Dr Ahmet Yaka"], 8: ["Dr Yazgı Kaya", "Dr Teslime Acar", "Dr Rana Aydın"], 9: ["Dr Büşra Haklı", "Dr Hakkı Aydın"],
10: ["Dr Neriman Çalı", "Dr Sümeyye Darı", "Dr Ahmet Zorlu"], 11: ["Dr Esma Batar", "Dr Hasan Aydın"],12: ["Dr Rana Sarı", "Dr Çağatay Akman"],
13: ["Dr Aslı Ekli", "Dr Talat Ersin"], 14: ["Dr Feride Kuçak", "Dr Eslem Türk", "Dr Enes Kara"],15: ["Dr Zeynep Yazgı", "Dr İsmail Uygar"],
16: ["Dr Eslem Talat", "Dr Nuri Saygılı","Dr Pakize Satır"],17: ["Dr Sıla Kaygılaroğlu", "Dr Kaya Ay", "Dr Şakir Bakıroğlu"],
18: ["Dr Elif Zakum", "Dr Kemal Kahraman"], 19: ["Dr Esra Yazgı", "Dr Ekrem Talat", "Dr Oruç Saklı","Dr Eslem Aydın"],20: ["Dr Recep Yazar", "Dr Ebru Yılmaz"],
21: ["Dr Sultan Akın", "Dr Faruk Demirhan"], 22: ["Dr Aslı Aydınoğlu", "Dr Bekir Koçlu"],23: ["Dr Osman Yazgı", "Dr Sena Köse"],
24: ["Dr Yiğit Alp Yazgın", "Dr Melisa Aydın"], 25: ["Dr Saliha Akpınar", "Dr Semih Kayahan"],26: ["Dr Kerem Terzi", "Dr Fethi Kaygısız", "Dr Ayşe Çetin"],
27: ["Dr Ali Ünal", "Dr Gamze Tezel"], 28: ["Dr Rümeysa Kaya", "Dr Sinan Koza"],29: ["Dr Irmak Yeşilkoy", "Dr Burak Şahin"],
30: ["Dr Buse Öz", "Dr Nihal Koç"],31: ["Dr Hakan Kale", "Dr Gizem Ünlü"], 32: ["Dr Simay Çalışkan", "Dr Mesut Erşanlı"],33: ["Dr Ahmet Batur", "Dr Safiye Karlı"],
34: ["Dr Ateş Evren", "Dr Sıla Yıldırım"], 35: ["Dr Büşra Kerpiç", "Dr Zehra Yıldız"],37: ["Dr Fırat Zorlu", "Dr Ferdi Kaymaz"],
38: ["Dr Feyza Akçil", "Dr Esra Çaycı"], 39: ["Dr Emine Orak", "Dr Emin Avcı"],40: ["Dr Ecem Eser", "Dr Ezgi Özkaya"], 41: ["Dr Ahmet Cantürk", "Dr Sevcan Ata"],
42: ["Dr Fatma Aktaş", "Dr Mehmet Alca"], 43: ["Dr Murat Yüksel", "Dr Azra Demirtaş"],44: ["Dr Selinay Açar", "Dr Hazel Güler"],
45: ["Dr Ayşe Arınsoy", "Dr Aylin Koçan"], 46: ["Dr Muhammed Gümüş", "Dr Asuman Akkan"],47: ["Dr Furkan Albayrak", "Dr Şükran Gürdağ"],
48: ["Dr Kadriye Yurt", "Dr Şule Solmaz", "Dr Sebahattin Öztürk"],49: ["Dr Yusuf Ayaz", "Dr Arda Emrem"]}
def isim_kontrolu(ad_soyad):
    try:
        for char in ad_soyad:
            if '0' <= char <= '9':
                raise ValueError("İsim içinde sayı bulunmamalı!")
        print("İsim geçerli.")
        return ad_soyad  # Eğer isim geçerli ise adı geri döndür
    except ValueError as e:
        print(e)
        ad_soyad = input("Geçerli bir isim giriniz: ").upper()
        return isim_kontrolu(ad_soyad)
def tc_kontrol(tc):
    try:
        if len(tc)!=11:
            raise ValueError("Tc 11 haneden oluşmalıdır!")
        print("Tc geçerli.")
        return tc
    except ValueError as e:
        print (e)
        tc=input("Gecerli bir Tc giriniz:")
        return tc_kontrol(tc)

def randevu_kayıt():
    global klinikler
    global doktorlar
    tc = tc_kontrol(input("Tc girin: "))
    ad_soyad = isim_kontrolu(input("Ad ve Soyad girin: ").upper())
    yas = int(input("Yaş: "))
    cinsiyet = input("Cinsiyet: ").upper()

    print("Klinikler:")
    #klinikleri yazdırma.
    for k_id, k_adi in klinikler.items():
        print(f"{k_id} : {k_adi}")

    klinik_id = int(input("Klinik seçiniz: "))
    klinik_adi = klinikler.get(klinik_id, "Bilinmeyen Klinik")#sözlükte yoksa bilinmeyen klinik yazacak.
    if klinik_id not in doktorlar:
        print("Seçtiğiniz klinik için doktor bulunamadı.")
        return

    print("Doktorlar:")
    #girilen kliniğe göre doktor isimlerini numaralı şekilde gösterip kullanıcıdan seçim yapılması istenilecek.
    for d_id, doktor in enumerate(doktorlar[klinik_id], 1):
        print(f"{d_id} : {doktor}")

    doktor_id = int(input("Doktor seçiniz: "))
    doktor_adi = doktorlar[klinik_id][doktor_id - 1]#0 dan başladığı için 1 eksik aldım.
    # açma ve kapama aynı anda yapılsın diye böyle yaptım.
    with open("23100011055.txt", 'a', encoding='utf-8') as dosya:
      dosya.write(f"TC:{tc:<15} AD_SOYAD:{ad_soyad:<35} YAŞ:{yas:<5} CİNSİYET:{cinsiyet:<10} KLİNİK :{klinik_adi:<40} DOKTOR :{doktor_adi:<30}\n")
    print("Randevu başarıyla eklendi ve dosyaya kaydedildi.")
    while True:
        secim = input("Yeni randevu kaydı yapacak mısınız? (Evet için 1 / Hayır için 2): ")
        if secim == '1':
            randevu_kayıt()
            break
        elif secim == '2':
            randevu_islemleri()
            break
        else:
            print("Yanlış secim yaptınız lütfen tekrar deneyiniz.")


def randevu_guncelle():
    global klinikler
    global doktorlar
    tc_guncellenecek = input("Güncellemek istediğiniz randevunun TC Kimlik No'sunu giriniz: ")
    bulundu = False
    yeni_satirlar = []
    with open("23100011055.txt", 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()

    for satir in satirlar:
        if satir.startswith(f"TC:{tc_guncellenecek}"):
            bulundu = True
            print("Mevcut randevu bilgileri:")
            print(satir)

            # Yeni bilgiler girilecek
            ad_soyad = isim_kontrolu(input("Ad ve Soyad girin: ").upper())
            yas = input("Yeni Yaş: ")
            cinsiyet = input("Yeni Cinsiyet: ").upper()

            print("Klinikler:")
            for k_id, k_adi in klinikler.items():
                print(f"{k_id} : {k_adi}")

            klinik_id = int(input("Yeni Klinik seçiniz: "))
            klinik_adi = klinikler.get(klinik_id, "Bilinmeyen Klinik")

            if klinik_id not in doktorlar:
                print("Seçtiğiniz klinik için doktor bulunamadı.")
                return

            print("Doktorlar:")
            for d_id, doktor in enumerate(doktorlar[klinik_id], 1):#doktor adlarını numaralı şekilde versin diye enumerate kullandım.
                print(f"{d_id} : {doktor}")

            doktor_id = int(input("Yeni Doktor seçiniz: "))
            doktor_adi = doktorlar[klinik_id][doktor_id - 1]

            yeni_satir = f"TC:{tc_guncellenecek:<15} AD_SOYAD:{ad_soyad:<35} YAŞ:{yas:<5} CİNSİYET:{cinsiyet:<10} KLİNİK :{klinik_adi:<40} DOKTOR :{doktor_adi:<30}\n"
            yeni_satirlar.append(yeni_satir)
        else:
            yeni_satirlar.append(satir)
    with open("23100011055.txt", 'w', encoding='utf-8') as dosya:
        dosya.writelines(yeni_satirlar)

    if bulundu==True :
        print("Randevu başarıyla güncellendi.")
    else:
        print("Girdiğiniz TC Kimlik No'ya ait randevu bulunamadı.")

    randevu_islemleri()


def randevu_arama():
    aranan_randevu=input("Aramak istediğiniz randevu'nun TC Kimlik No'sunu giriniz:")
    bulundu=False
    with open("23100011055.txt", 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()

    for satir in satirlar:
        if satir.startswith(f"TC:{aranan_randevu}"):
            bulundu = True
            print("Aradığınız Randevu:")
            print(satir)
    if bulundu!=True:
        print("Girdiğiniz TC Kimlik No'ya ait randevu bulunamadı.")

    randevu_islemleri()
def randevu_silme():
    tc_silinecek = input("Silmek istediğiniz randevunun TC Kimlik No'sunu giriniz: ")
    silindi = False

    with open("23100011055.txt", 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()

    with open("23100011055.txt", 'w', encoding='utf-8') as dosya:

        for satir in satirlar:
            #dosya üzerine yazılırken girilen tc nin oldugu satır atlanarak yazdırdım bu sayede dosyadan silindi.
            if satir.startswith(f"TC:{tc_silinecek}"):
                silindi = True
                continue
            dosya.write(satir)

    if silindi==True:
        print("Randevu başarıyla silindi.")
    else:
        print("Girdiğiniz TC Kimlik No'ya ait randevu bulunamadı.")

    randevu_islemleri()


def yatıs_islemleri():
    odalar=[]
    for i in range(1,101):
        odalar.append(i)
    global klinikler
    global doktorlar
    ameliyathane_kayitlari = {}

    def kayit_ekle(ad_soyad, tc, yas, poliklinik_id, doktor_id, oda_bilgisi):
        poliklinik = klinikler[poliklinik_id]
        doktor_adi = doktorlar[poliklinik_id][doktor_id - 1]
        ameliyathane_kayitlari[tc] = {
            "Ad Soyad": ad_soyad,
            "TC": tc,
            "Yaş": yas,
            "Poliklinik": poliklinik,
            "Doktor Adı": doktor_adi,
            "Oda Bilgisi": oda_bilgisi
        }
        if int(oda_bilgisi) in odalar:
            odalar.remove(int(oda_bilgisi))
        print(f"{ad_soyad} adlı hastanın {oda_bilgisi} numaralı odaya yatışı yapıldı.")

    def kayit_sil(tc):
        if tc in ameliyathane_kayitlari:
            del ameliyathane_kayitlari[tc]
            print(f"TC {tc} numaralı hastanın kaydı silindi.")
        else:
            print(f"TC {tc} numaralı hasta bulunamadı.")

    def kayitlari_listele():
        if ameliyathane_kayitlari:
            for tc, bilgiler in ameliyathane_kayitlari.items():
                print(f"TC: {tc}")
                for anahtar, deger in bilgiler.items():
                    print(f"{anahtar}: {deger}")
                print("----------")
        else:
            print("Hiç kayıt bulunmuyor.")

    while True:
        secim = input("""
        HASTANE YATIŞ İŞLEMLERİ
        1-KAYIT EKLE 
        2-KAYIT SİL
        3-KAYITLARI LİSTELE
        4-GERİ DONUŞ
        0-ÇIKIŞ
        SEÇİMİNİZ: """)
        if secim not in ["0", "1", "2", "3","4"]:
            print("Yanlıs secim yaptınız.Tekrar deneyiniz.")
            ana_menu()
        elif secim == "1":
            tc = tc_kontrol(input("TC:"))
            ad_soyad = isim_kontrolu(input("Ad Soyad:").upper())
            yas = input("Yaş: ")
            print("Klinikler:")
            for k_id, k_adi in klinikler.items():
                print(f"{k_id} : {k_adi}")
            poliklinik_id = int(input("Poliklinik ID: "))
            print("Doktorlar:")
            for d_id, doktor in enumerate(doktorlar[poliklinik_id], 1):  # doktor adlarını numaralı şekilde versin diye enumerate kullandım.
                print(f"{d_id} : {doktor}")
            doktor_id = int(input("Doktor seçiniz: "))
            print(odalar)
            oda_bilgisi = input("Oda Bilgisi girniz: ")
            kayit_ekle(ad_soyad, tc, yas, poliklinik_id, doktor_id, oda_bilgisi)
        elif secim == "2":
            tc = input("Silinecek hastanın TC numarası: ")
            kayit_sil(tc)
        elif secim == "3":
            kayitlari_listele()
        elif secim == "4":
            hastane_islemleri()
        elif secim=="0":
            print("Çıkış ypılıyor...")
            exit()


def r_ucret_tahsil():
    global klinikler
    tc = input("Tc giriniz:")
    tc_kontrol(tc)
    ucretler = {"1": 100, "2": 200, "3": 300, "4": 400, "5": 250, "6": 270, "7": 230, "8": 280, "9": 150, "10": 180,
                "11": 220, "12": 240, "13": 260, "14": 290, "15": 310, "16": 330, "17": 350, "18": 370, "19": 390,
                "20": 410, "21": 430, "22": 450, "23": 470, "24": 490, "25": 510, "26": 530, "27": 550, "28": 570,
                "29": 590, "30": 610, "31": 630, "32": 650, "33": 670, "34": 690, "35": 710, "36": 730, "37": 750,
                "38": 770, "39": 790, "40": 810, "41": 830, "42": 850, "43": 870, "44": 890, "45": 910, "46": 930,
                "47": 950, "48": 970}
    print("Klinikler:")
    # klinikleri yazdırma.
    for k_id, k_adi in klinikler.items():
        print(f"{k_id} : {k_adi}")
    klinik = input("Klinik seçiniz: ")
    ucret = ucretler.get(klinik, "Bilinmeyen Klinik")
    # ücretin %35'i sigorta tarafından karşılatıldığı varsayılmıştır.
    ödenecek_tutar = int(ucret) * 0.65
    print(f"{tc} nolu hasta {ödenecek_tutar} TL ücret ödeyecektir.")
def y_ucret_tahsil():
    while True:
        tc = input("Tc giriniz:")
        tc_kontrol(tc)
        ucret=0
        giriş = input("Giriş tarihi girin (YYYY-AA-GG): ")
        if len(giriş) != 10:
            print("Yanlış giriş. Tekrar Deneyiniz.")
            continue
        çıkış = input("Çıkış tarihi girin (YYYY-AA-GG): ")
        if len(çıkış) != 10:
            print("Yanlış çıkış. Tekrar Deneyiniz.")
            continue
        t1_yil, t1_ay, t1_gun = map(int, giriş.split('-'))
        t2_yil, t2_ay, t2_gun = map(int, çıkış.split('-'))
        # İlk tarihi toplam gün cinsine dönüştürme
        t1_gunler = t1_yil * 365 + t1_ay * 30 + t1_gun
        # İkinci tarihi toplam gün cinsine dönüştürme
        t2_gunler = t2_yil * 365 + t2_ay * 30 + t2_gun
        # İki tarih arasındaki farkı hesaplama mutlak degerli döndürecek
        gun_farki = abs(t2_gunler - t1_gunler)
        #günlük ücret 100tl olarak düşünülecektir.
        ucret=gun_farki*100
        # ücretin %35'i sigorta tarafından karşılatıldığı varsayılmıştır.
        ucret =ucret * 0.65
        print(f"{tc} nolu hasta {ucret} TL ücret ödeyecektir.")
        break  # Sonsuz döngüyü kır
def ucret_islemleri():
    while True:
        secim = input("""
            1-RANDEVU ÜCRETİ TAHSİL ETME
            2-YATIŞ ÜCRETİ TAHSİL ETME
            3-GERİ DÖNÜŞ
            0-ÇIKIŞ
            SECİMİNİZ:""")
        if secim not in ["0", "1", "2", "3"]:
            print("Yanlıs secim yaptınız.Tekrar deneyiniz.")
            ana_menu()
        if secim == "1":
            r_ucret_tahsil()
        elif secim == "2":
            y_ucret_tahsil()
        elif secim == "3":
            hastane_islemleri()
        elif secim=="0":
            print("Çıkış yapılıyor...")
            exit()

def randevu_islemleri():
    secim =input ("""
    1-RANDEVU KAYIT
    2-RANDEVU GÜNCELLE
    3-RANDEVU ARAMA 
    4-RANDEVU SİLME
    5-GERİ DÖNÜŞ
    0-ÇIKIŞ
    SECİMİNİZ:""")
    if secim not in ["0","1","2","3","4","5"]:
        print("Yanlıs secim yaptınız.Tekrar deneyiniz.")
        randevu_islemleri()
    elif secim=="1":
        randevu_kayıt()
    elif secim=="2":
        randevu_guncelle()
    elif secim=="3":
        randevu_arama()
    elif secim=="4":
        randevu_silme()
    elif secim=="5":
        ana_menu()
    elif secim=="0":
        print("Çıkış yapılıyor...")
        exit()

def hastane_islemleri():
    secim=input("""
     1-YATIŞ İŞLEMLERİ
     2-UCRET TAHSİL İŞLEMLERİ
     3-GERİ DÖNÜŞ
     0-ÇIKIŞ
     SEÇİMİNİZ:""")
    if secim not in ["0","1","2","3"]:
        print("Yanlıs secim yaptınız.Tekrar deneyiniz.")
        hastane_islemleri()
    elif secim=="1":
        yatıs_islemleri()
    elif secim=="2":
        ucret_islemleri()
    elif secim=="3":
        ana_menu()
    elif secim=="0":
        print("Çıkış yapılıyor...")
        exit()



def ana_menu():
    secim=int(input("""***BAHAR HASTANESİNE HOSGELDİNİZ***
    1-RANDEVU  İŞLEMLERİ
    2-HASTANE İŞLEMLERİ
    0-ÇIKIŞ
    SECİMİNİZ:"""))
    if secim not in [0,1,2]:
        print("Yanlıs secim yaptınız.Tekrar deneyiniz.")
        ana_menu()
    elif secim==1:
        randevu_islemleri()
    elif  secim==2:
        hastane_islemleri()
    elif secim==0:
        print ("Çıkıs yapıldı.")
        exit()

ana_menu()
