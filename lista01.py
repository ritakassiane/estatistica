import pandas as pd


# Função que pega uma sequencia de numeros separados por espaço e substitui por virgula 
def space_to_point(string):
    new = string.replace(" ", ",")
    print(new)
    return new

# Função que recebe uma string e substitui as , por .
def virgula_to_point(string):
    new = string.replace(",",".")
    print(new)
    return new

# A função abaixo recebe uma string e retorna do jeito ideal para trabalhar no pandas
def roll(string):
    new = space_to_point(virgula_to_point(string))
    print(new)
    return new


# A função abaixo recebe uma string, adiciona a uma lista e a transforma em uma serie pandas
def string_array_serie(string):
    array = []
    array.append(string)
    series = pd.Series(string)
    print(series)
    return series

roll("""4,10 6,36 8,96 10,00 10,68 13,36 14,97 17,45 19,84 21,18 24,43 28,72
4,34 6,53 9,35 10,21 10,88 13,56 16,44 17,46 20,03 21,37 26,09 28,93
4,38 6,91 9,83 10,21 12,53 14,23 16,47 17,90 20,40 22,38 26,48 29,58
4,73 7,59 9,89 10,24 13,00 14,24 17,13 17,95 20,73 23,00 27,40 30,07
6,17 8,92 9,92 10,44 13,34 14,80 17,16 19,17 20,84 23,41 28,10 30,79
""")

