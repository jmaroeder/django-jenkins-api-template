from django.urls import include, path
from rest_framework import routers

# Create a router and register our viewsets with it.
router = routers.SimpleRouter(trailing_slash=False)

app_name = "api"

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
