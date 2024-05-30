import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { InfoDataComponent } from '../info-data/info-data.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  constructor(public dialog: MatDialog) {}

  openInfoDialog(): void {
    this.dialog.open(InfoDataComponent);
  }
}
