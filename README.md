# Program na kompilaci plantuml

## Instalace

Program se může rovněž spustit příkazem ``python3 pyuml.py``

### Linux

 - stáhnutí projektu
 - nastavení správného interpretru
    - pomocí příkazu ``which python3``
    - Přímo z pythonu 
        - ``import os``
        - ``os.environ["_"]``
 - nastavení cesty 
    - ``vim ~/.bashrc``
    - přidání řádku ``export PATh=$PATH:/cesta/do/vaseho/adresare/kde/je/script``
 - nastavení prostředí ``source ~/.bashrc``

## Argumenty programu

### Pozicové

Na první pozici se zadává název souboru ke kompilaci, nebo se může zadat ``.`` (tečka) pro kompilaci všech souborů v aktuálním adresáři s koncovkou ``.plantuml``