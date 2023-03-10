# # pages/urls.py
# from django.urls import path
# from .views import homePageView

# urlpatterns = [
#     path('', homePageView, name='home')
# ]

# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, curtisView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('curtis/', curtisView, name='curtis'),
    path('homePost/', homePost, name='homePost'),
    path('<int:choice>/results/', results, name='results'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]

