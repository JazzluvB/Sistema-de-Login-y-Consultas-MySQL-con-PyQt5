# 🔐 Sistema de Login y Consultas MySQL

> Proyecto desarrollado en **Python** con **PyQt5** y **Qt Designer**, que permite conectarse dinámicamente a una base de datos MySQL mediante un formulario de **Login** y ejecutar **consultas generales o específicas** sobre la tabla de empleados.

---

## 🧠 Descripción

Sistema de **Login y Consultas SQL** que permite:

- Ingresar credenciales de conexión: host, usuario, contraseña y base de datos.
- Validar la conexión mostrando mensaje de éxito o error.
- Acceder a una interfaz de **Consultas** para ver toda la base de datos o ejecutar queries específicas.
- Limpiar campos y cancelar la sesión de manera segura.

Ideal para **gestión de datos internos** y análisis de información de empleados.

---

## ⚙️ Funcionalidades principales

### 🔑 Login
- Ingreso de **host, usuario, contraseña y base de datos**.
- **Validación de conexión** con mensaje visual de éxito.
- Selección de base de datos mediante **ComboBox**.

### 📊 Consultas
- **Consulta general:** muestra todos los registros (ej. 851 empleados).
- **Consulta específica:** permite escribir queries personalizadas.
- **Botones funcionales:**
  - `Consultar` → ejecuta la consulta.
  - `Limpiar` → limpia la caja de texto.
  - `Cancelar` → cierra la ventana y la conexión.
- Datos mostrados: ID, Apellidos, Nombre, Año/Mes de nacimiento, Estado, Puesto, Sueldo, Próximo a jubilarse, Antigüedad, Edad, Peso, Altura, Presión y Glucosa.

---

## 🧰 Tecnologías utilizadas

| Tecnología | Descripción |
|------------|------------|
| Python 3.x | Lenguaje principal |
| PyQt5 | Framework de interfaz gráfica |
| Qt Designer | Creación visual de interfaces |
| MySQL Workbench | Administración de bases de datos |
| PyMySQL | Conexión Python ↔ MySQL |
| Pandas | Manejo de datos tabulares |
| QtCore / QtWidgets / QtGui | Componentes gráficos de PyQt5 |

---

## 🧱 Estructura del proyecto

## ⚙️ Instalación y Ejecución

Sigue estos pasos para instalar y ejecutar el sistema de **Login y Consultas MySQL**:

### 1️⃣ Clonar el repositorio

Primero, descarga el proyecto desde GitHub usando `git clone`:

```bash
git clone https://github.com/TU_USUARIO/login-consultas-mysql.git
cd login-consultas-mysql
