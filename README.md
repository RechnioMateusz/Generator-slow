### **Generator słów**
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