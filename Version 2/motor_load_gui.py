import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import obd
import numpy as np

class MotorLoadGui:
    def __init__(self, parent, connection):
        self.parent = parent
        self.connection = connection
        self.query_sent = False

        live_test_bench_window = tk.Toplevel(parent)
        live_test_bench_window.title("MotorLast")
        live_test_bench_window.geometry('600x400')

        self.fig = plt.Figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Zeit (m)")
        self.ax.set_ylabel("Werte")
        self.ax.set_title("Motorlast")
        self.ax.set_xlim([0, 10])

        self.rpm_values = []
        self.speed_values = []
        self.boost_values = []
        self.motor_load_values = []  # Liste für die Motorlast-Werte

        self.canvas = FigureCanvasTkAgg(self.fig, master=live_test_bench_window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_plot()

    def update_plot(self):
        if self.connection:
            if not self.query_sent:
                self.query_sent = True  # Set the query_sent flag to True to prevent multiple queries

                # RPM
                rpm_response = self.connection.query(obd.commands.RPM)
                rpm = rpm_response.value.magnitude if not rpm_response.is_null() else None
                self.rpm_values.append(rpm)

                # Speed
                speed_response = self.connection.query(obd.commands.SPEED)
                speed = speed_response.value.magnitude if not speed_response.is_null() else None
                self.speed_values.append(speed)

                # Boost
                boost_response = self.connection.query(obd.commands.INTAKE_PRESSURE)
                boost_kpa = boost_response.value.magnitude if not boost_response.is_null() else None
                boost_bar = boost_kpa / 100 if boost_kpa is not None else None
                self.boost_values.append(boost_bar)

                # Calculate Motor Load
                if rpm is not None and speed is not None and boost_bar is not None:
                    motor_load = (rpm * speed) / boost_bar
                    self.motor_load_values.append(motor_load)

            self.ax.clear()
            # Plotting RPM with color based on value
            rpm_color = 'red' if self.rpm_values and self.rpm_values[-1] and self.rpm_values[-1] <= 4000 else 'red'  # Example color condition
            self.ax.plot(np.arange(0, len(self.rpm_values)*10, 10), self.rpm_values, label="RPM", color=rpm_color, marker='o')

            # Plotting Speed with color based on value
            speed_color = 'green' if self.speed_values and self.speed_values[-1] and self.speed_values[-1] <= 100 else 'green'  # Example color condition
            self.ax.plot(np.arange(0, len(self.speed_values)*10, 10), self.speed_values, label="Geschwindigkeit", color=speed_color, marker='o')

            # Plotting Boost with color based on value
            boost_color = 'yellow' if self.boost_values and self.boost_values[-1] and self.boost_values[-1] <= 1.5 else 'yellow'  # Example color condition
            self.ax.plot(np.arange(0, len(self.boost_values)*10, 10), self.boost_values, label="Ladedruck", color=boost_color, marker='o')

            # Plotting Motor Load with color based on value
            motor_load_color = 'blue' if self.motor_load_values and self.motor_load_values[-1] and self.motor_load_values[-1] <= 100 else 'blue'  # Example color condition
            self.ax.plot(np.arange(0, len(self.motor_load_values)*10, 10), self.motor_load_values, label="Motorlast", color=motor_load_color, marker='o')

            self.ax.legend()
            self.ax.set_xlabel("Zeit (m)")
            self.ax.set_ylabel("Werte")
            self.ax.set_title("Motorlast")
            self.ax.set_xlim([0, len(self.rpm_values)*10])  # Dynamically adjust X-axis limit based on the number of data points
            self.canvas.draw()

        update_plot_job = self.parent.after(1000, self.update_plot)
