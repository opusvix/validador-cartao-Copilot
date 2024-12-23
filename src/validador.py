def identificar_bandeira(numero_cartao):
    numero_cartao = str(numero_cartao)
    
    prefixos = {
        'Visa': ['4111'],
        'MasterCard': [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)],
        'Elo': ['4011', '4312', '4389'],
        'American Express': ['34', '37'],
        'Discover': ['6011', '65'] + [str(i) for i in range(644, 650)],
        'Hipercard': ['6062'],
        'Diners Club': ['300'],
        'EnRoute': ['2149', '2014'],
        'JCB': ['35'],
        'Voyager': ['86'],
        'Aura': ['50']
    }
    
    for bandeira, prefixo_list in prefixos.items():
        if any(numero_cartao.startswith(prefixo) for prefixo in prefixo_list):
            return bandeira
    
    return 'Bandeira desconhecida'

# Exemplo de uso
if __name__ == "__main__":
    cartoes_teste = [
        '4011123456789012',  # Elo
        '4111111111111111',  # Visa
        '5105105105105100',  # MasterCard
        '371449635398431',   # American Express
        '6011111111111117',  # Discover
        '6062825588876543',  # Hipercard
        '30000000000004',    # Diners Club
        '201400000000009',   # EnRoute
        '3530111333300000',  # JCB
        '869999999999999',   # Voyager
        '5019717010103742',  # Aura
    ]

    for cartao in cartoes_teste:
        print(f'Número: {cartao}, Bandeira: {identificar_bandeira(cartao)}')