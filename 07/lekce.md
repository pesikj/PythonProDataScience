

```py

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

data = pandas.read_csv("clean_train.csv")

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

## Cvičení

### Rozšíření modelu

Přidej do regresního modelu plochu garáže (`GarageArea`). Přidání provedeš tím, že ve svém programu upravíš řádek `formula` přidáním ` + GarageArea`. Jak se změnil koeficient determinace modelu?

Dále můžeš přidat plochu pozemku (`LotArea`) a rok, kdy byl dům naposledy rekonstruován (`YearRemodAdd`). Jaký je výsledný index determinace?

