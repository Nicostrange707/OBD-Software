import tkinter as tk
from tkinter import messagebox
import obd

class ThrottleGui:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Drosselklappenüberwachung")
        self.parent.geometry("300x150")
        self.connection = obd.OBD()  # OBD-Verbindung initialisieren

        self.throttle_value = tk.StringVar()
        self.relative_throttle_value = tk.StringVar()
        self.commanded_throttle_value = tk.StringVar()

        self.query_sent = False  # Flag, um zu überprüfen, ob die Abfrage bereits gesendet wurde

        self.create_widgets()
        self.parent.after(1000, self.update_values)  # Verzögerung, um sicherzustellen, dass die Anzeigen geladen werden

    def create_widgets(self):
        # Label für Drosselklappenstellung
        throttle_label = tk.Label(self.parent, text="Drosselklappenstellung:")
        throttle_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        throttle_value_label = tk.Label(self.parent, textvariable=self.throttle_value)
        throttle_value_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        throttle_unit_label = tk.Label(self.parent, text="%")
        throttle_unit_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # Label für relative Drosselklappenstellung
        relative_throttle_label = tk.Label(self.parent, text="Relative Drosselklappenstellung:")
        relative_throttle_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        relative_throttle_value_label = tk.Label(self.parent, textvariable=self.relative_throttle_value)
        relative_throttle_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        relative_throttle_unit_label = tk.Label(self.parent, text="%")
        relative_throttle_unit_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Label für befohlenen Drosselklappensteller
        commanded_throttle_label = tk.Label(self.parent, text="Befohlener Drosselklappensteller:")
        commanded_throttle_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        commanded_throttle_value_label = tk.Label(self.parent, textvariable=self.commanded_throttle_value)
        commanded_throttle_value_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        commanded_throttle_unit_label = tk.Label(self.parent, text="%")
        commanded_throttle_unit_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    def update_values(self):
        try:
            if not self.query_sent:  # Überprüfen, ob die Abfrage bereits gesendet wurde
                # Abfrage der Drosselklappenwerte
                throttle_response = self.connection.query(obd.commands.THROTTLE_POS)
                relative_throttle_response = self.connection.query(obd.commands.RELATIVE_THROTTLE_POS)
                self.query_sent = True  # Setzen der Flagge auf True, um anzuzeigen, dass die Abfrage gesendet wurde

                # Aktualisierung der Anzeigewerte
                if throttle_response:
                    self.throttle_value.set(throttle_response.value)
                if relative_throttle_response:
                    self.relative_throttle_value.set(relative_throttle_response.value)
                
            # Befohlener Drosselklappensteller aktualisieren, falls verfügbar
            try:
                commanded_throttle_response = self.connection.query(obd.commands.COMMANDED_THROTTLE_POS)
                if commanded_throttle_response:
                    self.commanded_throttle_value.set(commanded_throttle_response.value)
            except AttributeError:
                # Ausnahme behandeln, wenn COMMANDED_THROTTLE_POS nicht verfügbar ist
                self.commanded_throttle_value.set("N/A")

            # Fortsetzen der Aktualisierung nach 1000 Millisekunden (1 Sekunde)
            self.parent.after(1000, self.update_values)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    throttle_gui = ThrottleGui(root)
    root.mainloop()
