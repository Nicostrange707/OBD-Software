import { createFeatureSelector, createSelector } from "@ngrx/store";
import { AppState, OBDState } from "./state";

const selectFeature = createFeatureSelector<AppState, OBDState>('obd');

export const selectOBDData = createSelector(
    selectFeature,
    (state: OBDState) => state?.data
);

export const selectAllOBDData = createSelector(
    selectOBDData,
    (obdData) => obdData
);