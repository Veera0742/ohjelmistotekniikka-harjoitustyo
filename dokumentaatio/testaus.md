# Testausdokumentti

Ohjelmaa on testattu unittestillä yksikkö- ja integraatiotestein, sekä manuaalisesti. 

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

*ShopService*-luokkaa, joka vastaa sovelluslogiikasta, testataan *TestShopService*-testiluokalla. Jotta testeissä ei käytettäisi pysyväistallennusta, testeihin on luotu luokat *FakeUserRepository*, *FakeItemRepository* sekä *FakeMessageRepository* tiedon tallennukseen testien aikana.

### Repositiot

Repositio-luokkia *UserRepository*, *ItemRepository* ja *MessageRepository* testataan *TestUsers*, *TestItems* ja *TestMessages* - luokilla.

### Testikattavuus

Sovelluksen testauksen haaraumakattavuus on 88%.

Raportin saa luotua komennolla:

> poetry run invoke coverage-report

Raportti luodaan *htmlcov*-hakemistoon.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti

### Asennus ja konfigurointi

Sovellus on käynnistetty käyttöohjeiden mukaan ja sitä on käytetty Window- ja Linux ympäristöissä.

### Toiminnallisuudet

Kaikki määrittelydokumentissa ja käyttöohjeessa mainitut toiminnallisuudet on käyty läpi. Sovelluksessa on myös testattu laajasti mahdolliset virheelliset syötteet ja niiden tuottamat virheilmoitukset.

## Sovellukseen jääneet laatuongelmat

- Sovellus ei anna virheilmoitusta kun tuotteen määrä ei ole numero.