from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic


from agency.models import Topic, Redactor, Newspaper
from agency.forms import (
    NewspaperSearchForm,
    NewspaperForm,
    TopicSearchForm,
    RedactorForm,
    RedactorSearchForm,
)


def index(request):
    context = {
        "num_topics": Topic.objects.count(),
        "num_redactors": Redactor.objects.count(),
        "num_newspaper": Newspaper.objects.count(),
    }
    return render(request, "agency/index.html", context)


class TopicListView(generic.ListView):
    model = Topic
    queryset = Topic.objects.all()
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = TopicSearchForm(initial={"title": title})

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")

        if title:
            return self.queryset.filter(name__icontains=title)

        return self.queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency: topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 7
    queryset = Redactor.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        username = self.request.GET.get("username")

        if username:
            return self.queryset.filter(username__icontains=username)

        return self.queryset


class RedactorCreateView(generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("agency:index")
    form_class = RedactorForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
    form_class = RedactorForm


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class NewspapersListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.all()
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspapersListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewspaperSearchForm(initial={"title": title})

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")

        if title:
            return self.queryset.filter(title__icontains=title)

        return self.queryset


class NewspapersCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
