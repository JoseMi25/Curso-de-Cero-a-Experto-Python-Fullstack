import { Routes } from '@angular/router';
import { EmpleadoListaComponent } from './empleado-lista/empleado-lista.component';
import { EmpleadoAgregarComponent } from './empleado-agregar/empleado-agregar.component';
import { EmpleadoEditarComponent } from './empleado-editar/empleado-editar.component';

export const routes: Routes = [
  { path: 'empleados', component: EmpleadoListaComponent },
  { path: 'agregar-empleado', component: EmpleadoAgregarComponent },
  { path: 'editar-empleado/:id', component: EmpleadoEditarComponent },
  { path: '', redirectTo: 'empleados', pathMatch: 'full' }
];