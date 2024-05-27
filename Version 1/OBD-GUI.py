import tkinter as tk
from tkinter import messagebox, filedialog
import obd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class OBDGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Steuergerät auslesen")
        self.root.geometry('400x450')

        # Variablen für die OBD-Daten
        self.rpm_value = tk.StringVar()
        self.speed_value = tk.StringVar()
        self.oil_temp_value = tk.StringVar()
        self.coolant_temp_value = tk.StringVar()
        self.boost_value = tk.StringVar()
        self.fuel_gauge_value = tk.StringVar()
        self.vin_value = tk.StringVar()
        self.voltage_value = tk.StringVar()

        # Verbindung zum OBD-Gerät
        self.connection = None

        # GUI-Elemente erstellen
        self.create_widgets()
        # Menü erstellen
        self.create_menu()

    def create_widgets(self):
        # Status-LED für OBD-Verbindung
        self.status_led = tk.Label(self.root, text="Status: Nicht verbunden", fg="red")
        self.status_led.grid(row=0, column=0, columnspan=3, pady=5, sticky="w")

        # Kraftstoffanzeige
        fuel_gauge_label = tk.Label(self.root, text="Tank Inhalt:")
        fuel_gauge_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        fuel_gauge_value_label = tk.Label(self.root, textvariable=self.fuel_gauge_value)
        fuel_gauge_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        fuel_gauge_unit_label = tk.Label(self.root, text="Liter")
        fuel_gauge_unit_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Drehzahl
        rpm_label = tk.Label(self.root, text="Drehzahl:")
        rpm_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        rpm_value_label = tk.Label(self.root, textvariable=self.rpm_value, fg="red")
        rpm_value_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        rpm_unit_label = tk.Label(self.root, text="RPM")
        rpm_unit_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        # Geschwindigkeit
        speed_label = tk.Label(self.root, text="Geschwindigkeit:")
        speed_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        speed_value_label = tk.Label(self.root, textvariable=self.speed_value)
        speed_value_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        speed_unit_label = tk.Label(self.root, text="km/h")
        speed_unit_label.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        # Öltemperatur
        oil_temp_label = tk.Label(self.root, text="Öltemperatur:")
        oil_temp_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        oil_temp_value_label = tk.Label(self.root, textvariable=self.oil_temp_value)
        oil_temp_value_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        oil_temp_unit_label = tk.Label(self.root, text="°C")
        oil_temp_unit_label.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        
        # Motor-Kühlmitteltemperatur
        coolant_temp_label = tk.Label(self.root, text="Motor-Kühlmitteltemperatur:")
        coolant_temp_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        coolant_temp_value_label = tk.Label(self.root, textvariable=self.coolant_temp_value)
        coolant_temp_value_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        coolant_temp_unit_label = tk.Label(self.root, text="°C")
        coolant_temp_unit_label.grid(row=5, column=2, padx=10, pady=5, sticky="w")

        # Ladedruck
        boost_label = tk.Label(self.root, text="Ladedruck:")
        boost_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        boost_value_label = tk.Label(self.root, textvariable=self.boost_value)
        boost_value_label.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        boost_unit_label = tk.Label(self.root, text="bar")
        boost_unit_label.grid(row=6, column=2, padx=10, pady=5, sticky="w")

        # Spannung des Steuermoduls
        voltage_label = tk.Label(self.root, text="Spannung des Steuermoduls:")
        voltage_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        voltage_value_label = tk.Label(self.root, textvariable=self.voltage_value)
        voltage_value_label.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        voltage_unit_label = tk.Label(self.root, text="V")
        voltage_unit_label.grid(row=7, column=2, padx=10, pady=5, sticky="w")

        # Fahrzeugidentifikation
        vin_label = tk.Label(self.root, text="Fahrzeugidentifikation (VIN):")
        vin_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        vin_value_label = tk.Label(self.root, textvariable=self.vin_value)
        vin_value_label.grid(row=8, column=1, padx=10, pady=5, sticky="w")

    def create_menu(self):
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Optionen", menu=filemenu)
        filemenu.add_command(label="OBD-Gerät verbinden", command=self.connect_to_obd)
        filemenu.add_command(label="Datei speichern", command=self.save_data_to_file)
        filemenu.add_separator()
        filemenu.add_command(label="Programm beenden", command=self.exit_program)

        displaymenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Live Anzeigen", menu=displaymenu)
        displaymenu.add_command(label="Live Motordrehzahl", command=self.show_live_rpm_gui)
        displaymenu.add_command(label="Live Geschwindigkeit", command=self.show_live_speed_gui)
        displaymenu.add_command(label="Live Ladedruck", command=self.show_live_boost_gui)
        
        test_bench = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Prüfstand", menu=test_bench)
        test_bench.add_command(label="Live Prüstand", command=self.show_live_test_bench_gui)

        self.root.config(menu=menubar)

    def connect_to_obd(self):
        try:
            self.connection = obd.OBD()  # automatische Verbindung zum USB- oder RF-Port
            if self.connection.is_connected():
                self.update_status_title("Verbunden")
                messagebox.showinfo("Verbindung erfolgreich", "Erfolgreich mit OBD-Gerät verbunden.")
                self.read_obd_data()
            else:
                self.update_status_title("Nicht verbunden")
                messagebox.showerror("Verbindung fehlgeschlagen", "Verbindung zum OBD-Gerät fehlgeschlagen.")
        except Exception as e:
            self.update_status_title("Nicht verbunden")
            messagebox.showerror("Verbindungsfehler", f"Ein Fehler ist aufgetreten: {e}")

    def read_obd_data(self):
        try:
            rpm_response = self.connection.query(obd.commands.RPM)
            rpm_val = rpm_response.value.magnitude if not rpm_response.is_null() else None
            self.rpm_value.set(f"{rpm_val} U/min" if rpm_val is not None and rpm_val <= 8000 else "Keine Daten")

            speed_response = self.connection.query(obd.commands.SPEED)
            self.speed_value.set(f"{speed_response.value.magnitude} km/h" if not speed_response.is_null() else "Keine Daten")

            oil_temp_response = self.connection.query(obd.commands.ENGINE_COOLANT_TEMP)
            self.oil_temp_value.set(f"{oil_temp_response.value.magnitude} °C" if not oil_temp_response.is_null() else "Keine Daten")
            
            coolant_temp_response = self.connection.query(obd.commands.COOLANT_TEMP)
            self.coolant_temp_value.set(f"{coolant_temp_response.value.magnitude} °C" if not coolant_temp_response.is_null() else "Keine Daten")

            boost_response = self.connection.query(obd.commands.INTAKE_PRESSURE)
            boost_val_kpa = boost_response.value.magnitude if not boost_response.is_null() else None
            boost_val_bar = boost_val_kpa / 100 if boost_val_kpa is not None else None
            self.boost_value.set(f"{boost_val_bar} bar" if boost_val_bar is not None else "Keine Daten")

            fuel_gauge_response = self.connection.query(obd.commands.FUEL_LEVEL)
            self.fuel_gauge_value.set(f"{fuel_gauge_response.value.magnitude} %" if not fuel_gauge_response.is_null() else "Keine Daten")

            vin_response = self.connection.query(obd.commands.VIN)
            self.vin_value.set(vin_response.value if not vin_response.is_null() else "Keine Daten")

            voltage_response = self.connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
            self.voltage_value.set(f"{voltage_response.value.magnitude} V" if not voltage_response.is_null() else "Keine Daten")

        except Exception as e:
            messagebox.showerror("Fehler beim Datenabruf", f"Ein Fehler ist aufgetreten: {e}")

    def save_data_to_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write("Tank Inhalt: " + self.fuel_gauge_value.get() + "\n")
                    file.write("Drehzahl: " + self.rpm_value.get() + "\n")
                    file.write("Geschwindigkeit: " + self.speed_value.get() + "\n")
                    file.write("Öltemperatur: " + self.oil_temp_value.get() + "\n")
                    file.write("Motor-Kühlmitteltemperatur: " + self.coolant_temp_value.get() + "\n")
                    file.write("Ladedruck: " + self.boost_value.get() + "\n")
                    file.write("Spannung des Steuermoduls: " + self.voltage_value.get() + "\n")
                    file.write("Fahrzeugidentifikation (VIN): " + self.vin_value.get() + "\n")
                messagebox.showinfo("Datei gespeichert", "Die Daten wurden erfolgreich in die Datei gespeichert.")
        except Exception as e:
            messagebox.showerror("Fehler beim Speichern", f"Ein Fehler ist aufgetreten: {e}")

    def exit_program(self):
        self.root.quit()

    def update_status_title(self, status):
        self.root.title(f"Steuergerät auslesen - Status: {status}")

    def show_live_rpm_gui(self):
        live_rpm_window = tk.Toplevel(self.root)
        live_rpm_window.title("Live Motordrehzahl")
        live_rpm_window.geometry('600x400')

        fig = plt.Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.set_xlabel("Zeit (s)")
        ax.set_ylabel("RPM")
        ax.set_title("Live Motordrehzahl")
        ax.set_xlim([0, 120])
        ax.set_ylim([0, 8000])
        rpm_values = []

        # Label für die aktuelle Drehzahl
        current_rpm_label = tk.Label(live_rpm_window, textvariable=self.rpm_value, fg='red')
        current_rpm_label.pack()

        canvas = FigureCanvasTkAgg(fig, master=live_rpm_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def update_plot():
            nonlocal rpm_values
            if self.connection:
                response = self.connection.query(obd.commands.RPM)
                rpm = response.value.magnitude if not response.is_null() else None
                rpm_values.append(rpm)
                ax.clear()
                ax.plot(np.arange(0, len(rpm_values)*10, 10), rpm_values, color='b', marker='o')
                ax.set_xlabel("Zeit (s)")
                ax.set_ylabel("RPM")
                ax.set_title("Live Motordrehzahl")
                canvas.draw()

                # Aktuelle Drehzahl aktualisieren
                self.rpm_value.set(f"Aktuelle Drehzahl: {rpm} U/min" if rpm is not None and rpm <= 8000 else "Keine Daten")

            update_plot_job = self.root.after(1000, update_plot)

        update_plot()

    def show_live_speed_gui(self):
        live_speed_window = tk.Toplevel(self.root)
        live_speed_window.title("Live Geschwindigkeit")
        live_speed_window.geometry('600x400')

        fig = plt.Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.set_xlabel("Zeit (s)")
        ax.set_ylabel("Geschwindigkeit (km/h)")
        ax.set_title("Live Geschwindigkeit")
        ax.set_xlim([0, 120])
        ax.set_ylim([0, 400])
        speed_values = []

        # Label für die aktuelle Geschwindigkeit
        current_speed_label = tk.Label(live_speed_window, textvariable=self.speed_value, fg='red')
        current_speed_label.pack()

        canvas = FigureCanvasTkAgg(fig, master=live_speed_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def update_plot():
            nonlocal speed_values
            if self.connection:
                response = self.connection.query(obd.commands.SPEED)
                speed = response.value.magnitude if not response.is_null() else None
                speed_values.append(speed)
                ax.clear()
                ax.plot(np.arange(0, len(speed_values)*10, 10), speed_values, color='g', marker='o')
                ax.set_xlabel("Zeit (s)")
                ax.set_ylabel("Geschwindigkeit (km/h)")
                ax.set_title("Live Geschwindigkeit")
                canvas.draw()

                # Aktuelle Geschwindigkeit aktualisieren
                self.speed_value.set(f"Aktuelle Geschwindigkeit: {speed} km/h" if speed is not None else "Keine Daten")

            update_plot_job = self.root.after(1000, update_plot)

        update_plot()

    def show_live_boost_gui(self):
        live_boost_window = tk.Toplevel(self.root)
        live_boost_window.title("Live Ladedruck")
        live_boost_window.geometry('600x400')

        fig = plt.Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.set_xlabel("Zeit (s)")
        ax.set_ylabel("Ladedruck (bar)")
        ax.set_title("Live Ladedruck")
        ax.set_xlim([0, 120])
        ax.set_ylim([0, 3])
        boost_values = []

        # Label für die aktuelle Drehzahl
        current_boost_label = tk.Label(live_boost_window, textvariable=self.boost_value, fg='red')
        current_boost_label.pack()

        canvas = FigureCanvasTkAgg(fig, master=live_boost_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def update_plot():
            nonlocal boost_values
            if self.connection:
                response = self.connection.query(obd.commands.INTAKE_PRESSURE)
                boost_kpa = response.value.magnitude if not response.is_null() else None
                boost_bar = boost_kpa / 100 if boost_kpa is not None else None
                boost_values.append(boost_bar)
                ax.clear()
                ax.plot(np.arange(0, len(boost_values)*10, 10), boost_values, color='r', marker='o')
                ax.set_xlabel("Zeit (s)")
                ax.set_ylabel("Ladedruck (bar)")
                ax.set_title("Live Ladedruck")
                canvas.draw()

                # Aktuellen Ladedruck aktualisieren
                self.boost_value.set(f"Aktueller Ladedruck: {boost_bar} bar" if boost_bar is not None else "Keine Daten")

            update_plot_job = self.root.after(1000, update_plot)

        update_plot()

    def show_live_test_bench_gui(self):
        live_test_bench_window = tk.Toplevel(self.root)
        live_test_bench_window.title("Live Prüfstand")
        live_test_bench_window.geometry('600x400')

        fig = plt.Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        ax.set_xlabel("Zeit (m)")
        ax.set_ylabel("Werte")
        ax.set_title("Live Prüfstand")
        ax.set_xlim([0, 10])

        rpm_values = []
        speed_values = []
        boost_values = []

        canvas = FigureCanvasTkAgg(fig, master=live_test_bench_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def update_plot():
            nonlocal rpm_values, speed_values, boost_values
            if self.connection:
                # RPM
                rpm_response = self.connection.query(obd.commands.RPM)
                rpm = rpm_response.value.magnitude if not rpm_response.is_null() else None
                rpm_values.append(rpm)

                # Speed
                speed_response = self.connection.query(obd.commands.SPEED)
                speed = speed_response.value.magnitude if not speed_response.is_null() else None
                speed_values.append(speed)

                # Boost
                boost_response = self.connection.query(obd.commands.INTAKE_PRESSURE)
                boost_kpa = boost_response.value.magnitude if not boost_response.is_null() else None
                boost_bar = boost_kpa / 100 if boost_kpa is not None else None
                boost_values.append(boost_bar)

                ax.clear()
                # Plotting RPM with color based on value
                rpm_color = 'red' if rpm and rpm <= 4000 else 'red'  # Example color condition
                ax.plot(np.arange(0, len(rpm_values)*10, 10), rpm_values, label="RPM", color=rpm_color, marker='o')

                # Plotting Speed with color based on value
                speed_color = 'green' if speed and speed <= 100 else 'green'  # Example color condition
                ax.plot(np.arange(0, len(speed_values)*10, 10), speed_values, label="Geschwindigkeit", color=speed_color, marker='o')

                # Plotting Boost with color based on value
                boost_color = 'yellow' if boost_bar and boost_bar <= 1.5 else 'yellow'  # Example color condition
                ax.plot(np.arange(0, len(boost_values)*10, 10), boost_values, label="Ladedruck", color=boost_color, marker='o')

                ax.legend()
                ax.set_xlabel("Zeit (m)")
                ax.set_ylabel("Werte")
                ax.set_title("Live Prüfstand")
                canvas.draw()

        update_plot()

        update_plot_job = self.root.after(1000, update_plot)

if __name__ == "__main__":
    root = tk.Tk()
    obd_gui = OBDGUI(root)
    root.mainloop()
