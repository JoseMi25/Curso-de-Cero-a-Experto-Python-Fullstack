import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms'; 
import { Router } from '@angular/router';
import { Empleado } from '../empleado';
import { EmpleadoServicio } from '../empleado.service';

@Component({
  selector: 'app-empleado-agregar',
  standalone: true,
  imports: [FormsModule], // Necesario para formularios
  templateUrl: './empleado-agregar.component.html',
  styleUrl: './empleado-agregar.component.css'
})
export class EmpleadoAgregarComponent {
  empleado: Empleado = {
    idEmpleado: 0,
    nombre: '',
    departamento: '',
    sueldo: 0
  };

  private empleadoService = inject(EmpleadoServicio);
  private router = inject(Router);

  onSubmit() {
    this.empleadoService.agregarEmpleado(this.empleado).subscribe({
      next: (datos) => {
        console.log('Empleado agregado:', datos);
        this.irALista();
      },
      error: (error) => console.log(error)
    });
  }

  irALista() {
    this.router.navigate(['/empleados']);
  }
}