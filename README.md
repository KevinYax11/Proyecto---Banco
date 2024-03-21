# Proyecto---Banco
Primer Proyecto Sobre Un Banco - Estructuras De Datos I - Universidad Rafael Landivar

El proyecto consiste en una aplicación de gestión bancaria llamada "Tinkoff Bank", desarrollada utilizando Python y la biblioteca PyQt5 para la interfaz gráfica. La aplicación proporciona funcionalidades para administrar asociados, préstamos y usuarios.

Funcionalidades Principales:

1. **Gestión de Asociados:**
   - Permite agregar, eliminar y administrar información de los asociados, como nombre, dirección, teléfono, DPI, NIT, archivos adjuntos y referencias.
   - Utiliza una estructura de datos de lista circular enlazada para almacenar la información de los asociados.

2. **Gestión de Préstamos:**
   - Permite solicitar préstamos, aprobarlos y pagar las cuotas.
   - La pestaña de préstamos muestra una tabla con información detallada sobre cada préstamo, como el código, el asociado, el estado, el monto solicitado, el número de cuotas, el monto aprobado, los ingresos, la       garantía y los archivos adjuntos.

3. **Gestión de Usuarios:**
   - Permite agregar, eliminar y actualizar información de los usuarios del sistema, incluyendo nombre, correo electrónico, contraseña y puesto.
   - Requiere autenticación de administrador para acceder a esta funcionalidad.

Librerías Utilizadas:
- PyQt5: Para crear la interfaz gráfica de usuario.
- sys: Para interactuar con el sistema operativo y la salida estándar.
- QFileDialog: Para abrir ventanas de diálogo para seleccionar archivos.
- QMessageBox: Para mostrar mensajes emergentes de advertencia o información.
- QInputDialog: Para obtener información del usuario a través de cuadros de diálogo de entrada.
- CircularLinkedList: Implementada manualmente para gestionar la lista de asociados de forma circular.

En resumen, "Tinkoff Bank" es una aplicación de gestión bancaria que permite administrar asociados, préstamos y usuarios de manera eficiente a través de una interfaz gráfica intuitiva y funcionalidades bien diseñadas.
