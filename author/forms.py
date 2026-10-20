from django import forms
from .models import Author

class CreateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "dob",
            "year_of_death",
        ]

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            data = ["first_name", "last_name"]
            for i in data:
                self.fields[i].widget.attrs.update(
                    {
                        "type":"text",
                        "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                    }
                )
            date = ["dob", "year_of_death"]
            for i in date:
                self.fields[i].widget=forms.DateInput(attrs=
                        {
                            "type":"date",
                            "class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl outline-none focus:ring-2 focus:ring-indigo-500"
                        }
                    )

class UpdateAuthorEntry(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "dob",
            "year_of_death",
        ]

    def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                data = ["first_name", "last_name"]
                for i in data:
                    self.fields[i].widget.attrs.update(
                        {
                            "type":"text",
                            "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                        }
                    )
                date = ["dob", "year_of_death"]
                for i in date:
                    self.fields[i].widget.attrs.update(
                            {   
                                "type":"date",
                                "class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl outline-none focus:ring-2 focus:ring-indigo-500"
                            }
                        )