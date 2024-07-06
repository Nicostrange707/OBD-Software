import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { InfoDataComponent } from 'src/app/component/info-data/info-data.component';

@Component({
  selector: 'app-pruefstand',
  templateUrl: './pruefstand.component.html',
  styleUrls: ['./pruefstand.component.scss']
})
export class PruefstandComponent {
  constructor(public dialog: MatDialog) {}

  openInfoDialog(): void {
    this.dialog.open(InfoDataComponent);
  }
}
