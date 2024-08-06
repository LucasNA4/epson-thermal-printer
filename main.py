from printerStrategy import PrinterStrategy
from factoryPrinter import FactoryPrinter


class Printer:
    printer_type: str
    ip: str = ''
    usb_address: str = ''
    printer: PrinterStrategy = None

    def __init__(self, printer_type, ip, usb_address) -> None:
        self.printer_type = printer_type
        self.ip = ip
        self.usb_address = usb_address

        self.printer = FactoryPrinter.get_printer(self.printer_type, self.ip, self.usb_address)

    def imprimir(self, txt_imprimir: str):
        chunks = txt_imprimir.split('\n')

        for chunk in chunks:
            if chunk != '':
                self.printer.imprimir(chunk)
                self.printer.cortar()
