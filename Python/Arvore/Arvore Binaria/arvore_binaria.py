from No import No

class ArvoreBinaria:
    def __init__(self):
        self.raiz = No(None, None, None, None, None)
        self.raiz = None

    def get_raiz(self):
        return self.raiz.elemento

    def inserir(self, elemento):
        novo = No(elemento, None, None, None, None)
        nivel = 0
        if self.raiz == None:
            novo.nivel = nivel
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                nivel += 1
                novo.nivel = nivel
                novo.pai = atual
                anterior = atual
                if elemento <= atual.elemento:
                    atual = atual.esquerdo
                    if atual == None:
                        anterior.esquerdo = novo
                        return
                else:
                    atual = atual.direito
                    if atual == None:
                        anterior.direito = novo
                        return

    def remover(self, elemento):
        if self.raiz == None:
            return False
        atual = self.raiz
        pai = self.raiz
        filho_esquerdo = True
        while atual.elemento != elemento:
            pai = atual
            if elemento < atual.elemento:
                atual = atual.esquerdo
                filho_esquerdo = True
            else:
                atual = atual.direito
                filho_esquerdo = False
            nivel = atual.nivel
            if atual == None:
                return False

        if atual.esquerdo == None and atual.direito == None:
            if atual == self.raiz:
                self.raiz = None
            else:
                if filho_esquerdo:
                    pai.esquerdo = None
                else:
                    pai.direito = None

        elif atual.direito == None:
            if atual == self.raiz:
                self.raiz = atual.esquerdo
                self.raiz.nivel = 0
            else:
                atual.esquerdo.nivel = nivel
                if filho_esquerdo:
                    pai.esquerdo = atual.esquerdo
                else:
                    pai.direito = atual.esquerdo

        elif atual.esquerdo == None:
            if atual == self.raiz:
                self.raiz = atual.direito
                self.raiz.nivel = 0
            else:
                atual.direito.nivel = nivel
                if filho_esquerdo:
                    pai.esquerdo = atual.direito
                else:
                    pai.direito = atual.direito

        else:
            sucessor = self.noSucessor(atual)
            if atual == self.raiz:
                #sucessor.nivel = 0
                self.raiz = sucessor
                self.raiz.nivel = 0
            else:
                sucessor.nivel = nivel
                if filho_esquerdo:
                    pai.esquerdo = sucessor
                else:
                    pai.direito = sucessor
            sucessor.esquerdo = atual.esquerdo

        return True

    def noSucessor(self, apaga):
        paiDoSucessor = apaga
        sucessor = apaga
        atual = apaga.direito

        while atual != None:
            paiDoSucessor = sucessor
            sucessor = atual
            atual = atual.esquerdo

        if sucessor != apaga.direito:
            paiDoSucessor.esquerdo = sucessor.direito
            sucessor.direito = apaga.direito

        return sucessor

    def buscar(self, elemento):
        if self.raiz == None:
            return None
        atual = self.raiz
        while atual.elemento != elemento:
            if elemento < atual.elemento:
                atual = atual.esquerdo
            else:
                atual = atual.direito
            if atual == None:
                return None
        return atual.elemento

    def grau(self, elemento):
        atual = self.get_elemento(elemento)
        if atual:
            if atual.esquerdo is None and atual.direito is None:
                return 0
            elif atual.esquerdo is None or atual.direito is None:
                return 1
            else:
                return 2
        else:
            return

    def profundidade(self, elemento):
        atual = self.get_elemento(elemento)
        profundidade = 0
        ancestral = atual.pai
        while ancestral:
            profundidade += 1
            ancestral = ancestral.pai
        return profundidade

    def altura(self, elemento):
        if elemento == None or elemento.esquerdo == None and elemento.direito == None:
            return 0
        else:
            if self.altura(elemento.esquerdo) > self.altura(elemento.direito):
                return 1 + self.altura(elemento.esquerdo)
            else:
                return 1 + self.altura(elemento.direito)

    def altura_(self, elemento):
        atual = self.get_elemento(elemento)
        if atual == None or atual.esquerdo == None and atual.direito == None:
            return 0
        else:
            if self.altura(atual.esquerdo) > self.altura(atual.direito):
                return 1 + self.altura(atual.esquerdo)
            else:
                return 1 + self.altura(atual.direito)

    def nivel(self, elemento):
        atual = self.get_elemento(elemento)
        if atual:
            return atual.nivel

    def quantidadeNos(self, elemento):
        if elemento == None:
            return 0
        else:
            return 1 + self.quantidadeNos(elemento.esquerdo) + self.quantidadeNos(elemento.direito)

    def get_elemento(self, elemento):
        if self.raiz == None:
            return None
        atual = self.raiz
        while atual.elemento != elemento:
            if elemento < atual.elemento:
                atual = atual.esquerdo
            else:
                atual = atual.direito
            if atual == None:
                return None
        return atual

    def inOrder(self, elemento):
        if elemento != None:
            self.inOrder(elemento.esquerdo)
            print(elemento.elemento, end=" ")
            self.inOrder(elemento.direito)

    def preOrder(self, elemento):
        if elemento != None:
            print(elemento.elemento, end=" ")
            self.preOrder(elemento.esquerdo)
            self.preOrder(elemento.direito)

    def posOrder(self, elemento):
        if elemento != None:
            self.posOrder(elemento.esquerdo)
            self.posOrder(elemento.direito)
            print(elemento.elemento, end=" ")

    def get_arvore(self, elemento):
        atual = self.get_elemento(elemento)
        espacos = " " * atual.nivel * 2
        prefixo = espacos + "|_" if atual.pai else ""
        print(prefixo + str(atual.elemento))
        if atual.esquerdo != None and atual.direito != None:
            self.get_arvore(atual.esquerdo.elemento)
            self.get_arvore(atual.direito.elemento)
        elif atual.esquerdo != None or atual.direito != None:
            if atual.esquerdo != None:
                self.get_arvore(atual.esquerdo.elemento)
            elif atual.direito != None:
                self.get_arvore(atual.direito.elemento)

    def get_arvore_invertida(self, elemento):
        atual = self.get_elemento(elemento)
        espacos = " " * atual.nivel * 2
        prefixo = espacos + "|_" if atual.pai else ""
        print(prefixo + str(atual.elemento))
        if atual.esquerdo != None and atual.direito != None:
            self.get_arvore(atual.direito.elemento)
            self.get_arvore(atual.esquerdo.elemento)
        elif atual.esquerdo != None or atual.direito != None:
            if atual.esquerdo != None:
                self.get_arvore(atual.esquerdo.elemento)
            elif atual.direito != None:
                self.get_arvore(atual.direito.elemento)
    
    def inserir_sequencia(self, sequencia):
        
        for elemento in sequencia:
            self.inserir(elemento)
    
    def inserir_sequencia_PosOrdem(self, sequencia):
        """
        Em uma sequência Pós Ordem o último elemento da mesma é a raiz da árvore,
        e fazemos a inserção dos elementos na ordem inversa (partindo do fim da lista).
        """
        for elemento in sequencia[::-1]:
            self.inserir(elemento)

    def inserir_sequencia_PreOrdem(self, sequencia):
        """
        Em uma sequência Pré Ordem o primeiro elemento da mesma é a raiz da árvore,
        e fazemos a inserção dos elementos na ordem correta (partindo do início da lista).
        """
        for elemento in sequencia:
            self.inserir(elemento)
