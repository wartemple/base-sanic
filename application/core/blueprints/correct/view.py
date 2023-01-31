from typing import Any

from sanic import Blueprint, HTTPResponse, Request, Sanic, html, json
from sanic.views import HTTPMethodView

bp = Blueprint("Correct", url_prefix="/correct")

@bp.get('/word')
def correct(request):
    return json({"messages": "success"})