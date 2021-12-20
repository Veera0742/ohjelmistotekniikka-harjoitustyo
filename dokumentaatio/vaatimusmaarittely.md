# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on helpottaa esimerkiksi perheen tai työyhteisön kommunikointia kaupasta ostettavien tuotteiden muistamiseksi. Sovelluksella voi olla useita käyttäjiä, jotka näkevät kaikille yhteisen ostoslistan. Sovellukseen voi myös kirjoittaa viestejä muille käyttäjille.

## Käyttäjät

Sovelluksessa on vain yhdenlaisia käyttäjiä, jotka kaikki voivat lukea, lisätä ja poistaa tuotteita ostoslistalta sekä lukea, lisätä ja poistaa viestejä viestitaululta.

## Käyttöliittymä

Sovellus koostuu kolmesta eri näkymästä:
- Kirjautumisnäkymä
- Uuden käyttäjän luomisnäkymä 
- Ostoslistanäkymä

Kun sovellus aukeaa, avautuu ensimmäisenä kirjautumisnäkymä, josta voi siirtyä joko ostoslistanäkymään olemassaolevilla tunnuksilla tai uuden käyttäjän luomisnäkymään, ja sitä kautta siirtyä ostoslistanäkymään.

## Toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda itselleen käyttäjätunnuksen ja salasana
	- Käyttäjätunnus ei saa olla käytössä kenelläkään muulla käyttäjällä, muuten järjestelmä antaa virheilmoituksen
	- Käyttäjätunnus pitää olla 3-15 merkkiä pitkä, muuten järjestelmä antaa virheilmoituksen
	- Salasanan tulee olla 8-20 merkkiä pitkä ja se pitää toistaa kaksi kertaa samanlaisena, muuten järjestelmä antaa virheilmoituksen
- Käyttäjä voi kirjautua sisään sovellukseen
	- Kirjautuminen tehdään kirjautumisnäkymässä jo luodulla käyttäjätunnuksella
	- Jos käyttäjää ei ole vielä luotu, järjestelmä antaa virheilmoituksen
	
### Kirjautumisen jälkeen

-  Käyttäjä voi luoda uuden tuotteen ostoslistalle sekä lisätä tuotteiden määrän listalle
	- Tämän jälkeen käyttäjälle näkyy listalla tuotteen lisääjä, tuotteen nimi sekä määrä
-  Käyttäjä voi poistaa tuotteen ostoslistalta 
-  Käyttäjä voi poistaa kaikki tuotteet listalta samalla kertaa
-  Käyttäjä voi kirjoittaa viestin muille käyttäjille 
	- Tämän jälkeen käyttäjälle näkyy listalla viestin kirjoittaja sekä viesti
-  Käyttäjä voi poistaa luetun viestin 
-  Käyttäjälle näkyy erilaisia virheilmoituksia, jos lisätyt tiedot ovat vääränlaisia
-  Käyttäjä voi kirjautua ulos järjestelmästä, jolloin näkymäksi palautuu kirjautumisnäkymä

## Jatkokehitysideat

- Sovellusta voi myös laajentaa muihin tehtäviin
- Viesteihin voisi lisätä päivämäärän ja kellonajan, milloin viesti on kirjoitettu
- Poistettujen tuotteiden tarkastelu
- Poistettujen tuotteiden ja viestien palautus
- Mahdollisuus tuotteiden määrien muuttamiseen
- Yksityisten tuotteiden lisääminen, jotka näkee vain tietty käyttäjä
- Yksityisten viestien lähettäminen muille käyttäjille