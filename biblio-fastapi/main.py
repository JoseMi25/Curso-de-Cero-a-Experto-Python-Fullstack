from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import necesario
from api import libros

app = FastAPI(
    title="Biblioteca Personal API",
    description="API REST para administrar libros personales",
    version="1.0.0"
)

# Configuración de Orígenes Permitidos
# Lista de URLs de frontend que tendrán permiso para consultar esta API
origins = [
    "http://localhost:5173", # Puerto por defecto de Vite (React/Vue)
    "http://localhost:4200", # Puerto por defecto de Angular
    "http://localhost:3000", # Puerto común de React Create App
    "http://localhost:8080", # El mismo backend (por si acaso)
]

# Agregar el Middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Qué dominios pueden entrar
    allow_credentials=True,     # Permitir cookies/auth headers
    allow_methods=["*"],        # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],        # Permitir todos los headers
)

app.include_router(libros.router)

@app.get("/")
def index():
    return {"mensaje": "Bienvenido a la API de Biblioteca Personal"}