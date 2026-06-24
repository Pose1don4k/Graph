from django.urls import path
from . import views

urlpatterns = [
    path('', views.graph_list, name='graph_list'),
    path('plot/', views.plot_view, name='plot'),
    path('plot/image/', views.plot_image, name='plot_image'),
    path('delete/<int:id>/', views.delete_graph, name='delete_graph'),
    path('graphs/create/', views.create_graph, name='create_graph'),
    path('graphs/mine/', views.my_graphs, name='my_graphs'),
    path('show/<int:id>/', views.show_graph, name='show_graph'),
    path('image/<int:id>/', views.render_graph_image, name='render_graph_image'),
]
