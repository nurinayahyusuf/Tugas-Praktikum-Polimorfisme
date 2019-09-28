class FakultasTeknik:
    def __init__(self, univ, fak, ta):
        self.univ = univ
        self.fak = fak
        self.ta = ta
    def cetakdata(self):
        print('Universitas       :',self.univ)
        print('Fakultas          :',self.fak)
        print('Tahun Ajaran      :',self.ta)

class TeknikKomputer(FakultasTeknik):
    def __init__(self, univ, fak, ta, ja):
        self.ja = ja
        FakultasTeknik.__init__(self, univ, fak, ta)

    def cetakdataA(self):
        print('Jumlah Angkatan   :',self.ja)

class Mekatronika(FakultasTeknik):
    def __init__(self, univ, fak, ta, ja):
        self.ja = ja
        FakultasTeknik.__init__(self, univ, fak, ta)

    def cetakdataB(self):
        print('Jumlah Angkatan   :',self.ja)

class PTIK(FakultasTeknik):
    def __init__(self, univ, fak, ta, ja, ju):
        self.ja = ja
        self.ju = ju
        FakultasTeknik.__init__(self, univ, fak, ta)

    def cetakdataC(self):
        print('Jumlah Angkatan   :',self.ja)
        print('Jurusan           :',self.ju)

def main():

    obj = FakultasTeknik('Universitas Negeri Makassar', 'Teknik', 2018)
    obj.cetakdata()

    del obj

    obj = TeknikKomputer('Universitas Negeri Makassar', 'Teknik', 2018, 2)
    print('\nTeknik Komputer\n')
    obj.cetakdata()
    obj.cetakdataA()

    obj = Mekatronika('Universitas Negeri Makassar', 'Teknik', 2018, 2)
    print('\nMekatronika\n')
    obj.cetakdata()
    obj.cetakdataB()

    del obj

    obj = PTIK('Universitas Negeri Makassar', 'Teknik', 2018, 13, 'Pendidikan Teknik Elektro')
    print('\nPendidikan Teknik Informatika & Komputer\n')
    obj.cetakdata()
    obj.cetakdataC()

if __name__== "__main__":
   main ()
