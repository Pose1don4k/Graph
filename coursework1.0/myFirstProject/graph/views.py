from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Graph
import matplotlib.pyplot as plt
import io
from django.contrib.auth import logout
from .forms import GraphForm
import math
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def render_graph_image(request, id):
    graph = get_object_or_404(Graph, id=id)

    x = [i / 10 for i in range(-10 * graph.scale, 10 * graph.scale + 1)]

    if graph.graph_type == 'parabola':
        y = [i ** 2 for i in x]
    elif graph.graph_type == 'exponent':
        y = [math.exp(i) for i in x]
    elif graph.graph_type == 'abs':
        y = [abs(i) for i in x]
    else:
        y = [0 for _ in x]

    fig, ax = plt.subplots()
    ax.plot(x, y, color=graph.color, linewidth=graph.thickness)
    ax.set_title(graph.title)
    ax.grid(True)

    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    return HttpResponse(buffer.read(), content_type='image/png')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return HttpResponseForbidden("Неверный метод выхода.")


def index(request):
    return render(request, 'myFirstProject/index.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def show_graph(request, id):
    graph = get_object_or_404(Graph, id=id)
    source = request.GET.get('source', 'all')
    if source == 'mine':
        back_url = 'my_graphs'
    else:
        back_url = 'graph_list'
    return render(request, 'graph/show_graph.html', {
        'graph': graph,
        'back_url': back_url
    })


def graph_list(request):
    if not request.user.is_authenticated:
        graphs = Graph.objects.all()
    else:
        graphs = Graph.objects.all()
    return render(request, 'graph/list.html', {'graphs': graphs})

def plot_view(request):
    return render(request, 'myFirstProject/plot.html')

def plot_image(request):
    func = request.GET.get("func", "x**2")
    try:
        x = [i / 10 for i in range(-100, 100)]
        y = [eval(func, {"x": i, "__builtins__": {}}) for i in x]
        plt.figure()
        plt.plot(x, y)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return HttpResponse(buf.read(), content_type='image/png')
    except Exception as e:
        return HttpResponse(f"Ошибка: {str(e)}", content_type='text/plain')

@login_required
def delete_graph(request, id):
    graph = get_object_or_404(Graph, id=id)
    if request.user == graph.user or request.user.is_superuser:
        graph.delete()
        return redirect('graph_list')
    return HttpResponseForbidden("Нет доступа.")


@login_required
def create_graph(request):
    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            graph = form.save(commit=False)
            graph.user = request.user
            graph.save()
            return redirect('graph_list')
    else:
        form = GraphForm()
    return render(request, 'graph/create.html', {'form': form})

@login_required
def my_graphs(request):
    graphs = Graph.objects.filter(user=request.user)
    return render(request, 'graph/my_graphs.html', {'graphs': graphs})
