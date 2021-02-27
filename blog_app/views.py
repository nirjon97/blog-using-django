from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import post,Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    queryset_list = post.objects.all()
    paginator = Paginator(queryset_list, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)

    context={
        'queryset_list' : queryset_list,
        'queryset' : queryset
        }
    return render(request,'my_blog.html',context)
#the details page

def details(request,id):
    queryset_list = post.objects.get(id=id)
    comments = queryset_list.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.Post =queryset_list
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    context={
         'queryset_list': queryset_list,
         'comments': comments,
         'new_comment': new_comment,
         'comment_form': comment_form
        }
        
    return render(request,'my_blog_details.html',context)

def about_me(request):
    context={
        
        }
    return render(request,'about_me.html',context)

def content_list(request):
    queryset_list = post.objects.all()
    context={
        'queryset_list' : queryset_list
        }
    return render(request,'content_list.html',context)