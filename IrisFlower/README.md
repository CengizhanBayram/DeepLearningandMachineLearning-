# Temel Bileşen Analizi (PCA) Hakkında

![alt text](image.png)

## Nedir?

Temel Bileşen Analizi (PCA), çok değişkenli veri setlerini daha düşük boyutlu bir alt uzayda temsil etmek için kullanılan bir lineer dönüşüm yöntemidir. PCA, veri setindeki değişkenler arasındaki ilişkileri bulmayı ve veri setinin boyutunu azaltmayı amaçlar.

## Nasıl Çalışır?

PCA'nın temel amacı, veri setindeki varyansı koruyarak veri boyutunu azaltmaktır. Bu, veri setindeki değişkenler arasındaki korelasyonu azaltarak yapılır. PCA, bu amaçla veri setinin kovaryans matrisini hesaplar ve bu matrisin özdeğer ve özvektörlerini bulur. Özvektörler, veri setinin boyutunu azaltmak için kullanılacak yeni değişkenlerin yönlerini belirler. Özdeğerler ise, bu yeni değişkenlerin ne kadar varyansı temsil ettiğini gösterir.

## Nasıl Kullanılır?

PCA genellikle aşağıdaki adımlarla uygulanır:

1. Veri setini standartlaştırma (ortalama 0, standart sapma 1).
2. Kovaryans matrisinin hesaplanması.
3. Kovaryans matrisinin özdeğer ve özvektörlerinin bulunması.
4. Özdeğerlerin sıralanması ve en büyük özdeğerlere karşılık gelen özvektörlerin seçilmesi.
5. Seçilen özvektörler kullanılarak yeni değişkenlerin oluşturulması (temel bileşenler).
6. Yeni değişkenler arasındaki ilişkinin yorumlanması.

## Kullanım Alanları

- Boyut azaltma
- Veri görselleştirme
- Gürültü azaltma
- Özellik seçimi

## Kaynaklar

- [Wikipedia - Temel Bileşen Analizi](https://tr.wikipedia.org/wiki/Temel_bile%C5%9Fen_analizi)
- [Scikit-learn Documentation - PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)


