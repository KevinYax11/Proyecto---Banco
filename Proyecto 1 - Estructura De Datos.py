import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QListWidget, QGridLayout, QPushButton, QFileDialog, QMessageBox, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView, QInputDialog

class Node:
    def __init__(self, data=None):
        self.data = data  # Valor almacenado en el nodo
        self.next = None  # Referencia al siguiente nodo en la lista

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Inicializa la cabeza de la lista como vacía

    def append(self, data):
        new_node = Node(data)  # Crea un nuevo nodo con el dato proporcionado
        if not self.head:  # Si la lista está vacía
            self.head = new_node  # El nuevo nodo se convierte en la cabeza de la lista
            new_node.next = self.head  # El siguiente del nuevo nodo apunta a sí mismo (lista circular)
        else:
            curr = self.head  # Empieza desde la cabeza
            while curr.next != self.head:  # Busca el último nodo en la lista
                curr = curr.next
            curr.next = new_node  # Establece el siguiente del último nodo como el nuevo nodo
            new_node.next = self.head  # Hace que el nuevo nodo apunte a la cabeza para cerrar el círculo

    def remove(self, data):
        if not self.head:  # Si la lista está vacía
            return
        current_node = self.head  # Empieza desde la cabeza
        prev_node = None  # Inicializa el nodo anterior como None
        found = False  # Bandera para indicar si se encuentra el dato
        while True:
            if current_node.data == data:  # Si el dato del nodo actual coincide con el dato buscado
                found = True  # Marca que se encontró el dato
                break
            prev_node = current_node  # Guarda el nodo actual como el anterior
            current_node = current_node.next  # Avanza al siguiente nodo
            if current_node == self.head:  # Si se ha vuelto a la cabeza (se completó el ciclo)
                break
        if found:  # Si se encontró el dato
            if current_node == self.head:  # Si el nodo actual es la cabeza
                if current_node.next == current_node:  # Si la lista tiene un solo nodo
                    self.head = None  # La lista se vacía
                else:
                    while current_node.next != self.head:  # Encuentra el último nodo
                        current_node = current_node.next
                    current_node.next = self.head.next  # Establece el siguiente del último nodo como el siguiente de la cabeza
                    self.head = self.head.next  # Actualiza la cabeza de la lista
            else:
                prev_node.next = current_node.next  # El siguiente del nodo anterior apunta al siguiente del nodo actual
        else:
            print("Data not found in the list")  # Mensaje si el dato no se encuentra en la lista

class YKBank(QMainWindow):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase QMainWindow
        self.setWindowTitle("Tinkoff Bank")  # Establece el título de la ventana principal
        self.setGeometry(100, 100, 1000, 900)  # Establece la geometría de la ventana principal

        # Cargar la imagen de fondo
        self.background_image = QPixmap("1.png")

        # Crear un widget central y un diseño de cuadrícula para organizar los elementos
        central_widget = QWidget(self)  # Crea un widget central para la ventana principal
        self.setCentralWidget(central_widget)  # Establece el widget central para la ventana principal
        grid_layout = QGridLayout(central_widget)  # Crea un diseño de cuadrícula para organizar los elementos

        # Crear y configurar la etiqueta de fondo
        self.background_label = QLabel(self)  # Crea una etiqueta para mostrar la imagen de fondo
        self.background_label.setPixmap(self.background_image)  # Establece la imagen de fondo en la etiqueta
        self.background_label.setScaledContents(True)  # Escala la imagen para que se ajuste al tamaño de la etiqueta

        # Agregar la etiqueta de fondo al diseño de cuadrícula en la posición (0, 0)
        grid_layout.addWidget(self.background_label, 0, 0, 1, 1)

        # Crear pestañas
        self.tabs = QTabWidget()  # Crea un widget de pestañas
        self.tab1 = QWidget()  # Crea la primera pestaña
        self.tab2 = QWidget()  # Crea la segunda pestaña
        self.tab3 = QWidget()  # Crea la tercera pestaña
        self.tabs.addTab(self.tab1, "Asociados")  # Agrega la primera pestaña con etiqueta "Asociados"
        self.tabs.addTab(self.tab2, "Préstamos")  # Agrega la segunda pestaña con etiqueta "Préstamos"
        self.tabs.addTab(self.tab3, "Usuarios")  # Agrega la tercera pestaña con etiqueta "Usuarios"

        # Pestaña de Asociados
        # Se crean varios elementos de interfaz de usuario y se configuran
        # Estos elementos se agregan a un diseño vertical
        # Luego, el diseño vertical se establece como diseño para la pestaña 1
        self.members_list = QListWidget()  # Lista para mostrar los asociados
        self.member_name_edit = QLineEdit()  # Campo de edición para el nombre del asociado
        self.member_address_edit = QLineEdit()  # Campo de edición para la dirección del asociado
        self.member_phone_edit = QLineEdit()  # Campo de edición para el teléfono del asociado
        self.member_dpi_edit = QLineEdit()  # Campo de edición para el DPI del asociado
        self.member_nit_edit = QLineEdit()  # Campo de edición para el NIT del asociado
        self.member_files_edit = QTextEdit()  # Campo de edición para los archivos relacionados con el asociado
        self.member_references_list = QListWidget()  # Lista para mostrar las referencias del asociado
        self.add_member_button = QPushButton("Agregar Asociado")  # Botón para agregar un nuevo asociado
        self.add_member_button.clicked.connect(self.add_member)  # Conecta el clic del botón a la función add_member
        self.remove_member_button = QPushButton("Eliminar Asociado")  # Botón para eliminar un asociado
        self.remove_member_button.clicked.connect(self.remove_member)  # Conecta el clic del botón a la función remove_member
        self.add_file_button = QPushButton("Agregar Archivo")  # Botón para agregar un archivo relacionado con el asociado
        self.add_file_button.clicked.connect(self.add_file)  # Conecta el clic del botón a la función add_file
        self.add_reference_button = QPushButton("Agregar Referencia")  # Botón para agregar una referencia al asociado
        self.add_reference_button.clicked.connect(self.add_reference)  # Conecta el clic del botón a la función add_reference
        self.remove_reference_button = QPushButton("Eliminar Referencia")  # Botón para eliminar una referencia del asociado
        self.remove_reference_button.clicked.connect(self.remove_reference)  # Conecta el clic del botón a la función remove_reference

        # Configura el diseño vertical para la pestaña 1
        members_layout = QVBoxLayout()
        members_layout.addWidget(QLabel("Asociados"))  # Etiqueta para la sección de asociados
        members_layout.addWidget(self.members_list)  # Lista de asociados
        members_layout.addWidget(QLabel("Nombre"))  # Etiqueta para el campo de nombre
        members_layout.addWidget(self.member_name_edit)  # Campo de edición para el nombre
        members_layout.addWidget(QLabel("Dirección"))  # Etiqueta para el campo de dirección
        members_layout.addWidget(self.member_address_edit)  # Campo de edición para la dirección
        members_layout.addWidget(QLabel("Teléfono"))  # Etiqueta para el campo de teléfono
        members_layout.addWidget(self.member_phone_edit)  # Campo de edición para el teléfono
        members_layout.addWidget(QLabel("DPI"))  # Etiqueta para el campo de DPI
        members_layout.addWidget(self.member_dpi_edit)  # Campo de edición para el DPI
        members_layout.addWidget(QLabel("NIT"))  # Etiqueta para el campo de NIT
        members_layout.addWidget(self.member_nit_edit)  # Campo de edición para el NIT
        members_layout.addWidget(QLabel("Archivos"))  # Etiqueta para la sección de archivos
        members_layout.addWidget(self.member_files_edit)  # Campo de edición para los archivos
        members_layout.addWidget(self.add_file_button)  # Botón para agregar archivos
        members_layout.addWidget(QLabel("Referencias"))  # Etiqueta para la sección de referencias
        members_layout.addWidget(self.member_references_list)  # Lista de referencias
        members_layout.addWidget(self.add_reference_button)  # Botón para agregar referencias
        members_layout.addWidget(self.remove_reference_button)  # Botón para eliminar referencias
        members_layout.addWidget(self.add_member_button)  # Botón para agregar asociados
        members_layout.addWidget(self.remove_member_button)  # Botón para eliminar asociados

        self.tab1.setLayout(members_layout)  # Establece el diseño vertical como diseño para la pestaña 1

        # Pestaña de Préstamos
        self.loans_table = QTableWidget()  # Crear una tabla para mostrar información sobre los préstamos
        self.loans_table.setColumnCount(9)  # Establecer el número de columnas en la tabla
        self.loans_table.setHorizontalHeaderLabels(  # Establecer las etiquetas de encabezado de columna
            ["Código", "Asociado", "Estado", "Monto Solicitado", "Cuotas", "Monto Aprobado", "Ingresos", "Garantía",
             "Archivos"])
        self.loans_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)  # Ajustar el tamaño de las columnas para que se ajusten al contenido

        # Crear botones para la gestión de préstamos
        self.request_loan_button = QPushButton("Solicitar Préstamo")
        self.request_loan_button.clicked.connect(
            self.request_loan)  # Conectar el botón "Solicitar Préstamo" con la función request_loan
        self.approve_loan_button = QPushButton("Aprobar Préstamo")
        self.approve_loan_button.clicked.connect(
            self.approve_loan)  # Conectar el botón "Aprobar Préstamo" con la función approve_loan
        self.pay_loan_button = QPushButton("Pagar Cuota")
        self.pay_loan_button.clicked.connect(self.pay_loan)  # Conectar el botón "Pagar Cuota" con la función pay_loan

        # Crear el diseño vertical para organizar los elementos de la pestaña de préstamos
        loans_layout = QVBoxLayout()
        loans_layout.addWidget(self.loans_table)  # Agregar la tabla de préstamos al diseño
        loans_layout.addWidget(self.request_loan_button)  # Agregar el botón "Solicitar Préstamo"
        loans_layout.addWidget(self.approve_loan_button)  # Agregar el botón "Aprobar Préstamo"
        loans_layout.addWidget(self.pay_loan_button)  # Agregar el botón "Pagar Cuota"

        # Establecer el diseño de la pestaña de préstamos
        self.tab2.setLayout(loans_layout)

        # Crear la tabla de usuarios y configurar su estructura
        self.users_table = QTableWidget()
        self.users_table.setColumnCount(5)  # Establecer el número de columnas
        self.users_table.setHorizontalHeaderLabels(
            ["Código", "Nombre", "Correo", "Contraseña", "Puesto"])  # Establecer las etiquetas de encabezado de columna
        self.users_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)  # Ajustar el tamaño de las columnas para que se ajusten al contenido

        # Crear campos de edición y botones para la gestión de usuarios
        self.user_name_edit = QLineEdit()
        self.user_email_edit = QLineEdit()
        self.user_password_edit = QLineEdit()
        self.user_role_edit = QLineEdit()
        self.add_user_button = QPushButton("Agregar Usuario")
        self.add_user_button.clicked.connect(
            self.add_user)  # Conectar el botón "Agregar Usuario" con la función add_user
        self.remove_user_button = QPushButton("Eliminar Usuario")
        self.remove_user_button.clicked.connect(
            self.remove_user)  # Conectar el botón "Eliminar Usuario" con la función remove_user
        self.update_user_button = QPushButton("Actualizar Usuario")
        self.update_user_button.clicked.connect(
            self.update_user)  # Conectar el botón "Actualizar Usuario" con la función update_user

        # Crear el diseño vertical para organizar los elementos de la pestaña de usuarios
        users_layout = QVBoxLayout()
        users_layout.addWidget(self.users_table)  # Agregar la tabla de usuarios al diseño
        users_layout.addWidget(QLabel("Nombre"))  # Agregar etiqueta para el campo de nombre
        users_layout.addWidget(self.user_name_edit)  # Agregar campo de edición para el nombre
        users_layout.addWidget(QLabel("Correo Electrónico"))  # Agregar etiqueta para el campo de correo electrónico
        users_layout.addWidget(self.user_email_edit)  # Agregar campo de edición para el correo electrónico
        users_layout.addWidget(QLabel("Contraseña"))  # Agregar etiqueta para el campo de contraseña
        users_layout.addWidget(self.user_password_edit)  # Agregar campo de edición para la contraseña
        users_layout.addWidget(QLabel("Puesto"))  # Agregar etiqueta para el campo de puesto
        users_layout.addWidget(self.user_role_edit)  # Agregar campo de edición para el puesto
        users_layout.addWidget(self.add_user_button)  # Agregar botón "Agregar Usuario"
        users_layout.addWidget(self.remove_user_button)  # Agregar botón "Eliminar Usuario"
        users_layout.addWidget(self.update_user_button)  # Agregar botón "Actualizar Usuario"

        # Establecer el diseño de la pestaña de usuarios
        self.tab3.setLayout(users_layout)

        # Configurar la ventana principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)  # Agregar el widget de pestañas al diseño principal
        central_widget = QWidget()
        central_widget.setLayout(main_layout)  # Establecer el diseño principal para el widget central
        self.setCentralWidget(central_widget)  # Establecer el widget central de la ventana principal

        # Datos de ejemplo
        self.members = CircularLinkedList()
        self.loans = []
        self.users = []
        self.current_user = None  # Variable para el usuario actual

        # Conexión de señales
        self.tabs.currentChanged.connect(
            self.check_admin_access)  # Conectar la señal de cambio de pestaña con la función check_admin_access

    def add_member(self):
        # Obtener los datos de los campos de entrada
        name = self.member_name_edit.text()  # Obtener el nombre del asociado
        address = self.member_address_edit.text()  # Obtener la dirección del asociado
        phone = self.member_phone_edit.text()  # Obtener el teléfono del asociado
        dpi = self.member_dpi_edit.text()  # Obtener el DPI del asociado
        nit = self.member_nit_edit.text()  # Obtener el NIT del asociado
        files = self.member_files_edit.toPlainText()  # Obtener los archivos del asociado
        references = [self.member_references_list.item(i).text() for i in
                      range(self.member_references_list.count())]  # Obtener las referencias del asociado

        # Crear un diccionario con la información del nuevo miembro
        member = {
            "name": name,  # Nombre del asociado
            "address": address,  # Dirección del asociado
            "phone": phone,  # Teléfono del asociado
            "dpi": dpi,  # DPI del asociado
            "nit": nit,  # NIT del asociado
            "files": files,  # Archivos relacionados al asociado
            "references": references  # Referencias del asociado
        }

        # Agregar el nuevo miembro a la lista de asociados
        self.members.append(member)  # Se añade el nuevo asociado a la lista
        # Agregar el nombre y el DPI del nuevo miembro a la lista visual de asociados
        self.members_list.addItem(f"{name} ({dpi})")  # Se añade el nombre y DPI a la lista visual

    def remove_member(self):
        # Obtener el elemento seleccionado en la lista de asociados
        selected_item = self.members_list.currentItem()
        if selected_item:
            # Obtener los datos del asociado seleccionado
            member_data = selected_item.text().split("(")
            member_name = member_data[0].strip()  # Nombre del asociado
            member_dpi = member_data[1][:-1]  # DPI del asociado

            # Inicializar los nodos actual y previo
            curr_node = self.members.head
            prev_node = None

            # Recorrer la lista de asociados
            while curr_node:
                # Verificar si el nodo actual contiene los datos del asociado seleccionado
                if curr_node.data["name"] == member_name and curr_node.data["dpi"] == member_dpi:
                    # Eliminar el nodo actual de la lista
                    if not prev_node:
                        self.members.head = curr_node.next
                    else:
                        prev_node.next = curr_node.next
                    # Eliminar el elemento de la lista visual de asociados
                    self.members_list.takeItem(self.members_list.currentRow())
                    break
                prev_node = curr_node
                curr_node = curr_node.next

    def add_file(self):
        # Mostrar el diálogo para seleccionar un archivo
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*.*)")
        if file_path:
            # Agregar la ruta del archivo al campo de archivos del asociado
            self.member_files_edit.append(file_path)

    def add_reference(self):
        # Obtener la referencia ingresada por el usuario
        reference = self.member_name_edit.text()
        if reference:
            # Agregar la referencia a la lista visual de referencias del asociado
            self.member_references_list.addItem(reference)

    def remove_reference(self):
        # Obtener el elemento seleccionado en la lista de referencias del asociado
        selected_item = self.member_references_list.currentItem()
        if selected_item:
            # Eliminar la referencia seleccionada de la lista visual de referencias del asociado
            self.member_references_list.takeItem(self.member_references_list.currentRow())

    def request_loan(self):
        # Obtener los detalles del préstamo del usuario
        member_name = self.member_name_edit.text()  # Nombre del miembro solicitante
        member_dpi = self.member_dpi_edit.text()  # DPI del miembro solicitante
        loan_amount = int(
            QInputDialog.getText(self, "Monto del préstamo", "Ingrese el monto solicitado:")[0])  # Monto del préstamo
        num_payments = int(
            QInputDialog.getText(self, "Número de cuotas", "Ingrese el número de cuotas:")[0])  # Número de cuotas
        monthly_income = int(QInputDialog.getText(self, "Ingresos mensuales", "Ingrese sus ingresos mensuales:")[
                                 0])  # Ingresos mensuales
        guarantee = QInputDialog.getText(self, "Garantía", "Ingrese la garantía:")[0]  # Garantía del préstamo
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "",
                                                   "Todos los archivos (*.*)")  # Archivo adjunto

        # Crear un diccionario para representar el préstamo
        loan = {
            "member_name": member_name,
            "member_dpi": member_dpi,
            "status": "Creado",
            "amount_requested": loan_amount,
            "num_payments": num_payments,
            "amount_approved": 0,
            "monthly_income": monthly_income,
            "guarantee": guarantee,
            "file": file_path,
            "payment_plan": [],
            "payment_history": []
        }

        # Agregar el préstamo a la lista de préstamos y actualizar la tabla
        self.loans.append(loan)
        self.update_loans_table()

    def approve_loan(self):
        # Obtener la fila seleccionada en la tabla de préstamos
        selected_row = self.loans_table.currentRow()
        if selected_row >= 0:
            # Solicitar al usuario que ingrese el monto aprobado para el préstamo seleccionado
            approved_amount = int(QInputDialog.getText(self, "Monto aprobado", "Ingrese el monto aprobado:")[0])
            # Actualizar el monto aprobado y el estado del préstamo en la lista de préstamos
            self.loans[selected_row]["amount_approved"] = approved_amount
            self.loans[selected_row]["status"] = "Aprobado"
            # Actualizar la tabla de préstamos
            self.update_loans_table()

    def pay_loan(self):
        # Obtener la fila seleccionada en la tabla de préstamos
        selected_row = self.loans_table.currentRow()
        if selected_row >= 0:
            loan = self.loans[selected_row]
            if loan["status"] == "Aprobado":  # Verificar si el préstamo está aprobado
                # Solicitar al usuario el monto del pago de la cuota
                payment_amount = int(QInputDialog.getText(self, "Pago de cuota", "Ingrese el monto a pagar:")[0])
                # Agregar el monto del pago a la historia de pagos del préstamo
                loan["payment_history"].append(payment_amount)
                # Verificar si el préstamo está completamente pagado y actualizar su estado
                if sum(loan["payment_history"]) >= loan["amount_approved"]:
                    loan["status"] = "Finalizado"
                # Actualizar la tabla de préstamos
                self.update_loans_table()

    def add_user(self):
        # Obtener los detalles del nuevo usuario
        name = self.user_name_edit.text()  # Nombre del usuario
        email = self.user_email_edit.text()  # Correo electrónico del usuario
        password = self.user_password_edit.text()  # Contraseña del usuario
        role = self.user_role_edit.text()  # Rol del usuario

        # Crear un diccionario para representar al usuario
        user = {
            "name": name,
            "email": email,
            "password": password,
            "role": role,
            "status": "Activo"
        }

        # Agregar el usuario a la lista de usuarios y actualizar la tabla
        self.users.append(user)
        self.update_users_table()

    def remove_user(self):
        # Obtener la fila seleccionada en la tabla de usuarios
        selected_row = self.users_table.currentRow()
        if selected_row >= 0:
            # Eliminar la fila seleccionada de la tabla de usuarios y el usuario correspondiente de la lista de usuarios
            self.users_table.removeRow(selected_row)
            del self.users[selected_row]

    def update_user(self):
        # Obtener la fila seleccionada en la tabla de usuarios
        selected_row = self.users_table.currentRow()
        if selected_row >= 0:
            # Actualizar los datos de la fila seleccionada en la tabla de usuarios con los valores ingresados en los campos de edición
            self.users_table.setItem(selected_row, 0, QTableWidgetItem(str(selected_row + 1)))
            self.users_table.setItem(selected_row, 1, QTableWidgetItem(self.user_name_edit.text()))
            self.users_table.setItem(selected_row, 2, QTableWidgetItem(self.user_email_edit.text()))
            self.users_table.setItem(selected_row, 3, QTableWidgetItem(self.user_password_edit.text()))
            self.users_table.setItem(selected_row, 4, QTableWidgetItem(self.user_role_edit.text()))

    def update_loans_table(self):
        # Limpiar el contenido de la tabla de préstamos
        self.loans_table.clearContents()
        row = 0
        # Iterar sobre la lista de préstamos y agregar cada préstamo a la tabla de préstamos
        for loan in self.loans:
            self.loans_table.insertRow(row)
            self.loans_table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.loans_table.setItem(row, 1, QTableWidgetItem(loan["member_name"] + " (" + loan["member_dpi"] + ")"))
            self.loans_table.setItem(row, 2, QTableWidgetItem(loan["status"]))
            self.loans_table.setItem(row, 3, QTableWidgetItem(str(loan["amount_requested"])))
            self.loans_table.setItem(row, 4, QTableWidgetItem(str(loan["num_payments"])))
            self.loans_table.setItem(row, 5, QTableWidgetItem(str(loan["amount_approved"])))
            self.loans_table.setItem(row, 6, QTableWidgetItem(str(loan["monthly_income"])))
            self.loans_table.setItem(row, 7, QTableWidgetItem(loan["guarantee"]))
            self.loans_table.setItem(row, 8, QTableWidgetItem(loan["file"]))
            row += 1

    def update_users_table(self):
        # Limpiar el contenido de la tabla de usuarios
        self.users_table.clearContents()
        row = 0
        # Iterar sobre la lista de usuarios y agregar cada usuario a la tabla de usuarios
        for user in self.users:
            self.users_table.insertRow(row)
            self.users_table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.users_table.setItem(row, 1, QTableWidgetItem(user["name"]))
            self.users_table.setItem(row, 2, QTableWidgetItem(user["email"]))
            self.users_table.setItem(row, 3, QTableWidgetItem(user["password"]))
            self.users_table.setItem(row, 4, QTableWidgetItem(user["role"]))
            row += 1

    def check_admin_access(self, index):
        if index == 2:  # Índice de la pestaña "Usuarios"
            if self.current_user and self.current_user["role"] == "admin":
                pass  # Permitir acceso a la pestaña de usuarios
            else:
                self.authenticate_admin()
        else:
            pass  # Permitir acceso a otras pestañas

    def authenticate_admin(self):
        # Solicitar la contraseña de administrador para acceder a la pestaña de usuarios
        password, ok = QInputDialog.getText(self, "Autenticación de administrador",
                                            "Ingrese la contraseña de administrador:", QLineEdit.Password)
        if ok and password == "1234":  # Contraseña de administrador válida
            self.current_user = {"role": "admin"}  # Establecer el usuario actual como administrador
        else:
            # Mostrar un mensaje de advertencia si la contraseña es incorrecta
            QMessageBox.warning(self, "Acceso denegado",
                                "Contraseña incorrecta. No se puede acceder a la pestaña de usuarios.")

    # Crear una instancia de la aplicación QApplication
app = QApplication(sys.argv)
    # Crear una instancia de la ventana principal YKBank
window = YKBank()
    # Mostrar la ventana principal
window.show()
    # Salir de la aplicación cuando se cierra la ventana
sys.exit(app.exec_())
