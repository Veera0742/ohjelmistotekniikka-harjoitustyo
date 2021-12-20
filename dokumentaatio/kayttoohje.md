# Käyttöohje

Viimeisimmän releasen lähdekoodin löydät etusivulla olevan *"loppupalautus release"*-linkin kautta. Lataa se *Assets*-osion alta kohdasta *Source code*.

## Konfigurointi

Tallennukseen käytettävät tiedoston nimet löytyvät *.env*-tiedostosta, josta niitä voi halutessaan myös muokata. Tiedostot luodaan *data*-hakemistoon. 

## Ohjelman käynnistäminen

Asenna riippuvuudet komennolla:

> poetry install

Suorita alustustoimenpiteet komennolla:

> poetry run invoke build

Ohjelman voi käynnistää komennolla:

> poetry run invoke start

## Kirjautuminen

Sovellus aukeaa näkymään, jossa käyttäjä voi joko kirjautua sisään olemassaolevilla käyttäjätunnuksella tai valita *"Luo uusi käyttäjä"*-napin, jos käyttäjätunnuksia ei ole vielä olemassa.

## Uuden käyttäjän luominen

Uuden käyttäjän luominen onnistuu lisäämällä *"käyttäjätunnus"* kohtaan uniikki käyttäjätunnus, joka on 3-15 merkkiä pitkä. Sen jälkeen syötetään valittu salasana kaksi kertaa *"salasana"*-kohtiin. Salasanan täytyy olla sama kummassakin kohdassa sekä 8-20 merkkiä pitkä. Sen jälkeen painetaan *"Luo uusi käyttäjä"* -nappia.

Kirjautumisen jälkeen avautuu näkymä, jossa käyttäjä näkee Ostoslistalle lisättyjä tuotteita sekä viestejä ja mahdollisuuden lisätä uusia.

## Tuotteiden lisääminen ja poistaminen

Käyttäjä voi lisätä uusia tuotteita näkymässä olevan tekstikentän kautta. Tuotteen nimen lisäksi täytyy määrittää kappalemäärä. Näiden tietojen lisäyksen jälkeen, käyttäjä voi painaa *"Lisää uusi tuote"* - näppäintä, jolloin tuote lisätään näkymässä olevalle listalle. 
 
Näkymässä käyttäjä näkee omat ja muiden lisäämät tuotteet listana. Näiden lisäksi käyttäjä näkee myös tuotteen lisääjän käyttäjätunnuksen sekä napin *"Poista tuote listalta"*, jolla tuote voidaan poistaa näkymästä.

Jos käyttäjä on ostanut kaikki tuotteet listalta, voi myös painaa nappia *"Poista kaikki tuotteet"*, jolloin koko lista tyhjentyy

## Viestien lisääminen ja poistaminen

Käyttäjä voi lisätä uusia viestejä näkymässä olevan tekstikentän kautta. Viestin lisäämiseksi käyttäjä kirjoittaa viestin kenttään, jonka jälkeen painaa *"Lähetä viesti"*- nappia. Näin viesti lisätään näkymässä olevalle listalle. 

Näkymässä käyttäjä näkee tuotteiden lisäksi myös omat ja muiden lisäämät viestit listana. Käyttäjä näkee myös viestin lisääjän käyttäjätunnuksen sekä napin *"Luettu"*, jolla viesti voidaan poistaa näkymästä.

## Ulos kirjautuminen

Käyttäjä voi kirjautua ulos painamalla *"Kirjaudu ulos"*-nappia, jolloin käyttäjä kirjataan ulos sekä ohjelma palaa kirjautumisnäkymään.