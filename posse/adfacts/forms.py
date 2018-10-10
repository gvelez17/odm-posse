from .models import Ad, Org
from django.forms import ModelForm, ChoiceField
from simple_search import search_form_factory

#AdSearchForm = search_form_factory(Ad.objects.all(),
#                   ['title', 'race', 'district', 'candidate_or_initiative', 'support_oppose', 'format'])

class AdSearchForm(ModelForm):
    class Meta:
        model = Ad
        #fields = ['race', 'format']
        fields = ['race', 'candidate_or_initiative', 'support_oppose']

    def __init__(self, *args, **kwargs):
        super(AdSearchForm, self).__init__(*args, **kwargs)
        ads_for = list(set([ad.candidate_or_initiative for ad in Ad.objects.all()]))
        options = [('','')] + [(ad_name, ad_name) for ad_name in ads_for]

        self.fields['candidate_or_initiative'] = ChoiceField(
               choices = options
        )
        self.fields['candidate_or_initiative'].required = False
        self.fields['race'].required = False
