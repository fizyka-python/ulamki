"""
Plik ten zawiera definicję klasy reprezentującej ułamek zwykły.

Tutaj musi znajdować się klasa reprezentująca ułamek zwykły. Musi ona
nazywać się `Fraction` i posiadać następujące właściwości:

- zdefiniowane cztery podstawowe operatory matematyczne;
- elegancka konwersja na ciąg znaków w postaci „3/2”;
- skracania i porządkowanie w konstruktorze: licznik i mianownik podzielone
  przez ich największy wspólny dzielnik, sprawdzenie, czy mianownik nie jest
  zerem (w takim przypadku należy zgłosić `ValueError`), znak w liczniku,
  oba atrybuty liczbami całkowitymi (`TypeError` jeśli nie są);
- metoda `decimal` zwracająca wartość dziesiętną ułamka (licznik podzielony przez mianownik).
"""
from math import gcd


class Fraction:
    """
    Klasa reprezentująca ułamek zwykły.
    """

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom
