
from sanic import Blueprint, json
from sanic.log import logger


bp = Blueprint("Example", url_prefix="/hello_world")


@bp.get('/success')
def get_hello_word_view(request):
    # do something
    logger.info("success")
    return json({"messages": "success"})


@bp.post('/json_view')
def get_hello_word_view(request):
    # do something
    return json({"messages": "success"})