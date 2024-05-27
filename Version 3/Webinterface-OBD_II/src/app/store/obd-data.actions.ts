import { createAction, props } from "@ngrx/store";

export const loadObdData = createAction(
    '[OBD Data API] Load'
);
export const loadObdDataSuccess = createAction(
    '[OBD Data API] Load Success',
    props<{ data: any }>()
);
export const loadObdDataFailure = createAction(
    '[OBD Data API] Load Failure',
    props<{ error: any }>()
);

export const extractVin = createAction(
    '[OBD Data API] Extract VIN'
);