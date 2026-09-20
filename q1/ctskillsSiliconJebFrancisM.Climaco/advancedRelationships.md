# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethod.md)

[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: Pet

Child: Cat

Explanation: A Cat is a specific type of Pet. The Pet parent class holds general attributes such as name, age, and breed, while the Cat child class inherits these features and adds cat-specific properties like hunger_level and methods like meow.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Aggregation

Explanation: CatOwner has a weak HAS-A relationship with Cat. The CatOwner class contains a reference to a Cat instance, but the cat can exist independently outside the owner object. If a CatOwner instance is deleted, the Cat object remains active in memory.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
[Test](images/advancedTestRun.png)
## Object Diagram
[Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
