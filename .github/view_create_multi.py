# views.py
def create_multi_genere_book(request, method="GET"):
    generes = Genere.objects.all()

    if request.method == "POST":
        print(request.POST)
        data = request.POST
        list_generes = data.getlist("genere[]", [])
        list_number_books = data.getlist("book_number[]", [])

        if len(list_generes) and len(list_number_books):
            list_genere_books = []
            i = 0

            for ind in range(0, len(list_generes)):
                list_genere_books.append(
                    __new_genere_book(
                        genere_id=int(list_generes[ind]),
                        number_book=int(list_number_books[ind]),
                    )
                )
            GenegeBook.objects.bulk_create(list_genere_books)

            return redirect("list_books")

    return render(
        request, "books/_partial_book_genere.html", context={"generes": generes}
    )

 # urls.py
from django.urls import path

from management import views

urlpatterns = [
    path(
        "books/create-multi-genere-book",
        views.create_multi_genere_book,
        name="create_multi_genere_book",
    ),
]
