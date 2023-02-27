def main():
    #entrada = 'Peru, Colombia, Venezuela, Peru, Chile, Bolivia, Argentina, Chile'
    entrada = input("Ingresa nombres de paises separados por comas: ")
    entrada = entrada.split(',')
    entrada = set(map(lambda x: x.strip(), entrada))
    paises = sorted(entrada) 
    print(', '.join(paises))

if __name__ == "__main__":
    main()
