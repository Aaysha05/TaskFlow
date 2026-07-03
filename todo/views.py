from django.shortcuts import render, redirect,  get_object_or_404
from .models import Task

def home(request):

    if request.method == "POST":

        Task.objects.create(

            title=request.POST.get("title"),

            priority=request.POST.get("priority"),

            due_date=request.POST.get("due_date")

        )

        return redirect("/?dashboard=true")

    search = request.GET.get("search")

    if search:
        tasks = Task.objects.filter(title__icontains=search)
    else:
        tasks = Task.objects.all()

    completed_count = tasks.filter(completed=True).count()
    pending_count = tasks.filter(completed=False).count()

    edit_id = request.GET.get("edit")
    edit_task = None

    if edit_id:
        edit_task = get_object_or_404(Task, id=edit_id)

    return render(request, "home.html", {
        "tasks": tasks,
        "edit_task": edit_task,
        "completed_count": completed_count,
        "pending_count": pending_count,
        "search": search,
    })

def delete_task(request, id):

    task = get_object_or_404(Task, id=id)

    task.delete()

    return redirect("/?dashboard=true")

def complete_task(request, id):

    task = get_object_or_404(Task, id=id)

    task.completed = True

    task.save()

    return redirect("/?dashboard=true")

def edit_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":

        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.due_date = request.POST.get("due_date")

        task.save()

        return redirect("/?dashboard=true")

    return render(request, "edit.html", {"task": task})