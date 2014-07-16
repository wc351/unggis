from rest_framework import generics
from rest_framework import mixins
from geoapi import models
from geoapi import serializers
import django_filters


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type):integers})
        return qs


class CallBoxFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.CallBox
        fields = ['id', 'description',]


class CallBoxCollection(generics.ListAPIView):
    queryset = models.CallBox.objects.all()
    serializer_class = serializers.CBSerializer
    filter_class = CallBoxFilter


class SingleCallBoxCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = models.CallBox.objects.all()
    serializer_class = serializers.CBSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)