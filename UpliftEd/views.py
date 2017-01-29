from django.shortcuts import render
from UpliftEd.models import Users
from django.http import HttpResponse, HttpResponseRedirect
from UpliftEd.models import Users, Videos, Playlists
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.utils import timezone

# Create your views here.
'''def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)'''

def home(request):
   return render(request,'index.html')

def index(request):
   if request.user.is_authenticated:
      return render(request,'index.html')
   
   else: HttpResponseRedirect(reverse('home'))
      

def user(request,id):
   """
   Receives:
      - ID
      
   Fetch:
      -  Name
      -  Playlist Thumbnails
      -  Bio
      -  Reputatio
   Renders the page

   returns HttpResponse(RENDER_RESULT)
   
   """
   if request.user.is_authenticated:
      user = Users.objects.get(id=id)
      name = user.display_name
      reputation = user.reputation
      bio = user.bio
      playlists = Playlists.objects.filter(owner_ID=id)
      
      return render(request,'profile.html',{})
   
   else: HttpResponseRedirect(reverse('home'))
def category(request,cat):
   """
   Recieve:
      -category
   Fetch:
      - list of playlist
   renders the page"""
   if request.user.is_authenticated:
      playlists = Playlists.objects.filter(category=cat)
      return render(request,'category.html',{})
   
   else: HttpResponseRedirect(reverse('home'))
   
def video(request):
   """
   Recieve:
      -id
   Fetch:
      - video info
      - playlist
   renders the page"""
   '''video = Videos.objects.get(id=id)
   playlist = Playlists.objects.get(id=playlist_ID)'''
   print 'testt'
   return render(request,'video.html')
   

def playlist(request,id):
   """
   Recieve:
      -id
   Fetch:
      - videos info
      - playlist
   renders the page"""
   if request.user.is_authenticated:
      playlist = Playlists.objects.get(id=id)
      videos_info = Videos.objects.filter(playlist_ID=id)
      
      return render(request,'playlist.html',{})
   
   else: HttpResponseRedirect(reverse('home'))

def upload_video(request):
   if request.user.is_authenticated:
      return render(request,'upload.html',{})
   
   else: HttpResponseRedirect(reverse('home'))

def post_upload(request):
   link = []*10
   name = []*10
   category = request.POST['category']
   playlist_name = request.POST['playlist_name']
   thumbnail = request.POST['thumbnail']
   for i in range(1,11):
      link[i-1] = request.POST['link%d'%i]
      name[i-1] = request.POST['name%d'%i]
   playlist = Playlists(owner_ID=request.user.id,playlist_name=playlist_name,
                       category = category, rep_index=0,thumbnail=thumbnail,
                       created_datetime = timezone.now()
                       )
   playlist.save()
   for i in range(10):
      if name[i]:
         video = Videos(owner_ID=request.user.id, playlist_ID = playlist.id,
                        video_name=name[i], video_votes=0, video_index=i,
                        video_link=link[i]
                        )
         video.save()
   return  HttpResponseRedirect(reverse('playlist',args=(playlist.id,)))

def upvote(request,id):
   if request.user.is_authenticated:
      video = Videos.objects.get(id=id)
      video.video_votes += 1
      video.save()
      u = Users.objects.get(id=request.user.id)
      u.reputation += 1
      u.save()
      pl = Playlists.object.get(id=video.playlist_ID)
      pl.rep_index -=1
      pl.save()
      return HttpResponse('1')
   else: HttpResponseRedirect(reverse('home'))

def downvote(request,id):
   if request.user.is_authenticated:
      video = Videos.objects.get(id=id)
      video.video_votes -= 1
      video.save()
      u = Users.objects.get(id=request.user.id)
      u.reputation -= 1
      u.save()
      pl = Playlists.object.get(id=video.playlist_ID)
      pl.rep_index -=1
      pl.save()
      return HttpResponse('1')
   else: HttpResponseRedirect(reverse('home'))

   
def subscribe(request,id):
   if request.user.is_authenticated:
      s = Subscriptions(suscriber=request.user.id,suscribed_to=id)
      s.save()
      
   else: HttpResponseRedirect(reverse('home'))
   

def post_signup(request):
   username=request.POST['username']
   name = request.POST['name']
   password = request.POST['password']
   bio = request.POST['bio']
   user = Users.objects.create_user(username,password,name,bio)
   user.save()
   
def signin(request):
   username=request.POST['username']
   password = request.POST['password']
   user = authenticate(username=username,password=password)
   if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('home'))
   else:
      return HttpResponseRedirect(reverse('index'))


