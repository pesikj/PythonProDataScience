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
