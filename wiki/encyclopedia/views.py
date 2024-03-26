from django.shortcuts import render, HttpResponse, redirect
from markdown2 import Markdown
from . import util
from .util import fuck_generator
import random


#vars for converting md to html
markdowner = Markdown()
# end

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newpage(request):
    return render(request, "encyclopedia/newpage.html", {
        "entries": util.list_entries()
    })

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
    

# start new view (maybe title instead of page?)
def entry(request, title):
    page = util.get_entry(title)  # Pass the title to get_entry
    if page:
        page_converted = markdowner.convert(page)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page": page_converted
        })
    else:
        return render(request, "encyclopedia/404.html")
    
# end new view

def test(request):
    fucks = fuck_generator("can be anything. it just needs a string")
    return render(request, "encyclopedia/test.html", {'fucks': fucks})
