# Odevzdávání úkolů

## Založení repozitáře

Pro založení repozistáře je nutná registrace na serveru [Github.com](https://github.com/). Registraci provedeš kliknutím na tlačítko Sign up na titulní stránce. Poté následuje klasický formulář se zadáním e-mailu, hesla atd.

Po registraci a přihlášení je třeba vytvořit nový repizitář. To provedeš kliknutím na tlačítko `New` v levém sloupci. Poté vyplň název repozitáře (např. `python-042023`) a vyber, zda má být adresář veřejný (Public, viditelný všem) nebo soukromý (Private, viditelný pouze pro lidi, které do něj přidáš).

![](images/0a.png)

## Přidání kouče/koučky do repozitáře

Přidání provedeš tak, že si otevřeš svůj repozitář na GitHubu, klikneš na `Settings`, poté na `Manage access` a tam na tlačítko `Invite a collaborator`.

![](images/0.png)

Otevře se okno, do kterého zadej e-mail nebo přihlašovací jmého konkrétního kouče nebo lektora.

![](images/0b.png)

## Klonování repositáře

Zkopíruj si adresu repositáře. Tu najdeš po otevření repozitáře. V závislosti na tom, jestli je repositář prázdný, získat adresu buť na titulní stránce nebo po kliknutí na zelené tlačítko Code.

![](images/1a.png)

![](images/1b.png)

Otevři si terminál a v nějaké adresáři, kde chceš mít ukoly umístěné, zadej příkaz `git clone X`, kde `X` nahraď adresou respositáře.

Poté si adresář otevři ve Visual Studio Code.

## Nahrání úkolu na GitHub

Vytvoř si nový adresář s číslem úkolu (např. `Ukol1`).

Vytvoř si soubor pro uložení ukolu (např. `ukol.py`).

![](images/2.png)

V nově otevřeném editoru napiš program. Až budeš s úkolem spokojený(á), můžeš ho nahrát na GitHub. Nejprve klikni na ikonku `Source Control` vlevo. Poté myší najeď k nápisu `Changes`. Objeví se ikona `+`, na kterou klikneš. Tím přidáš soubory do `Staged Changes`, tj. mezi soubory, které jsou určené k nahrání na Git.

![](images/3.png)

Poté zadej nějakou zprávu od okna `Message` (např. `Odevzdávám první úkol`) a klikni na tlačítko `Commit`.

![](images/4.png)

Poté můžeš kliknout `Sync Changes`, alternativně (např. pokud vidíš nějakou chybovou zprávu) můžeš kliknout na ikonu tří teček a poté vyber možnost `Push`.

![](images/5a.png)

![](images/5b.png)

Poté vytvoř nové Issue ve svém repozitáři. Do názvu zadej název úkolu a v textu napiš přezdívku tvého kouče/koučky se zavináčem. Tím zajistíš, že kouč/koučka bude informován o založení issue e-mailem. Dále můžeš využít možnost `Assignees` a vybrat svého kouče/koučku. Pokud svého kouče/koučku nevidíš, je potřeba jej přidat do repozitáře, viz postup v podkapitole **Přidání kouče/koučky do repozitáře**.

![](images/6.png)

## Zadání úkolů

### Úkol 1

V souboru s daty na Slacku máš data o hodnotách finančních indikátorů 100 největších společností obchodovaných na americké burze. Naším cílem je zjistit, které indikátory nejvíce ovlivňují cenu, a vytvořit model, který odhadne cenu akcie na základě hodnot finančních indikátorů.

Jeden z indikátorů je označený jako *Y* a je poměrem ceny a účetní hodnoty akcie. Hodnota indikátoru je odrazem ceny akcie. Ostatní indikátory jso následující:

* běžná likvidita (Current Ratio, *CR*),
* zadluženost (Debt to Assets, *DA*),
* finanční páka (Financial Leverage, *FL*)
* provozní zisková marže (Operating Profit Margin, *OPM*),
* obrat pohledávek (Receivables Turnover, *RT*),
* obrat celkových aktiv (Total Assets Turnover, *TAT*).

- Úkol můžeš odevzdat jako Jupyter notebook.
- Nenahrávej prosím datový soubor na GitHub (neobsahuje veřejně dostupná data). Ze stejného důvodu jsou data anonymizovaná, tj. není v nich obsažen konkrétní název firmy.

#### Část 1

- Vytvoř korelační matici a podívej se, který ukazatel má největší vliv na indikátor *Y* akcie.

#### Část 2

- Vytvoř regresní model, který bude mít koeficient *Y* jako vysvětlovanou proměnnou. Do modelu vlož hodnoty ostatních indikátorů jako vysvětlující proměnné.
- S využitím modulu `statsmodels` vytvoř regresní model a zobraz si tabulku se souhrnem významů. Podívej se na hodnoty koeficientů a na výsledky testu statistické významnosti koeficientů. Pokud je některý koeficient (nebo více koeficientů) nevýznamný, sestav nový model bez tohoto koeficientů (případně beze všech nevýznamných koeficientů).
- Pro všechna data odhadni ukazatel *Y* s využitím tvého modelu a odhadnuté ceny vlož do původní tabulky s daty. Dále vypočítej rozdíl mezi odhadem koeficientu a jeho skutečnou hodnotou. Najdi akcii, kde je tento rozdíl největší (tj. hledáme akcii, které náš model predikuje výrazně vyšší cenu než jaká je ve skutečnosti, tato akcie je potenciálně na trhu podhodnocená).
- **Bonus 1:** Sestav model s využitím robustní regrese. Opět proveď vyřazení koeficinetů, které nejsou statisticky významné, a sestav model pouze s významnými koeficienty. Vlož odhady cen do původních dat a opět najdi potenciálně nejvíce podhodnocenou akcii. Jde v případě robustní regese o stejnou akcii, nebo se akcie liší?
- **Bonus 2:** Použij původní (tedy "nerobustní") model a vyčísli Cookovu vzdálenost pro všechny hodnoty. Vyřaď všechny akcie s Cookovou vzdáleností vyšší než 1 a přepočítej regresní model. Nakonec opět najdi potenciálně nejvíce podhodnocenou akcii a podívej se, jestli jde o stejnou akcii jako u předchozích modelů.
- **Bonus 3:** Přidej Sektor (poslední sloupec) jako vysvětlující proměnnou s využitím One Hot Encoding. Podívej se, které sektory mají kladný koeficient a které sektory mají záporný koeficient.


### Úkol 2

Ve strojovém učení často pracujeme i s jinými než textovými daty, například s obrázky. Práci s obrázky si vyzkoušíš v tomto úkolu. Jedním z nejznámějších datasetů je [MNIST](https://en.wikipedia.org/wiki/MNIST_database), který obsahuje obrázky rukou psaných číslic. K obrázkou jsou k dispozici i *labels*, tj. čísla, která na obrázku jsou. Tento dataset je přímo součástí modulu `scikitlearn`, a to ve formě číselné matice. Obrázky mají nízké rozlišení (8x8 pixelů, tj. každý obrázek se skládá 64 "políček" - 8 políček v 8 řádích, kterým lze přiřadit barvu) a je černobílý.

Tvým úkolem bude vytvořit model, který dokáže rozpoznat, jaké číslo je na každém z obrázků, přičemž využijeme algoritmus Support Vector Machine (SVM). Dataset si můžeš načíst s využitím následujícího kódu. Kód uloží data, která chceme zpracovat, do proměnné `data`. Čísla, která na obrázích skutečně jsou (tj. správné odpovědi) jsou v proměnné `y`.

```py
import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()
y = digits.target
data = digits.images
```

Níže je například matice, která reprezentuje první (v řeči Pythonu nultý) obrázek. Čím vyšší číslo je, tím tmavší je políčko. Čísla jsou v rozsahu 0 až 15.

```py
array([[ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.],
       [ 0.,  0., 13., 15., 10., 15.,  5.,  0.],
       [ 0.,  3., 15.,  2.,  0., 11.,  8.,  0.],
       [ 0.,  4., 12.,  0.,  0.,  8.,  8.,  0.],
       [ 0.,  5.,  8.,  0.,  0.,  9.,  8.,  0.],
       [ 0.,  4., 11.,  0.,  1., 12.,  7.,  0.],
       [ 0.,  2., 14.,  5., 10., 12.,  0.,  0.],
       [ 0.,  0.,  6., 13., 10.,  0.,  0.,  0.]])
```

Níže je obrázek, který je touto maticí reprezentován. Asi bychom ho odhadli jako 0, což je i správná odpověď.

![ukol_obrazky/ukol_2_obr_1.png](ukol_obrazky/ukol_2_obr_1.png)

Obrázek byl vytvořen pomocí modulu `matplotlib` a funkce `imshow`, která vykreslí číselnou matici jako obrázek. Pokud vybereme obrázek na pozici `0` a nastavíme černobílé barevné schéma (`cmap=plt.cm.gray_r`), získáme obrázek, který byl výše.

```py
plt.imshow(data[0], cmap=plt.cm.gray_r)
```

Správnou odpověď najdeme v poli `y` též na pozici 0.

```py
y[0]
```

Poslední krok je často označován převod dat na `flat`, tj. na plochá data. Nyní je totiž každé číslo reprezentováno dvourozměrnou maticí 8x8, ale pro použití algoritmu SVC potřebujeme, aby bylo každé číslo reprezentováno jednorozměrně. Můžeš si to představit tak, že chceme, aby každé číslo bylo reprezentováno jedním řádkem v tabulce, která má 64 sloupců.

Můžeme si to ukázat na číslu, které jsme si prohlíželi. Níže je číslo převedené do jednorozměrné formy. Když si čísla porovnáš s předchozím zápisem formou matice, uvidíš stejná čísla, ale pouze jeden pár hranatých závorek. To značí, že jde o jednorozměrné pole, tj. všechna čísla jsou v jednom řádku.

```py
array([ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.,  0.,  0., 13., 15., 10., 15.,  5.,  0.,  0.,  3., 15.,  2.,  0., 11.,  8.,  0.,  0.,  4., 12.,  0.,  0.,  8.,  8.,  0.,  0.,  5.,  8.,  0.,  0.,  9.,  8., 0.,  0.,  4., 11.,  0.,  1., 12.,  7.,  0.,  0.,  2., 14.,  5., 10., 12.,  0.,  0.,  0.,  0.,  6., 13., 10.,  0.,  0.,  0.])
```

Tento převod byl proveden pomocí metody `reshape(-1)`, které jsme dali parametr `-1`, což vede k tomu, že výsledkem je jednorozměrné pole.

```py
data[0].reshape(-1)
```

My ale potřebujeme převést všechna čísla, to uděláme příkazem níže. Hodnotou na nulté pozici seznamu říkáme, kolik máme v našem souboru pozorování, takže metoda `reshape()` vytvoří samostatný řádek každému z čísel.

```py
n_samples = len(data)
data = data.reshape([n_samples, -1])
```

Nyní je již řada na tobě. Napiš kód, kterým vytvoříš model, který bude klasifikovat obrázek do správné skupiny. Kód je velice blízký tomu, který jsme používali v lekci. Jinými slovy, stačí ti podívat se to materiálů k lekci, není potřeba nic Googlit nebo používat ChatGPT. Ale zakázané to samozřejmě není.

- Rozděl data na testovací a trénovací pomocí metody `train_test_split`, přičemž nastav parametry `test_size=0.3` a `random_state=42`. Použij stejné názvy proměnných, jaké jsme používali v lekci, tj. `X_train`, `X_test`, `y_train`, `y_test`.
- Použij klasifikátor `SVC` a jako `kernel` použij `linear`. Parametr `decision_function_shape` nenastavuj a využij výchozí hodnotu, tj. `ovo`. Nenastavuj ani žádné další parametry.
- Natrénuj model s využitím metody `fit()` a nakonec metodou `predict()` vytvoř pole predikcí pro testovací data, které pojmenuj `y_pred`.
- Zjisti hodnotu metriky accuracy (měla by ti vyjít přibližně `0.9796`) a matici záměn.

![ukol_obrazky/ukol_2_obr_2.png](ukol_obrazky/ukol_2_obr_2.png)

#### Nepovinný bonus

Algoritmus u některých obrázků nefungoval, určitě bude zajímavé si tyto obrázky prohlédnout. K tomu je potřeba doplnit následující kód, který vlož do svého programu. Na místa označená 1 a 2 je potřeba doplnit kód. Pokud vše doplníš správně, vytvoří ti program několik obrázků, které obsahují špatně predikované obrázky.

```py
for i in range(0, len(y_pred)):
    # 1 Napiš podmínku, která porovná predikovanou hodnotu pro i-tý obrázek a skutečnou hodnotu pro i-tý obrázek
    if :
        image = # 2 sem dej načtení i-tého obrázku z proměnné X_test
        # Obrázek převedeme zpět na matici 8x8
        image = image.reshape(8, 8)
        # Příkaz na zobrazení obrázku
        plt.imshow(image, cmap=plt.cm.gray_r)
        # Grafu dáme titulek, který porovnává predikovanou a skutečnou hodnotu
        plt.title(f'Predicted: {y_pred[i]}, Actual: {y_test[i]}')
        # Obrázek uložíme do souboru
        plt.savefig(f"{i}.png")
```

Níže je příklad jednoho z nich. Například toto bychom na 9 netipli asi ani my...

![ukol_obrazky/11.png](ukol_obrazky/11.png)
