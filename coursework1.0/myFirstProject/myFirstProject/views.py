from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from django.contrib.auth.decorators import login_required
from myFirstProject.graph.models import Graph


def index(request):
    return render(request, 'myFirstProject/index.html')

def plot_view(request):
    color = request.GET.get('color', 'blue')
    thickness = int(request.GET.get('thickness', 2))
    scale = int(request.GET.get('scale', 10))
    return render(request, 'myFirstProject/plot.html', {
        'color': color,
        'thickness': thickness,
        'scale': scale,
    })

def plot_image(request):
    color = request.GET.get('color', 'blue')
    thickness = int(request.GET.get('thickness', 2))
    scale = int(request.GET.get('scale', 10))

    x = np.linspace(-scale, scale, 500)
    y = x ** 2

    fig, ax = plt.subplots()
    ax.plot(x, y, color=color, linewidth=thickness)
    ax.set_title("y = x²")
    ax.grid(True)

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    return HttpResponse(buffer.read(), content_type='image/png')

@login_required
def my_graphs(request):
    graphs = Graph.objects.filter(user=request.user)
    return render(request, 'graph/my_graphs.html', {'graphs': graphs})
