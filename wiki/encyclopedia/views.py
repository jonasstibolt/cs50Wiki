from django.shortcuts import render

from markdown2 import Markdown

from . import util
from .util import fuck_generator


# #vars for converting md to html
# markdowner = Markdown()
# page = util.get_entry()
# page_converted = markdowner.convert(page)
#end

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# # start new view (maybe title instead of page?)
# def entry(request):
#     return render(request, f"encyclopedia/index/{page}.html", {
#         "page": page_converted
#     })
# # end new view

def test(request):
    fucks = fuck_generator("can be anything. it just needs a string")
    return render(request, "encyclopedia/test.html", {'fucks': fucks})