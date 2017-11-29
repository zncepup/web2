"""web2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import jiaotongzhaoshi.views as views_jtzs
import weixianjiashi.views as views_wxjs
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views_wxjs.index),
    url(r'^x',views_jtzs.x),
    url(r'^jubu_wxjs',views_wxjs.results),
    url(r'^jubu_jtzs',views_jtzs.results),
    url(r'^beginsearch',views_jtzs.search),
    url(r'^wxjs',views_wxjs.index),
    url(r'^jtzs',views_jtzs.index),
    url(r'^result_jtzs',views_jtzs.result_jtzs),
    url(r'^result_wxjs',views_wxjs.result_wxjs)
]
