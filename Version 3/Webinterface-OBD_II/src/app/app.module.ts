import { NgModule, isDevMode } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterModule } from '@angular/router';
import { routes } from './app.routes';
import { StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { EffectsModule } from '@ngrx/effects';
import { OBDEffects } from './store/obd-data.effects';
import { OBDDataReducer } from './store/obd-data.reducer';

import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatDividerModule } from '@angular/material/divider';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';

import { AppComponent } from './app.component';
import { StatusComponent } from './module/status/status.component';
import { ToolbarComponent } from './component/toolbar/toolbar.component';
import { MotorlastComponent } from './module/motorlast/motorlast.component';
import { PruefstandComponent } from './module/pruefstand/pruefstand.component';
import { LiveanzeigeComponent } from './module/liveanzeige/liveanzeige.component';
import { BauteileComponent } from './module/bauteile/bauteile.component';
import { HomeComponent } from './component/home/home.component';
import { InfoComponent } from './module/info/info.component';
import { NgChartsModule } from 'ng2-charts';
import { ExportDialogComponent } from './module/export-dialog/export-dialog.component';
import { InfoDataComponent } from './component/info-data/info-data.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ToolbarComponent,
    BauteileComponent,
    InfoComponent,
    LiveanzeigeComponent,
    MotorlastComponent,
    PruefstandComponent,
    StatusComponent,
    ExportDialogComponent,
    InfoDataComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    BrowserAnimationsModule,
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    MatDividerModule,
    MatIconModule,
    MatListModule,
    MatToolbarModule,
    StoreModule.forRoot({
      obddata: OBDDataReducer
    }),
    EffectsModule.forRoot([OBDEffects, ]),
    StoreDevtoolsModule.instrument({ maxAge: 25, logOnly: false }),
    NgChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
