from rest_framework import routers
from varlet.views_drf import SaferPageViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'pages', SaferPageViewSet)
