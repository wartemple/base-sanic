from sanic import Sanic

LOGGINGS = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format":'[%(asctime)s] [%(levelname)s] [%(process)d] [%(thread)d] [%(module)s] [%(name)s:%(lineno)s] %(message)s'
        }
    },
    "handlers": {
       "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "INFO",
            "class": "core.common.EnhancedRotatingFileHandler",
            "filename": "logs/app.log",
            "when": "M",
            "interval": 1,
            "maxBytes": 1024 * 1024 * 50, # 50M
            "backupCount": 40, # 约一个月
            "formatter": "verbose",
            "encoding": "utf8",
        }
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ['console', 'file'],
            "propagate": True
        }
    }
}

def create_app() -> Sanic:
    app = Sanic("GraphQLApp", log_config=LOGGINGS)

    from web.blueprints.view import bp  # noqa

    app.blueprint(bp)
    return app
