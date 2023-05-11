
```py

```

Výsledek je následující (čísla se můžou mírně lišit):

```py
KendalltauResult(correlation=0.543863812013887, pvalue=1.995410251143093e-211)
```



```py

```

Funkce vrací tajemný výsledek

```
ShapiroResult(statistic=0.8918800354003906, pvalue=8.921436004661806e-31)
```





# Regrese

Samotná informace o tom, že existuje statisticky významný vztah mezi obytnou plochou domu a jeho cenou, sice může být zajímavá, ale můžeme zjistit více. K tomu můžeme využít regresi. Regrese je nástroj, který umí vztah mezi dvěma proměnnými popsat. Abychom si pod slovem "popsat" dokázali něco představit, využijeme graf. Využijeme opět modul `seaborn`, tentokrát vygenerujeme graf pomocí funkce `regplot()`. U regrese vždy rozlušujeme mezi **závislou** (**vysvětlovanou**) a **nezávislou** (**vysvětlující**) proměnnou. Závislou proměnnou umísťujeme na svislou osu (*y*) a nezávislou vodorovnou osu (*x*). V našem případě je nezávislou proměnnou obytná plocha domu a závislou proměnnou cena. Tvrdíme totiž, že obytná plocha domu ovlivňuje cenu, tj. cenu vysvětlujeme pomocí obytné plochy.

```py
import pandas
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv("house_prices.csv")
g = seaborn.regplot(x="GrLivArea", y="SalePrice", data=data, scatter_kws={"s": 1}, line_kws={"color":"r"})
plt.show()
```

Graf, který vygeneruje funkce `regplot()`, je podobný grafu vygenerovanému funkcí `plot_joint()`. Navíc je tam červená čára. Právě tato čára je popisem vztahu mezi obytnou plochou a cenou. Pokud bychom na základě obytné plochy chtěli odhadnout cenu domu, pro příslušnou obytnou plochu na ose *x* přečteme cenu na ose *y*.

![](images/regplot.png)

Pro reálné použití modelu je ale lepší využít modul `scipy`, který nám dá matematický popis dané funkce. Naší snahou je nyní odhadnout model, který lze matematicky zapsat jako:

*y = a + b \* x + e*

kde *y* je cena domu, *x* je obytná plocha a koeficienty *a* a *b* jsou ty, které se snažíme odhadnout. Koeficient *b* udává "strmost" regresní čáry, tj. říká, jak rychle roste cena domu s růstem jeho obytné plochy. Koeficient *a* pak říká, kde červená čára prochází osou *y*. Pokud by došlo ke změně ceny všech domů bez ohledu na obytnou plochu (např. v důsledku ekonomické krize), změnila by se hodnota koeficientu *a*.

```py
import pandas
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pandas.read_csv("house_prices.csv")

formula = "SalePrice ~ GrLivArea"
data = sm.add_constant(data)
mod = smf.ols(formula=formula, data=data)
res = mod.fit()
print(res.params)
```

Program provedl následující hodnoty koeficientu *a* (`Intercept`) a *b* (`GrLivArea`).

```
Intercept    12581.885623
GrLivArea      111.230746
dtype: float64
```

Regresní model máme, otázkou ale je, jak dobrý den model je? Jedním ze základních ukazatelů modelu je **koeficient determinace**. Ten říká, kolik procent rozptylu závislé proměnné jsme naším modelem vysvětlili.

```py
print(res.rsquared)
```

V našem případě je jeho hodnota 0.519, tj. vysvětlili jsme 51.9 % rozptylu ceny, což zatím není moc dobrý výsledek. Další rozšíření modelu vyzkoušíme při cvičení.

Model můžeme použít k odhadu ceny domu. Níže je příklad toho, jak odhadnout cenu domu pro domy s plochou 2000, 2500 a 2900.

```py
# Vytvořím si slovník, kde jsou data, která chci odhadnout
# Chci odhadnout 3 domy s plochou 2000, 2500 a 2900
domy_k_odhadu = {'GrLivArea': [2000, 2500, 2900]}
# Převedu slovník na pandas tabulku
domy_k_odhadu = pandas.DataFrame(domy_k_odhadu)
# Přidám konstantu, podobně jako u tabulky pro tvorbu modelu
domy_k_odhadu = sm.add_constant(domy_k_odhadu)
# Na základě modelu provedu odhad
odhady = res.predict(domy_k_odhadu)
# Vypíšu výsledek - např. odhadovaná cena domu s plochou 2000 je 235043.377438
print(odhady)
```

## Cvičení

### Rozšíření modelu

Přidej do regresního modelu plochu garáže (`GarageArea`). Přidání provedeš tím, že ve svém programu upravíš řádek `formula` přidáním ` + GarageArea`. Jak se změnil koeficient determinace modelu?

Dále můžeš přidat plochu pozemku (`LotArea`) a rok, kdy byl dům naposledy rekonstruován (`YearRemodAdd`). Jaký je výsledný index determinace?


