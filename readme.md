# Classes:
#### Tieto = helps to add user names to the user table using inheritance
#### Kayttaja = contains functions for creating and modifying the user table
#### Tavara = contains functions for creating and modifying the item table
#### kayttajanTavara = contains functions for creating the user_items table and adding items from the user and item tables to it
#### Otsikko = contains the beginning title and is abstract
#### Otsikko1 = contains the ending greeting and exhibits Polymorphism
#### siirto = related to the functionality of Otsikko1
#### Valikko = here all program menus are linked together and multiple inheritance is used from the Kayttaja, Tavara, kayttajanTavara, and Otsikko classes
#### Main = contains the main program where multiple inheritance from Valikko and Otsikko1 classes occurs
# Methods:
## In the Kayttaja class
table creates the user table if it does not exist
haeKanta prints the user table
salasana displays the user's password
linkita adds the users and their teams written in the user table
etsiTiimi finds the team of the written user
vaihdaTiimi changes the team of the desired user
poista deletes the desired user

## In the Tavara class:
tavarat creates the item table if it does not exist
tavaraLista writes the items according to the instructions in the table
tavaraTaytto allows the user to change the value of an item
haeTavarat prints the item table
poistaTavarat deletes the item table

## In the kayttajanTavara class:
kayttajaTavara creates the user_items table if it does not exist
lisaaTavara adds the desired item to the desired user
naytaKayttajanTavara displays the items of the users
poistaa deletes the user_items table

## In the Otsikko, Otsikko1, and siirto classes:
Used to print the beginning title and ending greetings
Otsikko is abstract
Otsikko1 and siirto classes exhibit Polymorphism

## In the Valikko class:
Contains all menu functions with names valikko, valikko2, valikko3, valikko4
Multiple inheritance from the Kayttaja, Tavara, kayttajanTavara, and Otsikko classes occurs in this class

There is also a subprogram that creates a connection to sqlite3.

## In the Main class:
First, necessary functions are called to create tables if needed, and then the menu is opened.
Multiple inheritance from the Valikko and Otsikko1 classes occurs in this class.
