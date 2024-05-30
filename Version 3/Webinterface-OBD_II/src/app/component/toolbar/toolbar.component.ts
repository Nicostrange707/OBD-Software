import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ExportDialogComponent } from 'src/app/module/export-dialog/export-dialog.component';

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss']
})
export class ToolbarComponent {
  constructor(public dialog: MatDialog) { }

    openDialog(): void {
        const dialogRef = this.dialog.open(ExportDialogComponent, {
            width: '250px',
            // Weitere Konfigurationen hier...
        });

        dialogRef.afterClosed().subscribe(result => {
            console.log('Dialog geschlossen', result);
            // Hier können Sie nach dem Schließen des Dialogs weitere Aktionen ausführen.
        });
  }
}