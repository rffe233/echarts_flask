import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {film} from './film'


@Injectable({
  providedIn: 'root'
})
export class filmService {
  private apiUrl = 'http://localhost:5000/api/films/count_by_year'
  private apiUrl1 = 'http://localhost:5000/api/films/count_by_type'
  private apiUrl2='http://localhost:5000/api/films/avg_rate_by_region'
  private apiUrl3='http://localhost:5000/api/films/ratenum_by_year'
  private apiUrl4='http://localhost:5000/api/films/type_rate'
  private apiUrl5='http://localhost:5000/api/films/ratenum_by_year'
  private apiUrl6='http://127.0.0.1:5000/api/films/film_number'
  private apiUrl7='http://localhost:5000/api/films/film_rate'
  private apiUrl8='http://localhost:5000/api/films/film_region'
  private apiUrl9='http://localhost:5000/api/films/film_time'
  private apiUrl10='http://localhost:5000/api/films/gooddirector'
  private apiUrl11='http://localhost:5000/api/films/goodactor'
  private apiUrl12='http://localhost:5000/api/films/bestrate'
  private apiUrl13='http://localhost:5000/api/films/bestratenum'
  private apiUrl14='http://localhost:5000/api/films/longestruntime'
  private apiUrl15='http://localhost:5000/api/films/worstrate'
  private apiUrl16='http://localhost:5000/api/films/rate_by_year'


  constructor(private http: HttpClient) { }

  getFilmCountByYear(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
  getFilmCountByType(): Observable<any> {
    return this.http.get<any>(this.apiUrl1);
  }
  getFilmTypeByYear(): Observable<any> {
    return this.http.get<any>(this.apiUrl4);
  }
  getFilmNumber(): Observable<any> {
    return this.http.get<any>(this.apiUrl6);
  }
  getFilmRate(): Observable<any> {
    return this.http.get<any>(this.apiUrl7);
  }
  getFilmRegion(): Observable<any> {
    return this.http.get<any>(this.apiUrl8);
  }
  getFilmTime(): Observable<any> {
    return this.http.get<any>(this.apiUrl9);
  }
  getgood_director(): Observable<any> {
    return this.http.get<any>(this.apiUrl10);
  }
  getgood_actor(): Observable<any> {
    return this.http.get<any>(this.apiUrl11);
  }
  getbest_movie(): Observable<any> {
    return this.http.get<any>(this.apiUrl12);
  }
  getbest_rateum(): Observable<any> {
    return this.http.get<any>(this.apiUrl13);
  }
  getlongest_movie(): Observable<any> {
    return this.http.get<any>(this.apiUrl14);
  }
  getworst_movie(): Observable<any> {
    return this.http.get<any>(this.apiUrl15);
  }
  getratenum_year(): Observable<any> {
    return this.http.get<any>(this.apiUrl3);
  }

  getavg_rate_by_region(): Observable<any> {
    return this.http.get<any>(this.apiUrl2);
  }

}
