class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork


my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

# These print statements should throw errors
# print(my_artist.name)
# print(my_artist.medium)
# print(my_artist.style)
# print(my_artist.famous_artwork)

#Syntax is object_name + . +_Class_name + attribute_name
print(my_artist._Artist__name)
print(my_artist._Artist__medium)
print(my_artist._Artist__style)
print(my_artist._Artist__famous_artwork)