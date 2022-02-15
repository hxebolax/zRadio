# NVDA için zRadio Kılavuzu:  
## Yazarın önemli notları:  

Bu eklenti can sıkıntısından ve NVDA ile deneme yapma arzusundan geliyor.  

zRadio, yüklendikten sonra yaklaşık 120 MB olan çok ağır bir eklentidir.  

Bu, zRadio eklentisinin 0.1, 0.2 ve 0.3 sürümlerini kullanmaya devam ediyorsanız geçerlidir, ancak zRadio kullanıcılarını, boyutunu küçülttüğü ve zRadio eklentisinin performansını geliştirdiği için yeni sürüm 0.4'ü indirmeye davet ediyoruz. Daha fazla ayrıntı için lütfen aşağıdaki sürüm 0.4 için "Değişiklik günlüğü" bölümüne bakın.  

zRadio'nun iş için olmayan ve kabul edilebilir donanıma sahip bilgisayarlarda kullanılması önerilir.  

Düşük kaynağa sahip bazı bilgisayarlarda NVDA'yı yavaşlatabilir, bu nedenle eklentinin kaldırılması önerilir.  

Bu, zRadio eklentisinin 0.1, 0.2 ve 0.3 sürümlerini kullanmaya devam ediyorsanız geçerlidir, ancak zRadio kullanıcılarını, boyutunu küçülttüğü ve zRadio eklentisinin performansını geliştirdiği için yeni sürüm 0.4'ü indirmeye davet ediyoruz. Daha fazla ayrıntı için lütfen aşağıdaki sürüm 0.4 için "Değişiklik günlüğü" bölümüne bakın.  

Dediğim gibi, bu bir deneme ve olması gerektiği gibi, eklentiyi yükleyen kişi, eklentinin neden olabileceği yavaşlamadan ve söz konusu eklentiyi kullanmasından sorumludur.  

Eklentinin kullanımından veya oluşabilecek sorunlardan yazar sorumlu değildir.  

Yazar, Eklenti radyolarının hepsinin Çevrimiçi olduğunu, bu nedenle bağlantılardan sorumlu kişinin söz konusu bağlantıları sağlayan sayfa olduğunu, ayrıca radyo istasyonlarının emisyonuna karşılık gelen kısımdan kaynaklanan arıza veya arızalardan sorumlu olmadığını bildirir.  

Bu eklenti, yüksek performanslı bir bilgisayarda geliştirilmiştir, böylece yavaşlamadan muzdarip olmaz, bu kısım farklı medya tarafından bana verilen gözlemler üzerine yeniden yazılabilir.  

Eklentinin kaldırılması durumunda birkaç not:  

Eklenti, NVDA yapılandırma dizininde bulduğumuz zRadio dizinine yalnızca 3 dosya kaydeder ve bunlar şunlardır:  

* Opciones.dat  
* opt_radio.dat  
* fav_radios.dat  

Bu, zRadio kullanıcılarını yeni 0.4 sürümünü indirmeye davet etmemize rağmen, zRadio eklentisinin 0.1, 0.2 ve 0.3 sürümlerini kullanmaya devam ediyorsanız geçerlidir. Bu yeni sürümü yüklemek, şu ad verilen iki yeni dosyayı yükleyecektir:  

* cache.dat  
* radio_cache.dat  

Şimdi eklenti, zRadio eklentisinin bu yeni 0.4 sürümü kullanılırsa, NVDA yapılandırma dizininde bulduğumuz zRadio dizinine yalnızca 5 dosya kaydedecektir.  

Daha fazla ayrıntı için lütfen aşağıdaki sürüm 0.4 için "Değişiklik günlüğü" bölümüne bakın.  

0.5 sürümünde cache.dat ve radio_cache.dat dosyaları cache.sqlite ile değiştirilir.  

Çok şey bilen programcılar için, bu kadar kaba ve çok köhne bir kod için ve yorum yapmadığım ve düzenli olmak istiyorsa bir programcının yapması gerekmeyen her şeyi yaptığım için beni azarlamayın.  

Programlama şeklim kafamda ve tüm kodun kafamda olduğunu ve aniden ortaya çıktığını nasıl açıklayacağımı bilemezdim ve yazımda verimli olmadığım için her zaman kırdığım yönergeleri takip etmeye çalışıyorum. .  

Ama dediğim gibi ve savunmamda bu, can sıkıntısının ve NVDA ile deney yapma isteğinin bir sonucu.  

## ZRadio arayüzü

Eklentiyi açmak için NVDA / Araçlar menüsüne gitmemiz ve zRadio seçeneğini bularak onaylamamız gerekir.  

Ayrıca NVDA / Tercihler / Girdi hareketleri menüsüne gidip "zRadio ana penceresini göster" komutuyla ilişkili zRadio'yu arayarak eklentiyi açmak için tanımlı olmayan bir giriş hareketi atayabiliriz.  

Arayüz açıldığında yukarıdan aşağıya doğru 3 kategoriden oluşan bir ağaç listesinden oluşuyor, önce Genel ekranını, ikinci Favoriler ve üçüncü Arama motorunu buluyoruz. Ağaç listesindeyken yukarı ve aşağı oklar ile geçiş yapabiliriz. 3 kategoriyi hızlıca özetliyorum:  

* Genel, arama alanından önceden tanımladığımız istasyonlara sahip olacağız. Bu daha sonra açıklanacaktır.
* Favoriler, en çok dinlediğimiz ve daha önce bulduğumuz istasyonları ekleyebileceğimiz yer.  
* Arama motoru, bu kategoride radyolar için ülkelere, dile veya etikete göre genel bir arama yapabiliriz.  

Peki, odak seçili kategorideyken, onu etkinleştirmek için SEKME tuşuna basın ve bir istasyon aramak için veya Arama kategorisindeysek açılan kutuda bir kategori seçmek için bir arama alanına düşeceğiz.  

Bulmak istediğinizi yazdıktan sonra Ara düğmesine basın. Bu alana bir arama girdikten sonra da Enter tuşuna basabilirsiniz. Bu nedenle, bu eylem, Ara düğmesine basmış olmamızla aynı olacaktır.  

Tab yaparsak, istasyonların listesini bulacağız. Listedeyken radyo için mevcut seçenekleri göstermek için istasyon adının üzerine bir kez oklarla ve uygulamalar tuşuna veya shift + f10 tuşlarına basarak listede gezinebiliriz.  

Yeniden sıralarsak ve çalan hiçbir şey yoksa, varsayılan olarak ilk seferde %50 olan bir ses düzeyi çubuğuna düşeriz, bir istasyon oynatılıyorsa oynatmayı kontrol eden düğmelere düşeriz.  

Ses kontrolünde ses seviyesini artırmak ve azaltmak için hem sol veya sağ hem de yukarı ve aşağı okları kullanabiliriz. Düğmeleri hızlıca özetleme adımı:  

* Durdur, oynatmayı durduracak.  
* Çalmakta olan istasyonu yeniden yüklemek için Yeniden Yükle. Bu, ara belleğin kaybolması ve istasyonu tekrar aramak istemememiz durumunda kullanışlıdır.  
* Sesikapat, bu düğme, oynatma sırasında Sesi kapatabilmemizi sağlar. Basıldığında sesi aç olarak değişir.  

Tekrar sekme tuşuna basarsak şimdi sadece çıkış adlı bir düğme bulunan çubuğa düşeceğiz, ancak yakında daha fazla seçeneğe sahip olacak.  

## Genel Ekran

Bu ekranda ilk gireceğimiz şey, aramak istediklerimizi koyabileceğimiz bir arama alanıdır. Bu alandan büyük veya küçük harf koymamızın kayıtsız olduğunu ve yazdıklarımızı içeren sonucu döndüreceğini söyleyin.  

Eğer bir kelime yazarsak yazdığımız kelimeyi içeren bütün istasyonları bulur. Bir harf yazarsak, o harf ile başlayan bütün istasyonları bulur.  

Taba basarsak , Ara düğmesine erişeceğiz. Bu düğmeye basarsak arama başlayacak ve bu düğmenin adı Temizle olarak değişecektir. İstasyon listesine geri dönmek için temizle düğmesine basmalıyız.  

Not: Bu alana bir arama kriteri girdikten sonra Enter tuşuna da basabilirsiniz. Bu nedenle, bu eylem, Ara düğmesine basmış olmamızla aynı olacaktır.  

Yeniden tab tuşuna basarsak arama kutusunda ne yaptığımıza bağlı olarak bir istasyon listesi veya arama sonucu elde ederiz.  

## Favoriler ekranı

Bu ekranda elimizde olmasını istediğimiz istasyonları hızlıca ekleyebiliyoruz, istediklerimizin hepsini isimlerini çoğaltarak bile ekleyebileceğimizi söylüyoruz.  

Çalışma alanı, Genel ekranıyla tamamen aynıdır, bu yüzden tekrar anlatmayacağım.  

Hem istasyonlar hem de arama sonuçları listesinde, bir harfe basarak bizi adının başında o harfe sahip ilk istasyona götürecek olan hızlı bir şekilde hareket edebileceğimizi yorumlayın.  

Yeni 0.3 sürümünün zRadio arayüzüne aşağıdaki gibi yeni özellikler ekledim:  

* İstasyonları favorilere göre sıralayın.  
* Favorilere istasyon ekleyin, düzenleyin ve silin.  
* Artık, NVDA Girdi Hareketleri iletişim kutusundan "İstasyon hızlı bir şekilde çal ve ardından 1'den 5'e kadar numaralandırma" adlı her bir komutla ilişkili bir girdi hareketi kullanarak 5 hızlı istasyonu özel olarak başlatabilir ve zRadio'yu arayabilirsiniz.  

Yeni özelliklerin kullanımıyla ilgili ayrıntılar için lütfen aşağıdaki sürüm 0.3 için "Değişiklik Günlüğü" bölümüne bakın.  

## Arama ekranı  

Bu ekran öncekilerden farklıdır, çünkü bulacağımız ilk şey, nerede aranacağına dair farklı kategoriler içeren bir birleşik giriş kutusudur.  

İlk kategori olan Genel radyo aramasında, tüm radyo kataloğunu arayabiliriz.  

Ayrıca ülkeye, dile veya etikete göre de arama yapabiliriz. Etikete göre arama yapılması durumunda:  

Rock'ı ararsak, bize bu sınıflandırmaya sahip tüm etiketleri verecektir.  

Önceki kategorilerin herhangi birinde arama yapabiliriz, ancak yalnızca Genel kategorisinde doğrudan o kategoriden oynayabilir ve favorilere ekleyebilir ve istasyonun URL'sini kopyalayabiliriz.  

Diğer kategorilerde ise sadece Genel ekranına seçtiklerimizi ekleyebilir ve bahsi geçen Genel ekranında keşfedebiliriz.  

## Tuşlar, hareketler ve bağlamsal menülerle ilgili:  

İster istasyon ister arama olsun, her sonuç listesinde, seçtiklerimizle etkileşime geçmek için bağlamsal bir menü başlatabiliriz.  

Bu menüyü ya uygulama tuşu ile ya da uygulama tuşu olmayan bilgisayarlarda Shift + F10 ile başlatacağız.  

Genel ekranında, istasyonlar listesinden veya bir aramadan aşağıdakilerle etkileşim kurabiliriz:  

* Oynat, istasyonu oynatır.  
* Favorilere ekle, istasyonu Favoriler ekranına ekler.  
* URL'yi kopyala, istasyonun URL'sini panoya kopyalar, bir web tarayıcısında açabilir veya paylaşabiliriz.  

Favoriler ekranında aşağıdakilerle etkileşim kurabiliriz:  

İstasyon listesi:  

* Oynat, seçilen istasyonu oynatır.  
* Favorilerden kaldır, favori istasyonu siler.  
* URL'yi kopyala, istasyonun URL'sini panoya kopyalar.  

Bir arama listeleme:  

* Oynat, istasyonu oynatır.  
* URL'yi kopyala, istasyonun URL'sini panoya kopyalar.  

Ara ekranında aşağıdakilerle etkileşim kurabiliriz:  

Genel Radyo Arama kategorisini kullanarak aramanızı yaptıktan sonra:  

Genel bir aramanın sonuç listesinde:  

* Oynat  
* Favorilere ekle  
* Url'yi kopyala  

Zaten daha önce açıklanmıştır.  

Ülkeye göre ara, Dile göre ara ve Etikete göre ara kategorilerinde, hem istasyon listesinde hem de arama listesinde yalnızca aşağıdakileri kullanabiliriz:  

* Varsayılan olarak Genel'e ayarlayın, Genel ekranında bunu seçersek, seçtiğimize karşılık gelen istasyonlara sahip olacağız.  

Bu 3 kategoriye bakarsak, bu seçeneğe sahip kaç istasyona karşılık gelen bir numaraya sahiptirler.  

Diyelim ki bazen örneğin 9 istasyonlu bir tanesini seçsek ve General ekranına gittiğimizde sadece 8 tane yükleniyor çünkü eksik link doğru değil.  

Aynı şekilde, bir istasyona odaklanabildiğimiz ekranlarda, boşluk tuşuna basarsak, yeniden üretmeye başlayabiliriz.  

### Hızlı tuşlar:  

Aslında her düğmenin kendi kısayol tuşu vardır, bu yüzden daha önce açıkladığım için onları koymayacağım, içine düştüğümüzde NVDA'mız bize kısayolları verecektir.  

Ancak, görünmeyen bir kombinasyon varsa ve bu yalnızca zRadio penceresinin odaklanıp açık olduğu durumlar içindir.  

* Alt + V, bu tuş kombinasyonu bizi hızlı bir şekilde ses çubuğuna götürecek, böylece yön tuşlarıyla etkileşime geçebilelim.  

Ayrıca zRadio penceresinden çıkış butonu, Alt + F4 veya Escape ile çıkabileceğimizi söyleyelim.  

### Girdi hareketleri  

NVDA / Tercihler / Girdi hareketleri / zRadio menüsünde, zRadio kullanıcı penceresi de dahil olmak üzere herhangi bir yerden etkileşim kurabilmek için aşağıdaki komutlara bir girdi hareketi, yani tuş kombinasyonları atayabiliriz.  

Tuş kombinasyonunun başka bir işleve atanmadığından veya kullanılan uygulamaların herhangibiriyle çakışmadığından emin olun.  

Varsayılan olarak zRadio herhangi bir tuş atamadan gelir ve bu yapılandırmayı kullanıcıya bırakır.  

Ayrıca, bu tuşların hem zRadio ile çalışacağını, hem de pencereyi açıp kapattığını bilelim.  

zRadio, kullanıcının bir girdi hareketi eklemesi için aşağıdaki komutları sağlar:  

* Sesi azalt  
* Oynatmayı durdur  
* zRadio Ana penceresini görüntüler  
* Sesi Aç ve Kapat  
* Oynatmayı Yeniden Yükle  
* Oynatılan istasyon için bilgi  
* Sesi Arttır  

## Çevirmenler ve ortak çalışanlar:  

* Fransızca: Rémy Ruiz  
* Portekizce: Angelo Miguel Abrantes  
* İngilizce: slanovani  
* İtalyanca: Simone Dal Maso  
* Arapça: Wafiq Taher  
* Danimarka: Daniel Gartmann.  
* Turkçe: Umut KORKMAZ  

# Sürüm Geçmişi:  
## Sürüm 0.5.4:  

* Dilleri algılarken oluşan hata düzeltildi.  
* NVDA 2022.1.0 sürümü için hazırlanmıştır.  

## Sürüm 0.5.3:  

* Yeni diller eklendi.  

## Sürüm 0.5.2.

* NVDA'yı başlatırken yavaş yükleme düzeltildi.  

zRadio'nun neden olduğu NVDA önyükleme gecikmeleri düzeltildi. Şimdi NVDA önyüklemesi hemen gerçekleşecek.  

* Mors projesi için destek eklendi.  

NVDA'nın yeni sürümleri için destek eklendi, tam olarak yeni Alpha'larla kullanılmak üzere ve eklenti NVDA çıktığında hazır2021.1.  

Şimdilik eklenti, 2019.3 sürümünden itibaren uyumlu olmaya devam edecek.  

## Sürüm 0.5.1.

* Boşluk çubuğuna basarak bir istasyonu oynatma yeteneği eklendi.  

Bu yeni olasılık, Genel, Sık Kullanılanlar ve Genel radyo arama kategorisindeki Arama'da istasyonların bulunabileceği üç ekranda olacaktır.  

Bu 3 bölümden herhangi birinde odak bir istasyondayken boşluk tuşuna basarsak odağı Durdur düğmesine çevirerek oynatma başlayacaktır.  

* Eklentiyi ilk kez yükleyen yeni kullanıcılar için ciddi bir hata düzeltildi.  

## Sürüm 0.5.  

* Yeni önbellek yönetimi eklendi.  

Artık yükü hafifletmek için oluşturulan önbellek yerine kütüphanenin önceden tanımlanmış önbelleği kullanılıyor.  

Önceden tanımlanmış önbelleği kullanarak eklentinin yüklenmesi çok daha hızlıdır. Bazen sunucuya bağlantı nedeniyle bizi yavaşlatabilir, ancak şimdi eklentinin %95'inin NVDA'mızı geciktirmeden başka bir eklentiymiş gibi yüklenmesi gerekiyor.  

## Sürüm 0.4a.  

* İtalyanca ve Arapça dilleri eklendi  

## Sürüm 0.4.  

* Kod, boyutunu yarıdan fazla azaltarak optimize edildi.  

Kod, kurulum artık %60 daha küçük olacak şekilde optimize edilmiştir. Bu, hangi performansın daha iyi olduğunu etkiler.  

* Eklentinin başlatılmasını hızlandırmaya yardımcı olan küçük bir önbellek eklendi.  

Bazen bir azınlık botu, NVDA ekran okuyucusunun başlaması biraz zaman alabilir, bu eklentinin sunucu ile iletişim sorunudur.  

0.3 sürümünden önce, eklentiye koyduğum önbellekle, şimdi çok nadiren gerçekleşen önbellekle başlamak her zaman uzun zaman aldı.  

Pekala cache.dat dosyası, NVDA'yı her yeniden başlattığımızda güncellenir, çünkü taşıması gereken başlatma sayısını ve 5'e ulaştığı zaman sayacını içerir.a la sexta vez el archivo radio_cache.dat da güncellenecektir.  

cache.dat ve radio_cache.dat dosyaları, NVDA konfigürasyon dizininde bulunan zRadio dizininde depolanır.  

* Ülke sözlükleri, "NVDA Seçenekleri" iletişim kutusunun "Genel" kategorisi altında "Kullanıcı için varsayılan" NVDA dilini seçtiğimizde, "Fransızca, fr", "Portekizce ( Portekiz, Brezilya), Şu anda zRadio eklentisi tarafından desteklenen üç dil olan pt_PT / pt_BR "veya" İngilizce en ", İspanyolca diline ek olarak ülkelere göre arama yapıldığında ülke adları doğru bir şekilde görüntülenmektedir.  

Varsayılan olarak zRadio, "İspanyolca, es" dilini kullanacak şekilde yapılandırılmıştır, ancak "Kullanıcı için varsayılan" seçeneğini seçtiyseniz ve diliniz henüz çevrilmediyse, eklentinin arayüzüne her zaman İspanyolca olarak sahip olursunuz.  

* Portekizce (Portekiz / Brezilya) ve İngilizce'ye çeviri eklendi.  

## Sürüm 0.3.  

* Favorilerdeki istasyonları sıralama özelliği eklendi.  

Bu yeni seçenek sadece Favoriler içindir ve odağın bulunduğu istasyonu Alt + Yukarı veya Aşağı Ok ile yukarı veya aşağı hareket ettirebiliriz.  

Listenin hem başına hem de sonuna ulaşıldığında, listenin başında veya sonunda olduğumuz konusunda bizi uyarmak için bir ses çalınacaktır.  

Ses, nerede olduğumuzu iyi tanımlamak için farklıdır.  

* Favorilere istasyon ekleme, düzenleme ve silme özelliği eklendi.  

Favoriler kategorisine geldiğimizde Alt + E kısayol tuşu ile Eylem adlı yeni bir buton görüntülenecektir.  

Bu düğme yalnızca Favoriler kategorisinde olduğumuzda görünecektir.  

Arayüzün herhangi bir yerinden butonu çağırabiliriz ve aşağıdaki seçeneklerle görüntülenecek bir menüden oluşur:  

* Yeni istasyon: Kişisel bir istasyonu tanıtmak için bir diyalog açar.  
* İstasyonu düzenle: Odak Favoriler'de olan istasyonu düzenler.  
* Favorilerden kaldır: Odaklanan istasyonu siler. Bu geri döndürülemez.  

Hem Yeni istasyon hem de İstasyonu düzenle iletişim kutusu her iki seçenek için de aynıdır.  

Bu kutu, istasyonun adı ve istasyonun URL'si için iki düzenleme alanından oluşur.  

Bu alanlar zorunludur ve boş bırakılamaz.  

Favoriler listesinde aynı ada sahip istasyonlar olabilir, ancak daha iyi anlamamız için isimlerin farklılaştırılması önerilir.  

Ayrıca Tamam ve İptal olmak üzere iki düğmemiz var.  

Tamam ttuşuna basarsak yaptığımız şeye bağlı olarak değişiklikler kaydedilecektir ya Yeni istasyon ya da İstasyonu düzenle penceresinde.  

İptal edersek tüm veriler kaybolur ve hiçbir şey kaydedilmez.  

Bu iki eylemde Alt + F4 veya Escape tuşlarına basarak da diyaloğu kapatabiliriz, yaptıklarımız kaybolacaktır.  

* Hızlı istasyon imkanı eklendi.  

Bu yeni seçenek, bir istasyonu hızlı bir şekilde çalmaya başlamamızı sağlayacak.  

Şimdi 5 hızlı istasyonumuz olabilir, bu istasyonlar Favorilere ilk 5 sıraya yerleştirdiğimiz istasyonlar olacak.  

Bu yeni seçenek için NVDA menüsü / Tercihler / Girdi hareketleri ... / zRadio'ya giderek yapılandırmamız gereken 5 yeni Giriş hareketi eklendi.  

Yeni hareketlere hızlı istasyonu oynat denir ve ardından 1'den 5'e kadar bir numaralandırma gelir.  

Pekala, yapılandırdığımız her hareket, favorilerimizde bulunan istasyona karşılık gelecektir.  

Hızlı istasyon 1'i hızlı bir şekilde yapılandırırsak ve Favoriler'de Test Radyomuz var, zRadio penceresi açık veya pencere kapalıyken herhangi bir yere bastığımızda, bu sıraya atadığımız tuş kombinasyonu o istasyonu çalmaya başlayacak.  

Bu, her favori için bir giriş hareketi atadığımız sürece Favorilerin ilk 5 istasyonu için geçerlidir. Bu seçenek, daha önce belgelenen istasyonları sipariş edebilme seçeneği ile birlikte, hızlı erişim ile tercih edilen 5 istasyona sahip olabilmek için tamamlanmaktadır.

## Sürüm 0.2.  

* Fransızca dil eklendi.  
* Sabit belgeler.  
* Ara / Etikete göre aramada sabit gecikme.  

Artık arayüz askıda kalmayacak. Bu alan yeniden yapılandırılmış, varsayılan sonuçlar kaldırılmış ve yalnızca arandığında gösterilmiş.  

* Arama alanlarında Enter tuşuna basabilme özelliği eklendi.  
* Sabit kod hataları.  

## Sürüm 0.1.  

* İlk sürüm.