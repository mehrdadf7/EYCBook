from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from .forms import *
from .serializers import *
from rest_framework import filters

def fav_image_view(request):
    if request.method == 'POST':
        form = FavoriteEquipmentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FavoriteEquipmentForm()
    return render(request, 'fav_equ.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def display_fav_equ_images(request):
    if request.method == 'GET':
        images = FavoriteEquipment.objects.all()
        return render(request, 'display_fav_equ_images.html', {'fav_equ_images': images})


def error_message(message):
    return {
        "error": True,
        "errors": [
            {
                "message": '%s Not Found' % (message),
                "code": status.HTTP_404_NOT_FOUND
            }
        ]
    }


class APIListFavoriteEquipment(APIView):
    def get(self, request, format=None):
        queryset = FavoriteEquipment.objects.last()
        serializer = FavoriteEquipmentSerializer(queryset, many=False)
        return Response(serializer.data)


class APIListMagazineInfo(APIView):
    def get(self, request, format=None):
        queryset = MagazineInfo.objects.all()
        serializer = MagazineInfoSerializer(queryset, many=True)
        return Response({'magazines_info': serializer.data})


class APIListEquipmentCategory(APIView):

    def get_object(self, order):
        try:
            return EquipmentCategory.objects.all().order_by(order)
        except:
            raise CustomAPIException(error_message('Category'), status_code=status.HTTP_404_NOT_FOUND)

    def get(self, request, format=None):
        order = request.GET.get('order', '')
        categories = self.get_object(order)
        serializer = EquipmentCategorySerializer(categories, many=True)
        return Response(serializer.data)


class SmallPagesPagination(PageNumberPagination):
    page_size = 10


class IdsInFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        ids = request.QUERY_PARAMS.get('ids')
        if ids:
            ids = ids.split(",")
            return queryset.filter(id__in=ids)
        return queryset


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class APISearchEquipment(generics.ListCreateAPIView):
    model = Equipment
    serializer_class = EquipmentSerializer(model)

    def get_queryset(self):
        name          = self.request.query_params.get("name")
        # description   = self.kwargs['description']
        # category_name = self.kwargs['category_name']
        queryset = Equipment.objects.all()

        if name:
            self.queryset.filter(
                Q(name__contains=name)
                # |
                # Q(description__contains=description)
                # |
                # Q(category__name__contains=category_name)
            )
        # queryset = queryset.filter(name__contains=name)

        return queryset


class APIListEquipment(generics.ListCreateAPIView):
    # page = LimitOffsetPagination()
    # paginated_result = page.paginate_queryset(equipments, request)
    # search_fields = ['name', 'description', 'category__name']
    pagination_class = SmallPagesPagination
    filter_backends = (DynamicSearchFilter,)
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class APIListEquipmentInfo(generics.ListCreateAPIView):
    queryset = EquipmentInfo.objects.all()
    serializer_class = EquipmentInfoSerializer



class APIEquipmentDetail(APIView):
    # pagination_class = SmallPagesPagination

    def get_object(self, pk):
        try:
            return Equipment.objects.get(pk=pk)
        except:
            raise CustomAPIException(error_message('Equipment'), status_code=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        equipment_id = request.GET.get('id', '')
        equipment = self.get_object(equipment_id)
        serializer = EquipmentSerializer(equipment, many=False)
        return Response(serializer.data)


class APIEquipmentUsefulDetail(APIView):
    # pagination_class = SmallPagesPagination

    def get_object(self, pk):
        try:
            return EquipmentUseful.objects.get(id=pk)
        except:
            raise CustomAPIException(error_message('EquipmentUseful'), status_code=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        equipment_id = request.GET.get('id', '')
        equipment = self.get_object(equipment_id)
        serializer = EquipmentUsefulSerializer(equipment, many=False)
        return Response(serializer.data)


class CustomAPIException(ValidationError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'error'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code

class APICategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return EquipmentCategory.objects.get(pk=pk)
        except:
            raise CustomAPIException(error_message('Category'), status_code=status.HTTP_404_NOT_FOUND)

    def get(self, request, format=None):
        category_id = request.GET.get('id', '')
        category = self.get_object(pk=category_id)
        serializer = EquipmentCategorySerializer(category)
        return Response(serializer.data)


class APIEquipment(APIView):
    def get(self, request, format=None):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data)

class APIListEquipmentUseful(generics.ListCreateAPIView):
    pagination_class = SmallPagesPagination
    queryset = EquipmentUseful.objects.all()
    serializer_class = EquipmentSerializer



class APIListMagazine(APIView):
    def get(self, request, format=None):
        equipments = Magazine.objects.all()
        serializer = MagazineSerializer(equipments, many=True)
        return Response(serializer.data)

