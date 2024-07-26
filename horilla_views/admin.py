from django.contrib import admin

from horilla_views.models import ActiveGroup, ActiveTab, ToggleColumn

admin.site.register([ToggleColumn, ActiveTab, ActiveGroup])
