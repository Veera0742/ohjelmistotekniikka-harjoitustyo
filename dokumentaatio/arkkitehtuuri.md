# Arkkitehtuurikuvaus

## Rakenne

Ohjelmassa on neljä eri tyyppistä pakkausta:
- Pakkaus *ui* vastaa käyttöliittymästä
- Pakkaus *services* sovelluslogiikasta
- Pakkaus *entities* tietokohteista 
- Pakkaus *repositories* tiedon tallennuksesta

## Käyttöliittymä

Sovelluksen käyttöliittymässä on kolme näkymää:

- Kirjautuminen *(login_view)*
- Uuden käyttäjän luominen *(create_user_view)*
- Ostoslistan näyttäminen *(shopping_list_view)*

Jokainen ylläolevista näkymistä on oma luokkansa ja käyttöliittymä on eriytetty sovelluslogiikasta. 

## Sovelluslogiikka

Sovelluksen sovelluslogiikassa on kolme luokkaa, jotka kuvaavat käyttäjiä, tuotteita sekä viestejä.

Sovelluksen toiminnasta vastaa luokka *ShopService*, joka vastaa myös käyttöliittymän toimintaan liittyvistä metodeista. 

*ShopService* saa käyttäjiin liittyvät tallennetut tiedot *repositories* pakkauksesta ja siellä sijaitsevista tietokannan tallennuksesta vastaavista luokista *ItemRepository* sekä *MessageRepository*.

Ohjelman luokkien suhteita kuvaa alla oleva luokkakaavio:

![Luokkakaavio](/dokumentaatio/kuvat/luokkakaavio.png)

## Tietojen tallennus

Pakkauksessa *repositories* sijaitsevat luokat *UserRepository*, *ItemRepository* ja *MessageRepository*. 
Kaikki nämä luokat tallentavat datan SQLite-tietokantaan. 

## Päätoiminnallisuudet

Alla on kuvattu sovelluksen toimintalogiikka päätoiminnallisuuksien osalta. Sekvenssikaaviot selkeyttävät toiminnan kuvaamista

### Sisäänkirjautuminen

Ohjelman avautuessa käyttäjälle avautuu *login_view* näkymä ja käyttäjä voi kirjautua sisään olemassaolevilla käyttäjätunnuksilla. Alla on kuvattu sovelluksen kontrolli käyttäjätunnuksen ja salasanan kirjoittamisen sekä *"kirjaudu sisään"*- napin painamisen jälkeen:

![Sekvenssikaavio_login](/dokumentaatio/kuvat/sekvenssikaavio_login.png)

### Uuden käyttäjän luominen

Jos käyttäjällä ei ole luotu käyttäjätunnusta, *login_view*-näkymästä voi valita "Luo uusi käyttäjä"-napin. Alla on kuvattu sovelluksen kontrolli käyttäjätunnuksen ja salasanan kirjoittamisen jälkeen ja napin painamisen jälkeen:

![Sekvenssikaavio_create_user](/dokumentaatio/kuvat/sekvenssikaavio_create_user.png)

### Uuden tuotteen tai viestin lisääminen

Uuden tuotteen tai viestin lisääminen tapahtuvat samalla periaatteella. *Shopping_list_view*-näkymässä voi lisätä uuden tuotteen/viestin, valita määrän ja painaa "Lisää uusi tuote"/"Lähetä viesti" näppäintä. Alla on kuvattu uuden tuotteen lisääminen, viestin lisääminen toimii samalla periaattella, paitsi kappalemäärää ei ole: 

![Sekvenssikaavio_create_item](/dokumentaatio/kuvat/sekvenssikaavio_create_item.png)