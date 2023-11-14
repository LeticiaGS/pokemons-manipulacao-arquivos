arrPokemons = []

options = {
    1: '#',
    2: 'Name',
    3: 'Type 1',
    4: 'Type 2',
    5: 'Total',
    6: 'HP',
    7: 'Attack',
    8: 'Defense',
    9: 'Sp. Atk',
    10: 'Sp. Def',
    11: 'Speed',
    12: 'Generation',
    13: 'Legendary',
}

types = {
    1: 'Normal',
    2: 'Fire',
    3: 'Water',
    4: 'Grass',
    5: 'Flying',
    6: 'Fighting',
    7: 'Poison',
    8: 'Eletric',
    9: 'Ground',
    10: 'Rock',
    11: 'Psychic',
    12: 'Ice',
    13: 'Bug',
    14: 'Ghost',
    15: 'Steel',
    16: 'Dragon',
    17: 'Dark',
    18: 'Fairy',
}

with open ('pokemon.csv','r') as filePokemon:
    for line in filePokemon.readlines():
        arrPokemons.append(line.split(','))

def menu():
    print("\nBem vindo a nossa base de dados dos Pokemons! Relembrar é viver. =D\n\nSelecione uma opção do Menu: ")
    print('1. Filtragem de Pokemons')
    print('2. Resumo dos pokemons') 
    print('3. Relatório do Arquivo original: Pokemon.csv')

    op = int(input("\nPor favor, indique o número da operação que deseja realizar: "))
    
    if (op == 1): 
        print('\nEscolha como deseja filtrar o seu Pokemon: ')
        print('\n1. ID')
        print('2. Nome')

        op_pokemon = int(input("\nPor favor, indique o número da operação que deseja realizar: "))

        for key in options.keys():
            if key == op_pokemon:
                searchBy = options[key]
                searchPokemon(searchBy)
    
    if (op == 2):
        resumoPokemons()

    if (op == 3):
        relatorio()

def resumoPokemons():
    print("\nVamos gerar um arquivo agrupando os pokemons de um determinado tipo. Bora?")
    print("\nMenu: ")
    print(" 1.Normal      2.Fogo          3.Água       4.Grama      5.Voador        6.Lutador")
    print(" 7.Veneno      8.Elétrico      9.Terra     10.Pedra     11.Psíquico     12.Gelo")
    print("13.Inseto     14.Fantasma     15.Ferro     16.Dragão    17.Sombrio      18.Fada")

    op = int(input("\nPor favor, indique o número da operação que deseja realizar: "))
    print("\nDevemos agrupar por: ")
    print(" 1.Tipo Principal      2.Tipo Secundário          3.Ambos os tipos")
    op_type = int(input("\nPor favor, indique o número da operação que deseja realizar: "))

    inputType = types[op]
               
    resumePokemonsFile = open("resumePokemons.csv", "w")
    columnHeader = arrPokemons[0]
    resumePokemonsFile.write(', '.join(columnHeader))
    count_qtde = 0
    count_legendary = 0
    for pokemon in arrPokemons:
       if (op_type == 1):
            if (pokemon[2] == inputType):
                count_qtde += 1
                print(type(pokemon[12]))
                if (pokemon[12] == True):
                    count_legendary += 1
                resumePokemonsFile.write(', '.join(pokemon))
       elif (op_type == 2):
            if (pokemon[3] == inputType):
                count_qtde += 1
                if (pokemon[12] == 'True'):
                    count_legendary += 1
                resumePokemonsFile.write(', '.join(pokemon))
       elif (op_type == 3):
            if (pokemon[2] == inputType) or (pokemon[3] == inputType):
                count_qtde += 1
                if (pokemon[12] == 'True'):
                    count_legendary += 1
                resumePokemonsFile.write(', '.join(pokemon))
    resumePokemonsFile.write(f'\nExistem um total de {count_qtde} Pokemons do tipo {inputType}. {count_legendary} sao lendarios.')
    resumePokemonsFile.close

def relatorio():
    count_lines = len(arrPokemons)
    col_names = arrPokemons[0]
    print("\nO número de linhas que o arquivo original possui é: ",count_lines)
    print("\nAs colunas presentes no arquivo são: ")
    for col in col_names:
        print(col)

def searchPokemon(col_name): 
    indexCol = arrPokemons[0].index(col_name)
    arquivoTeste = open("aula.txt", "w")
    for pokemon in arrPokemons:
         arquivoTeste.write(f"{pokemon[indexCol]}\n")
    arquivoTeste.close


menu()