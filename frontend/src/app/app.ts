import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('frontend');
  private n : number = 0;

  public readN(n: string){

    this.n = parseInt(n);
  }


  public giveMeMyButtons(){
    let html : string = '';
    for (let i = 0; i < this.n; i++) {
      for (let j = 0; j < this.n; j++) {
        html += '<input type="text" inputmode="numeric" pattern="[0-9]" class="`"a[i][j]"`" ';
      }
    }

    console.log(html);
    return html
  }
  
}