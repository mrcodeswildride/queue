print()

print("Enter names into the queue, or press enter to get the next name.\n")

queue = []

while True:
  name = input("Enter a name: ")

  if name != "":
    queue.append(name)
  elif len(queue) == 0:
    print("\nThe queue is empty.\n")
  else:
    print(f"\n{queue[0]} is next in the queue.\n")
    del queue[0]
