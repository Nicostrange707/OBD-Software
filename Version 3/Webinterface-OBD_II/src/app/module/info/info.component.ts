import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from '../../store/state';
import * as ObdDataActions from '../../store/obd-data.actions'; 

@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.scss']
})
export class InfoComponent implements OnInit {

  vin: string = '';

  constructor(private store: Store<AppState>) { }

  ngOnInit(): void {
    this.store.dispatch(ObdDataActions.extractVin());

    this.store.select(state => state.obddata.vin)
      .subscribe((vin: string) => {
        this.vin = vin;
      });
  }
}