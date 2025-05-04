import random

class Father:
    def __init__(self, blood_type):
        """
        Inisialisasi kelas Father dengan golongan darah.
        
        Args:
            blood_type (str): Golongan darah ayah (A, B, AB, atau O)
        """
        self.blood_type = blood_type
        self.alleles = self._determine_alleles(blood_type)
    
    def _determine_alleles(self, blood_type):
        """
        Menentukan alel berdasarkan golongan darah.
        
        Args:
            blood_type (str): Golongan darah (A, B, AB, atau O)
        
        Returns:
            list: Daftar alel yang mungkin dimiliki
        """
        if blood_type == "A":
            return ["A", "A"] if random.random() < 0.5 else ["A", "O"]
        elif blood_type == "B":
            return ["B", "B"] if random.random() < 0.5 else ["B", "O"]
        elif blood_type == "AB":
            return ["A", "B"]
        elif blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah harus A, B, AB, atau O")


class Mother:
    def __init__(self, blood_type):
        """
        Inisialisasi kelas Mother dengan golongan darah.
        
        Args:
            blood_type (str): Golongan darah ibu (A, B, AB, atau O)
        """
        self.blood_type = blood_type
        self.alleles = self._determine_alleles(blood_type)
    
    def _determine_alleles(self, blood_type):
        """
        Menentukan alel berdasarkan golongan darah.
        
        Args:
            blood_type (str): Golongan darah (A, B, AB, atau O)
        
        Returns:
            list: Daftar alel yang mungkin dimiliki
        """
        if blood_type == "A":
            return ["A", "A"] if random.random() < 0.5 else ["A", "O"]
        elif blood_type == "B":
            return ["B", "B"] if random.random() < 0.5 else ["B", "O"]
        elif blood_type == "AB":
            return ["A", "B"]
        elif blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah harus A, B, AB, atau O")


class Child:
    def __init__(self, father, mother):
        """
        Inisialisasi kelas Child dengan menerima objek Father dan Mother.
        
        Args:
            father (Father): Objek dari kelas Father
            mother (Mother): Objek dari kelas Mother
        """
        self.father = father
        self.mother = mother
        self.inherited_alleles = self._inherit_alleles()
        self.blood_type = self._determine_blood_type()
    
    def _inherit_alleles(self):
        """
        Mewarisi alel secara acak dari kedua orang tua.
        
        Returns:
            list: Daftar alel yang diwarisi [dari_ayah, dari_ibu]
        """
        # Memilih satu alel secara acak dari ayah
        father_allele = random.choice(self.father.alleles)
        
        # Memilih satu alel secara acak dari ibu
        mother_allele = random.choice(self.mother.alleles)
        
        return [father_allele, mother_allele]
    
    def _determine_blood_type(self):
        """
        Menentukan golongan darah berdasarkan alel yang diwarisi.
        
        Returns:
            str: Golongan darah anak (A, B, AB, atau O)
        """
        alleles = sorted(self.inherited_alleles)
        
        if alleles == ["A", "A"] or alleles == ["A", "O"]:
            return "A"
        elif alleles == ["B", "B"] or alleles == ["B", "O"]:
            return "B"
        elif alleles == ["A", "B"]:
            return "AB"
        elif alleles == ["O", "O"]:
            return "O"
        else:
            return "Tidak valid"
    
    def display_inheritance(self):
        """
        Menampilkan informasi pewarisan golongan darah.
        """
        print(f"Golongan darah Ayah: {self.father.blood_type} (alel: {self.father.alleles})")
        print(f"Golongan darah Ibu: {self.mother.blood_type} (alel: {self.mother.alleles})")
        print(f"Anak mewarisi alel: {self.inherited_alleles}")
        print(f"Golongan darah Anak: {self.blood_type}")


def main():
    """
    Fungsi utama untuk menjalankan simulasi pewarisan golongan darah.
    """
    print("=== SIMULASI PEWARISAN GOLONGAN DARAH ===")
    
    # Input golongan darah dari pengguna
    while True:
        father_blood = input("Masukkan golongan darah Ayah (A/B/AB/O): ").upper()
        if father_blood in ["A", "B", "AB", "O"]:
            break
        print("Golongan darah tidak valid. Masukkan A, B, AB, atau O.")
    
    while True:
        mother_blood = input("Masukkan golongan darah Ibu (A/B/AB/O): ").upper()
        if mother_blood in ["A", "B", "AB", "O"]:
            break
        print("Golongan darah tidak valid. Masukkan A, B, AB, atau O.")
    
    # Membuat objek Father dan Mother
    father = Father(father_blood)
    mother = Mother(mother_blood)
    
    # Membuat objek Child
    child = Child(father, mother)
    
    print("\n=== HASIL PEWARISAN ===")
    child.display_inheritance()
    
    # Simulasi probabilitas
    print("\n=== SIMULASI PROBABILITAS ===")
    results = {"A": 0, "B": 0, "AB": 0, "O": 0}
    trials = 1000
    
    for _ in range(trials):
        temp_child = Child(father, mother)
        results[temp_child.blood_type] += 1
    
    print(f"Setelah {trials} kali simulasi, probabilitas golongan darah anak:")
    for blood_type, count in results.items():
        probability = (count / trials) * 100
        print(f"Golongan darah {blood_type}: {probability:.2f}%")


if __name__ == "__main__":
    main()