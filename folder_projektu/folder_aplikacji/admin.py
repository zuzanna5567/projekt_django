from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

admin.site.register(Team)
class PersonAdmin(admin.ModelAdmin):
    # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
    list_display = ['name', 'shirt_size', 'team']
    list_filter = ['team']

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Person, PersonAdmin)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "opis"]
    list_filter = ['nazwa']

admin.site.register(Stanowisko, StanowiskoAdmin)
class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description="Stanowisko (ID)")
    def stanowisko_with_id(self, obj):
        if obj.stanowisko:
            return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
        return "Brak stanowiska"

    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_with_id', 'data_dodania']
    list_filter = ["stanowisko", "data_dodania"]
admin.site.register(Osoba, OsobaAdmin)