import json

while True:

    print("""
    .....HOSGELDINIZ.....
    ZORLUK SEVISESI SECINIZ.
    1)KOLAY
    2)ORTA
    3)ZOR
    """)
    kolay = '{ "soru1":"2 * 3 = ?", "soru2":"2 + 2 = ?", "soru3":"4 / 2 = ?"}'
    k=json.loads(kolay)

    orta='{"soru1":"4 düzine kalem kaç kalem yapar?","soru2":"Kilosu 4 TL den 35 kg fındık ne kadar eder?","soru3":"Her gün 5 sayfa kitap okuyan Emrah, 60 sayfalık kitabı kaç günde bitirebilir?"}'
    o=json.loads(orta)

    zor='{"soru1":"Ali’ni 57 cevizi vardı. 86 ceviz de arkadaşı verdi. Kaç cevizi oldu?","soru2":"25 öğrenci olan bir sınıfta kızlar 9 kişi olduğuna göre, bu sınıfta kaç erkek öğrenci vardır?","soru3":"15 kedinin kaç ayağı vardır?"}'
    z=json.loads(zor)




    secim=int(input("Lütfen seviyenizi belirtiniz:"))

    if secim==1:

        print(k["soru1"])

        cevap1=int(input("Cevabınız:"))

        if cevap1==6:
            print("Doğru Cevap")
        else:
            print("Yanlış cevap")


        print(k["soru2"])

        cevap2=int(input("Cevabınız:"))

        if cevap2==4:
            print("Doğru Cevap")
        else:
            print("Yanlış Cevap")

        print(k["soru3"])

        cevap3=int(input("Cevabınız:"))

        if cevap3==2:
            print("Doğru Cevap")
        else:
            print("Yanlış Cevap")

    elif secim==2:

        print(o["soru1"])

        cevap1=int(input("Cevabınız:"))

        if cevap1==48:
            print("Doğru Cevap")
        else:
            print("Yanlış Cevap")


        print(o["soru2"])

        cevap2=int(input("Cevabınız:"))

        if cevap2==140:
            print("Doğru Ceavp")
        else:
            print("Yanlış Cevap")


        print(o["soru3"])

        cevap3=int(input("Cevabınız"))

        if cevap3==12:
            print("Doğru Cevap")
        else:
            print("Yanlış Cevap")

    elif secim==3:

        print(z["soru1"])

        cevap1=int(input("Cevabınız"))

        if cevap1==143:
            print("Doğru cevap")
        else:
            print("Yanlış Cevap")


        print(z["soru2"])

        cevap2=int(input("Cevabınız"))
        if cevap2==16:
            print("Doğru cevap")
        else:
            print("Yanlış Cevap")

        print(z["soru3"])

        cevap3=int(input("Cevabınız"))

        if cevap3==60:
            print("Doğru cevap")
        else:
            print("Yanlış Cevap")
    else:
        print("Yanlış Seviye Seçtiniz")