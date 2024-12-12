from animal import animal

# setiap class child itu memiliki 2 properti dan method
class amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas
    
    def info_amphibi(self):
        super().info_animal()
        print(f"Jenis Air \t\t\t : ", self.jenis_air,
              "\nBernapas \t\t\t : ", self.bernapas)
        
katak = amphibi("Katak","Serangga","Dua alam", "Bertelur", "Air Tawar", "Kulit dan Paru-paru")
katak.info_amphibi()
print("==============================================================")
kadal_air= amphibi("Kadal", "Serangga", "Air", "Bertelur dan Ovipar", "Air Tawar", "Paru-paru, kulit, dan rongga mulut")
kadal_air.info_amphibi()
print("================================================================================")
biawak = amphibi ("Biawak", "Serangga", "Dua alam", "Bertelur", "Air Tawar", "Paru-paru")
biawak.info_amphibi()
