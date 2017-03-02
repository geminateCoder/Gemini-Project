from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def blogPosts(request):
    pass


def BlogCreate(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def editBlogP(request):
    pass


def promptPost(request):
    pass


def createPromptP(request):
    pass


def editPromptP(request):
    pass


def delPost(request):
    pass
