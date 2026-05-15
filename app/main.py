# ponte de entrada do meu sistema 
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from app.controllers import auth_controller

app = FastAPI(title="Sistema de ponto de vendas")

# Configurar a pasta para servir os arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurar o Jinja2 para renderizar os HTML
templates = Jinja2Templates(directory="app/templates")

# Incluir as rotas de autenticação
app.include_router(auth_controller.router)