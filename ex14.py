def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
    
texto = "Socorram me  subi no onibus em Marrocos"
if verificar_palindromo(texto):
    print(texto, "é um palíndromo.")
else:
    print(texto, "não é um palindromo.")