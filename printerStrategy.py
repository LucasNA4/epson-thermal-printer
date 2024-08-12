from abc import ABC, abstractmethod

from escpos import printer
from escpos.printer import Network, Usb


class PrinterStrategy(ABC):
    @abstractmethod
    def imprimir(self, txt: str) -> None:
        pass

    @abstractmethod
    def cortar(self) -> None:
        pass

    def apagar(self) -> None:
        pass


class PrinterIP(PrinterStrategy):
    # ip: str
    kitchen: Network = None

    def __init__(self, ip: str):
        # self.ip = ip
        self.kitchen = Network(ip)

    def imprimir(self, txt: str) -> None:
        self.kitchen.set(align='center', font='a', bold=True, width=4, height=3, custom_size=True, smooth=True)
        self.kitchen.line_spacing(spacing=58, divisor=180)
        self.kitchen.text(txt)

    def cortar(self) -> None:
        self.kitchen.cut("PART")

    def cancelar(self) -> None:
        self.kitchen.eject_slip()

    def apagar(self) -> None:
        self.kitchen.close()


class PrinterUSB(PrinterStrategy):
    usb_address: str
    printer_usb: Usb

    def __init__(self, usb_address: str):
        self.usb_address = usb_address
        self.printer_usb = printer.Usb(0x04b8, 0x0E15)
        self.printer_usb.open()

    def imprimir(self, txt: str) -> None:
        self.printer_usb.set(align='center', font='a', bold=True, width=4, height=4, custom_size=True, smooth=True)
        self.printer_usb.line_spacing(spacing=58, divisor=180)
        self.printer_usb.text(txt)

    def cortar(self) -> None:
        self.printer_usb.cut("PART")

    def apagar(self) -> None:
        self.printer_usb.close()
