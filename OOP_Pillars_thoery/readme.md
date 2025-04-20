# 🚀 4 Pillars of Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **objects and classes**. Python fully supports OOP and is built on four core principles:

---

## 🔐 1. Encapsulation

**Encapsulation** means bundling data (attributes) and methods (functions) that operate on the data into a single unit — a class. It also helps restrict access to internal object details.

### ✅ Benefits:
- Protects internal state
- Improves code modularity
- Enables controlled access with getters/setters

### 🧠 Example:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance       # Protected (by convention)
        self.__pin = "1234"           # Private

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
```

---

## 🎭 2. Abstraction

**Abstraction** means exposing only the relevant details and hiding the complex implementation. In Python, it's implemented using abstract base classes (ABCs).

### ✅ Benefits:
- Simplifies usage for the user
- Reduces complexity
- Focuses on *what* to do, not *how*

### 🧠 Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started")

car = Car()
car.start_engine()
```

---

## 🧬 3. Inheritance

**Inheritance** allows a class (child) to inherit methods and properties from another class (parent), promoting reusability and code hierarchy.

### ✅ Benefits:
- Code reusability
- Logical hierarchy
- Method overriding

### 🧠 Example:

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()
```

---

## 🌀 4. Polymorphism

**Polymorphism** allows objects of different classes to be treated through the same interface, providing flexibility and dynamic behavior.

### ✅ Benefits:
- One interface, many implementations
- Improves code flexibility
- Enables duck typing in Python

### 🧠 Example:

```python
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def lift_off(entity):
    entity.fly()

lift_off(Bird())
lift_off(Airplane())
```

---

## 📝 Summary

| Pillar         | Description                            | Python Example      |
|----------------|----------------------------------------|---------------------|
| **Encapsulation** | Protect internal state and structure | `_` and `__` access control |
| **Abstraction**   | Hide complexity, expose essentials   | `abc` module        |
| **Inheritance**   | Reuse logic via class hierarchy      | `class Child(Parent)` |
| **Polymorphism**  | Same interface, different behavior   | Method overriding / Duck typing |

---
