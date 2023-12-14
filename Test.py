import tkinter as tk

class Hauptseite(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Hauptseite").pack()
        tk.Button(self, text="Zur Seite 2 wechseln", command=self.zu_seite_2).pack()

    def zu_seite_2(self):
        self.pack_forget()  # Aktuelle Seite ausblenden
        seite_2.pack()      # Neue Seite anzeigen

class Seite2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Seite 2").pack()
        tk.Button(self, text="Zurück zur Hauptseite", command=self.zurueck_zur_hauptseite).pack()

    def zurueck_zur_hauptseite(self):
        seite_2.pack_forget()   # Aktuelle Seite ausblenden
        hauptseite.pack()       # Neue Seite anzeigen

# Hauptfenster
root = tk.Tk()
root.title("Seitenwechsel mit Tkinter")

# Seiten erstellen
hauptseite = Hauptseite(root)
seite_2 = Seite2(root)

# Initial die Hauptseite anzeigen
hauptseite.pack()

# Hauptloop starten
root.mainloop()