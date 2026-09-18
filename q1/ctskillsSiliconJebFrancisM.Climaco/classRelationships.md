# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/jfmclimaco-a11y/9siliconcs3/blob/main/q1/ctskillsSiliconJebFrancisM.Climaco/classAttributesMethod.md)

## Existing Class
Class:Cat

Description: A carnivore often kept as a pet by humans.

## New Related Class
Class: Cat Food
Description: food made specifically for cats to eat

## Association
Relationship: A Cat eats CatFood.
Explanation: A Cat has a uses-a relationship with CatFood, where the cat consumes the food to perform an action.
## Multiplicity

Multiplicity: 1 : Many
Explanation: One cat can eat many different servings of cat food over time, but each individual serving of food is eaten by only one specific cat.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
- The classes have a usage association because Cat interacts with CatFood to perform an action. Specifically, a Cat object takes a CatFood object as an argument inside its eat method. The two classes remain independent, so destroying a cat does not destroy the food object.
### What multiplicity did you choose and why?
- A one to many multiplicity was chosen because one cat can eat many different food items over time. A one to one relationship would incorrectly mean a cat could only ever eat a single portion of food in its entire lifetime. Each specific CatFood item is consumed by one individual cat at a time.
### How did you implement the relationship in Python?
- The relationship is implemented by passing a CatFood instance as a parameter named food directly into the eat method of the Cat class. If you want to keep track of every meal permanently, you can store those objects in a meals list attribute inside the Cat initialization method. Calling the list append method saves the food object inside the cat instance.
### Why did you store an object reference instead of copying its data?
- Storing a reference points directly to the original CatFood object in memory instead of duplicating its values. For example, when running the eat method with food1, Python passes the live food1 instance directly to the function. This ensures that any changes to food1 are instantly reflected without duplicating data or breaking synchronization.
### If your relationship uses many, why is a list appropriate?
- A list is ideal because it can dynamically hold multiple items and grow as the cat eats more food. The list contains memory pointers that refer directly to active CatFood objects like food1 and food2. This allows you to loop through the list easily to inspect past meals or calculate total calories eaten.
  
