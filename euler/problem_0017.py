# Problem 17
# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
# hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
# usage.

number_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
               11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
               18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
               80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand', 0:''}

def get_name(num):
    num_list, num_name = map(int, list(str(num))[::-1]), ['']
    for i in range(0, len(num_list)):
        if i == 0: num_name.insert(0,' ' + number_dict[num_list[i]].strip())
        if i == 1:
            multiplier = num_list[i] * 10
            if multiplier == 10: num_name[0] = ' ' + number_dict[multiplier + num_list[i - 1]]
            elif multiplier > 10: num_name.insert(0,' ' + number_dict[multiplier])
        if i == 2: num_name.insert(0, ' ' + number_dict[num_list[i]] + ' ' +
                                   (number_dict[100] if num_list[i] > 0 else '') +
                                   (' and' if num_list[i] > 0 and (num_list[i - 1] != 0 or num_list[i - 2]) != 0
                                    else ''))
        if i == 3: num_name.insert(0, ' ' + number_dict[num_list[i]] + ' ' + number_dict[1000])
    return ''.join(num_name).strip()

def get_words_used(name_str):
    return len(name_str.replace(' ', ''))

def get_letter_count(num):
    count = 0
    for i in range (1, num + 1):
        count += get_words_used(get_name(i))
    return count