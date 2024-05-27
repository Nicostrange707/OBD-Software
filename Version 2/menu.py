import tkinter as tk
from tkinter import messagebox, filedialog
import obd
from live_rpm_gui import LiveRpmGui
from live_speed_gui import LiveSpeedGui
from live_boost_gui import LiveBoostGui
from live_test_bench_gui import LiveTestBenchGui
from throttle_gui import ThrottleGui
from engine_gui import EngineGui
from tank_gui import TankGui
from intake_gui import IntakeGui  
from motor_load_gui import MotorLoadGui

class MenuBar:
    def __init__(self, parent):
        self.parent = parent
        self.menubar = tk.Menu(parent)
        self.create_menu()

        # Initialize OBD connection and query status
        self.connection = None
        self.query_sent = False
        self.motor_load_window = None  # Variable zur Verfolgung des Motor Load Fensters

    def create_menu(self):
        # Option menu
        self.option_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Optionen", menu=self.option_menu)
        self.update_option_menu()

        # Components menu
        self.componentsmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Bauteile", menu=self.componentsmenu)
        self.update_components_menu()

        # Display menu
        self.displaymenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Live Anzeigen", menu=self.displaymenu)
        self.update_display_menu()

        # Test bench menu
        self.test_bench_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Prüfstand", menu=self.test_bench_menu)
        self.update_test_bench_menu()
        
        # Motor load menu
        self.motor_load_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Motorlast", menu=self.motor_load_menu)
        self.update_motor_load_menu()
        
        self.parent.config(menu=self.menubar)

    def connect_to_obd(self):
        try:
            if not self.connection or not self.connection.is_connected():
                self.connection = obd.OBD() 
            if self.connection.is_connected() and not self.query_sent:
                self.query_sent = True
                messagebox.showinfo("Verbindung erfolgreich", "Erfolgreich mit OBD-Gerät verbunden.")
            elif not self.connection.is_connected():
                messagebox.showerror("Verbindung fehlgeschlagen", "Verbindung zum OBD-Gerät fehlgeschlagen.")
        except Exception as e:
            messagebox.showerror("Verbindungsfehler", f"Ein Fehler ist aufgetreten: {e}")

    def save_data_to_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write("Tank Inhalt: " + "\n")
                    file.write("Treibstoffdruck: " + "\n")
                    file.write("Drehzahl: " + "\n")
                    file.write("Geschwindigkeit: " + "\n")
                    file.write("Öltemperatur: " + "\n")
                    file.write("Motor-Kühlmitteltemperatur: " + "\n")
                    file.write("Ansauglufttemperatur: " + "\n")    
                    file.write("Ladedruck: " + "\n")
                    file.write("Ansaugkrümmerdruck: " + "\n")
                    file.write("Drosselklappenstellung: " + "\n")
                    file.write("Relative Drosselklappenstellung: " + "\n")
                    file.write("Befohlener Drosselklappensteller: " + "\n")
                    file.write("Spannung des Steuermoduls: " + "\n")
                    file.write("Fahrzeugidentifikation (VIN): " + "\n")
                messagebox.showinfo("Datei gespeichert", "Die Daten wurden erfolgreich in die Datei gespeichert.")
        except Exception as e:
            messagebox.showerror("Fehler beim Speichern", f"Ein Fehler ist aufgetreten: {e}")

    def open_motor_load_file(self):
        try:
            file_path = "motor_load.py"
            with open(file_path, "r") as file:
                content = file.read()
            messagebox.showinfo("Motor Load File", content)
        except Exception as e:
            messagebox.showerror("Fehler beim Öffnen der Datei", f"Ein Fehler ist aufgetreten: {e}")

    def exit_program(self):
        if messagebox.askokcancel("Programm schließen", "Möchtest du das Programm wirklich beenden?"):
            self.parent.quit()

    def load_throttle_gui(self):
        ThrottleGui(tk.Toplevel(self.parent))

    def load_engine_gui(self):
        EngineGui(tk.Toplevel(self.parent))

    def load_live_rpm_gui(self):
        rpm_value = tk.StringVar()
        LiveRpmGui(self.parent, self.connection, rpm_value)

    def load_live_speed_gui(self):
        speed_value = tk.StringVar()
        LiveSpeedGui(self.parent, self.connection, speed_value)

    def load_live_boost_gui(self):
        boost_value = tk.StringVar()
        LiveBoostGui(self.parent, self.connection, boost_value)

    def load_live_test_bench_gui(self):
        LiveTestBenchGui(self.parent, self.connection)

    def open_settings(self):
        settings_window = tk.Toplevel(self.parent)
        settings_window.title("Einstellungen")
        settings_window.geometry("300x150")

        version_label = tk.Label(settings_window, text="Version: 2.0")
        version_label.pack(pady=10)

    def load_tank_gui(self):
        try:
            if self.connection and self.connection.is_connected():
                fuel_type_response = self.connection.query(obd.commands.FUEL_TYPE)
                fuel_level_response = self.connection.query(obd.commands.FUEL_LEVEL)
                fuel_pressure_response = self.connection.query(obd.commands.FUEL_PRESSURE)

                fuel_type = fuel_type_response.value.magnitude if fuel_type_response and fuel_type_response.value else "N/A"
                fuel_level = fuel_level_response.value.magnitude if fuel_level_response and fuel_level_response.value else "N/A"
                fuel_pressure = fuel_pressure_response.value.magnitude if fuel_pressure_response and fuel_pressure_response.value else "N/A"

                tank_window = tk.Toplevel(self.parent)
                tank_window.title("Tank GUI")
                TankGui(tank_window, fuel_type, fuel_level, fuel_pressure)
            else:
                tank_window = tk.Toplevel(self.parent)
                tank_window.title("Tank GUI")
                TankGui(tank_window, "N/A", "N/A", "N/A")
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

    def load_intake_gui(self):  
        IntakeGui(tk.Toplevel(self.parent))  

    def load_motor_load_gui(self):
        MotorLoadGui(self.parent, self.connection)
    
    def update_option_menu(self):
        self.option_menu.delete(0, tk.END)
        self.option_menu.add_command(label="OBD-Gerät verbinden", command=self.connect_to_obd)
        self.option_menu.add_command(label="Datei speichern", command=self.save_data_to_file)
        self.option_menu.add_command(label="Einstellungen", command=self.open_settings)
        self.option_menu.add_separator()
        self.option_menu.add_command(label="Beenden", command=self.exit_program)

    def update_display_menu(self):
        self.displaymenu.delete(0, tk.END)
        self.displaymenu.add_command(label="Live Motordrehzahl", command=self.load_live_rpm_gui)
        self.displaymenu.add_command(label="Live Geschwindigkeit", command=self.load_live_speed_gui)
        self.displaymenu.add_command(label="Live Ladedruck", command=self.load_live_boost_gui)

    def update_components_menu(self):
        self.componentsmenu.delete(0, tk.END)
        self.componentsmenu.add_command(label="Drosselklappe", command=self.load_throttle_gui)
        self.componentsmenu.add_command(label="Motor", command=self.load_engine_gui)
        self.componentsmenu.add_command(label="Tank", command=self.load_tank_gui)
        self.componentsmenu.add_command(label="Ansaugung", command=self.load_intake_gui)  

    def update_test_bench_menu(self):
        self.test_bench_menu.delete(0, tk.END)
        self.test_bench_menu.add_command(label="Live Prüfstand", command=self.load_live_test_bench_gui)

    def update_motor_load_menu(self):
        self.motor_load_menu.delete(0, tk.END)
        self.motor_load_menu.add_command(label="Motorlast", command=self.load_motor_load_gui)  

    def update_menu_titles(self):
        self.menubar.entryconfig("Bauteile", label="Bauteile")
        self.menubar.entryconfig("Live Anzeigen", label="Live Anzeigen")
        self.menubar.entryconfig("Prüfstand", label="Prüfstand")

    def update_window_title(self):
        self.parent.title("Hauptfenster")

if __name__ == "__main__":
    root = tk.Tk()
    obd_menu = MenuBar(root)
    root.mainloop()