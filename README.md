# Ułamki

Napisz klasę reprezentującą ułamek zwykły. Musi ona nazywać się `Fraction` i posiadać następujące właściwości:

- zdefiniowane cztery podstawowe operatory matematyczne (`+`, `-`, `*`, `/`);

- elegancka konwersja na ciąg znaków w postaci „3/2”;

- skracania i porządkowanie w konstruktorze:
  - licznik i mianownik podzielone przez ich największy wspólny dzielnik,
  - sprawdzenie, czy mianownik nie jest zerem (w takim przypadku należy zgłosić `ValueError`),
  - znak znajduje się w liczniku (mianownik jest zawsze dodatni),
  - oba atrybuty muszą być liczbami całkowitymi (`TypeError` jeśli nie są) - aby to sprawdzić można użyć funkcji Pythona `type` lub `isinstance`.;

- metoda `decimal` zwracająca wartość dziesiętną ułamka (licznik podzielony przez mianownik).
