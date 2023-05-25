from typing import Any

from sanic import Blueprint, HTTPResponse, Request, Sanic, html, json
from sanic.views import HTTPMethodView
import logging

logger = logging.getLogger(__name__)


bp = Blueprint("Correct", url_prefix="/correct")

@bp.get('/word')
def correct(request):
    # assert 1 == 2
    logger.info('*' * 90)
    logger.info('-' * 90)
    logger.info('+' * 90)
    return json({"messages": "success"})