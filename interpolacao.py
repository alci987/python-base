#!/usr/bin/env python

email_tpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s ?
Este produto é %(texto)s
Apenas %(quantidade)d disponíveis.

Preço promocional de  R$%(preco).2f
"""
clientes = ["David", "Thiago", "Thays", "Melissa"]

for cliente in clientes:
    print(email_tpl % {
                        "nome": cliente,
                        "produto": "Caneta",
                        "texto": "bom para escrever",
                        "quantidade": 2,
                        "preco": 50.5
                        })
