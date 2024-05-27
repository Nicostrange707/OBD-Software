import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import obd
import numpy as np

class LiveSpeedGui:
    def __init__(self, parent, connection, speed_value):
        self.parent = parent
        self.connection = connection
        self.speed_value = speed_value
        self.start_time = 0  # Startzeit für die Zeiterfassung

        live_speed_window = tk.Toplevel(parent)
        live_speed_window.title("Live Geschwindigkeit")
        live_speed_window.geometry('800x800')

        self.fig = plt.Figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Zeit (s)")
        self.ax.set_ylabel("Geschwindigkeit (km/h)")
        self.ax.set_title("Live Geschwindigkeit")
        self.ax.set_xlim([0, 60])  # Initial 60 Sekunden
        self.ax.set_ylim([0, 400])
        self.ax.set_xticks(np.arange(0, 61, 10)) 
        self.ax.set_yticks(np.arange(0, 401, 10))
        self.speed_values = []

        # Label für die aktuelle Geschwindigkeit
        self.current_speed_label = tk.Label(live_speed_window, textvariable=self.speed_value, fg='red')
        self.current_speed_label.pack()

        self.canvas = FigureCanvasTkAgg(self.fig, master=live_speed_window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_plot()

    def update_plot(self):
        if self.connection:
            response = self.connection.query(obd.commands.SPEED)
            speed = response.value.magnitude if not response.is_null() else None
            self.speed_values.append(speed)

            # Aktualisiere die maximale Zeit auf der X-Achse
            self.ax.set_xlim([0, len(self.speed_values)])

            # Aktualisiere die Startzeit, wenn es die erste Iteration ist
            if len(self.speed_values) == 1:
                self.start_time = self.parent.after_idle(self._get_current_time)

            self.ax.clear()
            self.ax.plot(np.arange(0, len(self.speed_values)), self.speed_values, color='g', marker='o')
            self.ax.set_xlabel("Zeit (s)")
            self.ax.set_ylabel("Geschwindigkeit (km/h)")
            self.ax.set_title("Live Geschwindigkeit")
            self.canvas.draw()

            # Aktuelle Geschwindigkeit aktualisieren
            self.speed_value.set(f"Aktuelle Geschwindigkeit: {speed} km/h" if speed is not None else "Keine Daten")

        update_plot_job = self.parent.after(1000, self.update_plot)

    def _get_current_time(self):
        # Berechne die aktuelle Zeit seit Beginn
        current_time = (self.parent.after(time_since_start := self.parent.after_cancel(self.start_time)) - time_since_start) / 1000
        return current_time
