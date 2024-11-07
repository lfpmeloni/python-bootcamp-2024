from django.shortcuts import render # type: ignore

from .models import Topic

# Create your views here.

def index(request):
    """
    The home page for learning_log app

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """
    Show a single topic and all its entries

    Args:
        request (_type_): _description_
        topic_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
