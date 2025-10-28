# 🔐 Sistema de Login y Consultas MySQL con PyQt5

> Proyecto desarrollado en **Python** utilizando **PyQt5**, **Qt Designer**, **MySQL** y **Pandas**, que permite conectarse dinámicamente a una base de datos MySQL mediante un formulario de **Login** y ejecutar **consultas generales o específicas** desde una interfaz gráfica profesional.

---

## 🧠 Descripción general

Este sistema permite establecer una **conexión dinámica a bases de datos MySQL** ingresando los datos de acceso desde una interfaz de **Login** diseñada con Qt Designer.  
Una vez validada la conexión, se despliega una segunda ventana (interfaz de **Consultas**) donde el usuario puede:

- Consultar toda la base de datos completa (en este caso, la tabla `empleados` con 851 registros).
- Ejecutar **consultas SQL específicas** ingresadas manualmente.
- Limpiar los campos de consulta.
- Cancelar la sesión y cerrar la conexión de manera segura.

Este proyecto sirve como base para **paneles administrativos**, **sistemas de gestión de datos** o **herramientas de análisis interno**, donde se requiera una conexión controlada a bases de datos MySQL mediante interfaz gráfica.

---

## ⚙️ Funcionalidades principales

### 🔑 Módulo de Login
- Campos configurables:
  - **Host**
  - **Usuario**
  - **Contraseña**
  - **Base de datos**
- **Validación de conexión** con mensajes visuales (“Conexión exitosa” o errores detallados).
- Permite seleccionar la base de datos mediante **ComboBox dinámico**.
- Al conectarse correctamente, se abre la ventana de **Consultas**.

### 📊 Módulo de Consultas
- **Consulta general:** muestra todos los registros de la base de datos.
- **Consulta específica:** permite escribir queries personalizadas (`SELECT`, `WHERE`, etc.).
- **Visualización tabular:** datos renderizados directamente desde **pandas DataFrame** en el entorno gráfico.
- **Botones funcionales:**
  - `Consultar` → Ejecuta la consulta general o personalizada.
  - `Limpiar` → Limpia el campo de texto.
  - `Cancelar` → Cierra la ventana de consultas y la conexión MySQL.
- Campos mostrados (ejemplo con tabla `empleados`):
  - ID, Apellido Paterno, Apellido Materno, Nombre, Año y Mes de Nacimiento,
    Estado, Puesto, Sueldo, Próximo a jubilarse, Antigüedad, Edad, Peso, Altura, Presión y Glucosa.

---

## 🧰 Tecnologías utilizadas

| Tecnología | Descripción |
|-------------|--------------|
| **Python 3.x** | Lenguaje principal |
| **PyQt5** | Framework para la interfaz gráfica |
| **Qt Designer** | Creación visual del diseño de ventanas |
| **MySQL Workbench** | Administración de bases de datos |
| **PyMySQL** | Conexión entre Python y MySQL |
| **Pandas** | Manejo y visualización de datos tabulares |
| **QtCore / QtGui / QtWidgets** | Componentes gráficos de PyQt5 |

---

## 🧱 Estructura del proyecto
