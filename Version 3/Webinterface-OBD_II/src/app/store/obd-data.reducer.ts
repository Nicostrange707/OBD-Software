import { createReducer, on } from "@ngrx/store";
import * as OBDActions from "./obd-data.actions";
import { OBDState, initialOBDState } from "./state";

export const OBDDataReducer = createReducer(
  initialOBDState,
  on(
    OBDActions.loadObdDataSuccess,
    (state, { data }): OBDState => {
      return { ...state, data: data };
    }
  )
);
