# ILA 3-1: Applying the Four Pillars of OOP
## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation bundles product attributes (such as name, price, and quantity) and the methods that modify them into a sing product class using private variables. External code cannot modify stock levels directly, relying instead on controlled methods like restock or sell that check for valid inputs. This prevents accidental data corruption, such as setting negative stock or prices, ensuring inventory data stays accurate and secure.

### 2. Abstraction
Abstraction hides the inner complexity of stock processing and presents only essential operations to the user. System actions handle updates, calculations, and stock checks behind the scenes without exposing procedural implementation details. This simplifies the interface for the store operator and makes the system easier to update or maintain.

### 3. Inheritance
Inheritance allows specialized items to receive attributes and methods from a general product base class. A perishable product class inherits fields like name and price while introducing unique attributes. This eliminates duplicate code across product types and allows new categories to be added easily

### 4. Polymorphism
Polymorphism allows different product types to execute shared methods in customized ways. This enables the store inventory to handle a list of varied items uniformly without complex conditional statements.

## Reflection
Object-oriented Programming models complex systems by organizing code into four intuitive, real-world principles. Encapsulation protects data within self-contained units, while Abstraction hides unnecessary backend complexity to keep interfaces clean and simple. Inheritance eliminates repetitive code by establishing shared hierarchies, and Polymorphism grants objects the flexibility to execute unique behaviors through a single interface. 
Encapsulation is the most useful pillar for improving the sari-sari store inventory system. In procedural programming, keeping track of items using separate arrays or global variables makes it easy to accidentally modify data, leading to valid prices or incorrect stock counts. It guarantees that product information can only be altered through strict, validated methods, protecting the core business data from unauthorized or unintended changes.
