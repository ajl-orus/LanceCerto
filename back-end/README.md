# Proyecto Full-Stack ISPC

## Back-end
Para executar o _back-end_ você deve primeiro instalar as dependências (fastapi, pytest, etc):

```
python -m pip install -r requirements.txt
```

ou

```
pip install -r requirements.txt
```

Em alguns sistemas (por exemplo Linux Ubuntu) é _python3_ e _pip3_, em outros _python_ e _pip_. A versão mínima é 3.9. Em outros sistemas, como as variantes SUSE, python3 é Python 3.6, então você deve primeiro instalar uma versão mais moderna, por exemplo, com _sudo zypper install python310-base_ e então usar _python3.10_ em vez de _python3_.

![image](https://user-images.githubusercontent.com/15602473/201264090-09e4e986-26aa-4809-9f9e-64ade8aaa3e1.png)


## Executar servidor
Para iniciar o servidor back-end a partir de um console ou shell nesse diretório:

```
python main.py
```
(ou _python3 main.py_ em algumas distribuições Linux). O servidor utiliza a porta 8000. Também é possível executá-lo da seguinte forma:
```
uvicorn main:app
```
Se configurado para rodar em MySQL ele criará o banco de dados e as tabelas necessárias caso elas não existam.

## Ejecutar pruebas unitarias

Para executar testes de unidade a partir de um console ou shell no diretório *_back-end:_*
```
pytest main_tests.py
```

Isso executará todos os testes de unidade encontrados no conjunto (que inclui todos aqueles no diretório _tests_). O pipeline usa uma linha um pouco mais longa que também pode ser usada manualmente:

```
pytest main_tests.py --cov-config=coverage.ini --doctest-modules --junitxml=main.coverage.xml --cov-append --cov . --cov-report xml --cov-report html
```

O que gera um arquivo *coverage.xml* com informações de cobertura e um arquivo *main.coverage.xml* com informações sobre testes executados em formato Junit.


## Ejecutar pruebas de integración con Postman

En la sección de documentación se adjunta un archivo con pruebas de Postman para realizar. Las pruebas se realizan sobre una base vacía de MySQL.
