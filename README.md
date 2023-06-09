# SyncList

SyncList is a Python list with automatic synchronization of data with a JSON file. This can be useful in cases where you
need to save data between program sessions or if you need to save the state of data in real time.

# Installation

You can install SyncList using pip:

```bash
pip install sync_list
```

# Usage

```python
from sync_list import SyncList

# Creating SyncList object with initial data
my_list = SyncList([1, 2, 3])

# Adding elements
my_list.append(4)
my_list.extend([5, 6])

# Inserting an element
my_list.insert(3, 0)

# Removing an element
my_list.remove(2)

# Accessing an element by index
print(my_list[0])  # 1

# Changing an element
my_list[0] = 0

# Sorting the list
my_list.sort()

# Reversing the list
my_list.reverse()
```

When the `sync()` method is called, the data in the list will be written to a file in JSON format. On the next program
run, the data will be loaded from the file and available for use in the SyncList object.

# Developers

- Azreil-OFD (fantom2413@gmail.com)