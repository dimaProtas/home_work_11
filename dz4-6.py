printer_warehouse = []
scanner_warehous = []
copier_warehous = []


class Warehouse:
    def __init__(self, name_department):
        self.name_departament = self.__class__.__name__


    def name_class(self):
        return f'Склад: {self.__class__.__name__}'


class OfficeEquipment(Warehouse):
    def __init__(self, model, firms, quantity):
        self.model = model
        self.firms = firms
        self.quantity = quantity


    def reception(self):
        dict_teh = {}
        if self.model == 'printer':
            print(f'Отправить на склад {Printer} :')
        elif self.model == 'scanner':
            print(f'Отправить на склад {Scanner} :')
        elif self.model == 'copier':
            print(f'Отправить на склад {Copier} :')
        else:
            print(f'Оборудование "{self.model}" не определино!')
        dict_teh[self.firms] = self.model
        if type(self.quantity) != int:
            raise ValueError(f'Невозможный параметр {self.quantity}, принимает только число!')
        else:
            dict_teh['quantity'] = self.quantity
        return dict_teh


class Printer(OfficeEquipment):
    def __init__(self, model, firm, quantity, color):
        super().__init__(model, firm, quantity)
        self.color = color


    def reception(self):
        printer = {}
        if self.model == 'printer':
            printer[self.firms] = self.model
            if type(self.quantity) != int:
                raise ValueError(f'Невозможный параметр {self.quantity}, принимает только число!')
            else:
                printer['quantity'] = self.quantity
            printer['color'] = self.color
        else:
            raise ValueError(f'определить на склад {self.model} !')
        printer_warehouse.append(printer)
        return printer


class Scanner(OfficeEquipment):
    def __init__(self, model, firm, quantity, size_screen):
        super().__init__(model, firm, quantity)
        self.size_screen = size_screen


    def reception(self):
        scanner = {}
        if self.model == 'scanner':
            scanner[self.firms] = self.model
            if type(self.quantity) != int:
                raise ValueError(f'Невозможный параметр {self.quantity}, принимает только число!')
            else:
                scanner['quantity'] = self.quantity
            scanner['size_screen'] = self.size_screen
        else:
            raise ValueError(f'определить на склад {self.model} !')
        scanner_warehous.append(scanner)
        return scanner


class Copier(OfficeEquipment):
    def __init__(self, model, firm, quantity, device_size):
        super().__init__(model, firm, quantity)
        self.device_size = device_size


    def reception(self):
        copier = {}
        if self.model == 'copier':
            copier[self.firms] = self.model
            if type(self.quantity) != int:
                raise ValueError(f'Невозможный параметр {self.quantity}, принимает только число!')
            else:
                copier['quantity'] = self.quantity
            copier['device_size'] = self.device_size
        else:
            raise ValueError(f'определить на склад {self.model} !')
        copier_warehous.append(copier)
        return copier


b = OfficeEquipment('printer', 'sumsung', 354)
a = Printer('printer', 'xiaomi', 122, 'green')
c = OfficeEquipment('copier', 'filips', 12)
d = Printer('printer', 'filips', 567, 'red')
f = Scanner('scanner', 'sonny', 56, '5x4')
g = Copier('copier', 'LG', 124, '12x15')
print(g.reception(), g.name_class())
print(f.reception(), f.name_class())
print(d.reception(), d.name_class())
print(c.reception(), c.name_class())
print(b.reception(), b.name_class())
print(a.reception(), a.name_class())
print(printer_warehouse)

