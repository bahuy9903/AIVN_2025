def example_1(): #list
    fruits = ["apple", "banana", "cherry", "date"]
    print (fruits[1])  # Output: banana
    fruits.append("elderberry") # Adding a new fruit to the list
    print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']
    fruits.remove("cherry") # Removing 'cherry' from the list
    print(fruits)  # Output: ['apple', 'banana', 'date', 'elderberry']
    fruits.sort() # Sorting the list of fruits
    print(fruits)  # Output: ['apple', 'banana', 'date', 'elderberry']

def example_2(): #tuple
    coordinates = (10.0, 20.0)
    print(coordinates[0])  # Output: 10.0

def example_3(): #set
    colors = {"red", "green", "blue","red"}
    colors.add("yellow")  # Adding a new color to the set
    print(colors)  # Output: {'red', 'green', 'blue', 'yellow'}
    colors.remove("green")  # Removing 'green' from the set
    print(colors)  # Output: {'red', 'blue', 'yellow'}

def example_4(): #dictionary
    preson = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print(preson["name"])  # Output: Alice
    preson["age"] = 31  # Updating age
    print(preson)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

if __name__ == "__main__":
    example_4()