text_num = '1234'

#Manually cast a String number in to an int
def num_to_int(text_num):
    list_chars = list(text_num)
    decimal = 10
    ciro_val = 48
    final_number = 0
    for char_num in list_chars:                
        real_val = ord(char_num) - ciro_val
        final_number = final_number * decimal
        final_number += real_val
    return final_number

print(num_to_int(text_num))
