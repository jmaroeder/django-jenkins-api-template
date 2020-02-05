from django.urls import include, path

import api.urls
import server.live.urls

urlpatterns = [
    path("", include((server.live.urls, "server.live"), namespace="live")),
    path("", include(api.urls, namespace="api")),
]
