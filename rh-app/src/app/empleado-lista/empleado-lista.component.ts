import { Component, inject, OnInit, signal } from '@angular/core';
import { Empleado } from '../empleado';
import { EmpleadoServicio } from '../empleado.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-empleado-lista',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './empleado-lista.component.html',
  styleUrl: './empleado-lista.component.css'
})
export class EmpleadoListaComponent implements OnInit {
  empleados = signal<Empleado[]>([]);
  private empleadoService = inject(EmpleadoServicio);

  ngOnInit(): void {
    this.obtenerEmpleados();
  }

  obtenerEmpleados() {
    this.empleadoService.obtenerEmpleados().subscribe({
      next: (datos: Empleado[]) => {
        this.empleados.set(datos);
      },
      error: (errores: any) => console.log(errores)
    });
  }

  // Método Nuevo Fase 4
  eliminarEmpleado(id: number) {
    const confirmar = confirm("¿Estás seguro de que deseas eliminar este empleado?");
    if (confirmar) {
      this.empleadoService.eliminarEmpleado(id).subscribe({
        next: () => {
          this.obtenerEmpleados();
        },
        error: (errores) => console.log(errores)
      });
    }
  }
}