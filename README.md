# CarTV kanal listesi

CarTV M3U adresi:
https://raw.githubusercontent.com/abdullahates-source/access/main/playlist.m3u

## Kapsam
- TV+ resmî kanal kataloğu: 156 kanal (25 Ekim 2026 tarihli sayfa).
- Oynatılabilir M3U: bağımsız resmî kaynaklardan doğrulanan 21 yayın.
- TV+ kataloğuyla 20 eşleşme; Kanal 7 Avrupa ayrıca korunur.
- Kanal numaraları eşleşen yayınlara tvg-chno olarak eklenir. CarTV bu alanı desteklemeyebilir.
- Katalogda olmak, M3U yayını bulunduğu veya bir TV+ paketinde erişim hakkı olduğu anlamına gelmez.

## Dosyalar
- playlist.m3u: CarTV'ye eklenecek yayın listesi.
- tvplus_channels.json: kanal numarası, adı, TV+ sayfası ve doğrulanmış yayın eşleşmesi.
- official_streams.json: 25 Ekim 2026'da yayın listesi ve video parçası erişimi kontrol edilmiş resmî adresler ve kaynakları.
- build_playlist.py: herkese açık TV+ kataloğunu indirip mevcut resmî yayın kayıtlarıyla eşleştirir.

## Listeyi yeniden oluşturma
Python 3 ile, dosyaların bulunduğu klasörde:

    python build_playlist.py

Ek paket veya TV+ üyeliği gerekmez. Kod yeni yayın URL'si keşfetmez ve mevcut yayınların çalışırlığını yeniden test etmez. Yeniden çalıştırıldığında katalog yenilenir; doğrulama tarihi değiştirilmez. Yeni yayınlar official_streams.json dosyasına yalnızca resmî kaynak ve video erişim kontrolünden sonra eklenmelidir.

TV+ kullanıcı adı, şifre, çerez, erişim anahtarı veya DRM lisansı kullanılmaz. TV+ üyeliğine ait yayınları dışa aktarma, erişim kısıtlamalarını kaldırma veya üyelikli kanallara adres uydurma işlemi yapılmaz. TV+ tarafından belgelenmiş bir M3U dışa aktarma özelliği bu çalışma kapsamında doğrulanmamıştır.

Yayın erişimi zamanla, ülkeye ve yayın haklarına göre değişebilir. iPhone CarTV üzerinde cihaz testi yapılmamıştır. CarTV'de mevcut listeyi yenileyin.

Katalog kaynağı: https://tvplus.com.tr/destek/sss/tvplus-kanallari
