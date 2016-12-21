# desafio-cargobr

Entregando mercadorias

Uma rede grande de varejo esta desenvolvendo um novo sistema de logística e sua ajuda é muito importante neste momento. Sua tarefa será desenvolver o novo sistema de entregas visando sempre o menor custo. Para popular sua base de dados o sistema precisa expor um web service que aceite o formato de malha logística (exemplo abaixo), nesta mesma requisição o requisitante deverá informar um nome para este mapa. É importante que os mapas sejam persistidos para evitar que a cada novo deploy todas as informações desapareçam. O formato de malha logística é bastante simples, cada linha mostra uma rota: ponto de origem, ponto de destino e distância entre os pontos em quilômetros.

A B 10
B D 15
A C 20
C D 30
B E 50
D E 30

Com os mapas carregados o requisitante irá procurar o menor valor de entrega e seu caminho, para isso ele passará o mapa, nome do ponto de origem, nome do ponto de destino, autonomia do caminhão (km/l) e o valor do litro do combustível, agora sua tarefa é criar este web service. Um exemplo de entrada seria, mapa SP, origem A, destino D, autonomia 10, valor do litro 2,50; a resposta seria a rota A B D com custo de 6,25.

-------------------------

# Ferramentas escolhidas
> Django 1.10

> Django-rest-framework 3.5.2

> sqlite3

Escolhi essas ferramentas por serem parte oficial do meu toolset, além de conseguir configurar um ambiente para desenvolver a solução em minutos.

# Como executar o código

### 1 - Instale os requisitos
> pip install -r requirements.txt

### 2 - Rode o servidor
> python3 manage.py runserver

### 3 - Acesse a API browseavel
> http://localhost:8000/api

> Usuário: admin

> Senha: cargobr2016

### 4 - Como realizar a consulta
Criei um endpoint aninhado visando melhor clareza para capturar as melhores rotas do dado mapa.

> http://locahost:8000/api/maps/{pk}/routes/{params}


> Ex.: http://localhost:8000/api/maps/1/routes/?origem=A&destino=D&autonomia=10&valor_litro=2.50