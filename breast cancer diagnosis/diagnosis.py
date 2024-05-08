import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Veri setini yükleme
url = r"C:\Users\cengh\DeepLearningandMachineLearning-\breast cancer diagnosis\breastcancer.csv"
data = pd.read_csv(url)

# Hedef değişken ve özellikler arasında ayırma
X = data.drop(['id', 'diagnosis'], axis=1)  # 'id' ve 'diagnosis' sütunlarını çıkar
y = data['diagnosis']  # Hedef değişken

# Eksik değerleri doldurma ve model oluşturma
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('classifier', HistGradientBoostingClassifier(random_state=42))
])

# Eğitim ve test setlerine ayırma ve modeli eğitme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Modeli değerlendirme
accuracy = pipeline.score(X_test, y_test)
print("Test Accuracy:", accuracy)
