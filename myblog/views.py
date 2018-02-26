from django.shortcuts import render,HttpResponse
from django.template.loader import get_template
from .models import *
import random
from PIL import Image
# Create your views here.
import html as h
# html.unescape('htmlSource')
def five_artical(artical):
    new_five_artical = artical[0:5]
    suiji_five_artical = random.sample(list(artical), 5)
    count_five_artical = Artical.objects.order_by("-count")[0:5]
    return new_five_artical,suiji_five_artical,count_five_artical
def index(request):
    template = get_template('index.html')
    artical= Artical.objects.all()
    new_five_artical, suiji_five_artical, count_five_artical = five_artical(artical)
    html = template.render(locals())
    return HttpResponse(html)
def about(request):
    template = get_template('about.html')
    artical = Artical.objects.all()
    new_five_artical, suiji_five_artical, count_five_artical=five_artical(artical)
    html = template.render(locals())
    return HttpResponse(html)
def say(request):
    template = get_template('shuo.html')
    if request.POST:
        content = request.POST['say_content']
        Say.objects.create(content=content)
    else:
        message="你提交了空的表单"
    say=Say.objects.all()
    html = template.render(locals())
    return HttpResponse(html)
def daynote(request):
    template = get_template('riji.html')
    if request.method == 'POST':
        img=request.FILES['img']
        content=request.POST['riji_content']
        Riji.objects.create(img=img,content=content)
    riji=Riji.objects.all()
    artical = Artical.objects.all()
    new_five_artical, suiji_five_artical, count_five_artical = five_artical(artical)
    html = template.render(locals())
    return HttpResponse(html)
def photo(request):
    template = get_template('xc.html')
    if request.method == 'POST':
        img=request.FILES['img']
        miaoshu=request.POST['miaoshu']
        height = random.randint(160, 300)
        Xc.objects.create(img=img,miaoshu=miaoshu,height=height)
    xc=Xc.objects.all()
    html = template.render(locals())
    return HttpResponse(html)
def learn(request):
    template = get_template('learn.html')
    artical = Artical.objects.all()
    new_five_artical, suiji_five_artical, count_five_artical = five_artical(artical)
    html = template.render(locals())
    return HttpResponse(html)
def guestbook(request):
    template = get_template('guestbook.html')
    artical = Artical.objects.all()
    new_five_artical, suiji_five_artical, count_five_artical = five_artical(artical)
    html = template.render(locals())
    return HttpResponse(html)
def artical(request,idd):
    template = get_template('artical.html')

    a = Artical.objects.get(id=idd)
    count1=a.count+1
    Artical.objects.filter(id=idd).update(count=count1)
    html = template.render(locals())
    return HttpResponse(html)
def editor(request):
    template = get_template('editor.html')
    html = template.render(locals())
    return HttpResponse(html)
def blogpost(request):
    template = get_template('editor.html')
    if request.POST:
        content = request.POST['content']

        author=request.POST['author']
        title = request.POST['title']
        category=request.POST['category']
        describe=request.POST['describe']
        Artical.objects.create(title=title, content=content,author=author,category=category,describe=describe)
        #p = Post(title=title, body=body)
        # p.save()
    else:
        message = "您提交了空的表单"

    html = template.render(locals())
    return HttpResponse(html)




