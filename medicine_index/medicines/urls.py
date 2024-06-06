from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, CustomTokenObtainPairView, insert_medicine, update_medicine, delete_medicine, fetch_all_medicines, fetch_medicine_by_id, search_medicines
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('insert/', insert_medicine, name='insert_medicine'),
    path('update/<int:pk>/', update_medicine, name='update_medicine'),
    path('delete/<int:pk>/', delete_medicine, name='delete_medicine'),
    path('fetch_all/', fetch_all_medicines, name='fetch_all_medicines'),
    path('fetch/<int:pk>/', fetch_medicine_by_id, name='fetch_medicine_by_id'),
    path('search/<str:query>/', search_medicines, name='search_medicines'),
]
