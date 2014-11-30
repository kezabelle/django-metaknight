from editregions.models import EditRegionConfiguration
from editregions.utils.data import attach_configuration
from editregions.utils.data import get_configuration
from rest_framework import routers
from rest_framework.fields import SerializerMethodField
from varlet.views_drf import SaferPageViewSet


class MKPageSerializer(SaferPageViewSet.serializer_class):
    editregions = SerializerMethodField('get_editregion_config')

    def get_editregion_config(self, obj):
        attach_configuration(obj, EditRegionConfiguration)
        try:
            return get_configuration(obj).tolist()
        except AttributeError:
            return None

    class Meta:
        model = SaferPageViewSet.serializer_class.Meta.model
        fields = (SaferPageViewSet.serializer_class.Meta.fields +
                  ['editregions'])


class PageViewSet(SaferPageViewSet):
    serializer_class = MKPageSerializer


v1_router = routers.DefaultRouter()
v1_router.register(r'pages', PageViewSet)
