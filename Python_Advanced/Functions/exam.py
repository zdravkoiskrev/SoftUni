from collections import deque

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

materials = [int(i) for i in input().split(" ")]
magic_levels = [int(i) for i in input().split(" ")]
magic_level_queue = deque(magic_levels)


def gift_checker(*arg):
    if 100 <= sum_m_m <= 199:
        gift = "gem"
    elif 200 <= sum_m_m <= 299:
        gift = "porcelain"
    elif 300 <= sum_m_m <= 399:
        gift = "gold"
    elif 400 <= sum_m_m <= 499:
        gift = "diamond"
    else:
        gift = None
    value = gift
    return value


def gift_checker2(*arg):
    if 100 <= new_sum <= 199:
        gift = "gem"
    elif 200 <= new_sum <= 299:
        gift = "porcelain"
    elif 300 <= new_sum <= 399:
        gift = "gold"
    elif 400 <= new_sum <= 499:
        gift = "diamond"
    else:
        gift = None
    value = gift
    return value


def gift_checker3(*arg):
    if 100 <= newest_sum <= 199:
        gift = "gem"
    elif 200 <= newest_sum <= 299:
        gift = "porcelain"
    elif 300 <= newest_sum <= 399:
        gift = "gold"
    elif 400 <= newest_sum <= 499:
        gift = "diamond"
    else:
        gift = None
    value = gift
    return value


def gift_checker4(*arg):
    if 100 <= n_devided_sum <= 199:
        gift = "gem"
    elif 200 <= n_devided_sum <= 299:
        gift = "porcelain"
    elif 300 <= n_devided_sum <= 399:
        gift = "gold"
    elif 400 <= n_devided_sum <= 499:
        gift = "diamond"
    else:
        gift = None
    value = gift
    return value


while len(materials) > 0 and len(magic_level_queue) > 0:
    material = materials.pop()
    magic = magic_level_queue.popleft()
    sum_m_m = material + magic
    if 100 <= sum_m_m <= 499:
        if gift_checker() == "gem":
            gemstone += 1
        elif gift_checker() == "porcelain":
            porcelain_sculpture += 1
        elif gift_checker() == "gold":
            gold += 1
        elif gift_checker() == "diamond":
            diamond_jewellery += 1
    elif sum_m_m < 100:
        if sum_m_m % 2 == 0:
            n_material = material * 2
            n_magic = magic * 3
            new_sum = n_material + n_magic
            if 100 <= new_sum <= 499:
                if gift_checker2() == "gem":
                    gemstone += 1
                elif gift_checker2() == "porcelain":
                    porcelain_sculpture += 1
                elif gift_checker2() == "gold":
                    gold += 1
                elif gift_checker2() == "diamond":
                    diamond_jewellery += 1
            else:
                continue
        elif not sum_m_m % 2 == 0:
            newest_sum = sum_m_m * 2
            if 100 <= newest_sum <= 499:
                if gift_checker3() == "gem":
                    gemstone += 1
                elif gift_checker3() == "porcelain":
                    porcelain_sculpture += 1
                elif gift_checker3() == "gold":
                    gold += 1
                elif gift_checker3() == "diamond":
                    diamond_jewellery += 1
            else:
                continue
    elif sum_m_m > 499:
        n_devided_sum = sum_m_m / 2
        if 100 <= n_devided_sum <= 499:
            if gift_checker4() == "gem":
                gemstone += 1
            elif gift_checker4() == "porcelain":
                porcelain_sculpture += 1
            elif gift_checker4() == "gold":
                gold += 1
            elif gift_checker4() == "diamond":
                diamond_jewellery += 1
        else:
            continue
    else:
        continue


if gemstone > 0 and porcelain_sculpture > 0:
    print("The wedding presents are made!")
elif gold > 0 and diamond_jewellery > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if len(materials) == 0 and len(magic_level_queue) > 0:
    new_list = list(magic_level_queue)
    new_list = [str(i) for i in new_list]
    new_list = ", ".join(new_list)
    print(f"Magic left: {new_list}")
elif len(materials) > 0 and len(magic_level_queue) == 0:
    another_new_list = list(materials)
    another_new_list = [str(i) for i in another_new_list]
    another_new_list = ", ".join(another_new_list)
    print(f"Materials left: {another_new_list}")

if gemstone > 0:
    print(f"Gemstone: {gemstone}")
if porcelain_sculpture > 0:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")
if gold > 0:
    print(f"Gold: {gold}")
if diamond_jewellery > 0:
    print(f"Diamond Jewellery: {diamond_jewellery}")

