class TomadaDeTresPinos:
    def ligar_na_tomada_de_tres_pinos(self):
        return "Ligado na tomada de três pinos."

class Adaptador(TomadaDeTresPinos):
    def __init__(self, tomada_de_dois_pinos):
        self.tomada_de_dois_pinos = tomada_de_dois_pinos

    def ligar_na_tomada_de_tres_pinos(self):
        return self.tomada_de_dois_pinos.ligar_na_tomada_de_dois_pinos()

class TomadaDeDoisPinos:
    def ligar_na_tomada_de_dois_pinos(self):
        return "Ligado na tomada de dois pinos."

def main():
    tomada_de_dois_pinos = TomadaDeDoisPinos()
    adaptador = Adaptador(tomada_de_dois_pinos)

    print(adaptador.ligar_na_tomada_de_tres_pinos())  # Saída: Ligado na tomada de dois pinos.

if __name__ == "__main__":
    main()
