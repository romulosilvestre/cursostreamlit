
def formata_numero(valor,prefixo):
   for unidade in ['','mil']:
       if valor <1000:
            return f'{prefixo} {valor:.2f} {unidade}'

