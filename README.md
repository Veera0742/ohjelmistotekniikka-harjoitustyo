# Ostoslista (Ohjelmistotekniikka, harjoitustyö)

Sovelluksen tarkoitus on helpottaa esimerkiksi perheen tai työyhteisön kommunikointia kaupasta ostettavien tuotteiden muistamiseksi. Sovelluksella voi myös kirjoittaa viestejä muille käyttäjille ostoslistaan liittyen.

Sovellus on testattu Python versiolla 3.8.

## Dokumentaatio

[Loppupalautus release](https://github.com/Veera0742/ohjelmistotekniikka-harjoitustyo/releases/tag/loppupalautus)

[Vaatimusmäärittely](https://github.com/Veera0742/ohjelmistotekniikka-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/Veera0742/ohjelmistotekniikka-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/Veera0742/ohjelmistotekniikka-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/Veera0742/ohjelmistotekniikka-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/Veera0742/ohjelmistotekniikka-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Asennus

1. Asenna riippuvuudet komennolla:

> poetry install

2. Suorita alustustoimenpiteet komennolla:

> poetry run invoke build

3. Käynnistä komennolla:

> poetry run invoke start

## Komentorivitoiminnot

**Ohjelman suorittaminen**

Ohjelman pystyy suorittamaan komennolla:

> poetry run invoke start

**Testaus**

Testit suoritetaan komennolla:

> poetry run invoke test

**Testikattavuus**

Testikattavuusraportin voi luoda komennolla:

> poetry run invoke coverage-report

**Pylint**

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

> poetry run invoke lint

 

