empty_list = []
nothing = None
zero = 0
zero_dict = {"valor": 0}

if __name__ == '__main__':
    if empty_list or nothing or zero:
        print("isso não é impresso")

    if zero:
        print("isso não é impresso")

    if zero:
        print("isso é impresso")

    if zero_dict.get("valor"):
        #isso não é impresso
        print(f"Não {zero_dict.get('valor')}")

    if zero_dict.get("valor") is not None:
        #isso é impresso
        print(f"Sim {zero_dict.get('valor')}")
