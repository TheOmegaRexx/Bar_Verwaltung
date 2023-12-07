from tkinter import *
# Stelle sicher, dass CTkMessagebox korrekt importiert ist
from CTkMessagebox import CTkMessagebox
import mysql.connector
import customtkinter
from CTkListbox import *
from abc import ABC, abstractclassmethod
import time
import random

geld = 100


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
            self.auswahl_listbox_getraenke.insert(index, f"{item.name} {item.preis}€")

        for index, item in enumerate(snacks_liste):
            self.auswahl_listbox_snacks.insert(index, f"{item.name} {item.preis}€")

        for index, item in enumerate(rauchwaren_liste):
            self.auswahl_listbox_rauchwaren.insert(index, f"{item.name} {item.preis}€")

        self.tressen_fenster.mainloop()
        

    def bestellung(self):
        pass

    def hinzufuegen(self):
        test = self.auswahl_listbox_getraenke.get()
        test.preis
        self.preis = self.preis
        print(test)

    def entfernen(self):
        pass

    def nachricht(self):
        # Erstellung eines Fensters für die Nachrichten
        nachrichten_fenster = customtkinter.CTkToplevel(self.tressen_fenster)
        nachrichten_label = customtkinter.CTkLabel(
            nachrichten_fenster, text="Nachricht").pack()
        nachrichten_textbox = customtkinter.CTkTextbox(
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
            self.auswahl_listbox_getraenke.insert(index, f"{item.name} {item.menge}")

        for index, item in enumerate(snacks_liste):
            self.auswahl_listbox_snacks.insert(index, f"{item.name} {item.menge}")

        for index, item in enumerate(rauchwaren_liste):
            self.auswahl_listbox_rauchwaren.insert(index, f"{item.name} {item.menge}")



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
    def __init__(self, name, preis, menge):
        self.name = name
        self.preis = preis
        self.menge = menge


class Getränke(Artikel):
    def __init__(self, name, preis, menge, liter, alkohol=True, eis=False):
        self.liter = liter
        self.alkohol = alkohol
        self.eis = eis
        super().__init__(name, preis, menge)


class Snacks(Artikel):
    def __init__(self, name, preis, menge):
        super().__init__(name, preis, menge)


class Rauchwaren(Artikel):
    def __init__(self, name, preis, menge):
        super().__init__(name, preis, menge)


if __name__ == "__main__":
    getraenke_liste = [
    Getränke("Cola", 2.5, 100, 1.5),
    Getränke("Bier", 3.0, 50, 0.5),
    Getränke("Wasser", 1.0, 200, 2.0, alkohol=False),
    Getränke("Eistee", 2.0, 80, 1.0),
    Getränke("Orangensaft", 2.8, 120, 1.0, eis=True),
    Getränke("Wein", 8.0, 30, 0.75),
    Getränke("Energy Drink", 2.5, 60, 0.25),
    Getränke("Smoothie", 4.0, 40, 0.5, alkohol=False, eis=True),
    Getränke("Eiskaffee", 3.5, 45, 0.3, eis=True),
    Getränke("Whisky", 20.0, 10, 0.7),
    ]

    snacks_liste = [
        Snacks("Chips", 2.0, 80),
        Snacks("Schokoriegel", 1.5, 120),
        Snacks("Studentenfutter", 3.0, 50),
        Snacks("Pretzel", 1.0, 100),
        Snacks("Gemüsesticks", 2.5, 60),
        Snacks("Popcorn", 1.8, 70),
        Snacks("Nüsse", 3.0, 40),
        Snacks("Obstsalat", 2.2, 90),
        Snacks("Cracker", 1.2, 110),
        Snacks("Käsestangen", 2.8, 30),
    ]

    rauchwaren_liste = [
        Rauchwaren("Zigaretten", 6.0, 50),
        Rauchwaren("Zigarillos", 8.0, 30),
        Rauchwaren("Pfeifentabak", 10.0, 20),
        Rauchwaren("Zigarren", 12.0, 15),
        Rauchwaren("Filter", 1.0, 100),
        Rauchwaren("Feuerzeug", 2.5, 80),
        Rauchwaren("Aschenbecher", 3.0, 40),
        Rauchwaren("Tabakdose", 5.0, 25),
        Rauchwaren("Zündhölzer", 0.5, 150),
        Rauchwaren("Wasserpfeife", 20.0, 10),
    ]
    Test = GUI()
