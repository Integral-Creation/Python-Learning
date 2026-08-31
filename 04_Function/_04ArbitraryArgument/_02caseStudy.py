def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('city')}")
    elif "poBox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('poBox')}")

    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('pinCode')}")

shipping_label(
            "Mr.", "Nikola", "Tesla",
            street="8 west 40th st", 
            poBox= "PO box 12",
            city="New York", 
            state="NY",
            pinCode=10018
        )

"""
Output:
        Mr. Nikola Tesla 
        8 west 40th st
        PO box 12
        New York, NY, 10018
"""