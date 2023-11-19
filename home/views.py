from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import RoutePage, ExpeditionBlock


@require_POST
@csrf_exempt
def finish_route(request, route_id):
    try:
        route = RoutePage.objects.get(id=route_id)
        route.finished = True
        route.save()
        return JsonResponse({"status": "success"})
    except RoutePage.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Route not found"}, status=404)


@require_POST
@csrf_exempt
def complete_expedition(request, route_id, expedition_name):
    try:
        route = RoutePage.objects.get(id=route_id)
        for expedition in route.expeditions:
            print(expedition)
            if expedition.value["name"] == expedition_name:
                expedition.value["completed"] = True
                route.save()
                return JsonResponse({"status": "success"})
    except RoutePage.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Route not found"}, status=404)
    