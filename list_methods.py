# python list methods

## 1. append() - add an item

items = [10, 20, 30]
items.append(40)
print(items)

## 2. extend() - add multiple items

items = [10, 20, 30]
items.extend([40, 50, 60])
print(items)

## 3. insert() - insert an item at an index

items = [10, 20, 30]
items.insert(1, 15)
print(items)

## 4. remove() - remove the first occurrence

items = [10, 20, 30, 20]
items.remove(20)
print(items)

## 5. pop() - remove and return the last item

items = [10, 20, 30]
removed_item = items.pop()
print(items)
print(removed_item)

## 6. index() - find the first occurrence

items = [10, 20, 30, 20]
index = items.index(20)
print(index)

## 7. count() - count occurrences

items = [10, 20, 20, 30, 20]
count = items.count(20)
print(count)

## 8. sort() - sort in ascending order

items = [40, 10, 30, 20]
items.sort()
print(items)

## 9. reverse() - reverse the list

items = [10, 20, 30, 40]
items.reverse()
print(items)

## 10. copy() - create a shallow copy

items = [10, 20, 30]
copied_items = items.copy()
print(copied_items)

## 11. clear() - remove all items

items = [10, 20, 30]
items.clear()
print(items)

## 12. merge and deduplicate two lists

list_a = [1, 2, 3, 2]
list_b = [3, 4, 5, 4]

merged_list = []

for item in list_a:
if item not in merged_list:
merged_list.append(item)

for item in list_b:
if item not in merged_list:
merged_list.append(item)

print(merged_list)
