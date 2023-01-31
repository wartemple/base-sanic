from sanic import Sanic

from core.common.log import setup_logging


def create_app() -> Sanic:
    app = Sanic("GraphQLApp")
    setup_logging(app)

    from core.blueprints.view import bp  # noqa

    app.blueprint(bp)

    return app
