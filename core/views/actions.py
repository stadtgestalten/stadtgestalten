from .. import forms
from django.forms import models as model_forms
from django.views.generic import (
        base as django_base, detail as django_detail, edit as django_edit)


class FormMixin(django_edit.FormMixin):
    def get_success_url(self):
        return self.related_object.get_absolute_url()


class ModelFormMixin(FormMixin, django_detail.SingleObjectMixin):
    def get_form_class(self):
        return model_forms.modelform_factory(
                self.model,
                fields=self.get_form_fields(),
                form=forms.ModelForm)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data_fields'] = self.get_data_fields()
        return kwargs

    def get_data_fields(self):
        return [field_class(self) for field_class in self.data_field_classes]

    def get_form_fields(self):
        return []


class BaseCreateView(ModelFormMixin, django_edit.BaseCreateView):
    def post(self, *args, **kwargs):
        self.related_object = self.get_related_object()
        return super().post(*args, **kwargs)


class TemplateResponseMixin(django_base.TemplateResponseMixin):
    def get_template_names(self):
        return ['stadt/form.html']
