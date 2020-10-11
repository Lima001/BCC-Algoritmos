def inverter_a_cada_dois(string):
    nova_string = ""
    for i in range(1,len(string),2):
        nova_string += string[i] + string[i-1]
    
    if len(string)%2 == 1:
        nova_string += string[-1]

    return nova_string 

def main():
    string = input("Digite a string: ")
    print(inverter_a_cada_dois(string))

if __name__ == "__main__":
    main()