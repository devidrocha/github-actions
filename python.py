from datetime import datetime, timedelta

def actualizar_readme():
    hora_actual = (datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S") - timedelta(hours=6)).strftime("%H:%M:%S")
    fecha_actual = datetime.now() - timedelta(hours=6)
    dia_actual = fecha_actual.day
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year
    nombres_meses = [
      "enero",
      "febrero",
      "marzo",
      "abril",
      "mayo",
      "junio",
      "julio",
      "agosto",
      "septiembre",
      "octubre",
      "noviembre",
      "diciembre"
    ]
    mes_actual_nombre =  nombres_meses[mes_actual]

    try:
        with open("README.md", "r") as archivo:
            contenido = archivo.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo README.md.")
        return

    for i, linea in enumerate(contenido):
        if "Repositorio actualizado automáticamente mediante una GitHub Action a las:" in linea:
            contenido[i] = f"* **Repositorio actualizado automáticamente mediante una GitHub Action a las: `{hora_actual}hrs.`**\n"
        elif "Modificado el día:" in linea:
            contenido[i] = f"* **Modificado el día: `{dia_actual}, del mes de {mes_actual_nombre}, del año {anio_actual}.`**\n"

    try:
        with open("README.md", "w") as archivo:
            archivo.writelines(contenido)
        print(f"README.md actualizado con la hora: {hora_actual}")
    except Exception as e:
        print(f"Error al escribir en el archivo README.md: {e}")

if __name__ == "__main__":
    actualizar_readme()
