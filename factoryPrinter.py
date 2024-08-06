from printerStrategy import PrinterStrategy, PrinterIP, PrinterUSB


class FactoryPrinter:

    @staticmethod
    def get_printer(printer_type, ip, usb_address) -> PrinterStrategy:
        if printer_type == 'IP':
            return PrinterIP(ip)
        if printer_type == 'USB':
            return PrinterUSB(usb_address)

        raise Exception("Unkown Printer")
