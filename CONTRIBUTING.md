# 🤝 Guía de Contribución (CONTRIBUTING)

¡Gracias por tu interés en aportar a este repositorio!

Este proyecto es un compendio de soluciones personales a los **101 ejercicios de lógica de programación** de [MoureDev](https://moure.dev) en [retosdeprogramacion.com](https://retosdeprogramacion.com/ejercicios). Aunque se trata de un repositorio personal de práctica y aprendizaje, las contribuciones constructivas que agreguen valor a la comunidad son siempre bienvenidas.

---

## 💡 ¿Cómo puedes colaborar?

Puedes participar de varias maneras:

1. **Optimizaciones algorítmicas:** Proponer implementaciones con mejor complejidad temporal ($O$) o espacial ($O$), o alternativas más *pythonic* y legibles.
2. **Casos borde (*Edge Cases*):** Añadir casos de prueba o validaciones adicionales en el bloque de comprobaciones al final de cada archivo.
3. **Correcciones:** Enmendar erratas ortográficas, fallos en enunciados o enlaces rotos en la documentación.
4. **Discusiones constructivas:** Sugerir enfoques alternativos a través de los *Issues* del repositorio.

> **Nota:** Por favor, no envíes Pull Requests que resuelvan retos pendientes que aún no hayan sido resueltos.

---

## 📐 Convenciones de Código y Estilo

Para mantener la consistencia en el repositorio, agradecemos seguir estas pautas:

- **Estándar PEP 8:** Respetar las guías de estilo oficiales de Python (nombres de variables y funciones en `snake_case`, indentación de 4 espacios, etc.).
- **Estructura del archivo:**
  - Mantener al inicio del script el bloque de comentarios o docstring `""" ... """` con el número del reto, título, dificultad y el enunciado original completo.
  - Definir la lógica en funciones reutilizables siempre que sea posible.
  - Mantener o ampliar la sección final de `# COMPROBACIONES` con ejemplos claros de entrada y salida esperada.
- **Sin dependencias externas innecesarias:** Priorizar la biblioteca estándar de Python salvo que el reto requiera explícitamente una librería externa (como manipulación de imágenes).
- **Legibilidad sobre ofuscación:** El código debe ser comprensible y didáctico para cualquier persona que esté aprendiendo.

---

## 🚀 Flujo para enviar un Pull Request

1. **Haz un Fork** del repositorio en tu cuenta de GitHub.
2. **Crea una rama descriptiva** para tus cambios:
   ```bash
   git checkout -b feat/optimizacion-reto-11
   # o
   git checkout -b fix/typo-reto-4
   ```
3. **Realiza tus cambios** y verifica que los scripts se ejecuten sin errores:
   ```bash
   python "#11.py"
   ```
4. **Haz commit** con mensajes claros y descriptivos:
   ```bash
   git commit -m "refactor(reto-11): optimizar balanceo de llaves usando pila"
   ```
5. **Envía tus cambios** a tu fork:
   ```bash
   git push origin feat/optimizacion-reto-11
   ```
6. **Abre un Pull Request** hacia la rama `main` de este repositorio explicando detalladamente la motivación del cambio y las pruebas realizadas.

---

## 🌟 Código de Conducta

Mantengamos este espacio como un entorno respetuoso, colaborativo y centrado en el aprendizaje mutuo. Toda crítica debe ser constructiva y fundamentada en la calidad técnica.
