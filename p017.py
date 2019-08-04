single = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundredand"

all = single + teens
twenty_to_ninety_nine = []

for i in tens:
    for j in single:
        twenty_to_ninety_nine.append(i + j)

all += twenty_to_ninety_nine

for i in single[1:]:
    all += i + "hundred"
    for j in single:
        all += i + hundred + j
    for j in teens:
        all += i + hundred + j
    for j in twenty_to_ninety_nine:
        all += i + hundred + j

print(all)
