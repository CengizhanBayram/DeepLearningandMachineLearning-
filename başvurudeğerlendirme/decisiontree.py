import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# Veri setini yükle
df = pd.read_csv("DecisionTreesClassificationDataSet.csv")

# Veri setini göster
print(df.head())

# Veri setindeki kategorik değerleri sayısal değerlere dönüştür
mapping = {'Y': 1, 'N': 0}
df['IseAlindi'] = df['IseAlindi'].map(mapping)
df['SuanCalisiyor?'] = df['SuanCalisiyor?'].map(mapping)
df['Top10 Universite?'] = df['Top10 Universite?'].map(mapping)
df['StajBizdeYaptimi?'] = df['StajBizdeYaptimi?'].map(mapping)
edu_mapping = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Egitim Seviyesi'] = df['Egitim Seviyesi'].map(edu_mapping)

# Bağımsız değişkenler (X) ve bağımlı değişken (y) ayırma
y = df['IseAlindi']
X = df.drop(['IseAlindi'], axis=1)

# Karar ağacı modelini oluştur ve eğit
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Tahminler yapma
print("Tahminler:")
print("5 yıl deneyimli, hazırda bir yerde çalışan ve 3 eski şirkette çalışmış olan, eğitim seviyesi Lisans, top-tier-school mezunu değil:")
print(clf.predict([[5, 1, 3, 0, 0, 0]]))
print("Toplam 2 yıllık iş deneyimi, 7 kez iş değiştirmiş çok iyi bir okul mezunu şuan çalışmıyor:")
print(clf.predict([[2, 0, 7, 0, 1, 0]]))
print("Toplam 2 yıllık iş deneyimi, 7 kez iş değiştirmiş çok iyi bir okul mezunu değil şuan çalışıyor:")
print(clf.predict([[2, 1, 7, 0, 0, 0]]))
print("Toplam 20 yıllık iş deneyimi, 5 kez iş değiştirmiş iyi bir okul mezunu şuan çalışmıyor:")
print(clf.predict([[20, 0, 5, 1, 1, 1]]))

# Random Forest kullanarak tahmin yapma
rnd_fr_clf = RandomForestClassifier(n_estimators=20)
rnd_fr_clf = rnd_fr_clf.fit(X, y)
print("Random Forest Tahminleri:")
print("İşsiz bir 10 yıllık veteran:")
print(rnd_fr_clf.predict([[10, 0, 4, 0, 0, 0]]))
print("Çalışan bir 10 yıllık veteran:")
print(rnd_fr_clf.predict([[10, 1, 4, 0, 0, 0]]))
