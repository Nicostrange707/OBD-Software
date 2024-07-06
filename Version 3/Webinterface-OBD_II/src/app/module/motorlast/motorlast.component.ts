import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { InfoDataComponent } from 'src/app/component/info-data/info-data.component';

@Component({
  selector: 'app-motorlast',
  templateUrl: './motorlast.component.html',
  styleUrls: ['./motorlast.component.scss']
})
export class MotorlastComponent {
  constructor(public dialog: MatDialog) {}

  openInfoDialog(): void {
    this.dialog.open(InfoDataComponent);
  }
}
