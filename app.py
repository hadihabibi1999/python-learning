# python

emojies = {
    ";D": "😁",
    ":)": "😂"
}
words = input('>enter: ').split()
out = ''
for word in words:
    out += emojies.get(word, word)+' '
print(f'>{out}')
