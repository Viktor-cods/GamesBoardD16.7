from django.filters import FilterSet, ModelMultipleChoiceFilter


from .models import Article


class CommentFilter(FilterSet):
    # Для организации поиска по объявлениям
    post = ModelMultipleChoiceFilter(
        field_name='post',
        queryset=Article.objects.all(),
        label='Объявления',
        conjoined=False,  # поиск по принципу ИЛИ
    )