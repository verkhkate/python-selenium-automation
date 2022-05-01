# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def convert_fn_and_ln_to_initials(fn, ln):
    result_converting_fn_and_ln_to_initials = (fn[0] + "." + ln[0]).upper()
    return result_converting_fn_and_ln_to_initials

first_name = input("\nPlease enter your first name: ")
last_name = input("Please enter your last name: ")

result_converting_fn_and_ln_to_initials = convert_fn_and_ln_to_initials(first_name, last_name)

print(f"\nConverting your full name into initials... \n{first_name} {last_name} => {result_converting_fn_and_ln_to_initials}")
print("\nThanks for participating! You've got a great name, by the way ;)")