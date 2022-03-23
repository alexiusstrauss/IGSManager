from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="IGSManager API",
        default_version='v1',
        description="IGS Service Manager",
        contact=openapi.Contact(email="contact@igs.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path(r'',
         RedirectView.as_view(permanent=False, url='/swagger/'),
         name='swagger'),

    path('api/', include('employee.urls')),
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),

    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),

    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
