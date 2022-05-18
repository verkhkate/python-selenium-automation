# You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, ' \
#    'you would like to find out the house number of the people on the other side of the street. The street looks something like this:
#
# Street
# 1|   |6
# 3|   |4
# 5|   |2
# Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.
#
# Example (address, n --> output)
# Given your house number address and length of street n, give the house number on the opposite side of the street.
#
# 1, 3 --> 6
# 3, 3 --> 4
# 2, 3 --> 5
# 3, 5 --> 8
# ----------------------------------------------------------------

def over_the_road(address, n):
    opposite_house_result = (2*n+1)-address
    return opposite_house_result

your_address = int(input('Please enter your house number: '))
street_length = int(input('How long is the street? Please enter a number: '))

opposite_house_result = over_the_road(your_address, street_length)

print(f'The opposite house number is: {opposite_house_result}')
