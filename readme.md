Programa Formação - FCamara - Hackathon

Um desafio criado pela empresa FCamara para realizar o agendamento de lugares nas escritorios de trabalho e respeitando a legislação do estado para o funcionamento de 40%.

E realizando um diferencial que é o agendamento da sala de reunião.

Os pré-requisitos é ter instalado Python3+ e pip.

Rodar e Instalar o requirements do projeto, com o comando abaixo:

`pip install -r requirements.txt`

Após instalar, rodar os comando abaixo para criar o banco de dados.

`python manage.py makemigrations`

`python manage.py migrate`

Com o banco de dados criado, vamos criar o superuser para a tela de administração do Django. O mesmo irá 
pedir um nome de usuário, e-mail e senha.

`python manage.py createsuperuser`

Por fim basta rodar o projeto.

`python manage.py runserver`

Vai ser direcionado para a tela de Administração do Django para cadastrar as informações no Banco de dados.

<imagem>

Para acessar as Api's criadas usar o endpoint /api.

<imagem>

Documentação da api acessar no endpoint /documentacao ou /swagger.

<imagem>
