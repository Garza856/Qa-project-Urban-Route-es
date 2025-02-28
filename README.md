# Proyecto: Pruebas Automatizadas con Selenium

## Descripción del Proyecto

El objetivo principal de este proyecto es desarrollar y ejecutar pruebas automatizadas para garantizar la funcionalidad y estabilidad de la aplicación **Urban Routes**, utilizando **Selenium WebDriver** como herramienta de automatización. **Urban Routes** es una aplicación de transporte que permite a los usuarios solicitar un taxi a través de una interfaz web, proporcionando opciones personalizadas como tarifas, número de teléfono, pagos con tarjeta de crédito, y más.

Este proyecto se centra en verificar que el flujo de pedido de un taxi funcione de manera eficiente y sin errores, cubriendo desde la configuración inicial hasta la confirmación del conductor asignado. Las pruebas automatizadas están diseñadas para replicar la experiencia del usuario real, asegurando que todas las funcionalidades clave de la aplicación funcionen correctamente.

Las pruebas cubren los siguientes aspectos:

1. **Configuración de la Dirección**: Asegura que el sistema pueda recibir y procesar correctamente la dirección del usuario.
2. **Selección de Tarifa**: Verifica que el usuario pueda seleccionar la tarifa de taxi adecuada (por ejemplo, tarifa Comfort).
3. **Relleno del Número de Teléfono**: Comprueba que el sistema acepte correctamente el número de teléfono del usuario para la confirmación del viaje.
4. **Ingreso de Información de Pago**: Validación del proceso de agregar una tarjeta de crédito, incluyendo la interacción con campos dinámicos en el formulario de pago.
5. **Confirmación del Pedido**: Asegura que el usuario pueda agregar solicitudes adicionales, como manta, pañuelos, o incluso helados, como parte del pedido.
6. **Búsqueda de Taxi**: Verifica que el modal de búsqueda de taxis se cargue correctamente y que se muestre la información del conductor asignado.

El propósito de estas pruebas es detectar fallos potenciales en la aplicación antes de su despliegue a producción, lo que mejora la calidad y fiabilidad del servicio para los usuarios finales.

## Tecnologías y Técnicas Utilizadas

El proyecto utiliza las siguientes tecnologías y técnicas para implementar las pruebas automatizadas:

- **Selenium WebDriver**: Herramienta de automatización de navegadores que permite interactuar con la interfaz de usuario de la aplicación web, como si fuera un usuario real. Se utiliza para simular clics, desplazamientos y la entrada de datos en los formularios.
  
- **Python**: Lenguaje de programación utilizado para escribir las pruebas debido a su facilidad de uso y su integración con Selenium. Python también facilita la escritura de pruebas de forma concisa y legible.
  
- **PyTest**: Framework de pruebas utilizado para organizar y ejecutar las pruebas. PyTest ofrece funciones como fixtures, que facilitan la configuración de pruebas, y reportes detallados sobre los resultados de las mismas.

- **CSS Selectors y XPath**: Técnicas utilizadas para localizar y manipular elementos en la página web. Estas técnicas permiten identificar los elementos de la interfaz de usuario de forma eficiente y precisa.

- **Git**: Sistema de control de versiones para gestionar el código fuente y colaborar de manera eficiente dentro del equipo de desarrollo.

## Instrucciones para Ejecutar el Proyecto

A continuación, se detallan los pasos necesarios para clonar el repositorio, instalar las dependencias y ejecutar las pruebas automatizadas:

1. **Clonar el Repositorio**:
   
   Primero, clona el repositorio en tu máquina local utilizando el siguiente comando:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
