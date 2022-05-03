import { Component } from '@angular/core';
import { ThemesService } from './service/themes.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'kryon-fhir';
  theme_value = false;
  constructor(

    private themesService: ThemesService
  ) {
    this.theme()
  }
  theme() {
   this.theme_value = !this.theme_value;
   console.log(this.theme_value);
   if (this.theme_value == false) {
   this.themesService.theme_change('dark');
     
   } else {
   this.themesService.theme_change('light');
     
   }

   
  }


}
