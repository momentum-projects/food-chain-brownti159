def lyrics():
    #animal_1 = "spider"
    #animal_2 = "bird"
    #animal_3 = "cat"
    #animal_4 = "dog"
    #animal_5 = "goat"
    #animal_6 = "cow"
    #animal_7 = "horse"
    animals = ["spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    verse_1 = "I know an old lady who swallowed a"
    verse_2 = "I don't know why she swallowed the fly. Perhaps she will die."

    for animal in animals: 
        # print(f'I know an old lady who swallowed a {animal}. Perhaps she will die.')
        # print(f'{verse} {animal}. Perhaps she will die' )
        if animal == "spider":
            print(f'{verse_1} {animal}. That wriggled and jiggled and tickled inside her.')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the fly. {verse_2}')
        elif animal == "bird":
            print(f'{verse_1} {animal}. How absurd to swallow a bird!')
            print(f'She swallowed the {animal} to cathch the {animals[animals.index(animal)-1]}.')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the fly. {verse_2}')
            # print(animals[animals.index(animal)-1])
        elif animal == "cat":
            print(f'{verse_1} {animal}. Imagine that, to swallow a cat!')
            print(f'She swallowed the {animal} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)-3]} to cathch the {animals[animals.index(animal)-2]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the fly.{verse_2}')
            # print(animals[animals.index(animal)-1])
        elif animal == "dog":
            print(f'{verse_1} {animal}. What a hog, to swallow a dog!')
            print(f'She swallowed the {animal} to cathch the {animals[animals.index(animal)+2]}')
            print(f'She swallowed the {animals[animals.index(animal)+2]} to cathch the {animals[animals.index(animal)+1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the fly.{verse_2}')
        elif animal == "goat":
            print(f'{verse_1} {animal}. Just opened her throat and swallowed a goat!')
            print(f'She swallowed the {animal} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the fly.{verse_2}')
            # print(f'She swallowed the {animals[animals.index(animal)-2]} to cathch the {animals[animals.index(animal)+3]}')
            # print(f'She swallowed the {animals[animals.index(animal)+4]} to cathch the {animals[animals.index(animal)+3]}')
            
        elif animal == "cow":
            print(f"{verse_1} {animal}. I don't know how she swallowed a cow! ")
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)+2]} to cathch the {animals[animals.index(animal)+1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the {animals[animals.index(animal)-1]}')
            print(f'She swallowed the {animals[animals.index(animal)]} to cathch the fly.{verse_2}')
            # print(f'She swallowed the {animals[animals.index(animal)+5]} to cathch the {animals[animals.index(animal)+4]}')
        
        elif animal == "horse":
            print(f"{verse_1} {animal}. She's dead, of course!")
        


lyrics()               
    #while still going through the list of animals repeat "I don't know why she swallowed the fly. Perhaps she'll die."
     
    