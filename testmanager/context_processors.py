from .forms import newScenario, newComment

def include_modal_context_processor(request):
    return {'newScenario': newScenario(request.POST or None)}

def include_comment_context_processor(request):
    return {'newComment': newComment(request.POST or None)}
