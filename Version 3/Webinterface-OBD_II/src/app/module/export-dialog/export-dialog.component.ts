import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-export-dialog',
  templateUrl: './export-dialog.component.html',
  styleUrls: ['./export-dialog.component.scss']
})
export class ExportDialogComponent {
  constructor(public dialogRef: MatDialogRef<ExportDialogComponent>) { }

  onCancelClick(): void {
    this.dialogRef.close();
  }


  onExportClick(): void {
    
    console.log('Exportieren...');
    this.dialogRef.close();
  }
}
