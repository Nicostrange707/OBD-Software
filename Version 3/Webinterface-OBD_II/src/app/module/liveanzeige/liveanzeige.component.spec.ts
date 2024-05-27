import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LiveanzeigeComponent } from './liveanzeige.component';

describe('LiveanzeigeComponent', () => {
  let component: LiveanzeigeComponent;
  let fixture: ComponentFixture<LiveanzeigeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LiveanzeigeComponent]
    });
    fixture = TestBed.createComponent(LiveanzeigeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
