import tkinter as tk
from menu import MenuBar

class OBDGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Steuergerät auslesen")
        self.root.geometry('400x300')  # Erhöhen der Fensterhöhe für zusätzliche Labels

        self.menubar = MenuBar(root)
        
        self.rpm_value = tk.StringVar()
        self.speed_value = tk.StringVar()
        self.oil_temp_value = tk.StringVar()
        self.coolant_temp_value = tk.StringVar()
        self.boost_value = tk.StringVar()
        self.throttle_position_value = tk.StringVar()  # Variable für die Drosselklappenstellung
        self.relative_throttle_position_value = tk.StringVar()  # Relative Drosselklappenstellung
        self.commanded_throttle_value = tk.StringVar()  # Befohlener Drosselklappensteller
        self.fuel_gauge_value = tk.StringVar()
        self.engine_runtime_value = tk.StringVar()  # Hinzufügen der Motorlaufzeit
        self.vin_value = tk.StringVar()
        self.voltage_value = tk.StringVar()
        self.fuel_pressure_value = tk.StringVar()  # Variable für den Treibstoffdruck
        self.intake_pressure_value = tk.StringVar()  # Variable für den Ansaugkrümmerdruck
        self.intake_air_temp_value = tk.StringVar()  # Variable für die Ansauglufttemperatur
        self.fuel_type_value = tk.StringVar()  # Variable für die Treibstoffart

        # Verbindung zum OBD-Gerät
        self.connection = None

        # GUI-Elemente erstellen
        self.create_widgets()

    def create_widgets(self):
        # Status-LED für OBD-Verbindung
        self.status_led = tk.Label(self.root, text="Status: Nicht verbunden", fg="red")
        self.status_led.grid(row=0, column=0, columnspan=3, pady=5, sticky="w")

        # Motorlaufzeit
        engine_runtime_label = tk.Label(self.root, text="Motorlaufzeit:")
        engine_runtime_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        engine_runtime_value_label = tk.Label(self.root, textvariable=self.engine_runtime_value)
        engine_runtime_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        engine_runtime_unit_label = tk.Label(self.root, text="min")
        engine_runtime_unit_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Kraftstoffart
        fuel_type_label = tk.Label(self.root, text="Treibstoffart:")
        fuel_type_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        fuel_type_value_label = tk.Label(self.root, textvariable=self.fuel_type_value)
        fuel_type_value_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Drehzahl
        rpm_label = tk.Label(self.root, text="Motordrehzahl:")
        rpm_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        rpm_value_label = tk.Label(self.root, textvariable=self.rpm_value, fg="red")
        rpm_value_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        rpm_unit_label = tk.Label(self.root, text="RPM")
        rpm_unit_label.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        # Relative Gaspedalstellung
        relative_throttle_position_label = tk.Label(self.root, text="Relative Gaspedalstellung:")
        relative_throttle_position_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        relative_throttle_position_value_label = tk.Label(self.root, textvariable=self.relative_throttle_position_value)
        relative_throttle_position_value_label.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        relative_throttle_position_unit_label = tk.Label(self.root, text="%")
        relative_throttle_position_unit_label.grid(row=6, column=2, padx=10, pady=5, sticky="w")

        # Geschwindigkeit
        speed_label = tk.Label(self.root, text="Geschwindigkeit:")
        speed_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        speed_value_label = tk.Label(self.root, textvariable=self.speed_value)
        speed_value_label.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        speed_unit_label = tk.Label(self.root, text="km/h")
        speed_unit_label.grid(row=7, column=2, padx=10, pady=5, sticky="w")

        # Spannung des Steuermoduls
        voltage_label = tk.Label(self.root, text="Spannung des Steuermoduls:")
        voltage_label.grid(row=16, column=0, padx=10, pady=5, sticky="w")
        voltage_value_label = tk.Label(self.root, textvariable=self.voltage_value)
        voltage_value_label.grid(row=16, column=1, padx=10, pady=5, sticky="w")
        voltage_unit_label = tk.Label(self.root, text="V")
        voltage_unit_label.grid(row=16, column=2, padx=10, pady=5, sticky="w")

        # Fahrzeugidentifikation
        vin_label = tk.Label(self.root, text="Fahrzeugidentifikation (VIN):")
        vin_label.grid(row=17, column=0, padx=10, pady=5, sticky="w")
        vin_value_label = tk.Label(self.root, textvariable=self.vin_value)
        vin_value_label.grid(row=17, column=1, padx=10, pady=5, sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    obd_gui = OBDGUI(root)
    root.mainloop()
