from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Article, Rubric, Hashtag, ArticleHashtag
from .forms import ArticleForm, RubricForm, HashtagForm, LoginForm, RegisterForm

# Create your views here.
def home(request):
    header = 'Новости науки'
    rubrics = Rubric.objects.raw('SELECT DISTINCT news_rubric.id, name '
                                 'FROM news_rubric '
                                 'JOIN news_article ON news_rubric.id = news_article.rubnum_id '
                                 'ORDER BY news_rubric.id;')
    articles = Article.objects.raw('SELECT * FROM news_article ORDER BY published DESC')
    if request.user.is_authenticated:
        auth = True
    else:
        auth = False
    return render(request, 'index.html', {'header': header, 'rubrics': rubrics, 'articles': articles, 'auth': auth})


@login_required
def article(request, artid):
    rubrics = Rubric.objects.raw('SELECT DISTINCT news_rubric.id, name '
                                 'FROM news_rubric '
                                 'JOIN news_article ON news_rubric.id = news_article.rubnum_id '
                                 'ORDER BY news_rubric.id;')
    rub = Rubric.objects.raw('SELECT news_rubric.id, name, news_article.published '
                             'FROM news_article '
                             'JOIN news_rubric ON news_article.rubnum_id = news_rubric.id '
                             'WHERE news_article.id = ' + str(artid) +
                             ' ORDER BY published DESC;')
    if request.user.is_authenticated:
        auth = True
    else:
        auth = False
    return render(request, 'article.html', {'rubrics': rubrics, 'rubric': rub,
                                            'article': Article.objects.filter(id=artid).values(), 'auth': auth})


@login_required
def rubric(request, rubid):
    header = 'Новости науки'
    rubrics = Rubric.objects.raw('SELECT DISTINCT news_rubric.id, name '
                                 'FROM news_rubric '
                                 'JOIN news_article ON news_rubric.id = news_article.rubnum_id '
                                 'ORDER BY news_rubric.id;')
    articles = Article.objects.raw('SELECT news_article.id, title, keywords, image, news_article.published '
                                   'FROM news_rubric '
                                   'JOIN news_article ON news_rubric.id = news_article.rubnum_id '
                                   'WHERE news_rubric.id = ' + str(rubid) +
                                   ' ORDER BY published DESC;')
    if request.user.is_authenticated:
        auth = True
    else:
        auth = False
    return render(request, 'rubric.html', {'header': header, 'rubrics': rubrics, 'rubric': Rubric.objects.get(id=rubid),
                                           'articles': articles, 'auth': auth})


@login_required
def addArticle(request):
    if request.method == 'POST':
            articleform = ArticleForm(request.POST, request.FILES)
        if articleform.is_valid():
            Article.objects.create(title=articleform.cleaned_data['title'],
                                   keywords=articleform.cleaned_data['keywords'],
                                   annotation=articleform.cleaned_data['annotation'],
                                   image=request.FILES['image'],
                                   rubnum=articleform.cleaned_data['rubnum'])
            ArticleHashtag.objects.bulk_create([
                ArticleHashtag(fk_id_art=Article.objects.latest('id'),
                               fk_id_ht=elem) for elem in articleform.cleaned_data['hashtag']
                ])
            return HttpResponseRedirect('/news/')
    else:
        articleform = ArticleForm()
    header = 'Добавить статью'
    act_url = '/news/add/article/'
    return render(request, 'addsmthnew.html', {'header': header, 'act_url': act_url, 'form': articleform})


@login_required
def addRubric(request):
    if request.method == 'POST':
        rubricform = RubricForm(request.POST)
        if rubricform.is_valid():
            Rubric.objects.create(name=rubricform.cleaned_data['name'])
            return HttpResponseRedirect('/news/')  # HttpResponse(f"""<h2>{rub}</h2>""")
    else:
        rubricform = RubricForm()
    header = 'Добавить рубрику'
    act_url = '/news/add/rubric/'
    return render(request, 'addsmthnew.html', {'header': header, 'act_url': act_url, 'form': rubricform})


@login_required
def addHashtag(request):
    if request.method == 'POST':
        hashtagform = HashtagForm(request.POST)
        if hashtagform.is_valid():
            Hashtag.objects.create(name=hashtagform.cleaned_data['name'])
            return HttpResponseRedirect('/news/')
    else:
        hashtagform = HashtagForm()
    header = 'Добавить хештег'
    act_url = '/news/add/hashtag/'
    return render(request, 'addsmthnew.html', {'header': header, 'act_url': act_url, 'form': hashtagform})


# @login_required
# def editArt(request, artid):
#     if request.method == 'POST':
#         articleform = ArticleForm(request.POST, request.FILES, instance=Article.objects.get(id=artid))
#         if articleform.is_valid():
#             Article.objects.filter(id=artid).update(title=articleform.cleaned_data['title'],
#                                                     keywords=articleform.cleaned_data['keywords'],
#                                                     annotation=articleform.cleaned_data['annotation'],
#                                                     image=request.FILES['image'],
#                                                     rubnum=articleform.cleaned_data['rubnum'])
#             ArticleHashtag.objects.filter(fk_id_art=Article(id=artid)).update([
#                 ArticleHashtag(fk_id_ht=elem) for elem in articleform.cleaned_data['hashtag']
#             ])
#             return HttpResponseRedirect('/news/')
#     else:
#         articleform = ArticleForm(instance=Article.objects.get(id=artid))
#     header = 'Добавить статью'
#     act_url = '/news/add/article/'
#     return render(request, 'addsmthnew.html', {'header': header, 'act_url': act_url, 'form': articleform})


@login_required
def deleteArt(request, artid):
    Article.objects.filter(id=artid).delete()
    return HttpResponseRedirect('/news/')


def mylogin(request):
    if request.method == 'POST':
        myloginform = LoginForm(request.POST)
        if myloginform.is_valid():
            user = authenticate(request, username=myloginform.cleaned_data['username'], password=myloginform.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/news/')
            else:
                return HttpResponse('Извините, но вы не смогли войти')
            # return HttpResponseRedirect('/news/')
    else:
        myloginform = LoginForm()
    header = 'Вход'
    return render(request, '_user/login.html', {'header': header, 'form': myloginform})


def myregister(request):
    if request.method == 'POST':
        myregisterform = RegisterForm(request.POST)
        if myregisterform.is_valid():
            User.objects.create_user(username=myregisterform.cleaned_data['username'],
                                     password=myregisterform.cleaned_data['password1'])
            return redirect('/news/')
    else:
        myregisterform = RegisterForm()
    header = 'Регистрация'
    return render(request, '_user/register.html', {'header': header, 'form': myregisterform})


def mylogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/news/')
    header = 'Выход'
    return render(request, '_user/logout.html', {'header': header})
