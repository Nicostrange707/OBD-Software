import tkinter as tk
from tkinter import messagebox
import obd

class EngineGui:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Motorüberwachung")
        self.parent.geometry("400x200")
        try:
            self.connection = obd.OBD()  # OBD-Verbindung initialisieren
        except Exception as e:
            messagebox.showerror("Fehler", f"Verbindungsfehler: {e}")
            self.parent.destroy()
            return

        self.runtime_value = tk.StringVar()
        self.rpm_value = tk.StringVar()
        self.coolant_temp_value = tk.StringVar()
        self.oil_temp_value = tk.StringVar()
        self.boost_value = tk.StringVar()

        self.query_sent = False  # Flag, um zu überprüfen, ob die Abfrage bereits gesendet wurde

        self.create_widgets()
        self.update_values()  # Senden der Abfrage beim Initialisieren

    def create_widgets(self):
        # Labels für die verschiedenen Werte
        labels = [
            ("Motorlaufzeit:", self.runtime_value, "min"),
            ("Motordrehzahl:", self.rpm_value, "RPM"),
            ("Ladedruck:", self.boost_value, "bar"),
            ("Motor-Kühltemperatur:", self.coolant_temp_value, "°C"),
            ("Öltemperatur:", self.oil_temp_value, "°C"),
        ]

        for i, (label_text, value_var, unit_text) in enumerate(labels):
            label = tk.Label(self.parent, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            value_label = tk.Label(self.parent, textvariable=value_var)
            value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            unit_label = tk.Label(self.parent, text=unit_text)
            unit_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")

    def update_values(self):
        try:
            if not self.query_sent:  # Überprüfen, ob die Abfrage bereits gesendet wurde
                # Abfrage der Motorlaufzeit
                runtime_response = self.connection.query(obd.commands.RUN_TIME)
                if runtime_response is not None and runtime_response.value is not None:
                    self.runtime_value.set(str(runtime_response.value))

                # Abfrage der Motordrehzahl
                rpm_response = self.connection.query(obd.commands.RPM)
                if rpm_response is not None and rpm_response.value is not None:
                    self.rpm_value.set(str(rpm_response.value))

                # Abfrage des Ladedrucks
                boost_response = self.connection.query(obd.commands.INTAKE_PRESSURE)
                if boost_response is not None and boost_response.value is not None:
                    self.boost_value.set(str(boost_response.value))

                # Abfrage der Motor-Kühltemperatur
                coolant_temp_response = self.connection.query(obd.commands.COOLANT_TEMP)
                if coolant_temp_response is not None and coolant_temp_response.value is not None:
                    self.coolant_temp_value.set(str(coolant_temp_response.value))

                # Abfrage der Öltemperatur
                oil_temp_response = self.connection.query(obd.commands.OIL_TEMP)
                if oil_temp_response is not None and oil_temp_response.value is not None:
                    self.oil_temp_value.set(str(oil_temp_response.value))

                self.query_sent = True  # Setzen der Flagge auf True, um anzuzeigen, dass die Abfrage gesendet wurde

            # Fortsetzen der Aktualisierung nach 1000 Millisekunden (1 Sekunde)
            self.parent.after(1000, self.update_values)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    engine_gui = EngineGui(root)
    root.mainloop()
