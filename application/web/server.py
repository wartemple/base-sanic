from sanic import Sanic

from web.common.log import setup_logging


def create_app() -> Sanic:
    app = Sanic("GraphQLApp")
    setup_logging(app)

    from web.blueprints.view import bp  # noqa

    app.blueprint(bp)

    return app
