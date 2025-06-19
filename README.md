# Viraj Tabelası İkaz Sistemi (Viraj İkaz Sistemi)

Bu proje, yol üzerindeki viraj tabelalarını YOLOv3 tabanlı bir derin öğrenme modeli ile algılayarak, Arduino üzerinden gerçek zamanlı uyarı veren bir viraj ikaz sistemi uygulamasıdır.

---

## Proje Özeti

- Viraj tabelalarının eğitim süreci Google Colaboratory üzerinde gerçekleştirilmiştir.
- Nesne algılama için YOLOv3 modeli kullanılmıştır.
- Python (Spyder IDE) ile görüntü işleme ve nesne tespiti yapılmıştır.
- Algılanan viraj türüne göre Arduino'ya seri haberleşme ile sinyal gönderilerek çıktı alınmaktadır.
- Sistem, %80 verimlilikle çalışmakta ve gerçek zamanlı ikaz sağlamaktadır.

---

## Kullanılan Teknolojiler

- Python 3.x
- OpenCV
- YOLOv3 (Darknet framework)
- Arduino (seri haberleşme ile)
- Adafruit SSD1306 OLED ekran
- Google Colaboratory (model eğitimi için)

---

## Kurulum ve Çalıştırma

1. Python ortamınızı oluşturun ve gerekli kütüphaneleri yükleyin:
    ```bash
    pip install opencv-python numpy pyserial
    ```
2. YOLOv3 yapılandırma dosyaları (`.cfg`) ve eğitimli ağırlık dosyalarını (`.weights`) proje dizinine koyun.
3. Arduino kodunu Arduino IDE üzerinden yükleyin.
4. Python dosyasını çalıştırarak viraj tespiti ve ikaz sistemini başlatın.
5. Arduino ve bilgisayarınızın seri portlarının doğru eşleştiğinden emin olun (`COM3` gibi).

---

## Dosyalar

- `arduino_code.ino` : Arduino için yazılan kod.
- `viraj_tespit.py` : Python ile YOLOv3 kullanarak viraj tespiti yapan kod.
- `models/` : YOLO yapılandırma ve ağırlık dosyaları.
- `images/` : Örnek viraj resimleri.

---

## Proje Görseli

![Viraj İkaz Sistemi](https://www.linkedin.com/posts/ahmetcantopcuoglu_yolov3-python-spyder-activity-7171544056571772929-7NK9?utm_source=share&utm_medium=member_desktop&rcm=ACoAADLb__MBdAHwaKz-Ccp6ceEVVNgI4kjRjnE)

---

## İletişim

Proje hakkında sorularınız için bana ulaşabilirsiniz:  
[GitHub Profilim](https://github.com/ahmetcantopcuoglu)

---

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.  
Detaylar için `LICENSE` dosyasına bakınız.
