note = [1000, 500, 100, 50, 10, 5, 2, 1]


def calculate_notes(amount, notes):
    tot_notes = 0
    if amount == 0:
        return False
    else:
        for note_index in range(len(notes)):
            if amount >= notes[note_index]:
                no_of_notes = amount // notes[note_index]
                rem = amount % notes[note_index]
                # no_of_notes, rem = divmod(amount, notes[note_index])
                amount = rem
                tot_notes += no_of_notes
                print(f"There are {no_of_notes} : {notes[note_index]} rs notes")
            else:
                continue
        return tot_notes


cash = int(input("Enter the amount here : "))
total_notes = calculate_notes(cash, note)
print("Minimum number of notes needed to given as change:", total_notes)
