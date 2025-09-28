<p align="center">
  <a href="https://python.org" target="_blank">
    <img src="https://www.python.org/static/community_logos/python-logo.png" width="200" alt="Python Logo">
  </a>
</p>


## 🚀 Inicialización Local FastAPI

### Requisitos Previos

- Python 3.13 (o superior)
- pip actualizado

### Pasos para la configuración

1. Descarga e instala Python 3.13 desde la página oficial:  
   [https://python.org/downloads](https://python.org/downloads)  
   - Durante la instalación, marca la opción **Add Python to PATH** antes de hacer clic en "Install Now".

2. Abre una terminal (cmd o PowerShell) y verifica la versión de Python:  
    ```
    python --version
    ```
3. Instalacion de dependencias: 
   ```
   python -m ensurepip --upgrade
   ```
   
   ```
   pip install fastapi uvicorn
   ```
   
   ```
   pip install scikit-learn
   ```

4. Ejecuta el servidor FastAPI:
    ```
    py -m uvicorn api_diagnostico:app --reload --port 8001
    ```
   
5. Abre en el navegador la documentación interactiva oficial para probar la API:  
    [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)
    -Te debe salir una ruta /diagnostico que es la que crea este proyecto
---

### Solución de problemas (Windows)

Si tienes problemas con el comando `python` o `pip` en VS Code, verifica que las variables de entorno PATH incluyan las rutas:
    `C:\Users\xxxxxxxx\AppData\Local\Programs\Python\Python313\` y
    `C:\Users\xxxxxxxx\AppData\Local\Programs\Python\Python313\Scripts\`
guardar y cerrar VS Code
- Abre tu proyecto en VS Code.
- Presiona `Ctrl + Shift + P` → escribe **Python: Select Interpreter**.
- Selecciona el que diga algo como:
    
    `Python 3.13.x  (C:\Users\xxxxxxxx\AppData\Local\Programs\)`

y probar python --version, si responde correctamente tu API FastAPI esta preparada para correr localmente y lista para integrarse con el proyecto Laravel o cualquier cliente que la consuma.

---

### Flujo general

- Laravel disponible en: `http://127.0.0.1:8000`
- FastAPI disponible en: `http://127.0.0.1:8001`
- El frontend Laravel envía los datos a `/diagnostico` y muestra el resultado en el formulario.

---

**¡Listo para desarrollar y probar la app localmente!**


