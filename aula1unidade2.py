convidados = ['João', 'Maria', 'Ana', 'José', 'Paulo']
print(f'Os convidados foram: {convidados}.')
confirmados = ['João', 'Maria', 'Paulo']
print(f'Os confirmados são: {confirmados}.')
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
print(f'Os não confirmados são: {nao_confirmados}.\n')
print(f'Irei enviar o convite novamente para eles: {nao_confirmados}.')
