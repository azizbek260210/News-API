from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
import datetime


@login_required(login_url='dashboard:log_in')
def index(request):
    """-----asosiy sahifa------"""
    categories = models.Category.objects.all()
    user = User.objects.last()

    context = {
        'categories': categories,
        'user': user,
    }

    return render(request, 'dashboard/index.html', context)

# ---------------------------category------------------------------

@login_required(login_url='dashboard:log_in')
def create_category(request):
    """-----category------"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Category.objects.create(
                name=name,
                )
            messages.success(request, 'Kategoriya muvoffaqqiyatli yaratildi')
        except:
            messages.error(request, 'Kategoriya yaratishda xatolik')

    return render(request, 'dashboard/category/create.html')


@login_required(login_url='dashboard:log_in')
def list_category(request):
    categories = models.Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'dashboard/category/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_category(request, id):
    category = models.Category.objects.get(id=id)
    context = {
        'category': category,
    }

    return render(request, 'dashboard/category/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_category(request, id):
    """--------category edit-------"""
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Category.objects.filter(id=id).update(
                name=name,
            )
            messages.success(request, 'Kategoriya muvaffaqqiyatli o`zgartirildi')
            return redirect('dashboard:detail_category', category.id)
        except:
            messages.error(request, 'Kategoriyani o`zgartirishda xatolik')

    return render(request, 'dashboard/category/edit.html', context={'category': category})


@login_required(login_url='dashboard:log_in')
def delete_category(request, id):
    """----categoriyani o'chirish----"""
    try:
        models.Category.objects.filter(id=id).delete()
        messages.success(request, 'Kategoriya muvoffaqqiyatli o`chirildi')
        return redirect('dashboard:list_category')
    except:
        messages.error(request, 'Kategoriyani o`chirishda xatolik')
    return render(request, 'dashboard/category/delete.html')

# ------------------------------region------------------------------

@login_required(login_url='dashboard:log_in')
def create_region(request):
    """-----region------"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Region.objects.create(
                name=name,
                )
            messages.success(request, 'Hudud muvaffaqqiyatli yaratildi')
        except:
            messages.error(request, 'Hudud yaratishda xatolik')

    return render(request, 'dashboard/region/create.html')


@login_required(login_url='dashboard:log_in')
def list_region(request):
    regions = models.Region.objects.all()
    context = {
        'regions': regions,
    }

    return render(request, 'dashboard/region/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_region(request, id):
    region = models.Region.objects.get(id=id)
    context = {
        'region': region,
    }

    return render(request, 'dashboard/region/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_region(request, id):
    """--------region edit-------"""
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Region.objects.filter(id=id).update(
                name=name,
            )
            messages.success(request, 'Hudud muvaffaqqiyatli o`zgartirildi')
            return redirect('dashboard:detail_region', region.id)
        except:
            messages.error(request, 'Hududni o`zgartirishda xatolik')

    return render(request, 'dashboard/region/edit.html', context={'region': region})


@login_required(login_url='dashboard:log_in')
def delete_region(request, id):
    """----regionni o'chirish----"""
    try:
        models.Region.objects.filter(id=id).delete()
        messages.success(request, 'Hudud muvoffaqqiyatli o`chirildi')
        return redirect('dashboard:list_region')
    except:
        messages.error(request, 'Hududni o`chirishda xatolik')
    return render(request, 'dashboard/region/list.html')

# ------------------------------post------------------------------

@login_required(login_url='dashboard:log_in')
def create_post(request):
    """-----post------"""
    users = models.User.objects.all()
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    context = {
        'users':users,
        'categories':categories,
        'regions':regions
    }
    if request.method == 'POST':
        try:
            title = request.POST['title']
            body = request.POST['body']
            banner_img = request.FILES['banner_img']
            date = datetime.datetime.strptime(request.POST['date'], '%m/%d/%Y').strftime('%Y-%m-%d')
            user_id = request.POST['user_id']
            category_id = request.POST['category_id']
            region_id = request.POST['region_id']
            user = models.User.objects.get(id=user_id)
            category = models.Category.objects.get(id=category_id)
            region = models.Region.objects.get(id=region_id)
            post = models.Post.objects.create(
                title=title,
                body=body,
                banner_img=banner_img,
                date=date,
                author=user,
                region=region,
                category=category
                )
            messages.success(request, 'Post muvaffaqqiyatli yaratildi')
        except:
            messages.error(request, 'Post yaratishda xatolik')

    return render(request, 'dashboard/post/create.html', context)


@login_required(login_url='dashboard:log_in')
def list_post(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'dashboard/post/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_post(request, id):
    post = models.Post.objects.get(id=id)
    context = {
        'post': post,
    }

    return render(request, 'dashboard/post/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_post(request, id):
    """--------post edit-------"""
    post = models.Post.objects.get(id=id)
    users = models.User.objects.all()
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    context = {
        'users':users,
        'categories':categories,
        'regions':regions
    }
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            body = request.POST.get('body')
            banner_img = request.POST.get('banner_img')
            date = request.POST.get('date')
            user_id = request.POST['user_id']
            category_id = request.POST['category_id']
            region_id = request.POST['region_id']
            user = models.User.objects.get(id=user_id)
            category = models.Category.objects.get(id=category_id)
            region = models.Region.objects.get(id=region_id)
            models.Post.objects.filter(id=id).update(
                title=title,
                body=body,
                banner_img=banner_img,
                date=date,
                author=user,
                region=region,
                category=category
            )
            messages.success(request, 'Post muvaffaqqiyatli o`zgartirildi')
            return redirect('dashboard:detail_post', post.id)
        except:
            messages.error(request, 'Postni o`zgartirishda xatolik')

    return render(request, 'dashboard/post/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_post(request, id):
    """----postni o'chirish----"""
    try:
        models.Post.objects.filter(id=id).delete()
        messages.success(request, 'Post muvoffaqqiyatli o`chirildi')
        return redirect('dashboard:list_post')
    except:
        messages.error(request, 'Postni o`chirishda xatolik')
    return render(request, 'dashboard/post/list.html')

# --------------------------------contact-------------------------------------

@login_required(login_url='dashboard:log_in')
def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts
        }
    return render(request, 'dashboard/contact/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_contact(request, id):
    contact = models.Contact.objects.get(id=id) 
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/detail.html', context)

@login_required(login_url='dashboard:log_in')
def edit_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == "POST":
        try:
            is_show = request.POST.get('is_show')  
            contact.is_show = is_show == 'on'
            contact.save()
            messages.success(request, 'Contactdagi ma`lumot muvaffaqqiyatli o`zgartirildi')
        except:
            messages.error(request, 'Contactdagi ma`lumotni o`zgartirishda xatolik yuz berdi')
        return redirect('dashboard:list_contact')
    context = {
        'contact': contact, 
    }
    return render(request, 'dashboard/contact/edit.html', context)


# ------------------------------register, login, logout----------------------------
def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            if password == password_confirm:
                User.objects.create_user(
                    username=username,
                    password=password
                )
            messages.success(request, 'Foydalanuvchi muvaffaqqiyatli yaratildi')
        except:
            messages.error(request, 'Foydalanuvchi yaratishda xatolik')
        return redirect('dashboard:index')
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'Xush kelibsiz!')
        except:
            messages.error(request, 'Xatolik')
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'dashboard/auth/login.html', {'error_message': 'Username yoki passwordd.'})
    else:
        return render(request, 'dashboard/auth/login.html')


@login_required(login_url='dashboard:log_in')
def log_out(request):
    """-----chiqish----"""
    logout(request)
    return redirect('main:index')


