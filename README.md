# Bluestorm Challenge

[![AppBuildProduction Actions Status](https://github.com/fmp95/bluestorm_challenge/workflows/AppBuildProduction/badge.svg)](https://github.com/fmp95/bluestorm_challenge/actions)  

[![AppBuildDevelopment Actions Status](https://github.com/fmp95/bluestorm_challenge/workflows/AppBuildDevelopment/badge.svg)](https://github.com/fmp95/bluestorm_challenge/actions)

Aplicativo proposto no teste da Bluestorm, para a pesquisa de informações de medicamentos utilizando o banco de dados oferecido. O aplicativo oferece um endpoint REST API para a buscar dessas informações. O aplicativo em sua maioria foi desenvolvido utilizando FastAPI (Python).

## Dependências
Python (3.9.1)  
Docker  
Outras listadas nos arquivos dentro da pasta ```requirements```

## Funcionalidades
- [x] Correção de erros ortográficos nos termos de pesquisa;
- [x] Testes automatizados;
- [x] Criação de imagem Docker para execução;
- [x] Padronização do código de forma automática;
- [x] Criação de targets make para execução fácil das principais tarefas;
- [x] Geração automática da documentação da API dentro dos padrões OpenAPI;
- [x] Modelagem das respostas de requisição; 
- [x] Teste automático de integração contínua usando Git Actions;   

## Como Funciona
O aplicativo fornece um endpoint ```/search/{medication_name}``` para a busca de informações sobre o medicamento. Na primeira vez que o endpoint é requisitado, o aplicativo faz a criação de um dicionário utilizando apenas as palavras que aparecem no campo de nome de medicação do banco de dados. Com esse dicionário, toda vez que o endpoint é requisitado, a palavra passa por uma checagem para encontrar possíveis erros de digitação.
Foi escolhido criar um dicionário próprio para evitar gastos computacionais comparando com palavras que não aparecem no arquivo. Outro processo escolhido foi corrigir a palavra antes de buscar no arquivo. Já que houve a criação do dicionário personalizado, foi uma forma de comparar o termo de busca com todas as entradas de forma mais simples. 

## Como Utilizar
```make install_development``` - Instalação das dependências Python para desenvolvimento;  
```make install_production``` - Instalação das dependências Python para produção;  
```make run``` - Execução do server para o uso da REST API;  
```make build-docker``` - Criação da imagem Docker;  
```make run-docker``` - Execução da imagem criada em um container isolado;  
```make run-tests``` - Execução dos testes;  
