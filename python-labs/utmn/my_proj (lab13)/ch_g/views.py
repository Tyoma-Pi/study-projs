from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.exceptions import ValidationError
from .models import Book, Author, Language, Genre, Print, AdditonalUserInfo, Favourites, \
    BookForm, AuthorForm, LanguageForm, GenreForm, PrintForm
from .forms import LoginForm, RegisterForm, ChangeAuthForm, ChangeProfForm, FilterForm


# Create your views here.
def beAtHome(request):
    top_dls = (Book.objects
               .order_by('-dlcount')
               .values_list('dlcount', flat=True)
               .distinct()[:5])
    top_books = (Book.objects
                 .order_by('-dlcount')
                 .filter(dlcount__in=top_dls[:5]))
    context = {'dls': top_dls, 'books': top_books}
    return render(request, 'home.html', context)


def seeAllBooks(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            filterf = form.cleaned_data['filterfield']
            if filter != '':
                match filterf:
                    case 'name':
                        books = Book.objects.filter(name__icontains=form.cleaned_data['filter'])
                    case 'author':
                        books = Book.objects.filter(authors__fsl_name__icontains=form.cleaned_data['filter'])
                    case 'language':
                        books = Book.objects.filter(languages__language__icontains=form.cleaned_data['filter'])
                    case 'genre':
                        books = Book.objects.filter(genres__genre__icontains=form.cleaned_data['filter'])
                    case 'year':
                        books = Book.objects.filter(year__year=form.cleaned_data['filter'])
                    case 'print':
                        books = Book.objects.filter(print__name__icontains=form.cleaned_data['filter'])
            else:
                books = Book.objects.all()
    else:
        form = FilterForm()
    context = {'books': books, 'form': form}
    return render(request, '_all/books.html', context)


def seeAllAuthors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, '_all/authors.html', context)


def seeExactBook(request, bookid):
    if request.method == 'POST':
        Book.objects.filter(id=bookid).update(dlcount=F('dlcount') + 1)
        return redirect('/ch-g.ru/')
    else:
        book = Book.objects.get(id=bookid)
        fav_count = Favourites.objects.filter(books=Book(id=bookid)).count()
        fav = False
        for favourites in Favourites.objects.filter(books=Book(id=bookid)):
            if book == favourites.books and request.user == favourites.user:
                fav = True
        context = {'book': book, 'fav': fav, 'fav_count': fav_count}
        return render(request, '_exact/book.html', context)


def seeExactAuthor(request, authorid):
    author = Author.objects.get(id=authorid)
    context = {'author': author}
    return render(request, '_exact/author.html', context)


@login_required
def addBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book.objects.create(name=form.cleaned_data['name'],
                                       description=form.cleaned_data['description'],
                                       year=form.cleaned_data['year'],
                                       print=form.cleaned_data['print'],
                                       isbn=form.cleaned_data['isbn'],
                                       dlcount=form.cleaned_data['dlcount'])
            book.authors.set(form.cleaned_data['authors'])
            book.languages.set(form.cleaned_data['languages'])
            book.genres.set(form.cleaned_data['genres'])
            return redirect('/ch-g.ru/')
    else:
        form = BookForm(initial={'dlcount': 0})
    header_text = 'Добавить книгу'
    button_text = 'Добавить'
    act_url = '/ch-g.ru/add/book/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def addAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(fsl_name=form.cleaned_data['fsl_name'],
                                  birthday=form.cleaned_data['birthday'],
                                  deathday=form.cleaned_data['deathday'],
                                  short_info=form.cleaned_data['short_info'])
            return redirect('/ch-g.ru/')
    else:
        form = AuthorForm()
    header_text = 'Добавить автора'
    button_text = 'Добавить'
    act_url = '/ch-g.ru/add/author/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def addLanguage(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            Language.objects.create(language=form.cleaned_data['language'])
            return redirect('/ch-g.ru/')
    else:
        form = LanguageForm()
    header_text = 'Добавить язык'
    button_text = 'Добавить'
    act_url = '/ch-g.ru/add/language/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def addGenre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            Genre.objects.create(genre=form.cleaned_data['genre'])
            return redirect('/ch-g.ru/')
    else:
        form = GenreForm()
    header_text = 'Добавить жанр'
    button_text = 'Добавить'
    act_url = '/ch-g.ru/add/genre/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def addPrint(request):
    if request.method == 'POST':
        form = PrintForm(request.POST)
        if form.is_valid():
            Print.objects.create(name=form.cleaned_data['name'],
                                 city=form.cleaned_data['city'],
                                 created=form.cleaned_data['created'],
                                 description=form.cleaned_data['description'])
            return redirect('/ch-g.ru/')
    else:
        form = PrintForm()
    header_text = 'Добавить издательство'
    button_text = 'Добавить'
    act_url = '/ch-g.ru/add/print/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def editBook(request, bookid):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(id=bookid)
            book.name = form.cleaned_data['name']
            book.description = form.cleaned_data['description']
            book.year = form.cleaned_data['year']
            book.print = form.cleaned_data['print']
            book.isbn = form.cleaned_data['isbn']
            book.dlcount = form.cleaned_data['dlcount']
            book.authors.set(form.cleaned_data['authors'])
            book.languages.set(form.cleaned_data['languages'])
            book.genres.set(form.cleaned_data['genres'])
            book.save()
            return redirect('/ch-g.ru/')
    else:
        foredit = Book.objects.get(id=bookid)
        form = BookForm(instance=foredit)
    header_text = 'Изменить книгу'
    button_text = 'Изменить'
    act_url = '/ch-g.ru/edit/book/' + str(bookid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def editAuthor(request, authorid):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            (Author.objects
             .filter(id=authorid)
             .update(fsl_name=form.cleaned_data['fsl_name'],
                     birthday=form.cleaned_data['birthday'],
                     deathday=form.cleaned_data['deathday'],
                     short_info=form.cleaned_data['short_info'])
             )
            return redirect('/ch-g.ru/')
    else:
        foredit = Author.objects.get(id=authorid)
        form = AuthorForm(instance=foredit)
    header_text = 'Изменить автора'
    button_text = 'Изменить'
    act_url = '/ch-g.ru/edit/author/' + str(authorid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def editLanguage(request, languageid):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            (
                Language.objects
                .filter(id=languageid)
                .update(language=form.cleaned_data['language'])
            )
            return redirect('/ch-g.ru/')
    else:
        foredit = Language.objects.get(id=languageid)
        form = LanguageForm(instance=foredit)
    header_text = 'Изменить язык'
    button_text = 'Изменить'
    act_url = '/ch-g.ru/edit/language/' + str(languageid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def editGenre(request, genreid):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            (
                Genre.objects
                .filter(id=genreid)
                .update(genre=form.cleaned_data['genre'])
            )
            return redirect('/ch-g.ru/')
    else:
        foredit = Genre.objects.get(id=genreid)
        form = GenreForm(instance=foredit)
    header_text = 'Изменить жанр'
    button_text = 'Изменить'
    act_url = '/ch-g.ru/edit/genre/' + str(genreid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def editPrint(request, printid):
    if request.method == 'POST':
        form = PrintForm(request.POST)
        if form.is_valid():
            (
                Print.objects
                .filter(id=printid)
                .update(name=form.cleaned_data['name'],
                        city=form.cleaned_data['city'],
                        created=form.cleaned_data['created'],
                        description=form.cleaned_data['description'])
            )
            return redirect('/ch-g.ru/')
    else:
        foredit = Print.objects.get(id=printid)
        form = PrintForm(instance=foredit)
    header_text = 'Изменить издательство'
    button_text = 'Изменить'
    act_url = '/ch-g.ru/edit/print/' + str(printid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def deleteBook(request, bookid):
    Book.objects.filter(id=bookid).delete()
    return redirect('/ch-g.ru/')


@login_required
def deleteAuthor(request, authorid):
    Author.objects.filter(id=authorid).delete()
    return redirect('/ch-g.ru/')


@login_required
def deleteLanguage(request, languageid):
    Language.objects.filter(id=languageid).delete()
    return redirect('/ch-g.ru/')


@login_required
def deleteGenre(request, genreid):
    Genre.objects.filter(id=genreid).delete()
    return redirect('/ch-g.ru/')


@login_required
def deletePrint(request, printid):
    Print.objects.filter(id=printid).delete()
    return redirect('/ch-g.ru/')


def logIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/ch-g.ru/')
            else:
                return HttpResponse('Извините, но вы не смогли войти')
    else:
        form = LoginForm()
    header = 'Вход'
    context = {'header': header, 'form': form}
    return render(request, '_user/login.html', context)


def regIn(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'],
                                     email=form.cleaned_data['email'])
            AdditonalUserInfo.objects.create(user=User.objects.get(username=form.cleaned_data['username'],
                                                                   email=form.cleaned_data['email']),
                                             birthday='2020-01-01')
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('/ch-g.ru/')
            else:
                return HttpResponse('Извините, но вы не смогли войти')
    else:
        form = RegisterForm()
    header = 'Регистрация'
    context = {'header': header, 'form': form}
    return render(request, '_user/register.html', context)


@login_required
def logOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/ch-g.ru/')
    header = 'Выход'
    context = {'header': header}
    return render(request, '_user/logout.html', context)


@login_required
def myCabinet(request, userid):
    userinfo = AdditonalUserInfo.objects.get(user=User(id=userid))
    users = User.objects.filter(is_superuser=False)
    header = 'Личный кабинет'
    context = {'header': header, 'userinfo': userinfo, 'users': users}
    return render(request, '_user/cabinet.html', context)


@login_required
def addToFavs(request, userid, bookid):
    Favourites.objects.create(user=User(id=userid), books=Book(id=bookid))
    return redirect('/ch-g.ru/book/' + str(bookid) + '/')


@login_required
def delFromFavs(request, userid, bookid):
    Favourites.objects.filter(user=User(id=userid), books=Book(id=bookid)).delete()
    return redirect('/ch-g.ru/book/' + str(bookid) + '/')


@login_required
def seeFavourites(request, userid):
    header_text = 'Избранное'
    favs = Favourites.objects.filter(user=User(id=userid))
    context = {'header_text': header_text, 'favs': favs}
    return render(request, '_user/favs.html', context)


@login_required
def ChangeAuth(request, userid):
    if request.method == 'POST':
        form = ChangeAuthForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=userid)
            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            if user.check_password('{}'.format(old_password)) == True and new_password1 == new_password2:
                user.set_password('{}'.format(new_password1))
                user.username = form.cleaned_data['username']
                user.email = form.cleaned_data['email']
                user.save()
                update_session_auth_hash(request, user)
                return redirect('/ch-g.ru/cabinet/' + str(userid) + '/')
            else:
                raise ValidationError('Какой-то из паролей не совпадает')
    else:
        form = ChangeAuthForm()
    header_text = 'Изменить логин/пароль/почту'
    button_text = 'Изменить'
    act_url = '/ch-g.ru/cabinet/editauth/' + str(userid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def ChangeProf(request, userid):
    userinfo = AdditonalUserInfo.objects.get(user=User(id=userid))
    if request.method == 'POST':
        form = ChangeProfForm(request.POST, request.FILES)
        if form.is_valid():
            userinfo.user.first_name = form.cleaned_data['first_name']
            userinfo.user.last_name = form.cleaned_data['last_name']
            userinfo.photo = request.FILES['photo']
            userinfo.city = form.cleaned_data['city']
            userinfo.birthday = form.cleaned_data['birthday']
            userinfo.about = form.cleaned_data['about']
            userinfo.user.save()
            userinfo.save()
            return redirect('/ch-g.ru/cabinet/' + str(userid) + '/')
    else:
        form = ChangeProfForm(
            initial={
                'first_name': userinfo.user.first_name,
                'last_name': userinfo.user.last_name,
                'city': userinfo.city,
                'birthday': userinfo.birthday,
                'about': userinfo.about
                })
    header_text = 'Редактировать данные'
    button_text = 'Редактировать'
    act_url = '/ch-g.ru/cabinet/editprof/' + str(userid) + '/'
    context = {'header_text': header_text, 'form': form, 'act_url': act_url, 'button_text': button_text}
    return render(request, 'addelems.html', context)


@login_required
def MakeStaff(request, mainuserid, userid, staff):
    user = User.objects.filter(id=userid)
    match staff:
        case 1:
            user.update(is_staff=True)
        case 0:
            user.update(is_staff=False)
    return redirect('/ch-g.ru/cabinet/' + str(mainuserid) + '/')
