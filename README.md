# Instalar as bibliotecas 

no terminal:
````bash
pip install -r requirements.txt
````

# Inicializar o alembic 
no terminal:
````bash
python -m alembic init migrations 
````

# editar o arquivo alembic init - na linha 89: 
sqlalchemy.url = 

# gerer a migration 
no terminal:
````bash
python -m alembic revision --autogenerate -m "Criar tabela usuarios"  
````

# aplicar a migration no banco 
no terminal:
````bash
python -m alembic upgrade head  
````