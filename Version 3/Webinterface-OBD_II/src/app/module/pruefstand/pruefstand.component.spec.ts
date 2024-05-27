import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PruefstandComponent } from './pruefstand.component';

describe('PruefstandComponent', () => {
  let component: PruefstandComponent;
  let fixture: ComponentFixture<PruefstandComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PruefstandComponent]
    });
    fixture = TestBed.createComponent(PruefstandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
