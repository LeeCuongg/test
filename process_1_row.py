file = open("raw_data.txt", "r")

data = file.readline()

data = data.split("\\n")

for i in range(len(data)):
    # remove \t \r
    data[i] = data[i].replace("\\r", "")
    data[i] = data[i].replace("\\t", "")

    # remove Tags
    tags = []
    for j in range(len(data[i])):
        if data[i][j] == "<":
            begin = j
        if data[i][j] == ">":
            end = j
            tags.append(data[i][begin:end+1])
    for tag in tags:
        data[i] = data[i].replace(tag, "")

    data[i] = data[i].strip()

unemty_lines = []
for i in range(len(data)):
    if data[i] != "":
        unemty_lines.append(data[i])
data = unemty_lines

file = open("test.txt", "w")
for i in range(len(data)):
    file.write(data[i] + "\n")
