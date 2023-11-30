from tkinter import *
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
        self.fenster = customtkinter.CTk()
        self.fenster.title("Bar")
        self.fenster.geometry()
        self.fenster.resizable(False, False)

        self.titel_label = customtkinter.CTkLabel(self.fenster, text="Bar")
        self.titel_label.grid(row=0, column=0)

        self.geld_label = customtkinter.CTkLabel(
            self.fenster, text=f"Geld:{geld}")
        self.geld_label.grid(row=0, column=1)

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


class Tressen():
        def __init__(self):
            preis = 0
            self.tressen_fenster = customtkinter.CTk()
            self.tressen_fenster.title("Tressen")
            self.tressen_fenster.geometry()
            self.tressen_fenster.resizable(False, False)

            self.tressen_label = customtkinter.CTkLabel(
                self.tressen_fenster, text="Tressen")
            self.tressen_label.grid(row=0, column=0)

            self.auswahl_label = customtkinter.CTkLabel(
                self.tressen_fenster, text="Artikel")
            self.auswahl_label.grid(row=1, column=0)

            self.bestellung_label = customtkinter.CTkLabel(
                self.tressen_fenster, text="Bestellung")
            self.bestellung_label.grid(row=1, column=1)

            self.preis_label = customtkinter.CTkLabel(self.tressen_fenster, text=f"Preis: {preis}")
            self.preis_label.grid(row=0, column=1)

            self.auswahl_listbox = CTkListbox(self.tressen_fenster)
            self.auswahl_listbox.grid(row=2, column=0)

            self.bestellung_listbox = CTkListbox(self.tressen_fenster)
            self.bestellung_listbox.grid(row=2, column = 1)

            self.hinzufuegen_button = customtkinter.CTkButton(self.tressen_fenster, text="Hinzufügen", command=self.hinzufuegen)
            self.hinzufuegen_button.grid(row=3, column=0)

            self.entfernen_button = customtkinter.CTkButton(self.tressen_fenster, text="Entfernen", command=self.entfernen)
            self.entfernen_button.grid(row=3, column=1)

            self.bestellung_button = customtkinter.CTkButton(self.tressen_fenster, text="Bestellen", command=self.bestellung)
            self.bestellung_button.grid(row=4, column=1)

            self.nachricht_button = customtkinter.CTkButton(self.tressen_fenster, text="Nachricht", command=self.nachricht)
            self.nachricht_button.grid(row=4, column=0)


            self.tressen_fenster.mainloop()


        def bestellung(self):
            pass

        def hinzufuegen(self):
            pass

        def entfernen(self):
            pass

        def nachricht(self):
            nachrichten_fenster = customtkinter.CTkToplevel(self.tressen_fenster)
            nachrichten_label = customtkinter.CTkLabel(nachrichten_fenster, text="Nachricht").pack()
            nachrichten_textbox = customtkinter.CTkTextbox(nachrichten_fenster).pack()
            nachrichten_button = customtkinter.CTkButton(nachrichten_fenster, text="Senden", command=self.nachricht_senden).pack()

            nachrichten_fenster.mainloop

        def nachricht_senden(self):
            auswahl = CTkMessagebox(title="Exit?", message="Möchten sie die Nachricht senden?",
                        icon="question", option_1="Nein", option_2="Ja")
            
            wahl = auswahl.get()
            if wahl == "Ja":
                CTkMessagebox(title="Erfolg", message="Die Nachricht wurde Erfolgreich gesendet", icon="check")



class Lager:
    def __init__(self):
        self.lager_fenster = customtkinter.CTk()
        self.lager_fenster.title("Lager")
        self.lager_fenster.geometry()
        self.lager_fenster.resizable(False, False)

        self.artikel_label = customtkinter.CTkLabel(
            self.lager_fenster, text="Lager")
        self.artikel_label.grid(row=0, column=0)

        self.artikel_listbox = CTkListbox(self.lager_fenster)
        self.artikel_listbox.grid(row=1)

        self.artikel_listbox.insert(0, "Name 0 3$")

        self.artikel_hinzufuegen_button = customtkinter.CTkButton(
            self.lager_fenster, text="Hinzufügen", command=self.artikel_hinzufuegen)
        self.artikel_hinzufuegen_button.grid(row=2)

        self.artikel_entfernen_button = customtkinter.CTkButton(
            self.lager_fenster, text="Entfernen", command=self.artikel_entfernen)
        self.artikel_entfernen_button.grid(row=3)

        self.lager_fenster.mainloop()

    def artikel_hinzufuegen(self):
        pass

    def artikel_entfernen(self):
        pass


class Rechnungen():
    def __init__(self):
        self.rechnungs_fenster = customtkinter.CTk()
        self.rechnungs_fenster.title("Rechnugen")
        self.rechnungs_fenster.geometry()
        self.rechnungs_fenster.resizable(False, False)

        self.rechnungen_label = customtkinter.CTkLabel(
            self.rechnungs_fenster, text="Rechnungen")
        self.rechnungen_label.grid(row=0, column=0)

        self.rechnungs_listbox = CTkListbox(self.rechnungs_fenster)
        self.rechnungs_listbox.grid(row=1, column=0)

        self.rechnungs_listbox.insert(0, "Option 0")

        self.rechnungs_textbox = customtkinter.CTkTextbox(self.rechnungs_fenster)
        self.rechnungs_textbox.grid(row=1, column=1)

        self.speichern_button = customtkinter.CTkButton(
            self.rechnungs_fenster, text="Speichern", command=self.speichern)
        self.speichern_button.grid(row=3, column=0)

        self.rechnungs_fenster.mainloop()

    def speichern(self):
        pass


class Statistik():
    def __init__(self):
        self.statistik_fenster = customtkinter.CTk()
        self.statistik_fenster.title("Statistiken")
        self.statistik_fenster.geometry()
        self.statistik_fenster.resizable(False, False)

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


class Artikel():
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
    Test = GUI()
