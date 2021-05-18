 <b>Link do repozytorium:</b>
https://github.com/MikolajMichalczak/cashier-simulator-project-python

<b>Opis projektu:</b>

Okno podzielone jest na dwie czesci:

  - Lewa: pusta, pojawiaja sie tam towary do skasowania

- Prawa: przyciski od 0 do 9, przycisk "backspace", przycisk ‘Wyczysć",
przycisk “Zważ” oraz pole tekstowe - wciskanie przycisków cyfr powoduje
dopisywanie ich do pola, backspace wymazuje ostatnio wpisana cyfre,
przycisk “Wyczysć" czysci pole tekstowe.
Jeśli zawartosć pola tekstowego to 1 i wciśniety został przycisk cyfry,
pole tekstowe jest czyszczone i dopisywana jest tam wybrana cyfra.

Na poczatku po lewej stronie znajduje się przycisk “Następny klient”, wciśniecie
go rozpoczyna grę (zapisanie aktualnego czasu i wyzerowanie licznika towarów)

W losowym miejscu lewej strony okna pojawia sie przycisk z:

- nazwą towaru i jego liczebnoscią, np. “Arbuz x10". Wciśnięcie przycisku
powoduje zmniejszenie liczebności towaru o tyle, ile wpisane jest w polu
tekstowym po prawej stronie, a pole to jest czyszczone (zawartosć ustawiana
na 1) lub

- nazwa towaru z napisem “?kg” oznaczającym, że jest to towar do zważenia.
Jego kasowanie polega na kliknięciu przycisku z towarem, następnie kliknięciu
przycisku “Zważ", a następnie ponownym kliknięciu przycisku z towarem. Po
naciśnięciu przycisku “Zważ" etykieta towaru powinna się zmienić (ma być
podana losowa waga od 0.05 do 2 kg).

Jeśli wartość pola tekstowego po prawej stronie przewyższa liczebnosć towaru, to gracz przegrywa i wyświetlane jest okno informujące o tym.

Po skasowaniu towaru (liczebność spadła do 0), do licznika towarów dodawana jest oryginalna liczebność towaru, oraz generowany jest kolejny towar.

Generowane jest od 10 do 20 towarów, połowa z nich na sztuki. Liczba sztuk ma wynosić od 1 do 50 (losowo). 
Prawdopodobieństwo wylosowania liczebności 1 (pojedynczy artykuł) ma wynosić 50%.

Po skasowaniu wszystkich towarów wyświetlany jest średni czas kasowania jednego przedmiotu (towar w liczebności 10 liczy sie za 10 przedmiotów).

Nazwy towarów maja być losowane z minimum dwudziestoelementowej listy.

Towary maja być reprezentowane przez obiekty TowarNaSztuki i TowarNaWage dziedziczących po klasie Towar. 
W obiektach ma być przechowywana nazwa towaru, liczba sztuk lub waga, czas pojawienia sie w lewej części okna i czas skasowania.

<b>Testy:</b>

1. Skasowanie towaru na sztuki po klikając na niego kilka razy.
2. Skasowanie towaru na sztuki wpisując jego liczność i klikając raz. Wymagane
jest resetowanie pola do wartosci 1.
3. Próba skasowania towaru na sztuki wpisując zbyt dużą liczność
(oczekiwana informacja o przegranej).
4. Próba zważenia towaru na sztuki (oczekiwana informacja o przegranej).
5. Próba skasowania towaru na wagę jakby był towarem na sztuki (oczekiwana informacja o przegranej).
6. Skasowanie wszystkich towarów (oczekiwane okno z podsumowaniem symulacji).
7. Pokazanie, ze liczebność 1 występuje odpowiednio czesto.
