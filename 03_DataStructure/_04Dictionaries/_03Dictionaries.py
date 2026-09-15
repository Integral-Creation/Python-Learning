contacts = {
    "Jane Doe" : {"phone" : "123-456-7890", "email:" : "janeDoe@example.com"},
    "Ellen Joe" : {"phone" : "987-654-3210", "email:" : "ellenjoe@example.com"},
    "Rina" : {"phone" : "987-123-4560", "email:" : "rina@example.com"}
}

name = input()

if name in contacts:
    new_phone = input()
    contacts[name].update({"phone" : new_phone})
else:
    print("Person Not Found")

print(contacts)

"""
Output:
Rina
678-091-2345
{'Jane Doe': {'phone': '123-456-7890', 'email:': 'janeDoe@example.com'}, 'Ellen Joe': {'phone': '987-654-3210', 'email:': 'ellenjoe@example.com'}, 'Rina': {'phone': '678-091-2345', 'email:': 'rina@example.com'}}
"""