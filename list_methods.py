class ListProcessor:

    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def extend_items(self, iterable):
        self.items.extend(iterable)

    def insert_at(self, index, item):
        self.items.insert(index, item)

    def remove_item(self, item):
        self.items.remove(item)

    def pop_last(self):
        return self.items.pop()

    def find_index(self, item):
        if item in self.items:
            return self.items.index(item)
        return -1

    def count_occurrences(self, item):
        return self.items.count(item)

    def sort_ascending(self):
        self.items.sort()

    def reverse_order(self):
        self.items.reverse()

    def clone(self):
        return self.items.copy()

    def clear_all(self):
        self.items.clear()


items = [30, 10, 20, 20, 40]

processor = ListProcessor(items)

print("original list:", processor.items)

processor.add_item(50)
print("after add_item:", processor.items)

processor.extend_items([60, 70])
print("after extend_items:", processor.items)

processor.insert_at(1, 15)
print("after insert_at:", processor.items)

processor.remove_item(20)
print("after remove_item:", processor.items)

removed_item = processor.pop_last()
print("popped item:", removed_item)
print("after pop_last:", processor.items)

print("index of 20:", processor.find_index(20))

print("count of 20:", processor.count_occurrences(20))

processor.sort_ascending()
print("after sort_ascending:", processor.items)

processor.reverse_order()
print("after reverse_order:", processor.items)

copied_list = processor.clone()
print("cloned list:", copied_list)

processor.clear_all()
print("after clear_all:", processor.items)
merged_list.append(item)

print(merged_list)
