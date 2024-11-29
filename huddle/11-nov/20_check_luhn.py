card_numbers = ["5340294763483127", "5390926584981131", "5556037520907642",
            "5466943210966179", "4196233053544313", "6584383985777752"]

def calc_luhn(cc):

    res = [int(x) for x in str(cc)]

    for i in range(len(res) - 2, -1, -2):
        res[i] *= 2
        if res[i] > 9:
            res[i] -= 9
    res_sum = sum(res)
 
    return res_sum % 10 == 0

for c in card_numbers:
    a = calc_luhn(c)

    if a:
        print(f"{c} ✅")
    else:
        print(f"{c} ❌")

