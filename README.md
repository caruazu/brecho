![Django](https://img.shields.io/badge/django-092e20?style=for-the-badge&logo=Django)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

# Brecho

## Sobre

> Suja lojinha de roupas usadas

Este projeto foi criado para demonstrar meus conhecimentos básicos com as tecnologias utilizadas. Não há intenção de utilizar esse código em qualquer aplicação comercial, e nem em futuras manutenções.

## Instalação

### ambiente python isolado

```
pyenv install
```

### Dependências

```
pipenv install
```

### Variáveis de ambiente

O projeto usa um ficheiro `.env` para gerir segredos e configurações locais (como senhas de banco de dados, chaves de API, etc.)

Fornecemos um ficheiro de exemplo para si:

1. Copie o ficheiro de exemplo:
    
    ```bash
    cp .env.example .env
    ```
    
2. Abra o ficheiro `.env` (que você acabou de criar) no seu editor de código.
    
3. Preencha os valores em falta (ex: `SECRET_KEY`, `DATABASE_URL`, etc.) de acordo com a sua configuração local.
    
### Execução

Com tudo configurado, você está pronto para executar o servidor de desenvolvimento:

1. Certifique-se de que o seu ambiente virtual está ativo:
    
    ```bash
    pipenv shell
    ```
    
2. Inicie o servidor de desenvolvimento do Django:
    
    ```bash
    (brecho)$ python manage.py runserver
    ```

Abra o seu navegador e acesse [http://127.0.0.1:8000/](https://www.google.com/search?q=http://127.0.0.1:8000/) para ver o projeto a funcionar.


#### (Opcional) Desativar a Ativação Automática do Terminal

Para evitar conflitos entre a ativação automática do VSCode e o comando `pipenv shell`, recomendamos desativar a ativação automática:

1. Abra as Configurações (`Ctrl + ,`).
    
2. Procure por `python.terminal.activateEnvironment`.
    
3. **Desmarque** a caixa de seleção.
    
4. Reinicie o terminal do VSCode. Agora, você deverá usar `pipenv shell` manualmente para ativar o ambiente, o que garante um fluxo de trabalho mais limpo.
