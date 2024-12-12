from animal import animal

class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_kulit, ukuran_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.ukuran_tubuh = ukuran_tubuh
        

    def info_mamalia(self):
        super().info_animal()
        print(f"Jenis kulit \t\t\t : ", self.jenis_kulit,
               "\nUkuran_tubuh \t\t\t : ", self.ukuran_tubuh)

kucing = mamalia ("Kucing", "Ikan", "Darat", "Melahirkan", "Berbulu", "Kecil")
kucing.info_mamalia()
print("======================")
gajah = mamalia ("Gajah", "Tumbuh-tumbuhan", "Darat", "Melahirkan", "Sedikit Berbulu", "Besar")
gajah.info_mamalia()
print("======================")
kelinci = mamalia ("Kelinci", "Tumbuh-tumbuhan", "Darat", "Melahirkan", "Berbulu", "Kecil")
kelinci.info_mamalia()
        