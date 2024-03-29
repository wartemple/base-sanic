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
            "when": "H",
            "interval": 6,
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
    app = Sanic("Main", log_config=LOGGINGS)

    from web.blueprints.view import bp  # noqa
    # 默认健康检查
    app.config.HEALTH = True
    app.config.HEALTH_ENDPOINT = True
    # 错误返回结果为json
    app.config.FALLBACK_ERROR_FORMAT = "json"
    app.blueprint(bp)
    return app
