
with open("./Input/Names/invited_names.txt") as i_names:
    names = i_names.readlines()
    # print(names)


with open("./Input/Letters/starting_letter.txt") as s_letter:
    letter = s_letter.read()
    # print(letter)
    for name in names:
        stripped_name = name.strip()
        new_text = letter.replace("[name]", stripped_name)
        # print(new_text)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_text)
