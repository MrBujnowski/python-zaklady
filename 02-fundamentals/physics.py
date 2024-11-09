'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''
import math

EARTH_GRAVITY = 9.80665        # normální pozemské tíhové zrychlení v m/s²
MOON_GRAVITY = 1.622           # měsíční gravitace v m/s²
SPEED_OF_LIGHT = 299792458     # rychlost světla ve vakuu v m/s
SPEED_OF_SOUND = 343           # rychlost zvuku při teplotě 20 °C v suchém vzduchu v m/s

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def light(distance_km):
    """Vypočítá čas, který světlo potřebuje k překonání dané vzdálenosti.

    Args:
        distance_km (float): Vzdálenost v kilometrech, kterou má světlo urazit.

    Returns:
        float: Čas v sekundách, který světlo potřebuje k překonání zadané vzdálenosti.
    """
    return distance_km * 1000 / SPEED_OF_LIGHT


def sound(distance_km):
    """Vypočítá čas, který zvuk potřebuje k překonání dané vzdálenosti.

    Args:
        distance_km (float): Vzdálenost v kilometrech, kterou má zvuk urazit.

    Returns:
        float: Čas v sekundách, který zvuk potřebuje k překonání zadané vzdálenosti.
    """
    return distance_km * 1000 / SPEED_OF_SOUND


def time_to_fall_earth(distance):
    """Vypočítá čas pádu objektu na Zemi z dané výšky.

    Args:
        distance (float): Výška v metrech, ze které objekt padá.

    Returns:
        float: Čas v sekundách, za který objekt dopadne na zem.
    """
    return math.sqrt(2 * distance / EARTH_GRAVITY)


def time_to_fall_moon(distance):
    """Vypočítá čas pádu objektu na Měsíci z dané výšky.

    Args:
        distance (float): Výška v metrech, ze které objekt padá.

    Returns:
        float: Čas v sekundách, za který objekt dopadne na Měsíc.
    """
    return math.sqrt(2 * distance / MOON_GRAVITY)



