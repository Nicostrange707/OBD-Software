import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-export-dialog',
  templateUrl: './export-dialog.component.html',
  styleUrls: ['./export-dialog.component.scss']
})
export class ExportDialogComponent {
  exportOptionsForm: FormGroup;

  constructor(
    public dialogRef: MatDialogRef<ExportDialogComponent>,
    private snackBar: MatSnackBar,
    private fb: FormBuilder
  ) {
    this.exportOptionsForm = this.fb.group({
      option1: false,
      option2: false,
      option3: false,
      option4: false,
      option5: false,
      option6: false,
      option7: false,
      option8: false,
      option9: false,
    });
  }

  onCancelClick(): void {
    this.dialogRef.close();
    this.snackBar.open('Export abgebrochen', 'Schließen', {
      duration: 2000,
    });
  }

  onExportClick(): void {
    const selectedOptions = this.exportOptionsForm.value;
    console.log('Selected options:', selectedOptions);
    this.dialogRef.close(selectedOptions);
    this.snackBar.open('Export gestartet', 'Schließen', {
      duration: 2000,
    });
  }

  onAllExportClick(): void{
    const selectedOptions = this.exportOptionsForm.value;
    console.log('Selected options:', selectedOptions);
    this.dialogRef.close(selectedOptions);
    this.snackBar.open('Export gestartet', 'Schließen', {
      duration: 2000,
    });
  }
}
