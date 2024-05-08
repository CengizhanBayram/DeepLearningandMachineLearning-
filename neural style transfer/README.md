# Stil Aktarımı Kullanarak Görüntü Dönüştürme

Bu kod, bir görüntünün içeriğini koruyarak farklı bir sanat tarzına sahip diğer bir görüntünün tarzını uygulamak için kullanılır. Örneğin, bir fotoğrafı Van Gogh'un resim tarzına dönüştürmek gibi.

## Kullanılan Yöntemler

1. **Önceden Eğitilmiş Model Kullanımı (VGG-19)**:
   - Bu kodda stil aktarımı için VGG-19 modeli kullanılır.
   - VGG-19 modeli, derin öğrenme modelidir ve görsel tanıma görevlerinde kullanılır.
   - Stil ve içerik özellikleri çıkarmak için VGG-19 modelinin özellik çıkarma yetenekleri kullanılır.

2. **Gram Matrisi**:
   - Stil özelliklerini temsil etmek için gram matrisi kullanılır.
   - Gram matrisi, bir özellik haritasındaki farklı özelliklerin çiftlerinin iç çarpımıdır.
   - Stil özelliklerinin korelasyonunu ifade eder.

3. **Stil ve İçerik Kayıpları**:
   - Stil aktarımı bir optimizasyon problemi olarak formüle edilir.
   - Stil kaybı ve içerik kaybı minimize edilmeye çalışılır.
   - Stil kaybı, stil özelliklerinin farkını ifade eder.
   - İçerik kaybı, içerik ve stil görüntülerinin benzerliğini ifade eder.

4. **Gradyan İnişi**:
   - Stil aktarımı işlemi gradyan inişi kullanır.
   - Her iterasyonda stil ve içerik kayıplarının gradyanı hesaplanır ve başlangıç görüntüsü güncellenir.

5. **Başlangıç Görüntüsü**:
   - Stil aktarımı işlemi, rastgele bir başlangıç görüntüsü ile başlar.
   - Başlangıç görüntüsü genellikle içerik görüntüsü olarak başlar ve stil aktarımı işlemi bu görüntü üzerine uygulanarak devam eder.

Bu yöntemlerin birleşimi, bir görüntünün içeriğini koruyarak belirli bir sanat tarzının özelliklerini başka bir görüntüye aktarmak için etkili bir şekilde kullanılır.
