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


class CharListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            chars = [v for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type):chars})
        return qs


class CallBoxFilter(django_filters.FilterSet):
    boxid = IntegerListFilter(name='id', lookup_type='in')

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


class LampFilter(django_filters.FilterSet):
    lampid = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Lamp
        fields = ['id', 'light_type', 'heads']


class LampCollection(generics.ListAPIView):
    queryset = models.Lamp.objects.all()
    serializer_class = serializers.LampSerializer
    filter_class = LampFilter


class SingleLampCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = models.Lamp.objects.all()
    serializer_class = serializers.LampSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ParkingLotFilter(django_filters.FilterSet):
    lotid = IntegerListFilter(name='id', lookup_type='in')
    lotname = CharListFilter(name='lot_name', lookup_type='in')

    class Meta:
        model = models.ParkingLot
        fields = ['id', 'lot_name', 'description']


class ParkingLotCollection(generics.ListAPIView):
    queryset = models.ParkingLot.objects.all()
    serializer_class = serializers.ParkingLotSerializer
    filter_class = ParkingLotFilter


class SingleParkingLotCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = models.ParkingLot.objects.all()
    serializer_class = serializers.ParkingLotSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

