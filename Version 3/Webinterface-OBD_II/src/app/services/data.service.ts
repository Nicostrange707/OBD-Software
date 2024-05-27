import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from "rxjs";
import { catchError } from "rxjs/operators";

@Injectable({
    providedIn: "root"
})
export class DataService {
    private baseUrl = 'http://192.168.178.62:5000/data';

    constructor(private http: HttpClient) {}

    getData(): Observable<any> {
        return this.http.get<any>(`${this.baseUrl}/data`)
            .pipe(
                catchError(this.handleError)
            );
    }

    getRpm(): Observable<number> {
        return this.http.get<number>(`${this.baseUrl}/rpm`)
            .pipe(
                catchError(this.handleError)
            );
    }

    getPsi(): Observable<number> {
        return this.http.get<number>(`${this.baseUrl}/psi`)
            .pipe(
                catchError(this.handleError)
            );
    }

    getSpeed(): Observable<number> {
        return this.http.get<number>(`${this.baseUrl}/speed`)
            .pipe(
                catchError(this.handleError)
            );
    }

    private handleError(error: HttpErrorResponse) {
        let errorMessage = 'Unknown error!';
        if (error.error instanceof ErrorEvent) {
            // Client-side errors
            errorMessage = `Error: ${error.error.message}`;
        } else {
            // Server-side errors
            errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
        }
        return throwError(errorMessage);
    }
}
