# CarTV resmî kanal listesi

CarTV'de liste ekle veya mevcut listeyi yenile:
https://raw.githubusercontent.com/abdullahates-source/access/main/playlist.m3u

25 Ekim 2026 itibarıyla 25 resmî kaynaklı yayın bulunur. Star TV, HT Spor, 360 TV ve TV4 eklendi. Her kaydın kaynak adresi ve kontrol tarihi official_streams.json dosyasındadır.

TV+ kataloğu, kanal numaraları ve TV+ bağlantısı kaldırılmıştır. Üyelik, kullanıcı adı, şifre, çerez veya oturum anahtarı kullanılmaz.

Gönderilen Gist'teki 56 adresin 29'unda teknik video erişimi sağlandı. Bunların tümünün resmî kaynak bağlantısı doğrulanamadığından hepsi eklenmedi. ATV, A2, A Haber, A Spor ve Minika için bulunan güncel resmî adresler erişimi reddetti. Bu kanallar için kısıtlama aşılmadı. Star TV için eski oturum parametresi yerine resmî oynatıcının ana yayın adresi kullanıldı.

## Dosyalar
- playlist.m3u: CarTV yayın listesi.
- official_streams.json: kaynak, adres ve kontrol tarihi.
- build_playlist.py: kayıt dosyasından M3U oluşturur.

Python 3 ile yeniden oluşturma:

    python build_playlist.py

Kod yeni URL keşfetmez; oynatmayı yeniden test etmez. Yeni kayıtlar ancak resmî kaynak ve video erişimi kontrolünden sonra eklenmelidir. iPhone CarTV cihaz testi yapılmamıştır; yayın erişimi ülkeye, haklara ve zamana göre değişebilir.
