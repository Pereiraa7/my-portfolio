from flask import Blueprint, render_template, request, make_response
from .constants import TRANSLATIONS

main = Blueprint('main', __name__)

@main.route('/')
def index():
    role = request.args.get('role', 'backend')
    lang = request.args.get('lang')
    
    # Busca idioma do cookie se não for passado via URL
    if not lang:
        lang = request.cookies.get('lang', 'pt')
    
    if role not in ('backend', 'data'):
        role = 'backend'
    if lang not in TRANSLATIONS:
        lang = 'pt'

    # Renderiza e injeta o cookie de idioma na resposta
    resp = make_response(render_template('index.html', role=role, lang=lang, t=TRANSLATIONS[lang]))
    resp.set_cookie('lang', lang, max_age=30*24*60*60) # 30 dias
    return resp
