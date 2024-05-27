import tkinter as tk
from tkinter import messagebox
import obd

class IntakeGui:
    def __init__(self, parent, air_temp="N/A", manifold_pressure="N/A"):
        self.parent = parent
        self.parent.title("Ansaugung")
        self.parent.geometry("300x150")
        self.connection = obd.OBD()  # OBD-Verbindung initialisieren

        self.air_temp = tk.StringVar(value=air_temp)
        self.manifold_pressure = tk.StringVar(value=manifold_pressure)

        self.query_sent = False  # Flag, um zu überprüfen, ob die Abfrage bereits gesendet wurde

        self.create_widgets()
        self.update_values()  # Senden der Abfrage beim Initialisieren

    def create_widgets(self):
        # Label für Ansauglufttemperatur
        air_temp_label = tk.Label(self.parent, text="Ansauglufttemperatur:")
        air_temp_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        air_temp_value_label = tk.Label(self.parent, textvariable=self.air_temp)
        air_temp_value_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        air_temp_unit_label = tk.Label(self.parent, text="°C")
        air_temp_unit_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # Label für Ansaugkrümmerdruck
        intake_pressure_label = tk.Label(self.parent, text="Ansaugkrümmerdruck:")  # Korrektur von self.root zu self.parent
        intake_pressure_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Änderung von row=12 zu row=1
        intake_pressure_value_label = tk.Label(self.parent, textvariable=self.manifold_pressure)  # Korrektur von self.root zu self.parent und self.intake_pressure_value zu self.manifold_pressure
        intake_pressure_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Änderung von row=12 zu row=1
        intake_pressure_unit_label = tk.Label(self.parent, text="bar")  # Korrektur von self.root zu self.parent
        intake_pressure_unit_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")  # Änderung von row=12 zu row=1

    def update_values(self):
        try:
            if not self.query_sent:  # Überprüfen, ob die Abfrage bereits gesendet wurde
                # Abfrage der Ansauglufttemperatur
                air_temp_response = self.connection.query(obd.commands.INTAKE_TEMP)
                if air_temp_response and air_temp_response.value:
                    self.air_temp.set(air_temp_response.value.magnitude)
                else:
                    self.air_temp.set("N/A")

                # Abfrage des Ansaugkrümmerdrucks
                manifold_pressure_response = self.connection.query(obd.commands.INTAKE_PRESSURE)
                if manifold_pressure_response and manifold_pressure_response.value:
                    self.manifold_pressure.set(manifold_pressure_response.value.magnitude)
                else:
                    self.manifold_pressure.set("N/A")

                self.query_sent = True  # Setzen der Flagge auf True, um anzuzeigen, dass die Abfrage gesendet wurde

            # Fortsetzen der Aktualisierung nach 1000 Millisekunden (1 Sekunde)
            self.parent.after(1000, self.update_values)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    intake_gui = IntakeGui(root)
    root.mainloop()
