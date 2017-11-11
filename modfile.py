import webbrowser

i=0
with open('inputs/flats.txt', 'r') as f:
    for line in f:
        i += 1
        webbrowser.open(line)
        if i > 5:
            break
