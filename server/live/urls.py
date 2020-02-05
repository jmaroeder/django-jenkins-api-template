from django.urls import path

from server.live.views.live import LiveView

urlpatterns = [
    path("live", LiveView.as_view(), name="live"),
]
