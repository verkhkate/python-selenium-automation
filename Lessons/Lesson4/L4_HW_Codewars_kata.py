# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example:
# 348597 => [7,9,5,8,4,3]
# 0 => [0]

def convert_to_reversed(num):
    array = list(map(int, str(num)))
    result_convert_to_reversed = array[::-1]
    return result_convert_to_reversed

number = input("\nPlease enter your number to be converted: ")
result_convert_to_reversed = convert_to_reversed(number)
print(f"\nConverting your number to reversed array of digits... \n{number} => {result_convert_to_reversed}")
