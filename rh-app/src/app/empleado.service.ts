import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Empleado } from './empleado';

@Injectable({
  providedIn: 'root'
})
export class EmpleadoServicio {
  private http = inject(HttpClient);
  private urlBase = 'http://localhost:8080/api/empleados';

  obtenerEmpleados(): Observable<Empleado[]> {
    return this.http.get<Empleado[]>(this.urlBase);
  }

  agregarEmpleado(empleado: Empleado): Observable<Empleado> {
    const { idEmpleado, ...empleadoSinId } = empleado;
    return this.http.post<Empleado>(this.urlBase, empleadoSinId);
  }

  obtenerEmpleadoPorId(id: number): Observable<Empleado> {
    return this.http.get<Empleado>(`${this.urlBase}/${id}`);
  }

  editarEmpleado(id: number, empleado: Empleado): Observable<Empleado> {
    return this.http.put<Empleado>(`${this.urlBase}/${id}`, empleado);
  }

  eliminarEmpleado(id: number): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.urlBase}/${id}`);
  }
}