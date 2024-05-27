import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import obd
import numpy as np

class LiveBoostGui:
    def __init__(self, parent, connection, boost_value):
        self.parent = parent
        self.connection = connection
        self.boost_value = boost_value

        self.live_boost_window = tk.Toplevel(parent)
        self.live_boost_window.title("Live Ladedruck")
        self.live_boost_window.geometry('600x400')

        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.setup_plot()

        self.current_boost_label = tk.Label(self.live_boost_window, textvariable=self.boost_value, fg='red')
        self.current_boost_label.pack()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.live_boost_window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_plot()

    def setup_plot(self):
        self.ax.set_xlabel("Zeit (s)")
        self.ax.set_ylabel("Ladedruck (bar)")
        self.ax.set_title("Live Ladedruck")
        self.ax.set_xlim([0, 60])  # Initial 60 Sekunden
        self.ax.set_ylim([0, 3])
        self.boost_values = []

    def update_plot(self):
        if self.connection:
            response = self.connection.query(obd.commands.INTAKE_PRESSURE)
            boost_kpa = response.value.magnitude if not response.is_null() else None
            boost_bar = boost_kpa / 100 if boost_kpa is not None else None
            self.boost_values.append(boost_bar)

            # Aktualisiere die maximale Zeit auf der X-Achse
            self.ax.set_xlim([0, len(self.boost_values)*10])

            self.ax.clear()
            self.ax.plot(np.arange(0, len(self.boost_values)*10, 10), self.boost_values, color='r', marker='o')
            self.setup_plot()  # Wiederholtes Setup des Plots ist nicht erforderlich
            self.canvas.draw()

            # Aktuellen Ladedruck aktualisieren
            self.boost_value.set(f"Aktueller Ladedruck: {boost_bar} bar" if boost_bar is not None else "Keine Daten")

        update_plot_job = self.parent.after(1000, self.update_plot)
