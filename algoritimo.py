# Função: Pesquisa binária
def pesquisa_binaria(lista,item):
    # baixo e alto acompanham a parte da lista que você está procurando
    baixo = 0 
    alto = len(lista) - 1 

    # enquanto você não tiver coberto toda a lista
    while baixo <= alto:

        # verifica o elemento central
        meio = (baixo + alto) // 2
        chute = lista[meio]

        # Acha o item
        if chute == item:
            return meio
        
        # O chute foi muito alto
        if chute > item:
            alto = meio - 1

        # O chute foi muito baixo            
        else:
            baixo = meio + 1

    # O item não existe
    return None

#lista de exemplo para testar a função
minha_lista = [1, 3, 5, 7, 9]

# Testando a função
print(pesquisa_binaria(minha_lista, 3)) # => 1
print(pesquisa_binaria(minha_lista, -1)) # => None