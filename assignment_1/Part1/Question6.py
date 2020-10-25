phone = input("phone_no: ")
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + ""
print(output)

# Out Put
!threethree!!!!!!one!
