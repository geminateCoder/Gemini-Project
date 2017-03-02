from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse_lazy
from .forms import CharacterForm
from .models import Character
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView
# Create your views here.


@login_required
def charaCreate(request):
    form = CharacterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.username = request.user
        instance.save()
        messages.success(request, "Successfully created the character!")
        return redirect('/character/create/')
    else:
        messages.error(request, "Character failed to create!")

    context= {
        "form": form,
        "title": "Create a Character"
    }
    return render(request, "create.html", context)


def charaProfile(request, id):
    instance = get_object_or_404(Character, id=id)
    context = {
        "instance": instance
    }
    return render(request, "charaProfile.html", context)

@login_required
def charaEdit(request, id):
    instance = get_object_or_404(Character, id=id)
    form = CharacterForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/character/edit/{}'.format(id))
    else:
        charaP = instance
        form = CharacterForm(instance=charaP)
    context = {
        "form":form,
        "instance": instance
    }
    return render(request, "charaEdit.html", context)


@login_required
def charaArchive(request):
    charaList = Character.objects.filter(username=request.user).order_by("-created_on")
    paginator = Paginator(charaList, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        charas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        charas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        charas = paginator.page(paginator.num_pages)
    context = {
        "charas": charas,
        "title": "RPground News"
    }
    return render(request, 'archive.html', context)

@login_required
def favChara(request):
    pass

class PermissionMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(PermissionMixin, self).get_object(*args, **kwargs)
        if not obj.username == self.request.user:
            raise PermissionDenied()
        else:
            return obj

class DelChara(PermissionMixin, DeleteView):
    model = Character
    success_url = reverse_lazy('archive')


"""def delChar(request, id):
    instance = get_object_or_404(Character, id=id)
    if instance.username == request.user:
        instance.delete()
        messages.success(request, "Successfully deleted the character!")
    else:
        raise Http404
    return redirect("/character/archive")"""