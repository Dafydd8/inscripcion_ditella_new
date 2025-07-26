# Bot de Inscripción UTDT

Este script automatiza el proceso de inscripción a materias en la plataforma de inscripciones de la Universidad Torcuato Di Tella (SIGEDU), utilizando Selenium y `undetected_chromedriver`.

## 🚀 ¿Qué hace?

- Inicia sesión automáticamente con tu cuenta UTDT (Microsoft login).
- Navega hasta la sección de **Materias fijadas**.
- Espera hasta una fecha y hora específicas.
- Intenta inscribirse en todas las materias disponibles que tengan el botón **Inscribirme** habilitado.

---

## ⚙️ Requisitos

- Python 3.8+
- Google Chrome instalado
- ChromeDriver compatible con tu versión de Chrome
- Una cuenta UTDT con materias fijadas

### 📦 Instalación de dependencias

```bash
pip install selenium undetected-chromedriver
```

---

## 🧾 Estructura

- `main.py`: Script principal que automatiza la inscripción.
- `datos.py`: Archivo de configuración con tus datos y parámetros de ejecución.

---

## ✍️ Cómo usar

1. Cloná el repositorio:

```bash
git clone https://github.com/Dafydd8/inscripcion_ditella_new.git
cd inscripcion_ditella_new
```

2. Editá el archivo `datos.py`:

```python
usuario = 'tu_correo@alumno.utdt.edu'
clave = 'tu_contraseña'

# Acá va la fecha y hora a la que te toca inscribirte
anio = 2025
mes = 7
dia = 25
hora = 16
minutos = 0
segundos = 0

chromedriverpath = './chromedriver'  # Ruta absoluta o relativa al ejecutable del chromedriver

esperar = True     # True para esperar hasta la hora especificada, False para ejecutar inmediatamente
loops = 10         # Cantidad de intentos de inscripción por materia
```

3. Ejecutá el script:

```bash
python main.py
```

4. ⚠️ Una vez que llegues a la página de inscripción, **abrí la DevTools (F12 o Ctrl+Shift+I)** y luego presioná Enter en la terminal para continuar. Esto ayuda a evitar que la web detecte el uso de Selenium.

---

## 🛠 Notas técnicas

- Se usa `undetected_chromedriver` para evitar que la web bloquee al bot.
- El script usa JavaScript (`driver.execute_script`) para hacer clic en botones invisibles o difíciles de acceder directamente.
- Es necesario abrir las DevTools manualmente para evitar que el sitio detecte la automatización (puede fallar sin este paso).
- El `while` previo a la inscripción congela el proceso hasta que se alcanza la hora deseada.

---

## 📌 TODOs / Mejoras posibles

- Mejor manejo de errores.
- Loop para reintentar inscripciones fallidas (`loops` por ahora no se usa).

---

## 🧑‍💻 Autor

Este script fue desarrollado por Dafydd Jenkins para uso personal durante la cursada en UTDT.

> Disclaimer: Usá este bot bajo tu propia responsabilidad. No está asociado oficialmente con UTDT.
