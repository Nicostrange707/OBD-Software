import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import obd
import numpy as np

class LiveRpmGui:
    def __init__(self, parent, connection, rpm_value):
        self.parent = parent
        self.connection = connection
        self.rpm_value = rpm_value
        self.start_time = 0  # Startzeit für die Zeiterfassung

        live_rpm_window = tk.Toplevel(parent)
        live_rpm_window.title("Live Motordrehzahl")
        live_rpm_window.geometry('600x400')

        self.fig = plt.Figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Zeit (s)")
        self.ax.set_ylabel("RPM")
        self.ax.set_title("Live Motordrehzahl")
        self.ax.set_xlim([0, 60])  # Initial 60 Sekunden
        self.ax.set_ylim([0, 8000])
        self.rpm_values = []

        # Label für die aktuelle Drehzahl
        self.current_rpm_label = tk.Label(live_rpm_window, textvariable=self.rpm_value, fg='red')
        self.current_rpm_label.pack()

        self.canvas = FigureCanvasTkAgg(self.fig, master=live_rpm_window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_plot()

    def update_plot(self):
        if self.connection:
            response = self.connection.query(obd.commands.RPM)
            rpm = response.value.magnitude if not response.is_null() else None
            self.rpm_values.append(rpm)

            # Aktualisiere die maximale Zeit auf der X-Achse
            self.ax.set_xlim([0, len(self.rpm_values)*10])

            # Aktualisiere die Startzeit, wenn es die erste Iteration ist
            if len(self.rpm_values) == 1:
                self.start_time = self.parent.after_idle(self._get_current_time)

            self.ax.clear()
            self.ax.plot(np.arange(0, len(self.rpm_values)*10, 10), self.rpm_values, color='b', marker='o')
            self.ax.set_xlabel("Zeit (s)")
            self.ax.set_ylabel("RPM")
            self.ax.set_title("Live Motordrehzahl")
            self.canvas.draw()

            # Aktuelle Drehzahl aktualisieren
            self.rpm_value.set(f"Aktuelle Drehzahl: {rpm} U/min" if rpm is not None and rpm <= 8000 else "Keine Daten")

        update_plot_job = self.parent.after(1000, self.update_plot)

    def _get_current_time(self):
        # Berechne die aktuelle Zeit seit Beginn
        current_time = (self.parent.after(time_since_start := self.parent.after_cancel(self.start_time)) - time_since_start) / 1000
        return current_time
