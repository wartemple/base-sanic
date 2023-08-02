
from sanic import Blueprint, json
from sanic.log import logger
from .validators import ExampleModel


bp = Blueprint("Example", url_prefix="/hello_world")


@bp.get('/success')
async def get_hello_word_view(request):
    # do something
    # input = ExampleModel(**request.args)
    # logger.info(input.dict())
    # logger.info(input.name)
    return json({"messages": "success"})


@bp.post('/json_view')
def json_view(request):
    # do something
    input = ExampleModel(**request.json)
    logger.info(input.dict())
    logger.info(input.name)
    return json({"messages": "success"})