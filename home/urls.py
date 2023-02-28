from django.urls import path, include



from . import views



urlpatterns = (
    # urls for Races
    path('', views.RacesListView.as_view(), name='home_races_list'),
    path('races/detail/<int:pk>/', views.RacesDetailView.as_view(), name='home_races_detail'),
)

urlpatterns += (
    # urls for events
    path('home/events/detail/<int:pk>/', views.eventsDetailView.as_view(), name='home_events_detail'),
)

urlpatterns += (
    path('home/circuit/detail/<int:pk>/', views.CircuitDetailView.as_view(), name='home_circuit_detail'),
)

