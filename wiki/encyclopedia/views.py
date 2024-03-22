from django.shortcuts import render

from markdown2 import Markdown

from . import util

#vars for converting md to html
markdowner = Markdown()
page = util.get_entry()
page_converted = markdowner.convert(page)
#end

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# start new view
def entry(request):
    return render(request, f"encyclopedia/index/{page}.html", {
        "page": page_converted
    })
# end new view