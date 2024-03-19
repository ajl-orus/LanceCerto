# Proyecto Full-Stack ISPC

## Content Provider

Neste diretório estão as representações dos repositórios suportados pelo sistema.

O repositório MySQL implementa abstrações de modelo em um banco de dados MySQL: ele transforma cada chamada de método em uma consulta e retorna a serialização usando um lambda.

Há também uma representação temporária, na memória, por meio de listas e dicionários. Este formulário é ideal para testes unitários, pois respondem automaticamente, podem ser inicializados com valores diferentes para simular bancos de dados utilizados e não precisam ter um banco de dados real instalado no sistema.

Utilizando modelos e esses repositórios, os serviços podem pedir a um modelo para criar um elemento e o _Content Provider_ irá criá-lo na mídia selecionada e retornar um modelo de forma transparente, sem que os próprios controladores, serviços ou modelos saibam onde estão impactando.

É possível implementar outros _Content Provider_ (por exemplo, arquivo CSV, arquivo JSON, Shelve, SQLite ou até mesmo bancos de dados não-sql como MongoDB ou ZODB).
