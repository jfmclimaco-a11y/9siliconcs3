# ILA 3-1: Applying the Four Pillars of OOP
## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation bundles product attributes (such as name, price, and quantity) and the methods that modify them into a single Product class using private variables. External code cannot modify stock levels directly, relying instead on controlled methods like restock(amount) or sell(amount) that check for valid inputs. This prevents accidental data corruption, such as setting negative stock or prices, ensuring inventory data stays accurate and secure.

### 2. Abstraction
Abstraction hides the inner complexity of stock processing and presents only essential operations to the user. System actions like processSale or displayInventory handle updates, calculations, and stock checks behind the scenes without exposing procedural implementation details. This simplifies the interface for the store operator and makes the system easier to update or maintain.

### 3. Inheritance
Inheritance allows specialized items to receive attributes and methods from a general Product base class. A PerishableProduct class (for example, milk or bread) inherits fields like name and price while introducing unique attributes like expirationDate. This eliminates duplicate code across product types and allows new categories to be added easily.

### 4. Polymorphism
Polymorphism allows different product types to execute shared methods in customized ways. A method like calculateDiscount can be overridden so that a PerishableProduct applies a higher discount as its expiration date approaches, whereas a standard product applies a flat rate. This enables the store inventory to handle a list of varied items uniformly without complex conditional statements.

## Reflection
Object-Oriented Programming models complex systems by organizing code into four intuitive, real-world principles. Encapsulation protects data within self-contained units, while Abstraction hides unnecessary backend complexity to keep interfaces clean and simple. Inheritance eliminates repetitive code by establishing shared hierarchies, and Polymorphism grants objects the flexibility to execute unique behaviors through a single interface. Together, these pillars transform messy scripts into modular, scalable, and easily maintainable software.

Encapsulation is the most useful pillar for improving the sari-sari store inventory system. In procedural programming, keeping track of items using separate arrays or global variables makes it easy to accidentally modify data, leading to invalid prices or incorrect stock counts. Encapsulation guarantees that product information can only be altered through strict, validated methods, protecting the core business data from unauthorized or unintended changes.
