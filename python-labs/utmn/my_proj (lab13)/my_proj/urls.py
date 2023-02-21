"""my_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ch_g import views

addurls = [
    path('book/', views.addBook),
    path('author/', views.addAuthor),
    path('language/', views.addLanguage),
    path('genre/', views.addGenre),
    path('print/', views.addPrint),
]

editurls = [
    path('book/<int:bookid>/', views.editBook),
    path('author/<int:authorid>/', views.editAuthor),
    path('language/<int:languageid>/', views.editLanguage),
    path('genre/<int:genreid>/', views.editGenre),
    path('print/<int:printid>/', views.editPrint),
]

deleteurls = [
    path('book/<int:bookid>/', views.deleteBook),
    path('author/<int:authorid>/', views.deleteAuthor),
    path('language/<int:languageid>/', views.deleteLanguage),
    path('genre/<int:genreid>/', views.deleteGenre),
    path('print/<int:printid>/', views.deletePrint),
]

cabineturls = [
    path('<int:userid>/', views.myCabinet),
    path('editprof/<int:userid>/', views.ChangeProf),
    path('editauth/<int:userid>/', views.ChangeAuth),
    path('<int:mainuserid>/makestaff/<int:userid>/<int:staff>/', views.MakeStaff),
    path('<int:userid>/favourites/', views.seeFavourites),
    path('<int:userid>/tofavs/<int:bookid>/', views.addToFavs),
    path('<int:userid>/fromfavs/<int:bookid>/', views.delFromFavs),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ch-g.ru/', views.beAtHome),
    path('ch-g.ru/books/', views.seeAllBooks),
    path('ch-g.ru/authors/', views.seeAllAuthors),
    path('ch-g.ru/book/<int:bookid>/', views.seeExactBook),
    path('ch-g.ru/author/<int:authorid>/', views.seeExactAuthor),
    path('ch-g.ru/add/', include(addurls)),
    path('ch-g.ru/edit/', include(editurls)),
    path('ch-g.ru/delete/', include(deleteurls)),
    path('ch-g.ru/register/', views.regIn),
    path('ch-g.ru/login/', views.logIn),
    path('ch-g.ru/logout/', views.logOut),
    path('ch-g.ru/cabinet/', include(cabineturls)),
]
