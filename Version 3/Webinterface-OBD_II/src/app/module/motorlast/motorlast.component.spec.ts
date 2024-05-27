import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MotorlastComponent } from './motorlast.component';

describe('MotorlastComponent', () => {
  let component: MotorlastComponent;
  let fixture: ComponentFixture<MotorlastComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MotorlastComponent]
    });
    fixture = TestBed.createComponent(MotorlastComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
