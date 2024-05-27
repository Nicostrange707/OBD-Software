import { OBDData } from "./models/data.model";


export interface OBDState {
    data: OBDData|null
}

export interface AppState {
    obd: OBDState,
    obddata: OBDData,
}

export const initialOBDState: OBDState = {
    data: null,
};