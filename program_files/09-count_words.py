from operator import itemgetter

text = open('../files/desolation_row.txt', 'r').read()
text = text.lower()

# punctuation = """!-,'".?;"""
# no_punc = ''
#
# for word in text:
#     if word not in punctuation:
#         revised = word + no_punc
#         # print(revised, end="")

punctuation = [".", "!", "?", ";", '"', ","]
for mark in punctuation:
    text = text.replace(mark, '')

cleaned = text.split()

words_dict = {}

for word in cleaned:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
counts = sorted(words_dict.items(), key= itemgetter(1), reverse=True)
print(f"{'Word':15s}{'Count':>7}")
print("-"* 20)
for word in counts:
    print(f"{word[0]:15s}{word[1]:>2}")

print(len(words_dict))
print(len(cleaned))





