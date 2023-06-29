from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Blog, Version


def index(request):
    """Главная страница, выводит четыре товара"""
    context = {
        'product_list': Product.objects.all()[:2],
        'title': "Главная"
    }
    return render(request, 'catalog/index.html', context)

class ProductsListView(generic.ListView):
    """Полный список товара"""
    model = Product
    extra_context = {
        'title': "Товар"
    }

    def get_queryset(self):
        """Выводит активную версию товара models class Version(ForeignKey-Product),
        отображается в inc_catalog_card.html"""
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('version_set')
        return queryset

class ProductsDetailView(generic.DetailView):
    """Карточка товара"""
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

class ProductsCreateView(generic.CreateView):
    """Класс контроллер создания товара"""
    model = Product
    form_class = ProductForm
    #fields = ('name', 'description', 'image', 'category', 'price', 'creation_at', 'modified_at',)
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'catalog/product_form.html'

class ProductsUpdateView(generic.UpdateView):
    """Класс контроллер редактирования товара"""
    model = Product
    form_class = ProductForm
    #fields = ('name', 'description', 'image', 'category', 'price', 'creation_at', 'modified_at',)
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'catalog/product_form_with_formset.html'


    def get_context_data(self, **kwargs):
        """Возвращает формсет для работы со связанными через внешний ключ объектами"""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Сохранение формсета, форм валид принимает пост запрос от get_context_data(сверху),
        сохраняем редактирование продукта """
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class ProductsDeleteView(generic.DeleteView):
    """Класс контроллер удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')








#_____________________________класс BLOG____________________________________________
class BlogListView(generic.ListView):
    """Полный список статей"""
    model = Blog
    extra_context = {
        'title': 'Статьи'
    }

    # метод отвечающий за положительный признак публикации
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication=True)
        return queryset

class BlogDetailView(generic.DetailView):
    """Карточка статьи"""
    model = Blog

    #метод отображения object, title
    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

    def get(self, *args, **kwargs):
        """счетчик просмотров"""
        self.object = self.get_object()
        self.object.number_views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class BlogCreateView(generic.CreateView):
    """Класс создания новой статьи"""
    model = Blog
    fields = ('name', 'content', 'creation_at', 'image',)
    success_url = reverse_lazy('catalog:blog_list')



class BlogUpdateView(generic.UpdateView):
    """Класс создания новой статьи"""
    model = Blog
    fields = ('image', 'name', 'content', 'creation_at',)
    success_url = reverse_lazy('catalog:blog_list')

def get_success_url(self):
    return self.object.get_absolute_url()


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


def toggle_activity(request, pk):
    '''Метод деактивация статьи'''
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.publication:
        blog_item.publication = False
    else:
        blog_item.publication = True

    blog_item.save()

    return redirect(reverse('catalog:blog_item', args=[blog_item.pk]))




def contacts(request):
    """Страница с контактами"""
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Пользователь {name} оставил контактный телефон {phone} и сообщение: {message}')

    context = {
        'title': "Контакты"
    }
    return render(request, 'catalog/contacts.html', context)


