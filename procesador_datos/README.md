# Procesador de Datos en Docker

Este es un programa en Python que lee y procesa archivos en formato `.txt`, `.csv` o `.json`, filtrando datos vacíos y guardando un log de ejecución (`backup.log`) junto al archivo procesado.

## ¿Cómo ejecutar el contenedor Docker?

El programa en Python requiere los siguientes argumentos:
1. `input_file`: Ruta del archivo de entrada a procesar.
2. `output_file`: Ruta del archivo de salida.
3. `--id`: (Opcional) Identificador o versión del cambio (por defecto `manual_v1`).
4. `--log`: (Opcional) Ruta del historial `backup.log`.

### 1. Construir la imagen de Docker

Abre tu terminal (PowerShell) en la carpeta donde esté el Dockerfile (`c:\Users\lolo3\Desktop\Clase 15\procesador_datos`) y ejecuta:

```powershell
docker build -t processor-bot .
```

### 2. Procesar tus archivos (Usando Volúmenes)

Como el programa debe leer los archivos de tu computadora y dejar ahí los resultados y un log, debes montar la carpeta de datos locales usando la bandera `-v`. Hemos proporcionado datos de prueba dentro de la carpeta `data/`.

**Para procesar el archivo CSV de ejemplo:**
```powershell
docker run --rm -v "${PWD}/data:/app/data" processor-bot /app/data/datos.csv /app/data/datos_procesados.csv --id "v1-csv" --log /app/data/backup.log
```

**Para procesar el archivo JSON de ejemplo:**
```powershell
docker run --rm -v "${PWD}/data:/app/data" processor-bot /app/data/datos.json /app/data/datos_procesados.json --id "v1-json" --log /app/data/backup.log
```

**Para procesar el archivo TXT de ejemplo:**
```powershell
docker run --rm -v "${PWD}/data:/app/data" processor-bot /app/data/datos.txt /app/data/datos_procesados.txt --id "v1-txt" --log /app/data/backup.log
```

### 3. Verificar los resultados

Después de correr los comandos, puedes revisar la carpeta `data/`. Deberías encontrar los archivos filtrados:
- `datos_procesados.csv`
- `datos_procesados.json`
- `datos_procesados.txt`

Y especialmente el archivo `backup.log` con el registro de la ejecución indicando fechas de proceso, cuántos datos se procesaron y tu identificador manual.
