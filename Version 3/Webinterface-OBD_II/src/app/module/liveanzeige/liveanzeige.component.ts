import { Component, OnInit } from '@angular/core';
import { Chart } from 'chart.js';
import { DataService } from '../../services/data.service';
import { MatDialog } from '@angular/material/dialog';
import { InfoDataComponent } from 'src/app/component/info-data/info-data.component';

@Component({
  selector: 'app-liveanzeige',
  templateUrl: './liveanzeige.component.html',
  styleUrls: ['./liveanzeige.component.scss']
})
export class LiveanzeigeComponent{
  constructor(public dialog: MatDialog) {}

  openInfoDialog(): void {
    this.dialog.open(InfoDataComponent);
  }
}
