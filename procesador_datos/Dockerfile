FROM python:3.11-slim

# Creamos un directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el script de python al contenedor
COPY procesador.py /app/procesador.py

# El punto de entrada será python y nuestro script
ENTRYPOINT ["python", "procesador.py"]

# Por defecto mostramos la ayuda si no se pasan argumentos (se pueden sobrescribir)
CMD ["--help"]
