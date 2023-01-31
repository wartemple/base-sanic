from sanic import Blueprint

from .correct.view import bp as correct_bp

bp = Blueprint.group(correct_bp, version=1)
