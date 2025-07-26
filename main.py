from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import datos
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

### PATH DEL DRIVER DE GOOGLE
chromedriver = datos.chromedriverpath

### URL DE SIGEDU
login = 'https://inscripciones.utdt.edu'

### DATOS DE LA INSCRIPCION
esperar = datos.esperar
user = datos.usuario
contra = datos.clave

hora_de_inscripcion = datetime(datos.anio, datos.mes, datos.dia, datos.hora, datos.minutos)
loops = datos.loops

### LOG IN EN PAGINA DE INSCRIPCIONES
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")


driver = uc.Chrome(headless=False, options=options)
driver.get(login)

try:
	ingreso_con_microsoft = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/button')))
	ingreso_con_microsoft.click()
except:
	print("No se pudo encontrar el botón de ingreso con Microsoft. Verifique la URL o el estado del sitio web.")
	driver.quit()
	exit()

print("La pagina detecto el driver:", driver.execute_script("return navigator.webdriver"))

# Ingresar usuario, contraseña y hacer click en no recordar
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]'))).send_keys(user)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input'))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input'))).send_keys(contra)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[5]/div/div/div/div/input'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input'))).click()

try:
	input("Cuando estés en la página, tenes que abrir la DevTools. Hace enter cuando estés listo.")
	titulo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/h2')))
	print(titulo.text)
	if 'Inscripciones' in titulo.text:
		print("Ingreso exitoso.\n")

except:
	print("No se pudo ingresar a la pagina de inscripciones.")
	driver.quit()
	exit()


# Abrir la pagina de materias fijadas
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[4]/div/div[1]/h2[2]'))).click()
print("Se hizo click en el botón de materias fijadas.")

# Esperar hasta que sea la hora de inscripción
while esperar and datetime.now() < hora_de_inscripcion:
	pass

# Obtener las tarjetas de materias
cards =driver.find_elements(By.CLASS_NAME, 'desktop-subject-item-container')

# Inscribir en las materias
for i, card in enumerate(cards):
	card_text = card.get_attribute("innerText")
	materia_nombre = card_text.split('\n')[0]
	if 'Inscribirme' in card_text:
		inscribir_btn = card.find_element(By.CLASS_NAME, 'desktop-action-add')
		try:
			driver.execute_script("arguments[0].click();", inscribir_btn)
			print("Se hizo click en el botón de inscribir.")
		except Exception as e:
			print(f"No se pudo hacer click en el botón de inscribir: {e}")
			continue
	else:
		print("No se puede inscribir en la materia:", materia_nombre)
time.sleep(300)

