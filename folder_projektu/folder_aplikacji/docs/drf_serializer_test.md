from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# tworzymy nowe obiekty

stanowisko = Stanowisko.objects.create(nazwa = "kierownik", opis = "Zarządza tymi co zarządzają.")
osoba = Osoba.objects.create(imie = "Jan", nazwisko = "Malinowski, plec = 2, stanowisko = stanowisko)

# inicjalizacja serializera dla Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# ('id': 6, 'imie': 'Jan', 'nazwisko': 'Malinowski', 'plec': 'Męzczyzna', 'stanowisko': stanowisko.id, 'data_dodania': osoba.data_dodania)

osoba_json = JSONRenderer().render(osoba_serializer.data)

# ('id': 6, 'imie': 'Jan', 'nazwisko': 'Malinowski', 'plec': 'Męzczyzna', 'stanowisko': 4, 'data_dodania': '2024-12-17')

import io

#   strumienie danych JSON
stream - io.BytesIO(osoba_json)

#   pasowanie JSON do słownika
data = JSONParser().parse(stream)

# tworzymy obiekt desrializers dla danych JSON
deserializer = OsobaSerializer(data = data)

# walidacaj danych
print(deserializer.is_valid())
print(deserializer.errors)

# True

# błędne dane
invalid_data = ('imie': 'Adam', 'nazwisko': 'Nowak', 'plec': Nieznany', 'stanowisko': stanowisko.id)
invalid_serializer = OosobaSerializer(data = invalid_data)
print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

# False
# {'plec': ['"Nieznany" is not a valid choice.']}

# zapis do Bazy Danych
if deserializer.is_valid():
    deserializer.save()

# inicjowanie serializera dla stanowiska
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# {'id': 1, 'nazwa': 'Kierownik', 'opis': 'Zarządza tymi co zarządzają.'}

# serializacja do JSON
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# {'id': 1, 'nazwa': 'Kierownik', 'opis': 'Zarządza tymi co zarządzają.'}

# deserializacja z JSON
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data = data)
print(deserializer.is_valid())

if desersalizer.is_valid():
    deserializer.saver()