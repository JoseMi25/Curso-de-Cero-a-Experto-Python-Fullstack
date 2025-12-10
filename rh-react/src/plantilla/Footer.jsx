import React from 'react'

export default function Footer() {
  return (
    <div className="container-fluid bg-dark text-white text-center p-3 mt-5 border-top border-secondary">
        <p className="m-0 small">
            &copy; {new Date().getFullYear()} Sistema de Recursos Humanos | Desarrollado con Django y React
        </p>
    </div>
  )
}