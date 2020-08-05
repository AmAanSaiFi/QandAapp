from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.models import User
from .models import Title, Question, Post
from .forms import NewQuestion, PostAns
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(req):
    t= Title.objects.all()
    ques_count=[]
    for i in t:
        ques_count.append(Question.objects.filter(title=i).count())
    #print(ques_count)
    return render(req,'index.html',{'t':t,'ques_count':ques_count})

def title_questions(req,pk):
    #t=Title.objects.get(pk=pk)
    t= get_object_or_404(Title,pk=pk)
    ques = Question.objects.filter(title=t)
    return render(req,'ques.html',{'t':t,'ques':ques}) 

@login_required
def new_ques(req,pk):
    title = get_object_or_404(Title, pk=pk)
    # user = User.objects.first()
    user = req.user
    if req.method == 'POST':
        form = NewQuestion(req.POST)
        if form.is_valid():
            ques = form.save(commit = False)
            ques.title = title
            ques.started_by = user
            ques.save()
        
            Post.objects.create(
                ans = form.cleaned_data.get('ans'),
                question = ques,
                created_by = user
            )

            return redirect('title_ques', pk=pk, ques_pk = ques.pk)
    else:
        form = NewQuestion()
    
    return render(req, 'new_ques.html', {'title':title,'form':form})


def show_ans(req, pk, ques_pk):
    ques = get_object_or_404(Question, title__pk = pk, pk=ques_pk)
    ques.views += 1
    ques.save()
    return render(req, 'show_ans.html', {'ques' : ques})

@login_required
def post_ans(req, pk, ques_pk):
    ques = get_object_or_404(Question, title__pk = pk, pk=ques_pk)
    if req.method == 'POST':
        form = PostAns(req.POST)
        print("Post Request...")
        if form.is_valid():
            print("Form is valid...")
            ans = form.save(commit=False)
            ans.question = ques
            ans.created_by = req.user
            ans.save()
            print("Form saved successfully...")
            return redirect('show_ans', pk=pk, ques_pk = ques_pk)
    else:
        form = PostAns()
            
    return render(req, 'post_ans.html', {'ques' : ques, 'form' : form})
