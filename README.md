# Python-CLI-CSV-Data-Cleaner
CLI CSV Data Cleaner es una herramienta de línea de comandos en Python que limpia y procesa archivos CSV eliminando filas vacías y espacios en celdas. Ideal para tareas rápidas de limpieza y análisis de datos, muestra los resultados directamente en la consola. Fácil de usar y eficiente.

### Ejemplo de README Ideal para el Repositorio de GitHub


# CLI CSV Data Cleaner

**CLI CSV Data Cleaner** es una aplicación de línea de comandos (CLI) desarrollada en Python que permite limpiar y analizar archivos CSV de manera sencilla. El programa elimina filas vacías, limpia espacios en celdas y muestra los resultados directamente en la consola.

---

## Características

- **Eliminación de filas vacías**: Excluye filas completamente vacías del archivo.
- **Limpieza de celdas**: Elimina espacios en blanco al inicio y final de cada celda.
- **Procesamiento eficiente**: Muestra los resultados limpios en la consola, sin necesidad de escribir archivos adicionales.
- **Manejo de errores**: Verifica la existencia del archivo antes de procesarlo.

---

## Requisitos

- Python 3.7 o superior.

---

## Uso

1. Ejecuta el programa desde la línea de comandos:
   ```bash
   python csv_cleaner.py
   ```
2. Ingresa la ruta del archivo CSV cuando se te solicite:
   ```plaintext
   Ingrese la ruta del archivo CSV: data.csv
   ```

El programa procesará el archivo y mostrará el contenido limpio en la consola.

---

## Ejemplo de Entrada y Salida

### Entrada (Archivo `data.csv`):
```csv
Name, Age, Occupation
John Doe , 28 , Developer
, , 
Jane Smith, 34 , Designer
Michael Brown , , Engineer
```

### Salida:
```plaintext
Archivo CSV Limpio:
----------------------------------------
Name, Age, Occupation
John Doe, 28, Developer
Jane Smith, 34, Designer
Michael Brown, Engineer
----------------------------------------
```

---

## Estructura del Código

1. **Verificación de la existencia del archivo**: Asegura que el archivo CSV proporcionado existe antes de procesarlo.
2. **Lectura del archivo**: Usa la biblioteca estándar `csv` para cargar el archivo en memoria.
3. **Limpieza de datos**: Filtra filas vacías y limpia celdas de espacios en blanco.
4. **Visualización de resultados**: Imprime el archivo limpio en la consola.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## Contacto

Creado por [RogerPyDev](https://github.com/RogerPyDev).  
Para cualquier consulta, no dudes en contactarme.

