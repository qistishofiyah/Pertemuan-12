from animal import animal

class karnivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kecepatan_berlari, jenis_gigi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.kecepatan_berlari = kecepatan_berlari
        self.jenis_gigi = jenis_gigi

    def info_karnivora(self):
        super().info_animal()
        print(f"kecepatan berlari \t\t : ", self.kecepatan_berlari,
               "\njenis gigi \t\t\t : ", self.jenis_gigi)
        
singa = karnivora ("Singa", "Daging", "Darat", "Melahirkan", "Sangat Tinggi", "Gigi seri,gigi taring,gigi geraham")
singa.info_karnivora()
print("======================================================================")
harimau = karnivora ("Harimau", "Daging", "Darat", "Melahirkan", "Sangat Tinggi", "Gigi seri,gigi taring,gigi geraham depan,gigi geraham belakang")
harimau.info_karnivora()
print("==================================================================================================")
beruang = karnivora ("Beruang", "Daging", "Darat", "Melahirkan", "Lambat","Gigi taring, gigi geraham depan,gigi molar")
beruang.info_karnivora()