from django.urls import path


from ..forms import AdvancedSearchForm
from ..views.snippets import autocomplete, advanced_search,basic_search


urlpatterns = [
    path('', basic_search, name='cab_search'),
    path('autocomplete/', autocomplete, name='snippet_autocomplete'),
    path('advanced/', advanced_search, name='cab_search_advanced'),
]
