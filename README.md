# Python 2

* Informace o kurzu [na webu Czechitas](https://www.czechitas.cz/kurzy/python-2).
* Návod na odevzdávání úkolů na GitHub je [zde](ukoly.md).

| Týden | Blok | Téma                                                            | Odkaz                   | 
|------:|---|--------------------------------------------------------------------|-------------------------|
|    1. | Pandas a vizualizace  | Running total, duplicity                       | [odkaz](01/lekce.ipynb) | 
|    2. | Pandas a vizualizace  | Pivot tabulky                                  | [odkaz](02/lekce.ipynb) |
|    3. | Pandas a vizualizace  | Práce s datem a časem, funkce shift            | [odkaz](03/lekce.ipynb) |
|    4. | Pandas a vizualizace  | Použití vlastních funkcí                       | [odkaz](04/lekce.ipynb) |
|    5. | Statistické metody  | Popisná statistika                               | [odkaz](05/lekce.ipynb) |
|    6. | Statistické metody  | Testování statistických hypotéz                  | [odkaz](06/lekce.ipynb) |
|    7. | Statistické metody  | Korelace a regrese                               | [odkaz](07/lekce.ipynb) |
|    8. | Strojové učení a umělá inteligence  | Obecná technika strojového učení, binární klasifikace |    |
|    9. | Strojové učení a umělá inteligence  | Klasifikace do více tříd, grid search |                    |
|   10. | Strojové učení a umělá inteligence  | Rozhodovací stromy               |                         |
|   11. | Strojové učení a umělá inteligence  | Clustering                       |                         |
|   12. | Strojové učení a umělá inteligence  | NLP                              |                         |



## Podmínky absolvování kurzu

- Účast na lekcích (min. 80 %)
- Odevzdání domácích úkolů:
  * Úkol z bloku *pandas a vizualizace*.
  * Jeden ze dvou úkolů z bloku *statistické metody* (bude zadán po 7. lekci, na zpracování budou dva týdny).
  * Jeden ze dvou úkolů z bloku *strojové učení a umělá inteligence* (bude zadán po 10. lekci, na zpracování budou dva týdny).

## Zadání úkolů

- [Úkol č. 1](domaci_ukoly/01.ipynb) (povinný, je nutné jej zpracovat do **12. května 2023**)
- [Úkol č. 2](domaci_ukoly/02.ipynb) (povinný, je nutné jej zpracovat do **9. června 2023**)
- [Úkol č. 3](domaci_ukoly/03.ipynb) (povinný, je nutné jej zpracovat do **9. června 2023**)

Pro získání certifikátu je nutné zpracovat minimálně tři úkoly:

- úkol 1,
- úkol 2 nebo úkol 3 (je samozřejmě možné zpracovat oba),
- úkol 4 nebo úkol 5 (je samozřejmě možné zpracovat oba).

## Další zdroje

- [Mapping with Matplotlib, Pandas, Geopandas and Basemap in Python
](https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac)
Mapa světa, lze použít např. pro analýzu tržeb firmy.
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) 
- [Visualization and Interactive Dashboard in Python
](https://towardsdatascience.com/visualization-and-interactive-dashboard-in-python-c2f2a88b2ba3)

### Pandas a vizualizace

Příklady:

- Délka po sobě jdoucích událostí pomocí shift.
- Kontrola následující události pomocí shift.
- Výpadky televizního signálu a jejich slučování.

Tipy na vizualizace:
- [Hat graph](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html#sphx-glr-gallery-lines-bars-and-markers-hat-graph-py),
- [Discrete distribution as horizontal bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html#sphx-glr-gallery-lines-bars-and-markers-horizontal-barchart-distribution-py),
- [Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-gallery-lines-bars-and-markers-scatter-hist-py),
- [Scatter Masked](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_masked.html#sphx-glr-gallery-lines-bars-and-markers-scatter-masked-py),
- [hlines and vlines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html#sphx-glr-gallery-lines-bars-and-markers-vline-hline-demo-py),
- [Creating annotated heatmaps](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py),
- [Box plots with custom fill colors](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py),
- [Time Series Histogram](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html#sphx-glr-gallery-statistics-time-series-histogram-py),
- [Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html#sphx-glr-gallery-pie-and-polar-charts-nested-pie-py.)

Seaborn:
- [Violin plot](https://seaborn.pydata.org/examples/grouped_violinplots.html)

### Statistické metody

- [Statistics Lecture](https://www.youtube.com/watch?v=9FtHB7V14Fo&list=PL5102DFDC6790F3D0) - Série přednášek o
  statistice a testování hypotéz. Sice v angličtině, ale v pomalém a klidném tempu.
- [StatistikaJednoduse.cz](https://statistikajednoduse.cz/) - Stránka s dalšími texty o statistice a příklady výpočtů
testu v Excelu.
- [p-values: What they are and how to interpret them](https://www.youtube.com/watch?v=vemZtEM63GY) - Vysvětlení
p-hodnoty na příkladu s porovnáním účinnosti léků.

### Strojové učení a umělá inteligence

- [Elements of AI](https://www.elementsofai.cz/) (CZ, EN) - Bezplatný online kurz, jehož cílem je 
demystifikovat umělou inteligenci. Kurz kombinuje teorii s cvičeními.
- [ML for Beginners](https://github.com/microsoft/ML-For-Beginners) (EN, ale aktivně překládaný do dalších jazyků dobrovolníky) -
Veřejně dostupný a bezplatný kurz klasického strojového učení od Microsoftu. Připravuje se i kurz "AI for Beginners" a již existuje 
["Data Science for Beginners"](https://github.com/microsoft/Data-Science-For-Beginners) 
- [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) (EN) - Článek o metodě t-SNE, jejích
parametrech a interpretaci. Článek doprovází spousta (interaktivních) vizualizací.
