import { Component, inject, OnInit, ChangeDetectorRef } from '@angular/core'; // 1. Importar ChangeDetectorRef
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Empleado } from '../empleado';
import { EmpleadoServicio } from '../empleado.service';

@Component({
  selector: 'app-empleado-editar',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './empleado-editar.component.html',
  styleUrl: './empleado-editar.component.css'
})
export class EmpleadoEditarComponent implements OnInit {
  empleado: Empleado = { idEmpleado: 0, nombre: '', departamento: '', sueldo: 0 };
  
  private empleadoService = inject(EmpleadoServicio);
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private cdr = inject(ChangeDetectorRef); // 2. Inyectar el detector de cambios

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.empleadoService.obtenerEmpleadoPorId(Number(id)).subscribe({
        next: (datos) => {
          this.empleado = datos;
          this.cdr.detectChanges();
          console.log('Datos cargados y vista actualizada:', this.empleado);
        },
        error: (errores) => console.log(errores)
      });
    }
  }

  onSubmit() {
    this.empleadoService.editarEmpleado(this.empleado.idEmpleado, this.empleado).subscribe({
      next: (datos) => {
        this.irALista();
      },
      error: (errores) => console.log(errores)
    });
  }

  irALista() {
    this.router.navigate(['/empleados']);
  }
}