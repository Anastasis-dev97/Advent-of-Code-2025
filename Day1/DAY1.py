import os, math


os.chdir("/home/fotiadis/Desktop/PythonProjects")

print(os.getcwd())

filename="day1.txt"

def parse_sequences(lines):
    result = []
    for seq in lines:
        seq = seq.strip()
        if not seq:  # skip empty lines
            continue
        direction = seq[0]          # 'R' or 'L'
        distance = int(seq[1:])     # numeric part
        result.append((direction, distance))
    return result

with open(filename, "r") as file:
    lines = file.readlines()


moves = parse_sequences(lines)


position=50
code=0

for direction, distance in moves:
    if direction == 'R':
       
        if distance % 100 > 100-position :
           code = code + 1
        position = (position+ distance) % 100
    
    else:
       if abs(distance % 100) > position > 0:
           code = code + 1
       position = (position-distance) % 100

    code = code + int(abs(distance)/100)

    if position == 0:
        code+= 1

print(code)