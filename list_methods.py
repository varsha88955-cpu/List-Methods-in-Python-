# python list methods

class ListProcessor:

```
def __init__(self, items):
    self.items = items

# 1. append() - add an item
def add_item(self, item):
    self.items.append(item)
    print(self.items)

# 2. extend() - add multiple items
def extend_items(self, iterable):
    self.items.extend(iterable)
    print(self.items)

# 3. insert() - insert an item at an index
def insert_at(self, index, item):
    self.items.insert(index, item)
    print(self.items)

# 4. remove() - remove the first occurrence
def remove_item(self, item):
    self.items.remove(item)
    print(self.items)

# 5. pop() - remove and return the last item
def pop_last(self):
    removed_item = self.items.pop()
    print(self.items)
    print(removed_item)
    return removed_item

# 6. index() - find the first occurrence
def find_index(self, item):
    if item in self.items:
        index = self.items.index(item)
    else:
        index = -1
    print(index)
    return index

# 7. count() - count occurrences
def count_occurrences(self, item):
    count = self.items.count(item)
    print(count)
    return count

# 8. sort() - sort in ascending order
def sort_ascending(self):
    self.items.sort()
    print(self.items)

# 9. reverse() - reverse the list
def reverse_order(self):
    self.items.reverse()
    print(self.items)

# 10. copy() - create a shallow copy
def clone(self):
    copied_items = self.items.copy()
    print(copied_items)
    return copied_items

# 11. clear() - remove all items
def clear_all(self):
    self.items.clear()
    print(self.items)

# 12. merge and deduplicate two lists
@staticmethod
def merge_and_dedup(list_a, list_b):
    merged_list = []

    for item in list_a:
        if item not in merged_list:
            merged_list.append(item)

    for item in list_b:
        if item not in merged_list:
            merged_list.append(item)

    print(merged_list)
    return merged_list
```

# create list

items = [10, 20, 30, 20]

# create object

processor = ListProcessor(items)

# 1. append()

processor.add_item(40)

# 2. extend()

processor.extend_items([50, 60])

# 3. insert()

processor.insert_at(1, 15)

# 4. remove()

processor.remove_item(20)

# 5. pop()

processor.pop_last()

# 6. index()

processor.find_index(30)

# 7. count()

processor.count_occurrences(20)

# 8. sort()

processor.sort_ascending()

# 9. reverse()

processor.reverse_order()

# 10. copy()

processor.clone()

# 11. clear()

processor.clear_all()

# 12. merge and deduplicate

list_a = [1, 2, 3, 2]
list_b = [3, 4, 5, 4]

ListProcessor.merge_and_dedup(list_a, list_b)
