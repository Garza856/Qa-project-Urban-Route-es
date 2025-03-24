
NOMBRE: Fabiola Garza Contreras Grupo QA21 

TITULO Y DESCRIPCION DEL  PROYECTO:
El proyecto se llevó a cabo utilizando Selenium WebDriver 
como herramienta clave para la automatización de pruebas en la
aplicación "Urban Routes", diseñada para la planificación de viajes.
A través de esta herramienta, se logró replicar de manera precisa la
interacción del usuario con la aplicación, permitiendo realizar pruebas 
en el navegador de forma eficiente. Esto no solo optimizó los tiempos de
prueba, sino que también mejoró la calidad de la aplicación al garantizar
su correcto funcionamiento a través de simulaciones realistas de uso.

TECNOLOGIAS UTILILIZADAS 
Para ejecutar las pruebas del proyecto se utilizo, pytest como herramienta 
de automatización la instalacion de pytest se realiza de la siguiente manera.
1. Abre PyCharm en una terminal como (Git Bash si es que utilizas windows).
2. Verifica que Python este correctamente instalado ejecutando el comando python--version.
3. Para instalar Pytest, ejecuta el siguiente comando: pip install pytest
4. Para confirmar que Pytest se ha instalado correctamente, ejecuta el comando: Pytest -- version.

--ISTALACION DE SELENIUM
1. Selecciona la version del controlador que coincida con la version de tu navegador.
2. Descargar el archivo correspondiente
3. Descomprime el archivo y crea una carpeta llamada WebDriver/bin

INSTRUCCIONES PARA EJECUCION DE PRUEBAS 
1.PYTEST:
Para ejecutar las pruebas, sigue estos pasos para instalar y configurar Pytest:
°Abrir Pycharm en una terminal 
°Verificar la instalacion de pyhton ejecutando el comando pytest--versión 
°Instalar Pytest ejecutable pip intall pytest
°verifique la instalción de pyteste ejecutando  pyteste--version
2.Controlador WEB SELENIUM
°Dirigete al sitio web de Selenium, donde se encuentran disponible los controladores.
°Selecciona la versión adecuada al controlador 
°Existen varios archivos comprimidos disponibles en la carpeta. Descarga al que 
sea compatible con tu sistema operativo. Luego, descomprima el archivo. crea una carpeta
WebDiver/bin y almacena el archivo ahí.
°Adjunta la ruta de la carpeta bin A la PATH. Ten en cuenta  el algoritmo depende del sistema operativo.
-INSTALACION DE SELENIUM PARA PYTHON 
°Abre la consola desde la terminal 
-COMANDO DE EJECUCION DE INSTALACION 
°Agrega este comando para su instalación del paquete de SELENIUM: 
pip install selenium.
-ABRE EN NAVEGADOR CON PYCHARM 
Importa el paquete Selenium WebDriver:from selenium import webdriver
°Importa el paquete time:import time
Activa el controlador del navegador.

EJECUCIÓN DE LAS PRUEBAS
En la realizacón de pruebas, verifica tener instalados los siguientes paquetes
°Pytest y Selenium
°Pip install pytest
°pip install selenium
Las pruebas se realizán en el navegador de crhome así que asegurate de tenerlo instalado,
sino cuentas con en vee a gogle eh instala la versón mas nueva..
Para relizar las pruebas verifica esta en el directorion "main.py",
donde se encuentran las pruebas, pytest mostrará un resumen de los resultados en la terminal.

CICLO DE PRUEBAS
-Las siguientes pruebas automatizadas abarcan las etapas del proceso de solicitud.
°Establecer la dirección
°Escoger la tarifa premium 
°Ingresar el número de telefono 
°Ingresar una tarjeta de crédito:Se simula la interacción con el modal de "Añadir una trajeta"
y se verifica que el campo  CVV(id="code") este presente y funcione conrrectamente.
class]="card-nput")pierde el enfoque para hablilitar el botón
-Solicitar manta y pañuelos 
-Pedir 2 helados.
-Espera la loaclización de un taxi:Se verifica que el modal de busqueda del conductor se muestre
correctamente y que la cuenta regresiva comience de manera adecuada.

-Las pruebas automatizadas abarcaron todo el proceso de solicitud de un taxi,
permitiendo identificar.
°Flujo optimizado:Se verificó que la configuración de las direcciones, la selección
de la tarifa y la confirmación del viaje se efectúa.


-Problemas detectados.
°Se detectaron inconvenientes en la activación del botón de pago al ingreesar la tarjeta.
°Pruebas repetibles.
°Se redujo el tiempo de validación manual, lo que facilitó la realización de pruebas continuas.

MONITOREO CONSTANTE
°OPTIMIZAR LA VERIFICACIÓN DE CAMPOS:Garantizar que los elementos esenciales de la intefaz sean 
manipulables en todos los escenarios.

-INCREMENTAR LA EXTENSIÓN DE LAS PRUEBAS.
°Incorporar situaciones extremas, como conexiones inestables o datos incorrectos
en los formularios.

-Automatizacón dentro de la integración continua.
°Realice pruebas automáticas con cada actualización para prevenir regresiones.

La integración de pruebas automatizadas con Selenium y Pytest facilitón la 
detección temprana de errores antes de llegar a producción, lo que redujo el 
tiempo de pruebas en un X% y aunmentón la estabilidad de la aplicación. Esto
asegura que URBAN ROUTES ofrecerá una experiencia confiablea a sus usuarions y
minimiza las interrupciones en el servicio.




