# Cvičení

import pandas
import requests
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

# V tomto cvičení zkus naimplementovat klasifikátor, který rozpozná pozitivní recenzi produktu od
# negativní. Takové úloze se občas říká _sentiment analysis_.

# Pracuj se souborem `reviews.csv`. Soubor obsahuje text recenze, a výstupní proměnnou `label` se
# dvěma hodnotami, `neg` a `pos`. Můžeš si všimnout, že data už nějakým čištěním prošla. Porovnej
# alespoň dva algoritmy. Jaké je nejlepší f1-score, kterého jsi dosáhl/a?
r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/reviews.csv"
)
open("reviews.csv", "wb").write(r.content)

data = pandas.read_csv("reviews.csv")

X = data["review"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

vectorizer = TfidfVectorizer(ngram_range=(1, 2))

X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

classifier = LinearSVC(random_state=0)

classifier.fit(X_train_transformed, y_train)

y_pred = classifier.predict(X_test_transformed)

print(
    f"accuracy: {round(accuracy_score(y_test, y_pred), 2)}",
    f"f1 score: {round(f1_score(y_test, y_pred, average='weighted'), 2)}",
)

### Dobrovolný doplněk

# Identifikuj ty recenze, které tvůj model označil špatně. Na pár z nich se podívej, a zkus odvodit,
# proč model chyboval.
df = pandas.DataFrame({"text": X_test, "true": y_test, "pred": y_pred}).reset_index(
    drop=True
)

misclassified = df[df["true"] != df["pred"]]

print(misclassified.loc[1489].to_list())
