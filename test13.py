def luhn(card_number):
    length = len(card_number)
    oddSum = evenSum = 0
    if (length == 0): 
        return 0
    else:
        if (length % 2 == 0):
             num = int(card_number[-1])
             evenSum += num
             return evenSum + luhn(card_number[:-1])
        else:
            num = int(card_number[-1])
            num *= 2
            part_sum = num//10 + num%10
            oddSum += part_sum
            return oddSum + luhn(card_number[:-1])

card_number = input ('Δώσε ένα 16ψήφιο αριθμό πιστωτικής κάρτας: ')
total = luhn(card_number)
if (total % 10 == 0):
    print('Ο αριθμός είναι έγκυρος.')
else:
    print('Ο αριθμός δεν είναι έγκυρος.')
