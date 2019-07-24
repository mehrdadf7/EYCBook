from django.conf import settings

from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'bio'

urlpatterns = [
    path('image_upload/'                   , views.fav_image_view, name = 'image_upload'),
    path('success/'                        , views.success, name = 'success'),
    path('get_favorite_equipment_images/'  , views.display_fav_equ_images),
    path('get_favorite_equipment/'         , views.APIListFavoriteEquipment.as_view()),
    path('get_categories/'                 , views.APIListEquipmentCategory.as_view()),
    path('get_equipments/'                 , views.APIListEquipment.as_view()),
    path('get_equipments_useful/'          , views.APIListEquipmentUseful.as_view()),
    path('get_equipments_info/'            , views.APIListEquipmentInfo.as_view()),
    path('get_magazines/'                  , views.APIListMagazine.as_view()),
    path('get_magazine_info/'              , views.APIListMagazineInfo.as_view()),
    path('get_equipment/'                  , views.APIEquipmentDetail.as_view()),
    path('get_equipment_useful/'           , views.APIEquipmentUsefulDetail.as_view()),
    path('get_category/'                   , views.APICategoryDetail.as_view()),
    path('search/'                         , views.APISearchEquipment.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
