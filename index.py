import os
import paths

arrPokemons = []

options = {
    1: '#',
    2: 'Name',
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

with open ('Original_CSV/pokemon.csv','r') as originalFilePokemon:
    for line in originalFilePokemon.readlines():
        arrPokemons.append(line.split(','))

def menu():
    print("-------------------------------------------------------------------------------------------")
    print("\nBem vindo a nossa base de dados dos Pokemons! Relembrar é viver. =D\n\nSelecione uma opção do Menu: ")
    print('0. Sair')
    print('1. Filtragem de Pokemons')
    print('2. Resumo dos pokemons') 
    print('3. Relatório do Arquivo original: Pokemon.csv')

    op = getInputOperation()
    
    while ((op < 0) or ( op > 3)):
            print('\nVocê digiou um valor inváido! Tente novamente.')
            op = getInputOperation()

    if (op == 0):
        exit()
    elif (op == 1): 
        searchPokemon()
    
    elif (op == 2):
        resumePokemons()

    elif (op == 3):
        reportPokemon() 

def resumePokemons():
    print("-------------------------------------------------------------------------------------------")
    print("\nVamos gerar um arquivo agrupando os pokemons de um determinado tipo. Bora?")
    print("\nMenu: ")
    print(" 1.Normal      2.Fogo          3.Água       4.Grama      5.Voador        6.Lutador")
    print(" 7.Veneno      8.Elétrico      9.Terra     10.Pedra     11.Psíquico     12.Gelo")
    print("13.Inseto     14.Fantasma     15.Ferro     16.Dragão    17.Sombrio      18.Fada")

    op = getInputOperation()
    if (op >= 1 and op <= 18):
        print("\nDevemos agrupar por: ")
        print(" 1.Tipo Principal      2.Tipo Secundário          3.Ambos os tipos")
        op_type = getInputOperation()

        while (op_type < 1 or op_type > 3):
            print("\nOpps! Valor inválido. Por favor, responda de acordo com as opções disponíves:")
            print("Devemos agrupar por: ")
            print(" 1.Tipo Principal      2.Tipo Secundário          3.Ambos os tipos")
            op_type = getInputOperation()

        inputType = types[op]
        resumePokemonsFile = open(f"Resume_Pokemon/{inputType}_Pokemon.csv", "w")
        columnHeader = arrPokemons[0]
        resumePokemonsFile.write(', '.join(columnHeader))
        count_qtde = 0
        count_legendary = 0
        for pokemon in arrPokemons:
           formatedLegendaryColumn = (str(pokemon[12])).strip()
           if (op_type == 1):
                if (pokemon[2] == inputType):
                    count_qtde += 1
                    if( formatedLegendaryColumn == "True"):
                        count_legendary += 1
                    resumePokemonsFile.write(', '.join(pokemon))
           elif (op_type == 2):
                if (pokemon[3] == inputType):
                    count_qtde += 1
                    if (formatedLegendaryColumn == 'True'):
                        count_legendary += 1
                    resumePokemonsFile.write(', '.join(pokemon))
           elif (op_type == 3):
                if (pokemon[2] == inputType) or (pokemon[3] == inputType):
                    count_qtde += 1
                    if (formatedLegendaryColumn == 'True'):
                        count_legendary += 1
                    resumePokemonsFile.write(', '.join(pokemon))
        resumePokemonsFile.write(f'\nExistem um total de {count_qtde} Pokemons do tipo {inputType}. {count_legendary} sao lendarios.')
        resumePokemonsFile.close
        print("\nOba!! Seu arquivo ficou pronto! Confira na raiz do projeto =)")

        print("\nDeseja voltar ao menu principal? ")
        print("1. Sim\n2. Não")
        op_return = getInputOperation()
        if (op_return == 1):
            menu()

    else: 
        print("\nOpps! Digitou um valor inválido!")
        print("Deseja tentar novamente? ")
        print("1. Sim\n2. Não\n3. Voltar ao Menu Principal")
        op_return = getInputOperation()
        if (op_return == 1):
            resumePokemons()
        elif (op_return == 3):
            menu()

def reportPokemon():
    print("-------------------------------------------------------------------------------------------")
    print("\nVamos criar alguns relatórios! Escolha as opções abaixo: ")
    print("1. Arquivo Original dos pokemons\n2. Pokemons Filtrado\n3. Resumo de Pokemons")
    op = getInputOperation()
    arrReportFile = []
    path = ''

    if ((op>= 1) and (op<= 3)):
        if (op == 1):
            path = f'{paths.CURRENT_DIR}/Original_CSV'
        elif (op == 2):
            path = f'{paths.CURRENT_DIR}/Filtred_Pokemon'
        elif (op == 3):
            path = f'{paths.CURRENT_DIR}/Resume_Pokemon'
    
        print("\nOpções de arquivo para gerar relatórios:")
        # Extracting all the contents in the directory corresponding to path
        l_files = os.listdir(path)
        for i in range(len(l_files)):
            file_path = f'{path}\\{l_files[i]}'
            if (os.path.isfile(file_path)):
                print(f'{i+1}. {l_files[i]}')

        op_files = int(input("Indique o arquivo de sua escolha pelo indice correspondente: "))
        choosen_file = l_files[op_files - 1]
        folder_file = os.path.basename(path)
        file_name = (choosen_file.split('.')[0]).title()

        with open (f'{folder_file}\{choosen_file}','r') as fileToReport:
             for line in fileToReport.readlines():
                 arrReportFile.append(line.split(','))

        count_lines = len(arrReportFile)
        columnHeader = arrReportFile[0]

        reportPokemonFile = open(f"Report_Files\{file_name}_Report.csv", "w")
        reportPokemonFile.write(f"O número de linhas que o arquivo original possui é: {count_lines}")
        reportPokemonFile.write("\n\nAs colunas presentes no arquivo são: \n")
        reportPokemonFile.write('\n '.join(columnHeader))
        reportPokemonFile.close
        print("\nOba! Seu arquivo ficou pronto, confira na raiz do projeto. =)\n")
        print("\nDeseja voltar ao menu principal? ")
        print("1. Sim\n2. Não")
        op_return = getInputOperation()
        if (op_return == 1):
            menu()
    else:
        print("\nOpps! Digitou um valor inválido!")
        print("Deseja tentar novamente? ")
        print("1. Sim\n2. Não\n3. Voltar ao Menu Principal")
        op_return = getInputOperation()
        if (op_return == 1):
            reportPokemon()
        elif (op_return == 3):
            menu()

def searchPokemon(): 
    print("-------------------------------------------------------------------------------------------")
    print('\nEscolha como deseja filtrar o seu Pokemon: ')
    print('\n1. ID')
    print('2. Nome')

    op_pokemon = getInputOperation()
    
    if (op_pokemon == 1 or op_pokemon == 2):

        searchByColName = options[op_pokemon]
        indexCol = arrPokemons[0].index(searchByColName)
        searchBy = 'ID' if op_pokemon == 1 else 'nome'
        
        IdOrName = str(input(f"\nDigite o {searchBy} do pokemon que deseja filtrar: "))

        foundPokemon = False
        for pokemon in arrPokemons:
             if (((str(pokemon[indexCol])).upper().strip()) == (IdOrName.upper().strip())):
                 foundPokemon = True

        if not foundPokemon:
            print(f"\nInfelizmente não conseguimos encontrar seu pokemon por este {searchBy}. :/ \nGostaria de realizar uma nova filtragem?")
            print("1. Sim\n2. Não")
            op = getInputOperation()
            if (op == 1):
                searchPokemon()
        else:
            fileName = (str(input("Escolha o nome que terá seu arquivo: "))).strip()

            pokemonFiltredFile = open(f"Filtred_Pokemon/{fileName}.csv", "w")
            columnHeader = arrPokemons[0]
            pokemonFiltredFile.write(', '.join(columnHeader))

            for pokemon in arrPokemons: 
                if (((str(pokemon[indexCol])).upper().strip()) == (IdOrName.upper().strip())):
                    pokemonFiltredFile.write(', '.join(pokemon))
            pokemonFiltredFile.close
            print("\nOba! Seu arquivo ficou pronto, confira na raiz do projeto. =)\n")

            print("\nDeseja voltar ao menu principal? ")
            print("1. Sim\n2. Não")
            op_return = getInputOperation()
            if (op_return == 1):
                menu()
    else: 
        print("\nOpps! Digitou um valor inválido!")
        print("Deseja tentar novamente? ")
        print("1. Sim\n2. Não\n3. Voltar ao Menu Principal")
        op_return = getInputOperation()
        if (op_return == 1):
            searchPokemon()
        elif (op_return == 3):
            menu()

def intTryParse(value):
    try:
        int(value)
        return True
    except ValueError:
        print("Caracter inválido! Observe os valores disponíveis e tente novamente.")
        return False

def getInputOperation():
    validationInputOp = True
    while (validationInputOp):
        input_op = (input("\nPor favor, indique o número da operação que deseja realizar: "))
        validationInputOp =  not intTryParse(input_op)

    return int(input_op)

menu()