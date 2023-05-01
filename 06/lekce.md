# Lekce 6

## Distribuční funkce a rozdělení

Uvažujme nyní, že bychom namísto sloupců použili čárový graf. Na osu *y* grafu pak nedáme absolutní počet hodnot v daném intervalu, ale relativní počet hodnot. Takový graf označujeme jako graf **funkce hustoty**. Pokud bychom nyní chtěli vědět, jaká část dat se nachází v nějakém intervalu, zjistili bychom to podle **plochy** pod křivkou.

K vytvoření grafu použijeme metodu `.plot.kde()`. Zkrakta KDE označuje *kernel density estimation*, tj. jádrový odhad hustoty. Musíme totiž myslet na to, že nemáme kompletní data, ale pouze jejich část, proto je naše funkce pouze odhadem funkce hustoty kompletních dat.

![](images/hustota.png)

```py
data["SalePrice"].plot.kde()
plt.show()
```

Pokud máme funkci hustoty, je to nejlepší možný popis jakýchkoli dat. Postupem času bylo zjištěno, že hustoty mnohých dat mají podobný tvar. Například níže máme čtyři funkce, které jsou sice různé (mají různě vysoké maximum a jsou různé "roztažené"), ale tvar mají podobný. Všechny čtyři hustoty mají stejné tzv. **statistické rozdělení**. To znamená, že všechny čtyři hustoty lze popsat stejnou matematickou funkcí, která se liší pouze proměnnými (konkrétně průměrem a rozptylem). Statistické rozdělení těchto hustot označujeme jako **normální (Gaussovo) rozdělení**.

![](https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg)

Normální rozdělení má spousta "jevů", které se vyskytují v přírodě, například délka, výška nebo hmotnost živé tkáně, krevní tlak lidí atd. Používá se také ve financích na oceňování opcí (např. v Black–Scholesově modelu). Normální rozdělení mají často i chyby měření při experimentech.

Vedle normálního rozdělení existuje spousta dalších. Jedním z nich je například exponenciální rozdělení. Exponenciální rozdělení často má délka intervalu mezi dvěma náhodnými událostmi, například příchozími telefonáty v call centru, nebo čas rozpadu radioaktivní částice.

![](https://upload.wikimedia.org/wikipedia/commons/0/02/Exponential_probability_density.svg)

Rovnoměrné rozdělení má pro každé dva stejně široké intervaly stejnou pravděpodobnost, jeho hustota je konstantní funkce. Pro rovnoměrné rozdělení uvažujeme krajní hodnoty *a* a *b*, mimo tyto krajní hodnoty je pravděpodobnost 0.

![](https://upload.wikimedia.org/wikipedia/commons/9/96/Uniform_Distribution_PDF_SVG.svg)

Rovnoměrné rozdělení existuje ve verzi pro celá i desetinná čísla, pro celá čísla bychom neměli graf hustoty čárový graf, ale graf by se skládal z "teček". Rovnoměrné rozdělení mají (resp. by měly mít) jevy, které souvisí s hazardními hrami. U hracích kostek či rulety by měla být pravděpodobnost padnutí každého z čísel stejná.

![](images/Uniform_discrete_pmf_svg.svg)


## Testování hypotéz

Hypotézou obecně myslíme nějaké tvrzení. Testování hypotéz se zabývá ověřením, zda je nějaká hypotéza platná. Při testování hypotéz předpokládáme, že máme k dispozici nějaký vzorek dat, nikoli kompletní data. To vnáší prvek určité nejistoty.

Vraťme se k prvnímu příkladu - srovnávní voleb a předvolebního průzkumu. Uvažujme tvrzení, že má různou podporu voličů v Praze než v Brně. Pokud se díváme na skutečný výsledek voleb, jasně vidíme, kolik strana ve volbách získala v obou městech. Pokud provádíme předvolební průzkum, pracujeme s nějakým vzorkem (výběrem) z populace, který má např. 500 lidí v obou městech. To přináší do našeho zkoumání nejistotu. Může se například stát, že jsme (čistě náhodou) do našeho průzkumu v jednom městě vybrali lidi, kteří mají danou stranu více rádi, než zbytek města.

Uvažujme například následující výsledky:

- V Praze podporuje danou stranu 40 % lidí a v Brně pouze 5 %. V takovém případě bychom se asi intuitivně shodli, že podpora v Praze je vyšší.
- V Praze podporuje danou stranu 10 % lidí a v Brně 50 %. V takovém případě bychom se asi intuitivně shodli, že podpora v Brně je vyšší.
- V Praze podporuje danou stranu 26 % lidí a v Brně 25 %. Zde už výsledek není jednoznačně, protože rozdíl je opravdu malý. Znamená 1 procentní bod rozdílu v našem průzkumu opravdu, že se podpora voličů liší? Co když se nám pouze náhodou do našeho vzorku v Praze dostalo více podporovatelů dané strany.

Právě na posledním příkladě se ukazuje, proč je testování hypotéz užitečné. Nedokáže sice jednoznačně říct, zda je hypotéza pravdivá, může nám ale říct, s jakou pravděpodobností je pravdivá nebo s jako pravděpodobností se mýlíme.

Vrátíme-li se k našemu souboru o cenách domů. Náš datový soubor určitě neobsahuje informace o všech domech v USA, ale pouze o některých, tj. o nějakém výběru domů. Pokud bychom tedy chtěli ověřit nějaká tvrzení o všech domech, opět se dostaneme do roviny testování hypotéz.

- Domy s bazénem jsou v průměru dražší než domy bez bazénu.
- Cena domu je ovlivněna jeho obytnou plochou.
- Ceny domu ve středně hustě zalidněných oblastech jsou méně různorodé než ceny domů ve velmi hustě zalidněných oblastech.
- Průměrná cena pozemků je různá pro různé typy umístění pozemku v zástavbě.

Testování hypotéz má pevný postup, který se skládá z následujících kroků:

* Formulace statistických hypotéz.
* Výběr vhodného testu.
* Výpočet hodnoty testového kritéria.
* Rozhodnutí o platnosti nulové hypotézy.

### Formulace statistických hypotéz

Při testování hypotéz vždy nejprve definujeme dvě hypotézy - **nulovou** a **alternativní**. Tyto dvě hypotézy musí být vždy ve sporu, tj. nemůže nastat situace, že by byly obě pravdivé. Nulová hypotéza v sobě má často znaménko *rovná se*, alternativní pak mívá znaménko *nerovná se*, *větší než* nebo *menší než*. Dále můžeme v nulové hypotéze tvrdit, že mezi dvěma sloupci v tabulce není závislost, a alternativní hypotéza bude říkat, že závislost existuje.

Navažme na předchozí lekci, kde jsme měřili sílu statistické závislosti mezi cenou domu a obytnou plochou. Hodnotu korelačního koeficientu sice známe, ale ta nám toho sama o sobě tolik neřekne. Nyní budeme chtít ověřit, že je vliv velikosti obytné plochy na cenu domu **statisticky významný**, tj. rozhodneme, zda tento vliv není čistě náhodný. 

Uvažujme následující dvojici hypotéz:

- Nulová hypotéza: Obytná plocha domu a jeho cena jsou lineárně nezávislé.
- Alternativní hypotéza: Obytná plocha domu a jeho cena jsou lineárně závislé.

Je zřejmé, že obě hypotézy nemohou být pravidivé.

Poněkud nepříjemnou zprávou pro vás může být informace, že výsledek našeho testu může být chybný, a to i v případě, že jsme postuovali správně. Může se totiž stát, že prostě máme smůlu na náš vzorek, který nereprezentuje data úplně správně.

Při testování se můžeme dopustit 2 chyb, které jsou popsány v tabulce níže.

|   | Nulová hypotéze platí | Nulová hypotéza neplatí |
|---|---|---|
| **Nezamítáme nulovou hypotézu** | Správný výsledek | Chyba II. druhu |
| **Zamítáme nulovou hypotézu**  | Chyba I. druhu | Správný výsledek |

Při testování hypotéz si zpravidla vybíráme pravděpodobnost, s jakou se chceme dopustit chyby I. druhu. Pravděpodobnost chyby I. druhu označujeme jako **hladinu významnosti**.

### Výběr vhodného testu

Dále zvolíme vhodný test pro ověření naší hypotézy.
Statistických testů existuje obrovské množství a výběr toho správného závisí obecně na několika faktech:

- Počet souborů (skupin) dat, se kterými chceme v testu pracovat. V tomto konkrétním případě chceme pracovat se dvěma soubory, můžeme mít ale pouze jeden či naopak 3 a více.
- Statistický ukazatel nebo skutečnost, kterou chceme ověřit. Může to být například průměr, rozptyl nebo (jak je tomu v našem případě) statistická závislost.
- Předpoklady testu. Předpoklad je nějaká podmínka, která musí být splněna, aby test dával kvalitní výsledky. Mnoho testů má předpoklad statistického rozdělení dat. Často testy rozdělujeme na parametrické a neparametrické, kde neparametrické testy jsou testy s mírnějšími předpoklady.

Vraťme se k výběru korelačního koeficientu. Pandas ve výchozím nastavení používá tzv. Pearsonův korelační koeficient. Pokud bychom s jeho pomocí chtěli ověřit, zda je vliv jedné veličiny na druhou statisticky významný, je potřeba pamatovat na to, že test hypotézy o závislosti za pomocí Pearsonova korelačního koeficientu **předpokládá, že data mají normální rozdělení** (normalitu dat).

Pokud si nejsme jisti, zda je tento předpoklad splněn, můžeme opět použít testování hypotéz.

### Test normality dat

Začneme s testem cen domů. Testujeme-li normalitu dat, formulujeme hypotézy následujícím způsobem:

- Nulová hypotéza: Ceny domů v našem souboru mají normální rozdělení.
- Alternativní hypotéza: Ceny domů v našem souboru nemají normální rozdělení.

Pro ověření normality dat existuje řada testů. Oblíbený je například Shapiro-Wilk test, který je součástí modulu `scipy`. Pro provedení testu použijeme funkci `shapiro` z modulu `scipy`. Funkci předáváme data ve sloupci `SalePrice`.

```py
import pandas
from scipy import stats

data = pandas.read_csv("clean_train.csv")
res = stats.shapiro(data["SalePrice"])
print(res)
```

Funkce vrací tajemný výsledek

```
ShapiroResult(statistic=0.8918800354003906, pvalue=8.921436004661806e-31)
```

Co tato záhadná čísla znamenají?

- `statistics` je hodnota statistiky testu. Statistika testu je v podstatě matematický vzoreček. Každý statistický test má vlastní vzorek pro výpočet statistiky. V případě Mann-Whitney testu měří vzoreček, jak jsou hodnoty v datech odlišné od normálního rozdělení.
- `pvalue` (p-hodnota) se váže k hladině významnosti. p-hodnotu využijeme pro rozhodnutí o platnosti alternativní hypotézy.

Platí následující pravidla.

- Pokud je **p-hodnota větší než hladina významnosti, zamítáme nulovou hypotézu** (tj. platí alternativní hypotéza).
- Pokud je **p-hodnota menší než hladina významnosti, nezamítáme nulovou hypotézu.**

Pokud si zvolíme hladinu významnosti jako 5 %, což je nejčastější volba, můžeme zapsat pravidlo konkrétněji.

- Pokud je **p-hodnota > 0.05, zamítáme nulovou hypotézu** (tj. platí alternativní hypotéza).
- Pokud je **p-hodnota < 0.05, nezamítáme nulovou hypotézu.**

Na internetu lze nalézt obrovské množství vědeckých i méně vědeckých obrázků, které vám umožní si toto pravidlo zapamatovat.

![](images/p-value_meme.png)

V našem případě je p-hodnota `8.921436004661806e-31`. Pozor, velmi důležitý je závěr `e-31`. Číslo je ve skutečnosti velmi malé, prvních 30 čísel desetinné části jsou 0 a až poté přichází nějaká nenulová čísla. Hodnota je tedy rozhodně menší než 0.05, tím pádem nulovou hypotézu zamítáme a tvrdíme, že data o cenách domů nemají normální rozdělení.

### Test korelace

Vraťme se k testu korelace. Víme, že data o cenách domů nemají normální rozdělení, měli bychom tedy použít test založený na Spearmanově koeficientu nebo na Kendallově tau.

Využijme Spearmanův koeficient.

```py
res = stats.spearmanr(data["GrLivArea"], data["SalePrice"])
print(res)
```

Program vrátí výsledek

```
SpearmanrResult(correlation=0.7312378789702222, pvalue=7.801875110918258e-244)
```

Číslo je opět velmi malé a menší než 0.05, v tomto případě zamítáme nulovou hypotézu. Tento výsledek je pro nás příznivý. Prokázali jsme totiž závislost mezi cenou domu a jeho podlahovou plochou. Podlahová plocha domu je tedy důležitou informací pro jeho ocenění.

## Cvičení

### Plocha garáže

Na minulé lekci jsme řešili korelaci mezi plochou garáže (`GarageArea`) a cenou domu. Ověř nyní, zda je tato korelace statisticky významná.

- Nejprve sestav hypotézy (nulovou i alternativní).
- Již víme, že cena domu nemá normální rozdělení, nelze tedy použít test na základě Pearsonova korelačního koeficientu. Použij Spearmanův koeficient i Kendallovo tau pro ověření statistické významnosti lineární závislosti. Zjisti p-hodnoty obou testů. Jaké jsou p-hodnoty? Jsou výsledky obou testů v souladu? A zamítáme nulovou hypotézu?


## Doplňkový text: Přehled statistických testů v Pythonu

Tato část vám pomůže s výběrem vhodného testu pro vaše projekty.

### Testy s jedním statistickým souborem

Tyto testy porovnávají jeden statistický soubor (jeden sloupec tabulky) oproti nějaké skutečnosti.

#### Testy na průměr

Testy na průměr porovnávají průměr souboru dat s nějakou námi definovanou hodnotou. U testů na průměr můžeme alternativní hypotézu formulovat pomocí znaménka není rovno, menší než nebo větší než.

Níže jsou příklady dvojic hypotéz.

* H0: Průměrná výška basketbalistek v České republice je 180 cm
* H1: Průměrná výška basketbalistek v České republice je více než 180 cm

* H0: Průměrná chyba při výrobě součástky do motoru je 0.1 mm
* H1: Průměrná chyba při výrobě součástky do motoru je méně než 0.1 mm

* H0: Průměrné zpoždění vlaku z Prahy do Plzně s odjezdem v 18:38 je 5 minut
* H1: Průměrné zpoždění vlaku z Prahy do Plzně s odjezdem v 18:38 není 5 minut (tj. je méně nebo více než 5 minut)

Pro test hypotézy můžeme využít následující testy:

* [t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html#scipy.stats.ttest_1samp), který předpokládá, že data mají normální rozdělení.

#### Testy na rozdělení

Příklad hypotéz:

* H0: Ceny domů mají normální rozdělení
* H1: Ceny domů nemají normální rozdělení

Pro test hypotézy můžeme využít následující testy:

* [Shapiro-Wilk test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html#scipy.stats.shapiro)
* Kombinace D'Agostinova and Pearsonova testu, který provádí funkce [normaltest](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html#scipy.stats.normaltest).

Pokud v hypotéze potřebujeme ověřit, zda data mají nějaké jiné rozdělení, můžeme použít [Kolmogorov-Smirnov test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html#scipy.stats.kstest).

### Testy se dvěma statistickými soubory

Tyto testy porovnávají dva různé statistické soubory.

#### Testy na průměr

U testu na průměr máme k dispozici poměrně hodně testů.

Uvažujme nejprve párová pozorování. Párovými pozorování myslíme, že pro každému pozorování z jednoho souboru můžeme přiřadit jiné pozorování podle nějakého logického klíče. Například uvažujme školení pracovníků pracující u výrobní linky. Pokud máme data o rychlosti montáže pracovníků před školením a po školení, můžeme použít párování, protože rychlost před školením a po školení pro jednoho pracovníka tvoří párové pozorování. Pokud bychom chtěli porovnat rychlost pracovníků v jiných směnách nebo jiných závodech, nejedná se o párová pozorování.

Příklad hypotéz:

* H0: Rychlost montáže pracovníků po školení je stejná jako před školením
* H1: Rychlost montáže pracovníků po školení je vyšší než před školením

Pro test hypotézy můžeme použít [párový t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html#scipy.stats.ttest_rel). Test předpokládá, že data mají normální rozdělení.

Pro nepárové testy můžeme mít následující hypotézy:

* H0: Rychlost montáže pracovníků v obou sledovaných směnách je stejná
* H1: Rychlost montáže pracovníků v obou sledovaných směnách je různá

Pro test hypotézy můžeme použít [t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind). Test předpokládám, že data mají normálhní rozdělení. U testu existují dvě varianty - jedna předpokládá, že data mají stejný rozptyl, druhá uvažuje, že soubory mají různé rozptyly.

#### Testy na rozdělení

Testy na rozdělení umožňují porovnat, zda mají dva statistické soubory stejné rozdělení, tj. zda mají stejnou distrubuční funkci. Opět rozlišujeme párový a nepárový test.

Pro párový test můžeme formulovat hypotézy:

* H0: Rozdělení rychlosti montáže pracovníků po školení je stejná jako před školením
* H1: Rozdělení rychlosti montáže pracovníků po školení je jiná než před školením

Pro test můžeme použít [Wilcoxonův test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html#scipy.stats.wilcoxon). Test je neparametrický, tj. nevyžaduje normální rozdělení.

Pro nepárová pozorování můžeme formulovat hypotézy:

* H0: Rozdělení rychlosti montáže v obou sledovaných směnách je stejná
* H1: Rozdělení rychlosti montáže v obou sledovaných směnách je různá

Pro otestování můžeme použít [Mann–Whitney test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html#scipy.stats.mannwhitneyu).

#### Testy závislosti kategoriálních dat

Kategoriální data jsou taková, která obecně není číslo, ale text (v řeči programování řetězec). Kategoriální proměnnou tedy může být oblíbený programovací jazyk, předmět na škole, nápoj, nejvyšší dosažené vzdělání, zda je člověk kuřák atd. Kategoriální proměnné můžeme porovnat mezi sebou a rozhodnout, zda je mezi nimi závislost.

Hypotézy mohou být například následující:

* H0: Oblíbený předmět nezávisí na pohlaví
* H1: Oblíbený předmět závisí na pohlaví

Pro test hypotézy můžeme použít [chí-kvadrát test nezávislosti](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html). Test je založený na použití kontingenční (pivot) tabulky.

#### Test statistické významnosti korelace

Test řeší, zda je zjištěná korelace statisticky významná. 

Uvažujme následující hypotézy:

H0: Cena domu a obytná plocha domu nejsou statisticky závislé
H1: Cena domu a obytná plocha domu jsou statisticky závislé


Pokud mají data normální rozdělení, lze využít test založený na [Pearsonově korelačním koeficientu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html#scipy.stats.pearsonr). Pokud data nemají normální rozdělení, můžeme využít test s využitím [Spearmanova koeficientu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr) nebo [Kendallova tau](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html#scipy.stats.kendalltau).

### Testy se třemi a více statistickými soubory

#### Test na průměr

Test na průměr umožňuje porovnat, zda jsou průměry hodnot různé u tří a více souborů.

Pro test můžeme formulovat hypotézy:

* H0: Průměrný čas montáže je stejný u pracovníků všech tří směn
* H1: Průměrný čas montáže různý alespoň dvě směny

Uvažujme, že máme ranní, odpolední a noční směnu. Test nám pouze řekne, zda je mezi směnami nějaký rozdíl, ale nevíme přesně jaký. Může tedy být například stejný průměr ranní a odpolední směny a noční se od nich liší, může být stejný průměr ranní a noční směny a odpolední se od nich liší nebo může mít každá směna průměr odlišný od ostatních.

Pokud mají všechny soubory normální rozdělení, můžeme použít [ANOVA test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html#scipy.stats.f_oneway). Pokud data nemají normální rozdělení, je možné využít neparametrický [Kruskall-Wallis test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html#scipy.stats.kruskal).
