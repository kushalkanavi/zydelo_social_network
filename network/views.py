from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import make_password, check_password

from .models import Post, User

def login(request):
    if request.method == 'POST':
        try:
            UserName = request.POST['user']
            Password = request.POST['pass']

            log_user = User.nodes.get(name=UserName)
            request.session['user_id'] = log_user.uid

            check_pass = check_password(Password, log_user.Passwoed)
        except:
            data = {'message' : 'Username Doesnt Exists, Create New User from Register'}
            return render(request,'login.html', data)
        
        if check_pass:
            return redirect(index)
        else:
            data = {'message' : 'Username or Password Does Not Match'}
            return render(request,'login.html', data)
    
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        try:
            UserName = request.POST['user']
            Password = request.POST['pass']

            new_password = make_password(Password)

            new_user = User(name=UserName, Passwoed=new_password)
            new_user.save()

        except Exception as e:
            data = {'message' : str(e) + ' Try different Username'}
            return render(request,'register.html', data)
        
        return render(request,'login.html')
    
    else:
        return render(request,'register.html')


def index(request):
    if request.method == 'POST':
        try:
            user_id = request.session['user_id']
            current_user = User.nodes.get(uid=user_id)
            current = False
            Follow = False
            user = request.POST['user']
            search_user = User.nodes.get(name=user)
        
            if search_user.uid == user_id:
                current = True
            
            for follow_user in current_user.follows.all():
                if follow_user.name == search_user.name:
                    Follow = True
                
            if current:
                data = {'CurrentUser': current_user.name,'Search_Username': search_user.name, 'currentFlag': current, 'followFlag': Follow}
            else:
                data = {'CurrentUser': current_user.name,'Search_Username': search_user.name, 'currentFlag': current, 'followFlag': Follow}
            return render(request,'index.html', data)
        except Exception as e:
            data = {'CurrentUser': current_user.name, 'message': 'User Name Doesnt Exists, Try Some other User Name'}
            return render(request,'index.html', data)
    
    else:
        user_id = request.session['user_id']
        user = User.nodes.get(uid=user_id)
        
        data_list = []
        for follow_user in user.follows.all():
            for follow_post in follow_user.user_post.all():
                data_list.append(
                    {
                        'User' : follow_user.name,
                        'Title' : follow_post.title,
                        'Description' : follow_post.Description,
                        'Image' : follow_post.Image,
                        'created_at' : follow_post.created_at
                    }
                )
        data_list = sorted(data_list, key=lambda k: k['created_at'], reverse=True) 
        if data_list:
            data = {
                'CurrentUser': user.name,
                'data_list': data_list
            }
            return render(request,'index.html', data)
        else:
            data = {
                'CurrentUser': user.name
                }
            return render(request,'index.html', data)


def myPosts(request):
    user_id = request.session['user_id']
    user = User.nodes.get(uid=user_id)

    data_list = []
    for user_post in user.user_post.all():
        data_list.append(
            {
                'Title' : user_post.title,
                'Description' : user_post.Description,
                'Image' : user_post.Image,
                'created_at': user_post.created_at
            }
        )
    
    data_list = sorted(data_list, key=lambda k: k['created_at'], reverse=True) 
    
    if data_list:
        data = {
            'data_list': data_list
        }
        return render(request,'mypost.html', data)
    else:
        return render(request,'mypost.html')

def createPosts(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        img = request.FILES['imageUpload']
        img_name = request.FILES['imageUpload'].name

        with default_storage.open('network/static/'+img_name, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)

        new_post = Post(title=title, Description=description, Image=img_name)
        new_post.save()

        user_id = request.session['user_id']
        user = User.nodes.get(uid=user_id)

        user.user_post.connect(new_post)

        return redirect(myPosts)
    
    else:
        return render(request,'createpost.html')

def follow(request):
    user_id = request.session['user_id']
    user = User.nodes.get(uid=user_id)
    follow_user = User.nodes.get(name=request.POST['user'])
    user.follows.connect(follow_user)
    return redirect(index)

def unfollow(request):
    user_id = request.session['user_id']
    user = User.nodes.get(uid=user_id)
    follow_user = User.nodes.get(name=request.POST['user'])
    user.follows.disconnect(follow_user)
    return redirect(index)
