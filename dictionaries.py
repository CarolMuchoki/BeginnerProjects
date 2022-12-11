greeting = input('>')
words = greeting.split(' ')
emojis = {
    ':)': '😊',
    ':(': '😐'
}
output = ""
for word in words:
    output += emojis.get(word, word) + ' '
print(output)
