def intToRoman(num: int) -> str:
    num_map = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000][::-1]

    result = ''
    for key in keys:
        q = num // key
        if q:
            result += q * num_map[key]
        num %= key

    return result
