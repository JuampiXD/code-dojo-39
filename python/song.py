ORIGINAL_ANIMALS_OF_THE_SONG = [
    'fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse']


class Song:
    first_verse_of_the_song = "There was an old lady who swallowed a {}."
    first_verse = "There was an old lady who swallowed a {};"
    first_middle_verse = "She swallowed the {} to catch the {},"
    middle_verse = "She swallowed the {} to catch the {};"
    last_verse = "I don't know why she swallowed a {} - perhaps she'll die!"
    final_verse_of_the_song = "There was an old lady who swallowed a {}...\n...She's dead, of course!"
    funny_verses = [
        'That wriggled and wiggled and tickled inside her.',
        'How absurd to swallow a {}.',
        'Fancy that to swallow a {}!',
        'What a hog, to swallow a {}!',
        "I don't know how she swallowed a {}!",
    ]

    def __init__(self, animals_for_song):
        if not animals_for_song:
            self.animals_for_song = ORIGINAL_ANIMALS_OF_THE_SONG
        else:
            self.animals_for_song = animals_for_song

    def adapt_original_lyrics(self):
        if len(self.animals_for_song) == 1:
            return self.final_verse_of_the_song.format(self.animals_for_song[0])
        else:
            return self.WritingSong()

    def WritingSong(self):
        creating_song = ""
        funny_verse_position = 0
        # Generando la cancion
        for position, animal in enumerate(self.animals_for_song):
            # Verifiacacion si es el primer animal dentro la iteracion, se genera el primer verso
            if position == 0:
                creating_song += self.first_verse_of_the_song.format(animal) + "\n" + self.last_verse.format(animal)
            # Verificando si el ultimo animal dentro de la iteracion, se genera el ultimo verso
            elif position == len(self.animals_for_song) - 1:
                creating_song += "\n\n" + \
                    self.final_verse_of_the_song.format(animal)
            # Se genera el resto de versos
            else:
                # Verificando si es el ultimo funny_verses para resetear
                creating_song += "\n\n" + self.first_verse.format(animal)
                # Verificando si es el primer funny_verses (no lleva un animal en el verso)
                if funny_verse_position == 0:
                    creating_song += "\n" + \
                        self.funny_verses[funny_verse_position]
                # El resto de los funny_verses tienen animales en el verso
                else:
                    creating_song += "\n" + \
                        self.funny_verses[funny_verse_position].format(animal)
                # Creacion de versos a partir del 3er parrafo
                creating_song = self.Write_midles(position, creating_song, animal)
                creating_song += "\n" + self.last_verse.format(self.animals_for_song[0])
                if funny_verse_position == len(self.funny_verses) - 1:
                    funny_verse_position = 0
                else:
                    funny_verse_position += 1
        return creating_song

    def Write_midles(self, position, creating_song, animal):
             # creacion de variable usada en while
        amount_of_animals_for_use_in_middle_verse = position
        while amount_of_animals_for_use_in_middle_verse > 0:
            if amount_of_animals_for_use_in_middle_verse > 1:
                creating_song += "\n" + self.first_middle_verse.format(self.animals_for_song[amount_of_animals_for_use_in_middle_verse],self.animals_for_song[amount_of_animals_for_use_in_middle_verse - 1])
            # Se inserta el penultimo verso a diferencia de los demas tiene ";"
            else:
                creating_song += "\n" + self.middle_verse.format(self.animals_for_song[amount_of_animals_for_use_in_middle_verse],self.animals_for_song[amount_of_animals_for_use_in_middle_verse - 1])
            # Reduccion de la variable para usar todos los animales desde la posicion actual hasta el primer animal
            amount_of_animals_for_use_in_middle_verse -= 1
        return creating_song


class Singer:
    def __init__(self):
        self.animals_for_song = []

    def choose_animals_for_song(self, animals_for_song):
        self.animals_for_song = animals_for_song

    def sing(self):
        return Song(self.animals_for_song).adapt_original_lyrics()


singer = Singer()
# singer.choose_animals_for_song(['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse'])
# singer.choose_animals_for_song(['fly'])
# singer.choose_animals_for_song(['fly', 'spider', 'bird', 'cat', 'dog', 'cow', 'horse', 'monkey'])
singer.choose_animals_for_song(
    ['perezoso', 'cucharacha', 'bb8', 'doraemon', 'marvinelmarciano', 'luisitocomunicia', 'messi', 'ibai'])
print(singer.sing())
