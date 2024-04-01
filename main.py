def main():
    templates = [
        """It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). 
    The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. 
    There are nurses here who have (Color) (Part of the Body). 
    If someone wants to come into my room I told them that they have to (Verb) first. 
    I’ve decorated my room with (Number2) (Noun2). 
    Today I talked to a doctor and they were wearing a (Noun3) on their (Part of the Body2). 
    I heard that all doctors (Verb) (Noun4) every day for breakfast. 
    The most (Adjective3) thing about being in the hospital is the (Silly Word) (Noun) !""",

        """This weekend I am going camping with (Proper Noun (Person’s Name)). 
    I packed my lantern, sleeping bag, and (Noun). 
    I am so (Adjective (Feeling)) to (Verb) in a tent. 
    I am (Adjective (Feeling2)) we might see a/an (Animal), I hear they’re kind of dangerous. 
    While we’re camping, we are going to hike, fish, and (Verb2).
    I have heard that the (Color) lake is great for (Verb (ending in ing)). 
    Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). 
    If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! 
    At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!""",

        """Dear (Proper Noun (Person’s Name)), I am writing to you from a (Adjective) castle in an enchanted forest. 
    I found myself here one day after going for a ride on a (Color) (Animal) in (Place). 
    There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural2)) here! 
    In the (Room in a House) there is a pool full of (Noun). 
    I fall asleep each night on a (Noun2) of (Noun (Plural3)) and dream of (Adjective4) (Noun (Plural4)). 
    It feels as though I have lived here for (Number) (Measure of time). 
    I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"""
    ]

    # Prompt user to choose a template
    print("Choose a template:")
    for i, template in enumerate(templates):
        print(f"{i + 1}. Template {i + 1}")

    # Handle user input using a try-except block
    while True:
        try:
            choice = int(input("Enter the template number (1, 2, or 3): ")) - 1
            if choice not in range(len(templates)):
                raise ValueError("Invalid template number")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Error: {e}")

    def generate_story():
        text = templates[choice]
        # Find placeholders in the text
        start_index = -1
        while True:
            start_index = text.find('(', start_index + 1)
            if start_index == -1:
                break
            end_index = text.find(')', start_index)
            if end_index == -1:
                break
            inner_start_index = text.find('(', start_index + 1)
            if start_index < inner_start_index < end_index:
                input_description = text[start_index + 1:end_index + 1].strip()
                user_input = input(f"Enter {input_description}: ")
                text = text.replace(text[start_index:end_index + 2], user_input, 1)
            else:
                input_description = text[start_index + 1:end_index].strip()
                user_input = input(f"Enter {input_description}: ")
                text = text.replace(text[start_index:end_index + 1], user_input, 1)
        return text

    story = generate_story()
    print(story)


main()
