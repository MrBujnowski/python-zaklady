'''
Importování modulů v Pythonu

Větší programy je žádoucí členit do samostatných modulů.
Modul je soubor obsahující definice a příkazy v Pythonu.
Moduly v Pythonu jsou uloženy v samostatných souborech s příponou .py.
Definice uvnitř modulů mohou být importovány do jiných modulů nebo do interaktivní pythonovské konzoly.
Připojení modulů provádíme klíčovým slovem import.
'''
import datetime
from turtledemo.clock import datum

'''
Příklad importu modulu math. V tomto případě můžeme pomocí tečkového operátoru využít všechny atributy a funkce,
které nám modul math nabízí.
'''
import math
print(math.pi)
print('Goniometrické funkce: sin 45° = {}, cos 45° = {}'.format(math.sin(45), math.cos(45)))

'''
Příklad importu modulu sys a jedné jeho funkce path. Použijeme k tomu konstrukci:
from jméno_modulu import jméno_funkce
'''

from sys import path
print(path) # Zobrazuje seznam (list) cest k adresářům, které aplikace využívá

'''
Moduly math a sys patří k interním modulům, jež jsou součástí standardní instalace Pythonu.
Externí moduly jsou distribuovány systémem balíčků (packages) a musí být instalovány pomocí nástroje pip.

pip install <jméno_balíčku>

Balíček můžeme odinstalovat příkazem:

pip uninstall <jméno_balíčku>

Používáme-li virtuální prostředí (virtual environment), jsou nainstalované balíčky ukládány v adresáři tohoto prostředí
(v našem případě venv) v podsložkách Lib a site-packages.

Přehled všech instalovaných balíčků získáme příkazem:

pip list

Můžeme také vytvořit soubor requirements.txt, který obsahuje záznam všech tzv. závislostí naší aplikace - čili 
informace o všech balíčcích, které je nutné do virtuálního prostředí nainstalovat, aby aplikace mohla fungovat.
Vytvoření souboru requirements.txt provedeme příkazem:

pip freeze > requirements.txt

Zobrazení podrobnějších informací o některém z nainstalovaných balíčků získáme příkazem:

pip show <jméno_balíčku>

Automatickou instalaci všech závislostí zaznamenaných v souboru requirements.txt provedeme příkazem:

pip install -r requirements.txt     
'''

# V konzoli virtuálního prostředí proveďte instalaci externího balíčku camelcase
# (venv) E:\python\projekt\venv>pip install camelcase
# Poté tento balíček importujte
import camelcase
c = camelcase.CamelCase() # Konstruktor třídy CamelCase() vytvoří objekt v proměnné c
txt = 'ahoj světáku'
print(c.hump(txt)) # Metoda hump() přeformátuje předaný řetězec podle zásad camel syntaxe (velká první písmena slov)

"""
Cvičení 4:

Použijte vhodné moduly v Pythonu (včetně jejich případné instalace) k tomu, abyste: 
1) vypsali aktuální datum a čas
2) vypsali datum velikonoční neděle (easter) v následujících 5 letech
3) vypsali nejbližší rok, v němž bude Štědrý den v neděli

K řešení prvního úkolu je možné doporučit importovat interní modul datetime
Řešení dalších dvou úkolů můžete odvodit z příkladů v dokumentaci k externímu modulu dateutil - viz https://pypi.org/project/python-dateutil/
"""

from dateutil.easter import *


# úkol 1.
# print(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

# úkol 2.
today = datetime.date.today()
for i in range(5):
    print(easter(today.year+i))

# úkol 3.

def next_christmas_sunday():
    year = datetime.datetime.now().year
    while True:
        christmas_date = datetime.date(year, 12, 24)
        if christmas_date.weekday() == 6:  # 6 značí neděli (pondělí je 0)
            return year
        year += 1

next_year = next_christmas_sunday()
print(f"Nejbližší rok, kdy bude Štědrý den v neděli, je {next_year}.")