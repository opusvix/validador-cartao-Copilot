# Bootcamp Microsoft AI for Tech - GitHub Copilot da [DIO](https://dio.me)

## Módulo "Começando a usar o GitHub Copilot".

### Desafio de Projeto "Criando um Validador de Bandeiras de Cartão de Crédito com o GitHub Copilot".

Este projeto contém uma função para identificar a bandeira de um cartão de crédito com base no número do cartão fornecido. 
A função suporta várias bandeiras de cartões, incluindo Visa, MasterCard, Elo, American Express, Discover, Hipercard, Diners Club, EnRoute, JCB, Voyager e Aura.

## Funcionalidades

- Identificação da bandeira do cartão de crédito com base no número do cartão.
- Suporte para várias bandeiras de cartões.
- Validação do número do cartão para garantir que contém apenas dígitos.

## Como usar

### Pré-requisitos

- Python 3.x

### Instalação

Clone o repositório para sua máquina local:

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Uso
Você pode usar a função `identificar_bandeira` diretamente no seu código Python ou executar o arquivo `validador.py` para testar a função com alguns números de cartões de exemplo.

### 🛠️ Exemplo de uso no código

```sh
from validador import identificar_bandeira

numero_cartao = '4111111111111111'
bandeira = identificar_bandeira(numero_cartao)
print(f'Número: {numero_cartao}, Bandeira: {bandeira}')
```
### 🛠️ Executando o arquivo de teste

```sh
python validador.py
```
### 📚 Estrutura do Projeto
```sh
.
├── validador.py
└── README.md
```
## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/58704060?s=400&u=c58b05997dcd842e95dd0f5c45ab04c2054df583&v=4"
    />
    <p>&nbsp&nbsp&nbspMaurício Barros<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/opusvix">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/mauriciodasilvabarros/">LinkedIn</a>
    &nbsp;|&nbsp;
    <a href="https://x.com/opusvix">
    X</a>&nbsp;|&nbsp;
    <a href="mailto:opusvix@gmail.com">E-mail</a>
&nbsp;|&nbsp;</p>
</p>
<br/><br/>
<p>

---

:hammer_and_wrench: com :sparkling_heart: por [Maurício Barros](https://github.com/opusvix)
