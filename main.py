import os
import pygame
import requests
from random import choice
from scale import scope
from data import cities, kinds_of_map

running = True
static_map_server = "https://static-maps.yandex.ru/1.x/"
geo_server = "http://geocode-maps.yandex.ru/1.x/"

pygame.init()
screen = pygame.display.set_mode((600, 450))

pygame.display.flip()
clock = pygame.time.Clock()

map_file = "map.jpg"

while running:
    city = choice(cities)
    kind = choice(kinds_of_map)

    geo_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": city,
        "format": "json"
    }

    geo_response = requests.get(geo_server, params=geo_params)

    json_response = geo_response.json()
    geo_obj = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    geo_obj_coordinates = geo_obj["Point"]["pos"].split()

    delta_x, delta_y = scope(geo_obj)

    static_map_params = {
        "ll": ",".join(geo_obj_coordinates),
        "spn": ",".join([delta_x, delta_y]),
        "l": kind
    }

    static_map_response = requests.get(static_map_server, params=static_map_params)

    with open(map_file, "wb") as file:
        file.write(static_map_response.content)

    while pygame.event.wait().type != pygame.QUIT:
        screen.blit(pygame.image.load(map_file), (0, 0))
        clock.tick(24)
        pygame.display.flip()

    pygame.quit()

os.remove(map_file)
