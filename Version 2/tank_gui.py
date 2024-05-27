import tkinter as tk
from tkinter import messagebox
import obd

class TankGui:
    def __init__(self, parent, fuel_type="N/A", fuel_level="N/A", fuel_pressure="N/A"):
        self.parent = parent
        self.parent.title("Tanküberwachung")
        self.parent.geometry("350x200")
        self.connection = obd.OBD()  # OBD-Verbindung initialisieren

        self.fuel_type = tk.StringVar(value=fuel_type)
        self.fuel_level = tk.StringVar(value=fuel_level)
        self.fuel_pressure = tk.StringVar(value=fuel_pressure)

        self.query_sent = False  # Flag, um zu überprüfen, ob die Abfrage bereits gesendet wurde

        self.create_widgets()
        self.parent.after(1000, self.update_values)  # Verzögerung, um sicherzustellen, dass die Anzeigen geladen werden

    def create_widgets(self):
        # Label für Treibstoffart
        fuel_type_label = tk.Label(self.parent, text="Treibstoffart:")
        fuel_type_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        fuel_type_value_label = tk.Label(self.parent, textvariable=self.fuel_type)
        fuel_type_value_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Label für Tankinhalt mit Einheit "Liter"
        fuel_level_label = tk.Label(self.parent, text="Tankinhalt:")
        fuel_level_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        fuel_level_value_label = tk.Label(self.parent, textvariable=self.fuel_level)
        fuel_level_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        fuel_level_unit_label = tk.Label(self.parent, text="Liter")
        fuel_level_unit_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Label für Treibstoffdruck mit Einheit "bar"
        fuel_pressure_label = tk.Label(self.parent, text="Treibstoffdruck:")
        fuel_pressure_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        fuel_pressure_value_label = tk.Label(self.parent, textvariable=self.fuel_pressure)
        fuel_pressure_value_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        fuel_pressure_unit_label = tk.Label(self.parent, text="bar")
        fuel_pressure_unit_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    def update_values(self):
        try:
            if not self.query_sent:  # Überprüfen, ob die Abfrage bereits gesendet wurde
                # Abfrage der Treibstoffart
                fuel_type_response = self.connection.query(obd.commands.FUEL_TYPE)
                if fuel_type_response and fuel_type_response.value:
                    self.fuel_type.set(fuel_type_response.value.magnitude)
                else:
                    self.fuel_type.set("N/A")

                # Abfrage des Tankinhalts
                fuel_level_response = self.connection.query(obd.commands.FUEL_LEVEL)
                if fuel_level_response and fuel_level_response.value:
                    self.fuel_level.set(fuel_level_response.value.magnitude)
                else:
                    self.fuel_level.set("N/A")

                # Abfrage des Treibstoffdrucks
                fuel_pressure_response = self.connection.query(obd.commands.FUEL_PRESSURE)
                if fuel_pressure_response and fuel_pressure_response.value:
                    self.fuel_pressure.set(fuel_pressure_response.value.magnitude)
                else:
                    self.fuel_pressure.set("N/A")

                self.query_sent = True  # Setzen der Flagge auf True, um anzuzeigen, dass die Abfrage gesendet wurde

            # Fortsetzen der Aktualisierung nach 1000 Millisekunden (1 Sekunde)
            self.parent.after(1000, self.update_values)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    tank_gui = TankGui(root)
    root.mainloop()
