# Proyecto Full-Stack ISPC

## Controller

Dentro deste diretório estão os controladores secundarios que são chamados a partir do controlador principal, _main.py_ no diretório superior.

Os controladores são responsáveis ​​por descompactar as informações provenientes do _front-end_ e passá-las para os serviços encontrados no diretório _services_, depois empacotam a resposta e serializam-na para JSON. Eles não têm lógica de negócios.