i = str(['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple'])
L = i[1:-1]
L = L.replace("'", "")
L = L.replace(" ", "")
L = L.split(",")