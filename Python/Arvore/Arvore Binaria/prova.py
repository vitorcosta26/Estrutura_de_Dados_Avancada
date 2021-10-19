from arvore_binaria import ArvoreBinaria

emOrdem = [10, 8, 5, 7, 9, 18, 13, 20]
arvore = ArvoreBinaria()
arvore.inserir_sequencia(emOrdem)
arvore.get_arvore(arvore.get_raiz())
print("\nIn Order")
arvore.inOrder(arvore.raiz)
print("\nPos Order")
arvore.posOrder(arvore.raiz)
print("\nPre Order")
arvore.preOrder(arvore.raiz)
print("\n")

#Fizemos as inserções baseadas na Pós Ordem e na Pré Ordem.
#A partir dos dados obtidos pela árvore acima.

#inserir_sequencia_PosOrdem
posOrdem = [7, 5, 9, 8, 13, 20, 18, 10]
arvorePos = ArvoreBinaria()
arvorePos.inserir_sequencia_PosOrdem(posOrdem)
arvorePos.get_arvore(arvorePos.get_raiz())
print("\nIn Order")
arvorePos.inOrder(arvorePos.raiz)
print("\nPos Order")
arvorePos.posOrder(arvorePos.raiz)
print("\nPre Order")
arvorePos.preOrder(arvorePos.raiz)
print("\n")

#inserir_sequencia_PreOrdem
preOrdem = [10, 8, 5, 7, 9, 18, 13, 20]
arvorePre = ArvoreBinaria()
arvorePre.inserir_sequencia_PreOrdem(preOrdem)
arvorePre.get_arvore(arvorePre.get_raiz())
print("\nIn Order")
arvorePre.inOrder(arvorePre.raiz)
print("\nPos Order")
arvorePre.posOrder(arvorePre.raiz)
print("\nPre Order")
arvorePre.preOrder(arvorePre.raiz)
print("\n")
