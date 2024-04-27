from django.shortcuts import render
from .models import  MainMenu , SubMenu

from .serializers import MainMenuSerializer ,SubMenuSerializer
from django.db.models import Avg, Count, Min , Sum



def index(request):

    main_menu_items = MainMenu.objects.all()
    sub_menu_items =SubMenu.objects.all()

    main_menu_serializer = MainMenuSerializer(main_menu_items , many=True)
    submenu_serializer = SubMenuSerializer (sub_menu_items , many=True)

    return render(request, 'core/base.html', {
        'main_menu' : main_menu_serializer.data,
        'submenu' : submenu_serializer.data
    })