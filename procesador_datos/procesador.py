import argparse
import sys
import json
import csv
import os
from datetime import datetime

def process_txt(filepath):
    filtered = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Filtro básico: Ignorar líneas vacías o que empiecen con '#'
            if line and not line.startswith('#'):
                filtered.append(line)
    return filtered

def process_csv(filepath):
    filtered = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Filtro básico: Ignorar filas completamente vacías
            if any(cell.strip() for cell in row):
                filtered.append(row)
    return filtered

def process_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Error: El archivo JSON no es válido.")
            return []
            
    # Filtro básico: Si es una lista, sacar items vacíos o nulls
    if isinstance(data, list):
        return [item for item in data if item]
    # Si es diccionario, sacar llaves con valores vacíos
    elif isinstance(data, dict):
        return {k: v for k, v in data.items() if v}
    return data

def save_txt(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")

def save_csv(data, filepath):
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def log_activity(log_path, filename, result_msg, identifier):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{now}] Archivo: {filename} | Resultado: {result_msg} | Version/ID: {identifier}\n"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)

def main():
    parser = argparse.ArgumentParser(description="Programa de procesamiento y filtrado de datos.")
    parser.add_argument('input_file', help="Ruta del archivo de entrada (.txt, .json, .csv)")
    parser.add_argument('output_file', help="Ruta del archivo de salida")
    parser.add_argument('--id', default="manual_v1", help="Identificador o versión del cambio")
    parser.add_argument('--log', default="backup.log", help="Ruta del archivo log donde guardar la actividad")
    
    args = parser.parse_args()
    
    input_file = args.input_file
    output_file = args.output_file
    identifier = args.id
    log_file = args.log
    
    if not os.path.exists(input_file):
        print(f"Error: El archivo de entrada '{input_file}' no existe.")
        sys.exit(1)
        
    ext = os.path.splitext(input_file)[1].lower()
    
    data = None
    count = 0
    try:
        if ext == '.txt':
            data = process_txt(input_file)
            save_txt(data, output_file)
            count = len(data)
        elif ext == '.csv':
            data = process_csv(input_file)
            save_csv(data, output_file)
            count = len(data)
        elif ext == '.json':
            data = process_json(input_file)
            save_json(data, output_file)
            count = len(data) if isinstance(data, list) else len(data.keys())
        else:
            msg = f"Error: Formato no soportado ({ext})"
            print(msg)
            log_activity(log_file, input_file, msg, identifier)
            sys.exit(1)
            
        msg = f"Se filtró {count} datos"
        print(msg)
        log_activity(log_file, input_file, msg, identifier)
        
    except Exception as e:
        error_msg = f"Error durante el procesamiento: {str(e)}"
        print(error_msg)
        log_activity(log_file, input_file, error_msg, identifier)
        sys.exit(1)

if __name__ == "__main__":
    main()
