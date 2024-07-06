import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { InfoDataComponent } from 'src/app/component/info-data/info-data.component';

@Component({
  selector: 'app-bauteile',
  templateUrl: './bauteile.component.html',
  styleUrls: ['./bauteile.component.scss']
})
export class BauteileComponent {
  constructor(public dialog: MatDialog) {}

  openInfoDialog(): void {
    this.dialog.open(InfoDataComponent);
  }
}
