import { Routes } from "@angular/router";
import { MotorlastComponent } from "./module/motorlast/motorlast.component";
import { PruefstandComponent } from "./module/pruefstand/pruefstand.component";
import { LiveanzeigeComponent } from "./module/liveanzeige/liveanzeige.component";
import { BauteileComponent } from "./module/bauteile/bauteile.component";
import { HomeComponent } from "./component/home/home.component";
import { DataExportComponent } from "./module/data-export/data-export.component";

const defaultRoute = 'home';

export const routes: Routes = [
    {
        path: '',
        redirectTo: defaultRoute,
        pathMatch: 'full',
    },
    {
        path: 'home',
        component: HomeComponent
    },
    {
        path: 'bauteile',
        component: BauteileComponent
    },
    {
        path: 'liveanzeige',
        component: LiveanzeigeComponent
    },
    {
        path: 'prüfstand',
        component: PruefstandComponent
    },
    {
        path: 'motorlast',
        component: MotorlastComponent
    },
    {
        path: 'export',
        component: DataExportComponent
    }
]