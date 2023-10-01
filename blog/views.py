from django.shortcuts import render

#create your view here
def post_list(request):
    return render(request, 'blog/post_list.html' , {})
