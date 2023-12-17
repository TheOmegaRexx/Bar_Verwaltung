from tkinter import *
from CTkMessagebox import CTkMessagebox
import mysql.connector
import customtkinter
from CTkListbox import *
from abc import ABC, abstractclassmethod


geld = 100

class Login:
    def __init__(self):
        self.login_fenster = customtkinter.CTk()
        self.login_fenster.title("Login")
        self.login_fenster.geometry("360x180")
        self.login_fenster.resizable(False, False)
    
        self.benutzer_label = customtkinter.CTkLabel(self.login_fenster, text="Benutzer")
        self.benutzer_label.pack()

        self.benutzer_entry = customtkinter.CTkEntry(self.login_fenster)
        self.benutzer_entry.pack()

        self.passwort_label = customtkinter.CTkLabel(self.login_fenster, text="Passwort")
        self.passwort_label.pack()

        self.passwort_entry = customtkinter.CTkEntry(self.login_fenster)
        self.passwort_entry.pack()

        self.login_button = customtkinter.CTkButton(self.login_fenster, text="Login", command=self.einlogen)
        self.login_button.pack(pady=20)
        self.login_fenster.mainloop()

    def einlogen(self):
        benutzer = self.benutzer_entry.get()
        passwort = self.passwort_entry.get()



class GUI:
    def __init__(self):
        # Initialisierung des Hauptfensters
        self.fenster = customtkinter.CTk()
        self.fenster.title("Bar")
        self.fenster.geometry()  # Hier solltest du die Größe des Fensters angeben
        # self.fenster.resizable(False, False)

        # Erstellung von GUI-Elementen im Hauptfenster
        self.titel_label = customtkinter.CTkLabel(self.fenster, text="Bar")
        self.titel_label.grid(row=0, column=0)

        self.bar_button = customtkinter.CTkButton(
            self.fenster, text="Tressen", command=self.tressen_oeffnen)
        self.bar_button.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        self.lager_button = customtkinter.CTkButton(
            self.fenster, text="Lager", command=self.lager_oeffnen)
        self.lager_button.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        self.rechnugen_button = customtkinter.CTkButton(
            self.fenster, text="Rechnungen", command=self.rechnungen_oeffne)
        self.rechnugen_button.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        self.statistiken_button = customtkinter.CTkButton(
            self.fenster, text="Statistiken", command=self.statistiken_oeffnen)
        self.statistiken_button.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        self.fenster.mainloop()

    def tressen_oeffnen(self):
        tressen = Tressen()

    def lager_oeffnen(self):
        lager = Lager()

    def rechnungen_oeffne(self):
        rechnungen = Rechnungen()

    def statistiken_oeffnen(self):
        statistiken = Statistik()


class Tressen:
    def __init__(self):
        self.preis = 0.0
        self.current_order = []

        # Initialisierung des Fensters für die Tresenansicht
        self.tressen_fenster = customtkinter.CTk()
        self.tressen_fenster.title("Tressen")
        self.tressen_fenster.geometry()
        self.tressen_fenster.resizable(False, False)

        # Erstellung von GUI-Elementen für die Tresenansicht
        self.auswahl_label = customtkinter.CTkLabel(
            self.tressen_fenster, text="Artikel")
        self.auswahl_label.grid(row=0, column=0)

        self.preis_label = customtkinter.CTkLabel(
            self.tressen_fenster, text=f"Preis: {self.preis}")
        self.preis_label.grid(row=0, column=1)

        # Erstellung von Registerkarten für Getränke, Snacks und Rauchwaren
        self.artikel_tab = customtkinter.CTkTabview(self.tressen_fenster)
        self.artikel_tab.grid(row=1, column=0)

        self.artikel_tab_getraenke = self.artikel_tab.add("Getränke")
        self.artikel_tab_snacks = self.artikel_tab.add("Snacks")
        self.artikel_tab_rauchwaren = self.artikel_tab.add("Rauchwaren")

        # Erstellung von Listboxen für die einzelnen Artikelkategorien
        self.auswahl_listbox_getraenke = CTkListbox(self.artikel_tab_getraenke)
        self.auswahl_listbox_getraenke.grid()

        self.auswahl_listbox_snacks = CTkListbox(self.artikel_tab_snacks)
        self.auswahl_listbox_snacks.grid()

        self.auswahl_listbox_rauchwaren = CTkListbox(
            self.artikel_tab_rauchwaren)
        self.auswahl_listbox_rauchwaren.grid()

        # Erstellung einer Listbox für die Bestellung
        self.bestellung_listbox = CTkListbox(self.tressen_fenster)
        self.bestellung_listbox.grid(row=1, column=1)

        # Erstellung von Buttons für Aktionen in der Tresenansicht
        self.hinzufuegen_button = customtkinter.CTkButton(
            self.tressen_fenster, text="Hinzufügen", command=self.hinzufuegen)
        self.hinzufuegen_button.grid(row=3, column=0)

        self.entfernen_button = customtkinter.CTkButton(
            self.tressen_fenster, text="Entfernen", command=self.entfernen)
        self.entfernen_button.grid(row=3, column=1)

        self.bestellung_button = customtkinter.CTkButton(
            self.tressen_fenster, text="Bestellen", command=self.bestellung)
        self.bestellung_button.grid(row=4, column=1)

        self.nachricht_button = customtkinter.CTkButton(
            self.tressen_fenster, text="Nachricht", command=self.nachricht)
        self.nachricht_button.grid(row=4, column=0)

        for index, item in enumerate(getraenke_liste):
            self.auswahl_listbox_getraenke.insert(
                index, f"{item.name} {item.preis}€")

        for index, item in enumerate(snacks_liste):
            self.auswahl_listbox_snacks.insert(
                index, f"{item.name} {item.preis}€")

        for index, item in enumerate(rauchwaren_liste):
            self.auswahl_listbox_rauchwaren.insert(
                index, f"{item.name} {item.preis}€")

        self.tressen_fenster.mainloop()

    def bestellung(self):
            # Hier können Sie den Bestellvorgang implementieren
            # Beachten Sie, dass Sie die Datenbankverbindung wiederherstellen müssen

            # Beispiel: Annahme, dass die Bestellung erfolgreich ist
            self.bestellung_abschließen()

    def bestellung_abschließen(self):
        # Hier implementieren Sie die Aktionen nach Abschluss der Bestellung

        # Annahme: Geld wird aktualisiert
        global geld
        geld += self.preis
        # Hier können Sie die Aktualisierung der Datenbank implementieren

        # Bestellung abschließen
        self.bestellung_listbox.delete(0, 'end')  # Leeren der Bestellungsliste
        self.preis = 0.0  # Zurücksetzen des Preises
        self.preis_label.config(text=f"Preis: {self.preis} €")  # Aktualisieren des Preislabels

    def hinzufuegen(self):
        # Erhalten Sie den ausgewählten Artikel aus der ausgewählten Liste
        selected_item = self.artikel_get()

        if selected_item:
            # Extrahieren Sie den Preis aus dem ausgewählten Artikel (angenommen, der Preis ist am Ende des Strings)
            selected_price = float(selected_item.split()[-1][:-1])
            
            # Fügen Sie den ausgewählten Artikel zur Bestellungsliste hinzu
            self.bestellung_listbox.insert("end", selected_item)

            # Aktualisieren Sie den Gesamtpreis
            self.preis += selected_price
            self.preis_label.configure(text=f"Preis: {self.preis} €")

    def artikel_get(self):
        # Erhalten Sie den ausgewählten Index aus der ausgewählten Liste
        selected_index = self.auswahl_listbox_getraenke.curselection()
        if selected_index:
            selected_item = self.auswahl_listbox_getraenke.get(selected_index)
        else:
            selected_index = self.auswahl_listbox_snacks.curselection()
            if selected_index:
                selected_item = self.auswahl_listbox_snacks.get(selected_index)
            else:
                selected_index = self.auswahl_listbox_rauchwaren.curselection()
                if selected_index:
                    selected_item = self.auswahl_listbox_rauchwaren.get(selected_index)
                else:
                    # Wenn nichts ausgewählt ist, gebe None zurück oder handle den Fall entsprechend
                    selected_item = None
        return selected_item

    def entfernen(self):
        # Erhalten Sie den ausgewählten Index aus der Bestellungsliste
        selected_index = self.bestellung_listbox.curselection()

        if selected_index:
            # Extrahieren Sie den ausgewählten Artikel aus der Bestellungsliste
            selected_item = self.bestellung_listbox.get(selected_index)

            # Extrahieren Sie den Preis des ausgewählten Artikels (angenommen, der Preis ist am Ende des Strings)
            selected_price = float(selected_item.split()[-1][:-1])

            # Entfernen Sie den ausgewählten Artikel aus der Bestellungsliste
            self.bestellung_listbox.delete(selected_index)

            # Aktualisieren Sie den Gesamtpreis
            self.preis -= selected_price
            self.preis_label.configure(text=f"Preis: {self.preis} €")

    def nachricht(self):
        # Erstellung eines Fensters für die Nachrichten
        nachrichten_fenster = customtkinter.CTkToplevel(self.tressen_fenster)
        nachrichten_label = customtkinter.CTkLabel(
            nachrichten_fenster, text="Nachricht").pack()
        nachrichten_textbox = customtkinter.CTkEntry(
            nachrichten_fenster).pack()
        nachrichten_button = customtkinter.CTkButton(
            nachrichten_fenster, text="Senden", command=self.nachricht_senden).pack()

        nachrichten_fenster.mainloop

    def nachricht_senden(self):
        # Bestätigungsnachricht für das Senden der Nachricht
        auswahl = CTkMessagebox(title="Exit?", message="Möchten sie die Nachricht senden?",
                                icon="question", option_1="Nein", option_2="Ja")

        wahl = auswahl.get()
        if wahl == "Ja":
  
            CTkMessagebox(
                title="Erfolg", message="Die Nachricht wurde Erfolgreich gesendet", icon="check")


class Lager:
    def __init__(self):
        # Initialisierung des Lagerfensters
        self.lager_fenster = customtkinter.CTk()
        self.lager_fenster.title("Lager")
        self.lager_fenster.geometry()
        self.lager_fenster.resizable(False, False)

        # Erstellung von GUI-Elementen im Lagerfenster
        self.artikel_label = customtkinter.CTkLabel(
            self.lager_fenster, text="Lager")
        self.artikel_label.grid(row=0, column=0)

        self.artikel_tab = customtkinter.CTkTabview(self.lager_fenster)
        self.artikel_tab.grid(row=1, column=0)

        self.artikel_tab_getraenke = self.artikel_tab.add("Getränke")
        self.artikel_tab_snacks = self.artikel_tab.add("Snacks")
        self.artikel_tab_rauchwaren = self.artikel_tab.add("Rauchwaren")

        # Erstellung von Listboxen für die einzelnen Artikelkategorien
        self.auswahl_listbox_getraenke = CTkListbox(self.artikel_tab_getraenke)
        self.auswahl_listbox_getraenke.grid()

        self.auswahl_listbox_snacks = CTkListbox(self.artikel_tab_snacks)
        self.auswahl_listbox_snacks.grid()

        self.auswahl_listbox_rauchwaren = CTkListbox(
            self.artikel_tab_rauchwaren)
        self.auswahl_listbox_rauchwaren.grid()

        self.artikel_hinzufuegen_button = customtkinter.CTkButton(
            self.lager_fenster, text="Hinzufügen", command=self.artikel_hinzufuegen)
        self.artikel_hinzufuegen_button.grid(row=2)

        self.artikel_entfernen_button = customtkinter.CTkButton(
            self.lager_fenster, text="Entfernen", command=self.artikel_entfernen)
        self.artikel_entfernen_button.grid(row=3)

        for index, item in enumerate(getraenke_liste):
            self.auswahl_listbox_getraenke.insert(
                index, f"{item.name} {item.menge}")

        for index, item in enumerate(snacks_liste):
            self.auswahl_listbox_snacks.insert(
                index, f"{item.name} {item.menge}")

        for index, item in enumerate(rauchwaren_liste):
            self.auswahl_listbox_rauchwaren.insert(
                index, f"{item.name} {item.menge}")

        self.lager_fenster.mainloop()

    def artikel_hinzufuegen(self):
        pass

    def artikel_entfernen(self):
        pass


class Rechnungen:
    def __init__(self):
        # Initialisierung des Rechnungsfensters
        self.rechnungs_fenster = customtkinter.CTk()
        self.rechnungs_fenster.title("Rechnugen")
        self.rechnungs_fenster.geometry()
        self.rechnungs_fenster.resizable(False, False)

        # Erstellung von GUI-Elementen im Rechnungsfenster
        self.rechnungen_label = customtkinter.CTkLabel(
            self.rechnungs_fenster, text="Rechnungen")
        self.rechnungen_label.grid(row=0, column=0)

        self.rechnungs_listbox = CTkListbox(self.rechnungs_fenster)
        self.rechnungs_listbox.grid(row=1, column=0)

        self.rechnungs_listbox.insert(0, "Option 0")

        self.rechnungs_textbox = customtkinter.CTkTextbox(
            self.rechnungs_fenster)
        self.rechnungs_textbox.grid(row=1, column=1)

        self.speichern_button = customtkinter.CTkButton(
            self.rechnungs_fenster, text="Speichern", command=self.speichern)
        self.speichern_button.grid(row=3, column=0)

        self.rechnungs_fenster.mainloop()

    def speichern(self):
        pass


class Statistik:
    def __init__(self):
        # Initialisierung des Statistikfensters
        self.statistik_fenster = customtkinter.CTk()
        self.statistik_fenster.title("Statistiken")
        self.statistik_fenster.geometry()
        self.statistik_fenster.resizable(False, False)

        # Erstellung von GUI-Elementen im Statistikfenster
        self.geld_label = customtkinter.CTkLabel(
            self.statistik_fenster, text=f"Geld: {geld}")
        self.geld_label.grid(row=0, column=0)

        self.profit_label = customtkinter.CTkLabel(
            self.statistik_fenster, text="Profit: ")
        self.profit_label.grid(row=1, column=0)

        self.belibste_label = customtkinter.CTkLabel(
            self.statistik_fenster, text="Beliebstes Artikel: ")
        self.belibste_label.grid(row=2, column=0)

        self.verkauf_label = customtkinter.CTkLabel(
            self.statistik_fenster, text="Anzahl der Verkäufe: ")
        self.verkauf_label.grid(row=3, column=0)

        self.titel2_label = customtkinter.CTkLabel(
            self.statistik_fenster, text="WIP: ")
        self.titel2_label.grid(row=4, column=0)

        self.statistik_fenster.mainloop()


class Artikel:
    def __init__(self, name, preis, menge, id):
        self.name = name
        self.preis = preis
        self.menge = menge


class Getränke(Artikel):
    def __init__(self, name, preis, menge, id, liter, alkohol=True):
        self.liter = liter
        self.alkohol = alkohol
        super().__init__(name, preis, menge, id)


class Snacks(Artikel):
    def __init__(self, name, preis, menge, id):
        super().__init__(name, preis, menge, id)


class Rauchwaren(Artikel):
    def __init__(self, name, preis, menge, id):
        super().__init__(name, preis, menge, id)


class Datenbank:
    # Konstruktor mit den notwendigen Parametern für die Datenbankverbindung
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None  # Initialisierung der Verbindungsvariable

    # Methode zum Herstellen einer Verbindung zur Datenbank
    def verbinden(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    # Methode zum Schließen der Datenbankverbindung
    def verbindung_schliessen(self):
        if self.connection:
            self.connection.close()

    # Methode zur Abfrage und Rückgabe der Snacks aus der Datenbank
    def db_snacks(self):
        snacks_liste = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, preis, menge, id FROM Snacks")
        for (name, preis, menge, id) in cursor:
            snacks_liste.append(Snacks(name, preis, menge, id))
        cursor.close()
        return snacks_liste

    # Methode zur Abfrage und Rückgabe der Rauchwaren aus der Datenbank
    def db_rauchwaren(self):
        rauchwaren_liste = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, preis, menge, id FROM Getraenke")
        for (name, preis, menge, id) in cursor:
            rauchwaren_liste.append(Rauchwaren(name, preis, menge, id))
        cursor.close()
        return rauchwaren_liste

    # Methode zur Abfrage und Rückgabe der Getränke aus der Datenbank
    def db_getraenke(self):
        getraenke_liste = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, preis, menge, liter, alkohol, id FROM Getraenke")
        for (name, preis, menge, liter, alkohol, id) in cursor:
            getraenke_liste.append(Getränke(name, preis, menge, liter, alkohol, id))
        cursor.close()
        return getraenke_liste
    
    def db_passwort(self):
        pass

    def db_benutzer(self):
        pass

    def db_geld(self):
        pass


if __name__ == "__main__":
    # Definition der Verbindungsinformationen
    HOST = "localhost"
    USER = "root"
    PASSWORD = "pass"
    DATABASE = "barverwaltung"

    # Erstellen einer Datenbankinstanz mit den Verbindungsinformationen
    datenbank = Datenbank(HOST, USER, PASSWORD, DATABASE)
    
    # Herstellen der Verbindung zur Datenbank
    datenbank.verbinden()

    # Abrufen der Listen von Getränken, Snacks und Rauchwaren aus der Datenbank
    getraenke_liste = datenbank.db_getraenke()
    snacks_liste = datenbank.db_snacks()
    rauchwaren_liste = datenbank.db_rauchwaren()

    # Schließen der Datenbankverbindung
    datenbank.verbindung_schliessen()

    # Erstellen einer GUI-Instanz (vorausgesetzt, dass die GUI-Klasse implementiert ist)
    Test = GUI()
    #Login()