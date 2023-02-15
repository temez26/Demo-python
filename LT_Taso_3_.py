##################################################
# Kurssi: AT00BT78-3005 Oliot ja tietokannat
# Ohjelmanimi: LT-Taso-3
# Tekijä: Teemu Kalmari
#
# Vakuutan, että tämä ohjelma on minun tekemä.
# Työhön olen käyttänyt seuraavia lähteitä, sekä
# saanut apua seuraavilta henkilöiltä:
# - Lähde X
# - Henkilö Y
##################################################
from pathlib import Path
from abc import ABC, abstractmethod
import sqlite3

DB_CONF = {"FILEPATH": Path().joinpath("./kanta.db")}
# Luokat 

#Linkittää datan syötön
class Tieto():
    try:
        
        def __init__(self, kayttaja, tiimi, rooli, salasana):
            self.kayttaja = str(kayttaja)
            self.tiimi = str(tiimi)
            self.rooli = str(rooli)
            self.salasana = str(salasana)
       
              
    except Exception as Virhe:
        print("Tietokanta virhe.")

#Yhdistää tietokannan ja aliohjelmat
class Kayttaja:
    # Luo taulun jos sitä ei ole
   
    def taulu(self):
        try:
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause = "CREATE TABLE IF NOT EXISTS kayttajat("
            sql_lause += "       nimi VARCHAR(15) primary key NOT NULL,"
            sql_lause += "       tiimi VARCHAR(10) NOT NULL,"
            sql_lause += "       rooli VARCHAR(10) NOT NULL, "
            sql_lause += "       salasana VARCHAR(10) NOT NULL "
            sql_lause += ");"
            kursori.execute(sql_lause)
            yhteys.close()

        except Exception as Virhe:
            print("tietokanta alustus virhe:" + str(Virhe))
        return None
    # Hakee taulun tiedot
   
    def haeKanta(self):
        try:
            print()
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            cur = yhteys.cursor()

            for row in cur.execute("SELECT * FROM kayttajat;"):

                print(f"| {row[0]:15} | {row[1]:15} | {row[2]:15} |")

        except Exception as Virhe:
            print("kantaa ei voitu hakea" + str(Virhe))
        return None

    def salasana(self):
        try:
            print()
            kayttaja = input("Syötä käyttäjä nimi: ")
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            cur = yhteys.cursor()

            for row in cur.execute('SELECT nimi,salasana FROM kayttajat where nimi = "' + str(kayttaja) + '";'):
                print()
                print(f"| {row[0]:15} | {row[1]:15} |")
            
        except Exception as Virhe:
            print("kantaa ei voitu hakea" + str(Virhe))
        return None

    # Lisää halutut käyttäjät
    def linkita(self):
    

          

        try:
            kayttaja = input("Anna käyttäjänimi: ")
            tiimi = input("\nAnna tiimin nimi: ")
            salasana = input("\nAnna salasana: ")

            rooli = "Pelaaja"
            data = Tieto(kayttaja, tiimi, rooli, salasana)
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause = "INSERT INTO kayttajat (nimi,tiimi,rooli,salasana) VALUES (?,?,?,?);"
            sql_data = [data.kayttaja, data.tiimi, data.rooli,data.salasana]
            
            kursori.execute(sql_lause, sql_data)
            yhteys.commit()

            yhteys.close()
            print()
        except Exception as Virhe:
            print("Kayttäjän vienti virhe:" + str(Virhe))
        return None
    # Etsii halutun käyttäjän tiimit
    
    def etsiTiimi(self):
        try:
            tiimi = input("\nSyötä tiimin nimi: ")
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            print()
            for row in kursori.execute(
                'SELECT * FROM kayttajat where tiimi ="' + str(tiimi) + '" ;'
            ):

                print(f"| {row[0]:10} | {row[1]:10} | {row[2]:10} |")

            yhteys.commit()
            yhteys.close()
        except Exception as Virhe:
            print("Tiimin etsintä epäonnistui. " + str(Virhe))
        return None
        
    # Vaihtaa käyttäjän tiimiä
    
    def vaihdaTiimi(self):
        try:
            kayttaja = input("\nSyötä käyttäjän nimi: ")
            tiimi = input("\nSyötä uuden tiimin nimi: ")

            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause = (
                "update kayttajat set tiimi ='"
                + str(tiimi)
                + "'  WHERE  nimi = '"
                + str(kayttaja)
                + "' ;"
            )

            kursori.execute(sql_lause)
            yhteys.commit()

            yhteys.close()
            print()
        except Exception as Virhe:
            print("Käyttäjän vienti virhe:" + str(Virhe))

        return None

    # Poistaa halutun käyttäjän
    
    def poista(self):
        try:
            kayttaja = input("\nSyötä poistettavan käyttäjän nimi: ")

            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause = "DELETE FROM kayttajat WHERE nimi='" + str(kayttaja) + "';"
            print()
            varmistus = input(
                "Oletko aivan varma, että haluat poistaa käyttäjän "
                + f'"{kayttaja}"'
                + " (K/E):"
            )

            if varmistus == "k" or varmistus == "K":
                kursori.execute(sql_lause)
                print()
                print("Käyttäjä " + f'"{kayttaja}"' " poistettu.")

            if varmistus == "e" or varmistus == "E":
                print()
                print("Käyttäjää ei poistettu.")
            yhteys.commit()
            yhteys.close()

        except Exception as Virhe:
            print("poisto epäonnistui" + str(Virhe))
        return None
#Tavara luokka        
class Tavara:
    # Luo tavarat taulun jos sitä ei ole
    
    def tavarat(self):

        try:
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause = "CREATE TABLE IF NOT EXISTS tavarat("
            sql_lause += "nimike VARCHAR(255) PRIMARY KEY NOT NULL,"
            sql_lause += "arvo DECIMAL(255)"
            sql_lause += ");"
            kursori.execute(sql_lause)
            yhteys.close()
            print()
            
        except Exception as Virhe:
            print("Tavara alustus virhe:" + str(Virhe))
        return None
    # Lisää tavarat tavarat tauluun
    
    def tavaraLista(self):
        try:

            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()
            sql_lause = "INSERT INTO tavarat (nimike,arvo) VALUES ('Kahvimuki','1'),('Haarniska','2304'),('Kala','14.45'),('Vasara','19.99'),('Tulitikut','0.25'),('Hammasharja','0.65'),('Miekka','3680'),('Taideteos','1840');"
            kursori.execute(sql_lause)
            yhteys.commit()
            yhteys.close()

        except Exception as Virhe:
            print("Tavara  virhe:" + str(Virhe))

        return None
        
    #Päivittää valitun tavaran tiedon
    
    def tavaraTaytto(self):
        try:
            tavara = input("\nAnna tuotteen nimi: ")

            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause1 = (
                "SELECT nimike FROM tavarat WHERE  nimike ='" + str(tavara) + "';"
            )
            sql_lause2 = (
                "SELECT arvo FROM tavarat WHERE  nimike ='" + str(tavara) + "';"
            )
            kursori.execute(sql_lause1)
            tulos = kursori.fetchall()
            kursori.execute(sql_lause2)
            tulos1 = kursori.fetchall()
            for row1 in tulos:

                for row in tulos1:
                    print("\nTuotteen ", f'"{row1[0]}"', "arvo on:", f"{row[0]}")

            arvo = int(input("Syötä uusi arvo: "))
            sql_lause = (
                "UPDATE tavarat SET arvo ='"
                + str(arvo)
                + "'  WHERE  nimike = '"
                + str(tavara)
                + "' ;"
            )
            kursori.execute(sql_lause)
            yhteys.commit()
            yhteys.close()
            print()
        except Exception as Virhe:
            print("Tavaran vienti virhe:" + str(Virhe))
        return None
        
    #Tulostaa tavara taulukon
    
    def haeTavarat(self):
        try:
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()
            print()
            for row in kursori.execute("SELECT nimike, arvo FROM tavarat"):

                print(f"| {row[0]:12} |          {row[1]:5}|")
            yhteys.commit()
            yhteys.close()
        except Exception as Virhe:
            print("kantaa ei voitu hakea" + str(Virhe))
        return None
    #Alustaa tavara taulukon
    
    def poistaTavarat(self):
        try:
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()
            kursori.execute("DELETE FROM tavarat;")
            yhteys.commit()
            yhteys.close()
        except Exception as Virhe:
            print("Tavaraa ei voitu poistaa "+str(Virhe))
            return None

        return None
#Käyttäjä_tavara luokka        
class kayttajanTavara:      

       
    #Luo käyttäjä tavara taulun    
    
    def kayttajaTavara(self):

        try:
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()  # kyselyiden hallinta kursori
            sql_lause = "CREATE TABLE IF NOT EXISTS Kayttaja_Tavara("
            sql_lause += "kayttaja TEXT,"
            sql_lause += "tavara TEXT"
            sql_lause += ");"
            kursori.execute(sql_lause)
            yhteys.close()
            print()
            
        except Exception as Virhe:
            print("Tavara alustus virhe:" + str(Virhe))
        return None  
    #lisää käyttäjälle tavaran     
    
    def lisaaTavara(self):
        try:
            kayttaja = input("Syötä käyttäjä: ")
            tavara = input("Syötä annettava tavara: ")
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()
            
            sql_lause2 = "INSERT INTO Kayttaja_Tavara SELECT nimi,nimike FROM kayttajat left join tavarat WHERE nimi ='" + str(kayttaja) + "' and nimike ='" + str(tavara) + "'   ;"
            kursori.execute(sql_lause2)
            yhteys.commit()
            
            yhteys.close()

        except Exception as Virhe:
            print("Tavaraa ei voitu lisätä "+str(Virhe))    
            return None
        return None
    #Näyttää käyttäjä_tavara taulun    
    
    def naytaKayttajanTavara(self):
        try:

            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()
            
            
            for row in kursori.execute("SELECT kayttaja, tavara FROM Kayttaja_Tavara"):

                print(f"| {row[0]:12} |          {row[1]:10}|")
            yhteys.commit()    
            yhteys.close()

        except Exception as Virhe:
            print("Taulua ei voinut tulostaa "+(Virhe))    
            return None
        return None  

    #Alustaaa käyttäjä tavara taulun    
     
    def poistaKayttajanTavarat(self):
        try:
            yhteys = Yhteys(DB_CONF["FILEPATH"])
            kursori = yhteys.cursor()
            
            kursori.execute("DELETE FROM Kayttaja_Tavara;")
            yhteys.commit()
            yhteys.close()
            
        except Exception as Virhe:
            print("Taulua ei voinut poistaa "+(Virhe))    
            return None
        return None
#Abstrakti
class Otsikko(ABC):
   @abstractmethod 
   def __init__(self, valinta):
    self.valinta = valinta
   def palauta(self):
       print(self.valinta)
#Näkemiin viesti Polymorfismi
class Otsikko1:
    def __init__(self,siirto):
        self.siirto = siirto
    def siirra(self):
        print(self.siirto)       
class siirto(Otsikko1):
    def __init__(self):
        super().__init__('nyt meni pieleen')   
    def siirra(self):
        print("Ensikertaan!")    
class Valikko(kayttajanTavara,Tavara,Kayttaja,Otsikko):

   def __init__(self):
             super().__init__("Tervetuloa pelisysteemiin")
   
         
#Käyttäjä_tavara valikko        
   
   def valikko4(self): 
    while True:
        try:
            print("\n2 Alavalikko:")
            print("1 - Näytä tavarat")
            print("2 - Näytä käyttäjät")
            print("3 - Valitse käyttäjä kenelle lisätään tavara")
            print("4 - Näytä käyttäjien tavarat")
            print("0 - Palaa edelliseen valikkoon")
            syote = input("Valintasi: ")
            valinta = int(syote)
           
        except Exception:
            valinta = -1
        if valinta == 1:
            self.haeTavarat()
        if valinta == 2:
            self.haeKanta()    
        if valinta == 3:
            self.lisaaTavara() 
        if valinta == 4:
            self.naytaKayttajanTavara()   
            
        if valinta == 0:
            print("Palataan edelliseen valikkoon.")
            break
   #Tavara valikko     
   def valikko3(self):

     while True:
        try:

            print("\nAlavalikko:")
            print("1 - Näytä tavarat")
            print("2 - Hinnoittele tavara uudelleen")
            print("0 - Palaa edelliseen valikkoon")
            syote = input("Valintasi: ")
            valinta = int(syote)
        except Exception:

            valinta = -1
        if valinta == 1:
            self.haeTavarat()
        if valinta == 2:
            self.tavaraTaytto()

        if valinta == 3:
            self.tavaraLista()
        if valinta == 0:
            print("\nPalataan edelliseen valikkoon.")
            print()
            break
   # käyttäjä valikko
   def valikko2(self):

    
    while True:
        try:
            print("\nAlavalikko:")
            print("1 - Lisää käyttäjä ")
            print("2 - Listaa käyttäjät")
            print("3 - Etsi kaikki tiimiin kuuluvat käyttäjät")
            print("4 - Muokkaa käyttäjän tiimiä")
            print("5 - Poista käyttäjä")
            print("6 - näytä käyttäjän salasana")
            print("0 - Palaa edelliseen valikkoon")
            syote = input("Valintasi: ")
            valinta = int(syote)
        except Exception:
            valinta = -1
        if valinta == 1:
            print()
            self.linkita()
        if valinta == 2:
            self.haeKanta()
        if valinta == 3:
            self.etsiTiimi()
        if valinta == 4:
            self.vaihdaTiimi()
        if valinta == 5:
            self.poista()
        if valinta ==6:
            self.salasana()       
        if valinta == 0:
            print("\nPalataan edelliseen valikkoon.")
            print()
            break  
   def valikko(self):
    
    try:
        print("Päävalikko: ")
        print("1 - Käyttäjät")
        print("2 - Tavarat")
        print("3 - Lisää käyttäjälle tavara")
        print("0 - Lopeta ohjelma")
        syote = input("Valintasi: ")
        print()
        valinta = int(syote)
    except Exception:
        valinta = -1
    return valinta        

# Ali ohjelmat.
def Yhteys(polku: str):
    # Polkutietokantaan
    try:
        yhteys = sqlite3.connect(polku)
        return yhteys
    except sqlite3.Error as sqliteVirhe:
        print(sqliteVirhe)
    except Exception as Virhe:
        print(Virhe)
    return None






#Pääohjelma
class Main(Valikko,Otsikko1):
 def __init__(self):
    self.self = self   
    terve = Valikko()
    terve.palauta()
    self.taulu()
    self.tavarat()
    self.poistaTavarat()
    self.tavaraLista()
    self.kayttajaTavara()
    

    while True:
        valinta = self.valikko()
        if valinta == 1:

            self.valikko2()
        elif valinta == 2:

            self.valikko3()
        elif valinta == 3:
            self.valikko4()
        elif valinta == 0:
            print("Ohjelma päättyy.")
            tulostus = siirto()
            print()
            tulostus.siirra()
            self.poistaKayttajanTavarat()
            
            break
        else:
            print("Tuntematon valinta, yritä uudelleen.")
    return None


if __name__ == "__main__":
    Main()
