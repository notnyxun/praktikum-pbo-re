import math

class Number:
    """
    Class Number yang merepresentasikan angka dengan operasi matematika
    menggunakan dunder methods untuk operator overloading
    """
    def __init__(self, value=0):
        self.value = float(value)
    
    def __str__(self):
        # Menghilangkan desimal jika nilai adalah bilangan bulat
        if self.value == int(self.value):
            return str(int(self.value))
        return str(self.value)
    
    def __repr__(self):
        return f"Number({self.value})"
    
    # Dunder method untuk operasi penjumlahan (+)
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return Number(self.value + float(other))
    
    # Dunder method untuk operasi pengurangan (-)
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return Number(self.value - float(other))
    
    # Dunder method untuk operasi perkalian (*)
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return Number(self.value * float(other))
    
    # Dunder method untuk operasi pembagian (/)
    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                raise ValueError("Pembagian dengan nol tidak diperbolehkan")
            return Number(self.value / other.value)
        if float(other) == 0:
            raise ValueError("Pembagian dengan nol tidak diperbolehkan")
        return Number(self.value / float(other))
    
    # Dunder method untuk operasi perpangkatan (^)
    def __pow__(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value)
        return Number(self.value ** float(other))
    
    # Method untuk operasi logaritma
    def log(self, base=10):
        if self.value <= 0:
            raise ValueError("Logaritma hanya didefinisikan untuk nilai positif")
        
        if isinstance(base, Number):
            base_value = base.value
        else:
            base_value = float(base)
        
        if base_value <= 0 or base_value == 1:
            raise ValueError("Basis logaritma harus positif dan tidak sama dengan 1")
        
        return Number(math.log(self.value, base_value))
    
    # Dunder method untuk operasi kesetaraan (==)
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        return self.value == float(other)
    
    # Dunder method untuk operasi tidak sama dengan (!=)
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Dunder method untuk operasi lebih besar dari (>)
    def __gt__(self, other):
        if isinstance(other, Number):
            return self.value > other.value
        return self.value > float(other)
    
    # Dunder method untuk operasi lebih kecil dari (<)
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value
        return self.value < float(other)
    
    # Dunder method untuk operasi lebih besar atau sama dengan (>=)
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    
    # Dunder method untuk operasi lebih kecil atau sama dengan (<=)
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    # Dunder method untuk konversi ke float
    def __float__(self):
        return float(self.value)
    
    # Dunder method untuk konversi ke int
    def __int__(self):
        return int(self.value)


# Abstract Base Class (ABC) untuk operasi matematika
class MathOperation:
    """
    Abstract Base Class untuk operasi matematika
    """
    def operate(self, a, b):
        """
        Method abstrak yang harus diimplementasikan oleh subclass
        """
        raise NotImplementedError("Subclass harus mengimplementasikan method operate()")
    
    def get_symbol(self):
        """
        Method abstrak untuk mendapatkan simbol operasi
        """
        raise NotImplementedError("Subclass harus mengimplementasikan method get_symbol()")


# Implementasi konkrit dari operasi matematika (Polimorfisme)
class Addition(MathOperation):
    def operate(self, a, b):
        return a + b
    
    def get_symbol(self):
        return "+"


class Subtraction(MathOperation):
    def operate(self, a, b):
        return a - b
    
    def get_symbol(self):
        return "-"


class Multiplication(MathOperation):
    def operate(self, a, b):
        return a * b
    
    def get_symbol(self):
        return "*"


class Division(MathOperation):
    def operate(self, a, b):
        if isinstance(b, Number):
            if b.value == 0:
                raise ValueError("Pembagian dengan nol tidak diperbolehkan")
        elif float(b) == 0:
            raise ValueError("Pembagian dengan nol tidak diperbolehkan")
        return a / b
    
    def get_symbol(self):
        return "/"


class Power(MathOperation):
    def operate(self, a, b):
        return a ** b
    
    def get_symbol(self):
        return "^"


class Logarithm(MathOperation):
    def operate(self, a, b):
        if isinstance(a, Number):
            return a.log(b)
        else:
            num = Number(a)
            return num.log(b)
    
    def get_symbol(self):
        return "log"


class Calculator:
    """
    Class Calculator yang menggunakan abstraksi dan polimorfisme
    untuk melakukan operasi matematika
    """
    def __init__(self):
        # Dictionary untuk memetakan simbol operasi ke objek operasi
        self.operations = {
            "+": Addition(),
            "-": Subtraction(),
            "*": Multiplication(),
            "/": Division(),
            "^": Power(),
            "log": Logarithm()
        }
    
    def calculate(self, a, b, operation_symbol):
        """
        Melakukan kalkulasi menggunakan polimorfisme dari operasi matematika
        """
        # Konversi input ke objek Number jika belum
        a_num = a if isinstance(a, Number) else Number(a)
        b_num = b if isinstance(b, Number) else Number(b)
        
        # Cek apakah operasi yang diminta ada
        if operation_symbol not in self.operations:
            raise ValueError(f"Operasi '{operation_symbol}' tidak didukung")
        
        # Gunakan polimorfisme untuk melakukan operasi
        operation = self.operations[operation_symbol]
        return operation.operate(a_num, b_num)
    
    def get_available_operations(self):
        """
        Mendapatkan daftar operasi yang tersedia
        """
        return list(self.operations.keys())


def demo_calculator():
    """
    Fungsi untuk mendemonstrasikan penggunaan kalkulator
    """
    calc = Calculator()
    print("=== Kalkulator dengan Dunder Methods, Abstraksi, dan Polimorfisme ===")
    print("Operasi yang tersedia:", ", ".join(calc.get_available_operations()))
    
    # Contoh penggunaan
    a = Number(10)
    b = Number(2)
    
    print(f"\nContoh operasi dengan objek Number:")
    print(f"{a} + {b} = {calc.calculate(a, b, '+')}")
    print(f"{a} - {b} = {calc.calculate(a, b, '-')}")
    print(f"{a} * {b} = {calc.calculate(a, b, '*')}")
    print(f"{a} / {b} = {calc.calculate(a, b, '/')}")
    print(f"{a} ^ {b} = {calc.calculate(a, b, '^')}")
    print(f"log_{b}({a}) = {calc.calculate(a, b, 'log')}")
    
    # Contoh dengan nilai langsung
    print(f"\nContoh operasi dengan nilai langsung:")
    print(f"15 + 5 = {calc.calculate(15, 5, '+')}")
    print(f"15 - 5 = {calc.calculate(15, 5, '-')}")
    print(f"15 * 5 = {calc.calculate(15, 5, '*')}")
    print(f"15 / 5 = {calc.calculate(15, 5, '/')}")
    print(f"15 ^ 2 = {calc.calculate(15, 2, '^')}")
    print(f"log_2(8) = {calc.calculate(8, 2, 'log')}")
    
    # Contoh penggunaan dunder methods langsung
    print(f"\nContoh penggunaan dunder methods langsung:")
    x = Number(20)
    y = Number(4)
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} ^ {y} = {x ** y}")
    print(f"log_{y}({x}) = {x.log(y)}")
    
    # Contoh perbandingan
    print(f"\nContoh operasi perbandingan:")
    print(f"{x} == {y}: {x == y}")
    print(f"{x} != {y}: {x != y}")
    print(f"{x} > {y}: {x > y}")
    print(f"{x} < {y}: {x < y}")
    print(f"{x} >= {y}: {x >= y}")
    print(f"{x} <= {y}: {x <= y}")


if __name__ == "__main__":
    demo_calculator()
