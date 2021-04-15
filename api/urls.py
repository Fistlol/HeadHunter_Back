from django.urls import path
from api.views import companies_list, companies_detail, companies_vacancies, \
    vacancies_list, vacancies_detail, vacancies_top_ten

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', companies_detail),
    path('companies/<int:company_id>/vacancies/', companies_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancies_detail),
    path('vacancies/top_ten/', vacancies_top_ten),
]
