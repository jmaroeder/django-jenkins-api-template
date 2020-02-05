from server.settings.components import config

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": config.drf.parser_classes,
    "DEFAULT_RENDERER_CLASSES": config.drf.renderer_classes,
    "UNAUTHENTICATED_USER": None,
}
