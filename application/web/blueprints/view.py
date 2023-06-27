from sanic import Blueprint

from .example.view import bp as example_bp

bp = Blueprint.group(example_bp, url_prefix='api/v1')
