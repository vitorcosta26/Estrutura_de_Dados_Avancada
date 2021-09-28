
class Arvore:
    def __init__(self, elemento):
        self.elemento = elemento
        self.filhos = []
        self.pai = None
    
    def set_filho(self, filho):
        filho.pai = self
        self.filhos.append(filho)
    
    def get_raiz(self):
        if self.get_nivel() == 0 and self.pai == None:
            print(self.elemento)
        else:
            return self.pai.get_raiz()
    
    def get_nos(self):
        if self.pai == None:
            pass
        else:
            print(self.elemento)
        if self.filhos:
            for filho in self.filhos:
                filho.get_nos()
    
    def get_folhas(self):
        if self.filhos:
            for filho in self.filhos:
                filho.get_folhas()
        else:
            print(self.elemento)
    
    def get_grau(self):
        return len(self.filhos)
    
    def get_altura(self):
        if self.filhos:
            for filho in self.filhos:
                return 1 + filho.get_altura()
        else:
            return 0
    
    def get_profundidade(self):
        profundidade = 0
        ancestral = self.pai
        while ancestral:
            profundidade += 1
            ancestral = ancestral.pai
        return profundidade
    
    def get_nivel(self):
        nivel = 0
        ancestral = self.pai
        while ancestral:
            nivel += 1
            ancestral = ancestral.pai
        return nivel

    def get_arvore(self):
        espacos = " " * self.get_nivel() * 2
        prefixo = espacos + "|_" if self.pai else ""
        print(prefixo + str(self.elemento))
        if self.filhos:
            for filho in self.filhos:
                filho.get_arvore()
