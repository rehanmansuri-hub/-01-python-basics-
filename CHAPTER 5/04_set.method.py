s = {1, 2, 3, 4, 5,5,5,5, "Hello"}

print(s, type(s)) # Output: {1, 2, 3, 4, 5, 'Hello'} - Duplicates are removed

s.add(6) 
print(type(s)) # Output: {1, 2, 3, 4, 5, 'Hello', 6}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.add(5)                  # Ek item add
a.remove(2)               # Item remove; nahi mila to error
a.discard(10)             # Item remove; nahi mila to error nahi

a.pop()                   # Koi ek item remove
a.clear()                 # Pura set empty
a.copy()                  # Set ki copy

a.union(b)                # Dono sets ke saare unique items
a.intersection(b)        # Common items
a.difference(b)          # a mein hain, b mein nahi
a.symmetric_difference(b) # Dono mein hain, lekin common nahi

a.update(b)               # b ke items a mein add
a.intersection_update(b)  # Sirf common items rakhta hai
a.difference_update(b)    # b ke items a se hata deta hai

a.issubset(b)             # Check: a, b ke andar hai?
a.issuperset(b)           # Check: a mein b ke saare items hain?
a.isdisjoint(b)           # Check: koi common item nahi hai?