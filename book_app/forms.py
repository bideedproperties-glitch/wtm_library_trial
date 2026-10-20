from django import forms
from .models import Book, BookRequest


class CreateBookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(
            format="%Y-%m-%d", attrs={"type": "date", "format": "%Y-%m-%d"}
        )
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "isbn",
            "author",
            "genre",
            "published_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data = ["title", "isbn","genre"]
        for i in data:
            self.fields[i].widget.attrs.update(
                {
                    "type":"text",
                    "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                }
            )
        self.fields["author"].widget.attrs.update(
                {
                    "type":"text",
                    "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                }
            )
        self.fields["published_date"].widget=forms.DateInput(attrs=
                {
                    "type":"date",
                    "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                }
            )

    def clean_title(self):
        cleaned_title = self.cleaned_data.get("title")
        proper_title = cleaned_title.title()  # Remove leading and trailing whitespace
        # check if the title already exists in the database
        if Book.objects.filter(title=proper_title).exists():
            raise forms.ValidationError(
                "This title already exists in the database, please choose a different title."
            )

        return proper_title


class UpdateBookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(
            format="%Y-%m-%d", attrs={"type": "date", "format": "%Y-%m-%d"}
        )
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "isbn",
            "author",
            "genre",
            "published_date",
            "status"
        ]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        fields= [
            "title","isbn","author","genre","status"
        ]
        for data in fields:
            self.fields[data].widget.attrs.update(
                {
                    "type":"text", "name":"author", 
                    "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all"
                }
            )
        self.fields['published_date'].widget=forms.DateInput(
            {
                "type":"date",
                "class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl outline-none focus:ring-2 focus:ring-indigo-500"
            }
        )


class ChangeBookStatusForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["status"]


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ["book", "book_date_request", "book_date_return"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["book"].queryset = Book.objects.filter(status="av")

        self.fields["book"].widget.attrs.update(
                        {
                            "type":"text", "name":"author", 
                            "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all"
                        }
                    )
        date = ["book_date_request", "book_date_return"]
        for i in date:
            self.fields[i].widget=forms.DateInput(
                        {
                        "type":"date",
                          "class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl outline-none focus:ring-2 focus:ring-indigo-500"
                        }
                    )

    def clean(self):
        cleaned_data = super().clean()
        request_date = cleaned_data.get("book_date_request")
        return_date = cleaned_data.get("book_date_return")
        if request_date and return_date:
            if return_date < request_date:
                raise forms.ValidationError(
                    {
                        "book_date_return": (
                            "The return date can not be earlier than the request date"
                        )
                    }
                )
        return cleaned_data
        # self.fields["book_date_request"].widget=forms.DateInput(
        #         attrs={
        #             "type":"date",
        #             "format": "%Y-%m-%d"
        #         }
        #     )
        # self.fields["book_date_return"].widget=forms.DateInput(
        #         attrs={
        #             "type":"date",
        #             "format": "%Y-%m-%d"
        #         }
        #     )
