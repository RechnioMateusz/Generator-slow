# **Generator słów**
__ __ __ __ __
__ __ __ __ __
### **Funkcjonalność**
__ __ __ __ __
Generator słów wykorzystujący teorię ciągów Markov'a
Program wykonuje następujące kroki:
* Import listy słów lub uprzednio zapisanej macierzy zależności
* Stworzenie macierzy zależności między kolejnymi literami na podstawie listy słów
* Generowanie słów
* Aktualizacja macierzy zależności
* Eksport macierzy do zewnętrznego pliku

### **Instalacja i uruchamianie (_windows_)**
__ __ __ __ __
Program jest napisany w języku [_Python ver. 3.6.5_](https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe).
Aby uruchomić program należy w konsoli przejść do folderu w którym zapisane są pliki źródłowe i użyć komendy:
- `python.py IWG.py`

### **Instrukcja użytkowania**
__ __ __ __ __
Po uruchomieniu programu należy wybrać rodzaj ładowanych danych. Następnie należy podać ścieżkę do odpowiedniego pliku

![loading](https://github.com/RechnioMateusz/Generator-slow/blob/master/READMEimages/loading.jpg)

Po załadowaniu danych można wybrać:

![menu](https://github.com/RechnioMateusz/Generator-slow/blob/master/READMEimages/menu.jpg)

* Po wybraniu "_a_" program przełączy się do menu generowania słów
* Po wybraniu "_b_" program wyświetli macierz zależności
* Po wybraniu "_s_" program wyeksportuje macierz do pliku zewnętrznego
* Po wybraniu "_x_" program zakończy działanie

Po przełączeniu się do menu generowania słów należy podać długość maksymalnego generowanego słowa. Wygenerowane zostanie słowo i będzie można wybrać:

* Po wybraniu "_y_" program aktualizuje macierz zależności
* Po wybraniu "_c_" program pozwala na poprawienie wygenerowanego słowa a następnie aktualizuje macierz zależności
* Po wybraniu "_x_" program powraca do menu

![generating](https://github.com/RechnioMateusz/Generator-slow/blob/master/READMEimages/generating.jpg)

### **Zasada działania**
__ __ __ __ __
Program importując listę słów tworzy na ich podstawie macierz zależności między literami.
Załóżmy, że program następującą listę:
* pies
* puszka
* sok

Po odczytaniu słowa _pies_ program stworzy następującą macierz:

| **•** | **ε** | **p** | **i** | **e** | **s** |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **ε** | 0     | 1     | 0     | 0     | 0     |
| **p** | 0     | 0     | 1     | 0     | 0     |
| **i** | 0     | 0     | 0     | 1     | 0     |
| **e** | 0     | 0     | 0     | 0     | 1     |
| **s** | 0     | 0     | 0     | 0     | 0     |

ε - znak pusty od którego zaczyna się każde słowo
W wierszu **p** są same zera oprócz przecięcia z kolumną **i**. Jest tak dlatego, ponieważ w słowie _pies_ po _p_ występuje _i_.

Po odczytaniu słowa _kot_ program zaktualizuje macierz do postaci:

| **•** | **ε** | **p** | **i** | **e** | **s** | **u** | **z** | **k** | **a** |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **ε** | 0     | 2     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| **p** | 0     | 0     | 1     | 0     | 0     | 1     | 0     | 0     | 0     |
| **i** | 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     | 0     |
| **e** | 0     | 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     |
| **s** | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 0     | 0     |
| **u** | 0     | 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     |
| **z** | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 0     |
| **k** | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 1     |
| **a** | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |

Następnie odczytywane jest kolejne słowo itd. aż do zakończenia listy.
Dodatkowo zliczane jest wystąpienie każdej litery aby możliwe było policzenie prawdopodobieństwa przejścia z jednej litery w drugą ([łańcuchy Markov'a](https://en.wikipedia.org/wiki/Markov_chain))

__ __ __ __ __

W momencie generowania słowa o maksymalnej długości _max_ losowana jest liczba od 0 do ilości wystąpień litery w liście słów. W pierwszym kroku wybrany zostaje wiersz _ε_ a następnie od wylosowanej liczby odejmowane są wartości kolejnych kolumn. Jeśli wylosowana liczba po odjęciu wartości z kolumny **_x_** będzie ujemna, do _ε_ zostaje doklejona litera **_x_**. Teraz program przechodzi do wiersza **_x_** i powtarza operację aż do osiągnięcia _max_ iteracji lub niemożności dalszego wyboru litery (kiedy suma wartości wiersza jest równa _0_)

### **Licencja**
__ __ __ __ __
>**_MIT License_**
>
>_Copyright (c) 2018 Mateusz Rechnio_
>
>_Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:_
>
>_The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software._
>
>_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE._

### **Przewidywane zmiany i rozwój**
Program ten jest eksperymentem z zastosowaniem łancuchów Markov'a. Nie jest pewne czy projekt będzie się rozwijał, jeśli tak to:
* Dodany zostanie interfejs graficzny z graficznym przedstawieniem grafu zależności zbudowanego na podstawie macierzy zależności
* System wyboru kolejnej litery zostanie rozbudowany o zależności sięgające głębiej niż o jedną literę wstecz
