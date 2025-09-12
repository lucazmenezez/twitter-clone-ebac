# Twitter Clone - Projeto Django

Um clone simplificado do Twitter, desenvolvido em **Django**, com funcionalidades de registro, login, e postagens básicas.  

## 🛠 Tecnologias Utilizadas
- Python 3.13  
- Django 5.2.6  
- Bootstrap 5 (para front-end)  
- SQLite (banco de dados padrão do Django)  

---

## ⚙ Pré-requisitos

Antes de rodar o projeto localmente, você precisará ter instalado:

- Python >= 3.10
- pip
- Git

---

## 🚀 Como rodar localmente

1. **Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/twitter-clone.git
cd twitter-clone


2. **Criar e ativar o ambiente virtual**

# Linux / Mac
python -m venv env
source env/bin/activate

# Windows
python -m venv env
env\Scripts\activate


3. **Instalar dependências**

pip install -r requirements.txt

4. **Aplicar migrations**

python manage.py migrate

5. **Criar superusuário (opcional)**

python manage.py createsuperuser

6. **Rodar o servidor local**

python manage.py runserver

7. **Acessar no navegador**

http://127.0.0.1:8000/
