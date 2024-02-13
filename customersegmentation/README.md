# K-Means Algoritması(unsupervised learning algoritması aynı zamanda)

K-means, veri kümeleme (clustering) için kullanılan bir makine öğrenmesi algoritmasıdır. Veri kümeleme, benzer özelliklere sahip veri noktalarını gruplamak için kullanılır. K-means algoritması, veri noktalarını K sayıda küme veya kümeye bölerek benzerliklerine göre gruplamayı amaçlar.
Toplu verilerin olduğu ve gruplama yapmak istediğiniz ancak yapamadığınız her alanda kullanılır.

## Nasıl Çalışır?

K-means algoritması genellikle aşağıdaki adımları izler:

1. Başlangıçta, K adet küme merkezi rastgele seçilir.
2. Her veri noktası, en yakın küme merkezine atanır.
3. Küme merkezleri, her kümeye ait veri noktalarının ortalaması olarak güncellenir.
4. Yeniden atanma ve merkez güncelleme adımları, küme merkezleri sabitlenene kadar veya bir iterasyon limitine ulaşılana kadar tekrarlanır.
5. Algoritma, veri noktalarının küme merkezlerine olan uzaklıklarının minimize edilmesiyle sonuçlanacak şekilde çalışır.

## Avantajlar ve Dezavantajlar

- **Avantajlar:**
  - Basit ve etkili bir kümeleme yöntemi olarak kullanılabilir.
  - Büyük veri kümeleri üzerinde hızlı bir şekilde çalışabilir.
  
- **Dezavantajlar:**
  - Başlangıç merkezlerin rastgele seçilmesi, farklı başlangıç noktalarında farklı sonuçlar üretebilir.
  - Küme sayısını önceden belirlenmiş bir parametre olarak alır, bu nedenle uygun K değerinin seçilmesi önemlidir.
  - Küme merkezlerinin rastgele seçilmesi, algoritmanın global minimuma ulaşma garantisi vermez.

K-means algoritması, basit ve etkili bir kümeleme yöntemi olarak yaygın olarak kullanılır. Ancak, veri setinin özelliklerine bağlı olarak uygun parametrelerin seçilmesi ve sonuçların doğru yorumlanması önemlidir.
