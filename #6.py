"""
#6 ASPECT RATIO DE UNA IMAGEN   Difícil #5 2022
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""
import math
import requests
import io
from PIL import Image

# urls para probar el ejercicio
# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmHgoO8TQODKgB4vBjwJCXWw-5TvaWprcNHLk3RZo1iKrcPzEFpNWYIq0&s=10
# https://s3.amazonaws.com/rails-camp-tutorials/blog/programming+memes/works-doesnt-work.jpg
# https://b3666184.assetcdn.net/3666184/wp-content/uploads/2024/04/programming-memes-coding-memes-4-20240404.jpg?lossy=2&strip=1&webp=1

try:

    url = input('url: ')
    r = requests.get(url)
    bytes = r.content
    virtual_file = io.BytesIO(bytes)
    image = Image.open(virtual_file)
    width, height = image.size
    gcd = math.gcd(width, height)
    x = width // gcd
    y = height // gcd
    print(f"aspect ratio: {x}:{y}")

    st_decimal = width / height

    if st_decimal < 0.85:
        print("Vertical")
    elif st_decimal < 1.165:
        print("closest standar aspect ratio: 1:1")
    elif st_decimal < 1.385:
        print("closest standar aspect ratio: 4:3")
    elif st_decimal < 2:
        print("closest standar aspect ratio: 16:9")
    else:
        print("closest standar aspect ratio: 21:9")

except Exception as e:
    print(f"Could not process the image from the URL: {e}")