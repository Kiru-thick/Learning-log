from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def topic_view(request):
    topic = Topic.objects.filter(owner=request.user)
    context = {
        'topics': topic
    }

    return render(request, 'topic.html', context)


def home_view(request):
    topic = Topic.objects.all()
    context = {
        'topics': topic
    }

    return render(request, 'home.html', context)

@login_required
def detail_view(request, id):
    # to get the entry of corresponding topic
    topic = Topic.objects.get(id=id)
    entries = topic.entry_set.order_by('-date')
    if topic.owner != request.user:
        raise Http404
    context = {
        'topic': topic,
        'entries''': entries

    }

    return render(request, 'detail.html', context)

@login_required
def form_view(request):
    # use post method to get the responses
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('topic'))

    context = {
        'form': form
    }

    return render(request, 'create.html', context)

@login_required
def entryform_view(request, id):
    topic = Topic.objects.get(id=id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return HttpResponseRedirect(reverse('detail', kwargs={'id': id}))

    context = {
        'form': form,
        'topic': topic
    }
    return render(request, 'entry.html', context)

@login_required
def edit_view(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail', args=[topic.id]))

    context = {
        'form': form,
        'topic': topic,
        'entry': entry
    }

    return render(request, 'edit.html', context)


