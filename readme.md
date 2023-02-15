# Teemu Kalmari Taso 3

# Luokat
Tieto = auttaa lisäämään käyttäjän nimet kayttaja pöytään perinnän avulla
Kayttaja = sisältää funktiot kayttaja pöydän luomiselle ja muokkaamiselle
Tavara = sisältää funktiot Tavarat pöydän luomiselle ja muokkaamiselle
kayttajanTavara = sisältää funktiot kayttajan_tavarat pöydän luomiselle ja lisäämisen kayttaja ja Tavara pöydästä itseensä
Otsikko = sisältää alku otsikon ja on abstracti
Otsikko1 = sisältää loppu tervehdyksen ja tässä tulee Polymorfismi
siirto = liittyy Otsikko1 toiminnallisuuteen
Valikko = Tässä on kaikki ohjelman valikot nidottu yhteeen ja käytössä on monin perintä kayttajanTavara,Tavara,Kayttaja,Otsikko luokista
Main = tässä on pää ohjelma ja tässäkin tapahtuu monin perintää Valikko ja Otsikko1 luokista
# Methodit
## Kayttaja luokkassa.
taulu luo kayttajat pöydän jos sitä ei ole
haeKanta tulostaa kayttajat pöydän
salasana näyttää kayttajan salasanan
linkita lisää kayttajat pöytään kirjoitetut käyttäjät ja niiden tiimit
etsiTiimi etsii kirjoitetun käyttäjän tiimin
vaihdaTiimi vaihtaa halutun käyttäjän tiimin
poista poistaa halutun käyttäjän

## Tavara luokkassa.
tavarat luo tavarat pöydän jos sitä ei ole
tavaraLista kirjoittaa pöydän sisään ohjeenannon mukaiset tavarat
tavaraTaytto antaa käyttäjälle vaihto ehdon muuttaa tavaran arvoa
haeTavarat tulostaa tavarat pöydän
poistaTavarat poistaa tavarat pöydän

## KayttajanTavara luokkassa.
kayttajaTavara luo kayttajan_Tavara pöydän jos sitä ei ole
lisaaTavara antaa halutulle käyttäjälle halutun tavaran
naytaKayttajanTavara näyttää käyttäjien tavarat
poistaa kayttajan_Tavara pöydän

## Otsikko,Otsikko1,siirto luokat.
Toimii alku otsikon ja loppuhyvästien tulostamiseen
Otsikko on abstracti 
Otsikko1 ja siirto luokissa toimii Polymorfismi

## Valikko luokkassa.
Tässä on kaikki valikko funktiot joiden nimet on valikko,valikko2,valikko3,valikko4
Tässä luokassa toimii monin perintä kayttajanTavara,Tavara,Kayttaja,Otsikko luokista

sitten on yksi ali ohjelma jossa luodaan yhteys sqlite3

## Main luokkassa.
Tässä luokassa on ensin haetaan tarpeelliset funktiot jotta luodaan pöydät tarvittaessa jonka jälkeen avataan valikko
tässä tapahtuu moniperintää valikko ja Otsikko1 luokista
