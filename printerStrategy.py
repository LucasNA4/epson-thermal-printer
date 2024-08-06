from abc import ABC, abstractmethod
from escpos.printer import Network


class PrinterStrategy(ABC):
    @abstractmethod
    def imprimir(self, txt: str) -> None:
        pass

    @abstractmethod
    def cortar(self) -> None:
        pass


class PrinterIP(PrinterStrategy):
    # ip: str
    kitchen: Network = None

    def __init__(self, ip: str):
        # self.ip = ip
        self.kitchen = Network(ip)

    def imprimir(self, txt: str) -> None:
        self.kitchen.text(txt)

    def cortar(self) -> None:
        self.kitchen.cut("PART")

    def cancelar(self) -> None:
        self.kitchen.eject_slip()


class PrinterUSB(PrinterStrategy):
    usb_address: str

    def __init__(self, usb_address: str):
        self.usb_address = usb_address

    def imprimir(self, txt: str) -> None:
        pass

    def cortar(self) -> None:
        pass
