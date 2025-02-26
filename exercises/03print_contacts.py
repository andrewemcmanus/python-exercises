# Write a method called `print_contacts` that takes a
# dictionary of key-value pairs for names and phone numbers,
# then outputs the `name` with the contact info.
#
# Try iterating over a dictionary with a for loop and printing
# out what values come back.
#
# Example method call:
#
# print_contacts(contacts)
#
# > Brian has a phone number of 333-333-3333
# > Lenny has a phone number of 444-444-4444
# > Daniel has a phone number of 777-777-7777
#
# Use the contacts below

contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777',
  'Andrew': '999-999-9999',
  'Amp': '888-888-8888',
  'Bolt': '222-222-2222',
  'Kristofer': '666-666-6666'
}
def print_contacts(dictionary):
    for key in dictionary:
        name = key
        number = dictionary[key]
        print(key + ' has a phone number of ' + number)
newname = input('Enter a new name: ')
newnumber = input('Enter a new number: ')
contacts[newname] = newnumber
print_contacts(contacts)

# print(keylist)
