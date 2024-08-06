# from main import Printer
# from tkinter import ttk
# from tkinter import *
#
#
# def imprimir_boton(printer_type, ip, txt, usb_address) -> None:
#     printer = Printer(printer_type, ip, usb_address)
#     printer.imprimir(txt)
#
#
# if __name__ == '__main__':
#     print("Menu - Interfaz Grafica")
#     # Caja de texto
#     texto = "hola1\nhola2\n"
#     # Radio de opciones
#     user_printer_type = 'IP'
#
#     # BOTON DE LA VISTA PARA IMPRIMIR
#     imprimir_boton(user_printer_type, '10.0.0.70', texto, '')


from main import Printer
# Configuración de la ventana principal
import tkinter as tk
from tkinter import ttk


def imprimir(user_printer_type, txt, ip, usb_address):
    printer = Printer(user_printer_type, ip, usb_address)
    printer.imprimir(txt)


def handle_imprimir():
    # Aquí va el código que manejará la impresión del contenido del Text widget
    user_printer_type = selected_option.get()
    print(f"metodo: {user_printer_type}.")
    txt = text_area.get("1.0", tk.END)
    print(f"data: {txt}")
    ip = entry_ip.get()
    print(f"direccion IP: {ip}")
    usb_address = entry_usb.get()
    print(f"direccion USB: {usb_address}")

    imprimir(user_printer_type, txt, ip, usb_address)

    # printer = Printer(user_printer_type, ip, usb_address)
    # printer.imprimir(txt)


# def center_window(root_tk, width=600, height=400):
#     # Obtener el tamaño de la pantalla
#     screen_width = root_tk.winfo_screenwidth()
#     screen_height = root_tk.winfo_screenheight()
#     # Calcular la posición x y y para centrar la ventana
#     x = (screen_width - width) // 2
#     y = (screen_height - height) // 2
#     root_tk.geometry(f'{width}x{height}+{x}+{y}')
#
#
# # Configuración de la ventana principal
# root = tk.Tk()
# root.title("Formulario de Selección")
#
# # Centrar la ventana
# center_window(root)
#
# # Crear un frame para contener los widgets
# frame = ttk.Frame(root, padding="10 10 10 10")
# frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
# # Etiqueta y opciones de selección
# ttk.Label(frame, text="Seleccione una opción:").grid(row=0, column=0, sticky=tk.W)
# selected_option = tk.StringVar(value="IP")
# ttk.Radiobutton(frame, text="IP", variable=selected_option, value="IP").grid(row=1, column=0, sticky=tk.W)
# ttk.Radiobutton(frame, text="USB", variable=selected_option, value="USB").grid(row=1, column=1, sticky=tk.W)
#
# # Área de texto grande
# ttk.Label(frame, text="Ingrese el texto:").grid(row=3, column=0, sticky=tk.W)
# text_area = tk.Text(frame, wrap="word", height=15, width=30)
# text_area.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
#
# # Barra de desplazamiento para el área de texto
# scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_area.yview)
# scrollbar.grid(row=4, column=2, sticky=(tk.N, tk.S))
# text_area['yscrollcommand'] = scrollbar.set
#
# # Botón de imprimir
# ttk.Button(frame, text="Imprimir", command=handle_imprimir).grid(row=5, column=0, columnspan=3, pady=(10, 0))
#
# # Expandir el frame para llenar la ventana
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# frame.columnconfigure(1, weight=1)
#
# root.mainloop()
def center_window(root_tk, width=600, height=400):
    # Obtener el tamaño de la pantalla
    screen_width = root_tk.winfo_screenwidth()
    screen_height = root_tk.winfo_screenheight()
    # Calcular la posición x y y para centrar la ventana
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root_tk.geometry(f'{width}x{height}+{x}+{y}')


def on_option_change(*args):
    selected = selected_option.get()
    if selected == "IP":
        entry_ip.config(state='normal')
        entry_usb.config(state='disabled')
    elif selected == "USB":
        entry_ip.config(state='disabled')
        entry_usb.config(state='normal')


# Configuración de la ventana principal
root = tk.Tk()
root.title("Thermal Print App")

# Centrar la ventana
center_window(root)

# Crear un frame para contener los widgets
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiqueta y opciones de selección
ttk.Label(frame, text="Seleccione una opción:").grid(row=0, column=0, sticky=tk.W)
selected_option = tk.StringVar()
selected_option.trace('w', on_option_change)
ttk.Radiobutton(frame, text="IP", variable=selected_option, value="IP").grid(row=1, column=0, sticky=tk.W)
ttk.Radiobutton(frame, text="USB", variable=selected_option, value="USB").grid(row=2, column=0, sticky=tk.W)

# Entradas para IP y USB
entry_ip = ttk.Entry(frame)
entry_ip.grid(row=1, column=1, sticky=tk.W)

entry_usb = ttk.Entry(frame)
entry_usb.grid(row=2, column=1, sticky=tk.W)

# Área de texto grande
ttk.Label(frame, text="Ingrese el texto:").grid(row=3, column=0, sticky=tk.W)
text_area = tk.Text(frame, wrap="word", height=15, width=30)
text_area.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E))

# Barra de desplazamiento para el área de texto
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_area.yview)
scrollbar.grid(row=4, column=3, sticky=(tk.N, tk.S))
text_area['yscrollcommand'] = scrollbar.set

# Botón de imprimir
ttk.Button(frame, text="Imprimir", command=handle_imprimir).grid(row=5, column=0, columnspan=3, pady=(10, 0))

# Expandir el frame para llenar la ventana
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Inicializar la opción seleccionada
selected_option.set("IP")
on_option_change()

root.mainloop()
