from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password


from myblog.models import Classes,Userinfo,Siteinfo
from myblog.toJson import Classes_data,Userinfo_data
@api_view(['GET','POST'])
def api_test(request):
    classes= Classes.objects.all()
    data = {
        'classes':[]
    }
    for c in classes:
        data_item = {
            'id':c.id,
            'text':c.text,
            'userlist':[]
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id':user.id,
                'nickName':user.nickName,
                'headImg':str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    return Response(data)


@api_view(['GET'])
def getMenuList(request):
   allClasses = Classes.objects.all()
   Sinfo=Siteinfo.objects.get(id=1)
   Siteinfo_data={
       "sitename":Sinfo.title,
       "logo":"http://127.0.0.1:9000/upload/"+str(Sinfo.logo)
   }
   #整理数据为json
   menu_data=[]
   for c in allClasses:
     #设计单挑数据的结构
     data_item = {
         'id':c.id,
         'text':c.text
     }
     menu_data.append(data_item)
   data={
       "menu_data":menu_data,
       "Siteinfo":Siteinfo_data
   }
   return Response(data)

@api_view(['GET','DELETE'])
def getUserList(request):
    if request.method == "DELETE":
        user_id=request.POST['id']
        print(user_id)
        deleteUser=Userinfo.objects.get(id=user_id)
        deleteUser.delete()
        return Response('ok')
    menuId=request.GET['id']
    print(menuId)
    menu=Classes.objects.get(id=menuId)
    print(menu)
    userlist=Userinfo.objects.filter(belong=menu)
    print(userlist)
    #整理数据为json
    data=[]
    for user in userlist:
    #设计单挑数据的结构
     data_item = {
        'id':user.id,
        'headImg':str(user.headImg),
        'nickName':user.nickName
     }
    data.append(data_item)
    return Response(data)

@api_view(['POST'])
def toLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    #查询用户数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        user_pwd = user[0].password
        auth_pwd = check_password(password,user_pwd)
        print(auth_pwd)
        if auth_pwd:
            token=Token.objects.update_or_create(user=user[0])
            token=Token.objects.get(user=user[0])
            print(token.key)
            data = {
                'token':token.key
            }
            return Response(data)
        else:
            return Response('pwderr')
    else:
        return Response('none')
    
    
@api_view(['GET','POST'])
def toRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username,password,password2)
    user=User.objects.filter(username=username)
    if user:
        return Response('same')
    else:
        newPwd=make_password(password,username)
        print(newPwd)
        newUser=User(username=username,password=newPwd)
        newUser.save()
    return Response('ok')


@api_view(['PUT','POST'])
def uploadLogo(request):
    
    if request.method =="PUT":
       sitename = request.POST['sitename']
       print("sitename")
       old_info=Siteinfo.objects.get(id=1)
       old_info.title = sitename
       new_info=Siteinfo.objects.get(id=2)
       old_info.logo=new_info.logo
       old_info.save()
       return Response('ok')
    img = request.FILES['logo'] 
    print(img) 
    test_siteLogo = Siteinfo.objects.get(id=2)
    test_siteLogo.logo=img
    test_siteLogo.save()
    data = {
      'img':str(test_siteLogo.logo)
     }
    return Response(data)

