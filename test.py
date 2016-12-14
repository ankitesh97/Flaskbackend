
with open('aba-04.png', 'rb') as f:
    data = f.read()

with open('picture_out.png', 'wb') as f:
    f.write(data)