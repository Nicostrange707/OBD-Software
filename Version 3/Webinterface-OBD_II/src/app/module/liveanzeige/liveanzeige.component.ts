import { Component, OnInit } from '@angular/core';
import { Chart } from 'chart.js';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-liveanzeige',
  templateUrl: './liveanzeige.component.html',
  styleUrls: ['./liveanzeige.component.scss']
})
export class LiveanzeigeComponent implements OnInit {

  rpmChart: any;
  psiChart: any;
  speedChart: any;

  rpmData: number[] = [];
  psiData: number[] = [];
  speedData: number[] = [];
  timeData: number[] = [];
  startTime: number = Date.now();

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.initializeCharts();
    this.updateCharts();
  }

  initializeCharts() {
    // Initialize RPM Chart
    const rpmCtx = document.getElementById('rpmChart') as HTMLCanvasElement;
    this.rpmChart = new Chart(rpmCtx, {
      type: 'line',
      data: {
        labels: this.timeData,
        datasets: [{
          label: 'RPM',
          data: this.rpmData,
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
          fill: false
        }]
      },
      options: {
        scales: {
          x: {
            type: 'linear',
            title: {
              display: true,
              text: 'Zeit (Sekunden)'
            },
            min: 0,
            max: 60
          },
          y: {
            title: {
              display: true,
              text: 'RPM'
            },
            min: 0,
            max: 8000
          }
        }
      }
    });

    // Initialize PSI Chart
    const psiCtx = document.getElementById('psiChart') as HTMLCanvasElement;
    this.psiChart = new Chart(psiCtx, {
      type: 'line',
      data: {
        labels: this.timeData,
        datasets: [{
          label: 'PSI',
          data: this.psiData,
          borderColor: 'rgba(192, 75, 192, 1)',
          borderWidth: 1,
          fill: false
        }]
      },
      options: {
        scales: {
          x: {
            type: 'linear',
            title: {
              display: true,
              text: 'Zeit (Sekunden)'
            },
            min: 0,
            max: 60
          },
          y: {
            title: {
              display: true,
              text: 'PSI'
            },
            min: 0,
            max: 100 // Adjust this as needed
          }
        }
      }
    });

    // Initialize Speed Chart
    const speedCtx = document.getElementById('speedChart') as HTMLCanvasElement;
    this.speedChart = new Chart(speedCtx, {
      type: 'line',
      data: {
        labels: this.timeData,
        datasets: [{
          label: 'Speed',
          data: this.speedData,
          borderColor: 'rgba(192, 192, 75, 1)',
          borderWidth: 1,
          fill: false
        }]
      },
      options: {
        scales: {
          x: {
            type: 'linear',
            title: {
              display: true,
              text: 'Zeit (Sekunden)'
            },
            min: 0,
            max: 60
          },
          y: {
            title: {
              display: true,
              text: 'Speed (km/h)'
            },
            min: 0,
            max: 300 // Adjust this as needed
          }
        }
      }
    });
  }

  updateCharts() {
    setInterval(() => {
      const currentTime = (Date.now() - this.startTime) / 1000;
      if (currentTime <= 60) {
        this.timeData.push(currentTime);
        this.dataService.getRpm().subscribe(rpm => {
          this.rpmData.push(rpm);
          this.rpmChart.update();
        });
        this.dataService.getPsi().subscribe(psi => {
          this.psiData.push(psi);
          this.psiChart.update();
        });
        this.dataService.getSpeed().subscribe(speed => {
          this.speedData.push(speed);
          this.speedChart.update();
        });
      }
    }, 1000); // Update every second
  }
}
