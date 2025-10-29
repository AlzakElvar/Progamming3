import time as t

start = t.time()

file = open("numbers.txt")
text = file.read().split(",")
f_text = []
for te in text:
    te = int(te.strip())
    f_text.append(te)

i = 0

while i < len(f_text):
    j = i
    while j > 0:
        if f_text[j] < f_text[j-1]:
            f_text[j-1] , f_text[j] = f_text[j] , f_text[j-1]
        j = j - 1
    i += 1
    

print(t.time() - start)
