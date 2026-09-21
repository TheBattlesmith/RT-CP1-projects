import random

plunder = random.randint(500, 5000)
total = plunder

while True:

    try:
        pirates = int(input("How many pirates are in your crew, aside from you and Peter? "))
    except:
        print("that's no number!")
    else:
        break

pirates = pirates + 2

plunder = plunder - ((3 * pirates) + 6)

yondu_bonus = 0.13 * plunder
plunder = plunder - (0.13 * plunder)
yondu_bonus = (round(yondu_bonus, 2))
plunder = (round(plunder, 2))

quill_bonus = 0.11 * plunder
plunder = plunder - (0.11 * plunder)
quill_bonus = (round(quill_bonus, 2))
plunder = (round(plunder, 2))


crew_shares = plunder / pirates
crew_shares = round(crew_shares, 2)

yondu_share = yondu_bonus + crew_shares
yondu_share = (round(yondu_share, 2))

quill_share = quill_bonus + crew_shares
quill_share = (round(quill_share, 2))

print(f"Units found: {total}")
print(f"Yondu's share: {round(yondu_share, 2)}")
print(f"Peter's share: {round(quill_share,2)}")
print(f"Crew's share: {round(crew_shares, 2)}")

