
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages module for displaying messages
from . import util
from .util import fuck_generator
from markdown2 import Markdown
import random

#vars for converting md to html
markdowner = Markdown()

class NewPageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title):
                form.add_error('title', 'Idiot! Titlen eksisterer allerede - prøv igen...')
            else:
                util.save_entry(title, content)
                return redirect('entry', title=title)
    else:
        form = NewPageForm()
    return render(request, 'encyclopedia/new_page.html', {'form': form})

def randompage(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)

def search_results(request):
    query = request.GET.get('q')
    if query:
        entries = util.list_entries()
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
        if matching_entries:
            return render(request, "encyclopedia/search_results.html", {"query": query, "entries": matching_entries})
        else:
            return render(request, "encyclopedia/search_results.html", {"query": query, "entries": []})
    else:
        return render(request, "encyclopedia/index.html")

def entry(request, title):
    page = util.get_entry(title)
    if page:
        page_converted = markdowner.convert(page)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page": page_converted
        })
    else:
        return render(request, "encyclopedia/404.html")

def edit_entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content:
        if request.method == 'POST':
            form = NewPageForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                util.save_entry(title, content)
                messages.success(request, f'Changes to "{title}" were saved successfully.')
                return redirect('entry', title=title)
        else:
            initial_data = {'content': entry_content}
            form = NewPageForm(initial=initial_data)
        return render(request, 'encyclopedia/edit_entry.html', {'form': form, 'title': title})
    else:
        return render(request, "encyclopedia/404.html")

def test(request):
    fucks = fuck_generator("can be anything. it just needs a string")
    return render(request, "encyclopedia/test.html", {'fucks': fucks})