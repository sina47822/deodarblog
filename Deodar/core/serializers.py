from rest_framework import serializers
from .models import MainMenu , SubMenu

class MainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenu
        fields = ['title', 'link', 'id']

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ['title', 'link' , 'id' , 'main_menu']

    def get_submenus(self, obj):
        submenus = SubMenu.objects.filter(main_menu=obj)
        # Assuming SubMenuSerializer exists and serializes SubMenu instances
        serializer = SubMenuSerializer(submenus, many=True)
