import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ThemesService {
  constructor() { }
  theme_change(param:string): void {
    document.documentElement.setAttribute('theme', param);

  }
}
