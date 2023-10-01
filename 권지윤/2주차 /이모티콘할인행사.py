discounts = [10, 20, 30, 40]
from itertools import product


def solution(users, emoticons):
    type = list(product(discounts, repeat=len(emoticons)))

    answer = [0, 0]
    for t in type:
        sign_up = 0
        amount = 0
        for target_type, target_price in users:
            price = 0
            for i, emoticon in enumerate(emoticons):
                if target_type <= t[i]:
                    price += int(emoticon // 100 * (100 - t[i]))

            if target_price <= price:
                sign_up += 1
            else:
                amount += price

            answer = max(answer, [sign_up, amount])

    return answer