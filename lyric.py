def lyrics():
    #animal_1 = "spider"
    #animal_2 = "bird"
    #animal_3 = "cat"
    #animal_4 = "dog"
    #animal_5 = "goat"
    #animal_6 = "cow"
    #animal_7 = "horse"
    animals = ["spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    verse = "I know an old lady who swallowed a"
    for animal in animals: 
        # print(f'I know an old lady who swallowed a {animal}. Perhaps she will die.')
        print(f'{verse} {animal}. Perhaps she will die' )
        if animal == "spider":
            return print(f'{verse} {animal}. That wriggled and jiggled and tickled inside her.')
        # else animal == "bird":
        #     return print(f'{animal}. How absurd to swallow a bird!')
        # elif animall == "cat":
        #     return f'{animal}. Imagine that, to swallow a cat!'
        # elif animal == "dog":
        #     return f'{animal}. What a hog, to swallow a dog!'
        # elif animal == "goat":
        #     return f'{animal}. Just opened her throat and swallowed a goat!'
        # elif animal == "cow":
        #     return f'{animal' I dont know how she swallowed a cow!'
        else:
            return "She's dead, of course!"
    


lyrics()               
    #while still going through the list of animals repeat "I don't know why she swallowed the fly. Perhaps she'll die."
     
    