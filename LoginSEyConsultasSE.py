# Carlos Palacios Betancourt
# Python 3.10.11

# ------------------------------
# Silenciar DeprecationWarnings
# ------------------------------
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ------------------------------
# Importaciones
# ------------------------------
import sys, pymysql, pandas
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5 import QtCore

# ------------------------------
# Clase Login
# ------------------------------
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r"Ruta_De_Acceso_Archivo_.UI", self)
        self.btnAceptar.clicked.connect(self.Aceptar)
        self.btnCancelar.clicked.connect(self.Cancelar)
        self.txtContrasena.setEchoMode(QLineEdit.Password)

        # Valores por defecto
        self.txtHost.setText("tu_host")
        self.txtUsuario.setText("Tu_Usuario")
        self.txtContrasena.setText("Tu_Contraseña")
        self.txtBD.setText("La_Base_de_Datos")

    def closeEvent(self, evento):
        try:
            if hasattr(self, "c") and self.c.open:
                    self.c.close()
        except AttributeError:
            print("Conexión cerrada correctamente desde closeEvent")
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")
        finally:
            evento.accept()

    def abrirConsultas(self):
        self.hide()
        print("Abriendo ventana Consultas...")
        self.consultas = Consultas(
            h=self.txtHost.text(),
            u=self.txtUsuario.text(),
            p=self.txtContrasena.text(),
            d=self.txtBD.text()
        )
        self.consultas.show()

    def conexion(self):
        global h, u, p, d
        h = self.txtHost.text()
        u = self.txtUsuario.text()
        p = self.txtContrasena.text()
        d = self.txtBD.text()
        
        if not all((h, u, p, d)):
            QMessageBox.warning(self, "Atención", "Todos los parámetros son obligatorios")
            return
        try:
            self.c = pymysql.connect(host=h, user=u, password=p, db=d)
            self.cur = self.c.cursor()
            QMessageBox.information(self, "Conexión", "Conexión exitosa")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error de conexión: {str(e)}")

    def Aceptar(self):
        global h, u, p, d
        h = self.txtHost.text()
        u = self.txtUsuario.text()
        p = self.txtContrasena.text()
        d = self.txtBD.text()
        self.abrirConsultas()

    def Cancelar(self):
        self.txtHost.clear()
        self.txtUsuario.clear()
        self.txtContrasena.clear()
        self.txtBD.clear()


# ------------------------------
# Clase Consultas
# ------------------------------
class Consultas(QMainWindow):
    def __init__(self, parent=None, h=None, u=None, p=None, d=None):
        super(Consultas, self).__init__(parent)
        self.h = h
        self.u = u
        self.p = p
        self.d = d

        loadUi(r"Ruta_De_Acceso_Archivo_.UI", self)

        # Conectar botones
        self.btnLimpiar.clicked.connect(self.Limpiar)
        self.btnCancelar.clicked.connect(self.Cancelar)
        self.btnConsultar.clicked.connect(self.consultaComboBox)
        
        self.mostrarTablas()

    # Forzar que la barra de menú se vea dentro de la ventana (macOS)
        self.menuBar().setNativeMenuBar(False)

        # Conectar las acciones del menú a sus funciones
        self.menuCerrarSesion.triggered.connect(self.cerrarSesion)
        self.menuExportar.triggered.connect(self.exportar)
        self.menuSalir.triggered.connect(self.salir)
        
    # ------------------------------
    # Conexión a MySQL
    # ------------------------------
    def conexionConsultas(self, h, u, p, d):
        try:
            host = str(h).strip()
            user = str(u).strip()
            passwd = str(p).strip()
            dbname = str(d).strip()

            print(f"Intentando conectar a MySQL en host: '{host}'")
            self.c = pymysql.connect(host=host, user=user, password=passwd, db=dbname)
            self.cur = self.c.cursor()
            QMessageBox.information(self, "Conexión", "Conexión exitosa en Consultas")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error de conexión en Consultas: {str(e)} ")

    # ------------------------------
    # Mostrar tablas en ComboBox
    # ------------------------------
    def mostrarTablas(self):
        global h, u, p, d 
        self.conexionConsultas(h, u, p, d)
        if not hasattr(self, "cur"):
            return
        try:
            self.cur.execute("SHOW TABLES")
            nombre_tablas = self.cur.fetchall()
            print("Tablas detectadas:", nombre_tablas)

            if isinstance(self.cbtablas, QComboBox):
                self.cbtablas.clear()
                for tabla in nombre_tablas:
                    self.cbtablas.addItem(str(tabla[0]))

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar tablas: {str(e)}")

    # ------------------------------
    # Consultar tabla seleccionada
    # ------------------------------
    def consultaComboBox(self):
        global h, u, p, d 
        tabla = self.cbtablas.currentText()

        try:
            if not hasattr(self, "cur") or self.cur is None:
                self.c = pymysql.connect(host=h, user=u, password=p, db=d)
                self.cur = self.c.cursor()

            sql_column_count = f"""
                SELECT COUNT(*) 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_SCHEMA = '{d}' 
                AND TABLE_NAME = '{tabla}'
            """
            self.cur.execute(sql_column_count)
            cantidad = self.cur.fetchone()[0]
            print("Cantidad de columnas:", cantidad)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al obtener cantidad de columnas: {str(e)}")
            return

        try:
            sql_column_names = f"""
                SELECT COLUMN_NAME 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_SCHEMA = '{d}' 
                AND TABLE_NAME = '{tabla}'
            """
            self.cur.execute(sql_column_names)
            nombre_columnas = self.cur.fetchall()
            lista = [n[0] for n in nombre_columnas]

            self.tablas.setColumnCount(len(lista))
            self.tablas.setHorizontalHeaderLabels(lista)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al obtener nombres de columnas: {str(e)}")
            return

        try:
            sql_datos = f"SELECT * FROM {tabla}"
            self.cur.execute(sql_datos)
            resultado = self.cur.fetchall()

            self.tablas.clearContents()
            self.tablas.setRowCount(0)

            for fila_index, fila_data in enumerate(resultado):
                self.tablas.insertRow(fila_index)
                for col_index in range(cantidad):
                    item = QTableWidgetItem(str(fila_data[col_index]))
                    self.tablas.setItem(fila_index, col_index, item)

            self.tablas.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning(self, f"Error al cargar datos: {str(e)}")
            return

    # ------------------------------
    # Consultar SQL específico
    # ------------------------------
    def consultaEspecifica(self):
        global h, u, p, d  

        self.conexionConsultas(h, u, p, d)

        consulta = self.txtConsulta.toPlainText()
        if len(consulta) == 0:
            QMessageBox.warning(self, "Atención", "Escriba una consulta MySQL")
            return

        try:
            self.cur.execute(consulta)
            resultados = self.cur.fetchall()
            columnas = [columna[0] for columna in self.cur.description]

            self.tablas.clearContents()
            self.tablas.setColumnCount(len(columnas))
            self.tablas.setHorizontalHeaderLabels(columnas)
            self.tablas.setRowCount(0)

            for fila, datos in enumerate(resultados):
                self.tablas.insertRow(fila)
                for columna, dato in enumerate(datos):
                    self.tablas.setItem(fila, columna, QTableWidgetItem(str(dato)))

            self.tablas.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning(self, f"Error en consulta: {str(e)}")

    # ------------------------------
    # Exportar tabla a Excel
    # ------------------------------
    def exportar(self):
        try:
            if self.tablas.rowCount() == 0:
                QMessageBox.warning(self, "Error", "La tabla está vacía.")
                return

            columnas = [self.tablas.horizontalHeaderItem(col).text() for col in range(self.tablas.columnCount())]

            datos = []
            for fila in range(self.tablas.rowCount()):
                fila_datos = []
                for columna in range(self.tablas.columnCount()):
                    item = self.tablas.item(fila, columna)
                    fila_datos.append(item.text() if item else "")
                datos.append(fila_datos)

            df = pandas.DataFrame(datos, columns=columnas)
            ruta, _ = QFileDialog.getSaveFileName(self, "Guardar como Excel", "datos.xlsx", "Archivos Excel (*.xlsx)")
            if not ruta:
                return
            df.to_excel(ruta, index=False)
            QMessageBox.information(self, "Éxito", "Los datos se exportaron con éxito")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error al exportar: {str(e)}")
            
    # ------------------------------
    # Cerrar Sesion
    # ------------------------------
    
    def cerrarSesion(self):
    # Oculta la ventana de Consultas y vuelve al login
        self.hide()
        self.parent().show()  # Si pasaste parent=self desde Login
        
    # ------------------------------
    # Salir
    # ------------------------------
    
    def salir(self):
    # Cierra la aplicación
        QApplication.quit()

    # ------------------------------
    # Limpiar interfaz
    # ------------------------------
    def LimpiarInterfaz(self):
        self.txtConsulta.clear()
        self.checkConsulta.setChecked(True)
        self.tablas.setRowCount(0)
        self.tablas.setColumnCount(0)

    # ------------------------------
    # Limpiar botones
    # ------------------------------
    def Limpiar(self):
        self.txtConsulta.clear()
        if hasattr(self, "cbtablas") and isinstance(self.cbtablas, QComboBox):
            self.cbtablas.setCurrentIndex(0)
        if hasattr(self, "txtResultados"):
            self.txtResultados.clear()

    # ------------------------------
    # Cerrar ventana
    # ------------------------------
    def Cancelar(self):
        self.close()

# ------------------------------
# Arranque de la aplicación
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    login = Login()
    login.show()
    sys.exit(app.exec())