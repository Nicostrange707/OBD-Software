import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BauteileComponent } from './bauteile.component';

describe('BauteileComponent', () => {
  let component: BauteileComponent;
  let fixture: ComponentFixture<BauteileComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BauteileComponent]
    });
    fixture = TestBed.createComponent(BauteileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
