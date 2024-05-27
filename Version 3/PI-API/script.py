from flask import Flask, jsonify, send_file
import obd
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "OBD-II API"

@app.route('/data')
def get_obd_data():
    data = {}
    try:
        # Verbindung zum OBD-II-Bus aufbauen
        connection = obd.OBD()
        if connection.is_connected():
            cmd_list = [obd.commands.SPEED, obd.commands.RPM, obd.commands.THROTTLE_POS]
            for cmd in cmd_list:
                response = connection.query(cmd)
                if response.is_null():
                    data[cmd.name] = "N/A"
                else:
                    data[cmd.name] = response.value.magnitude
            return jsonify({"status": "success", "data": data})
        else:
            return jsonify({"status": "error", "message": "Keine Verbindung zur OBD-II-Schnittstelle hergestellt"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/export')
def export_obd_data():
    try:
        data = {}
        # Verbindung zum OBD-II-Bus aufbauen
        connection = obd.OBD()
        if connection.is_connected():
            cmd_list = [obd.commands.SPEED, obd.commands.RPM, obd.commands.THROTTLE_POS]
            for cmd in cmd_list:
                response = connection.query(cmd)
                if response.is_null():
                    data[cmd.name] = "N/A"
                else:
                    data[cmd.name] = response.value.magnitude

            # Exportieren der Daten in eine CSV-Datei
            file_path = 'obd_data.csv'
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Command', 'Value'])
                for key, value in data.items():
                    writer.writerow([key, value])
            
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({"status": "error", "message": "Keine Verbindung zur OBD-II-Schnittstelle hergestellt"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)