face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
total = 0
for _ in range(6):
    u_input = input()
    if u_input in face_cards:
        total += face_cards.get(u_input)
    else:
        total += int(u_input)
print(total / 6)
