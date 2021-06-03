# Entity:- An object we want to model and store information about

"""
Attributes:-  are specific pieces of information about an entity

    Primary Key:- An attribute that uniquely identify an entry in the atabase table
    Composite attribute:- An attribute that can be broken up into sub-attributes
    Multi-Valued attribute:-  An attribute that can have more than one value
    Derived attribute:- An attribute that can be derived from other attributes

"""

# Multiple Entities:- you can define more that one entity in the diagram

# Relationships:- defines a relationship between two entities
    #Total participation:- All members ust participate in the relationship
    # Partial participation
# Relationship attribute:- An attribute about the relationship
# Relationship cardinality:- the number of instances of an entity from a relation that can be associated with the relation (1:1, 1:N, N:M)


# Weak Entity:- An entity that cannot be uniquely identified by its attributes alone

# Identifying relationship:- A relationship that serves to uniquely identify the weak entity









# company data requirement document ehich is used to create ER diagram.
"""
The company is organized into branches. Each branch has a unique number, a name, and a particular employee who manages it.

The company makes it’s money by selling to clients. Each client has a name and a unique number to identify it.

The foundation of the company is it’s employees. Each employee has a name, birthday, sex, salary and a unique number.

An employee can work for one branch at a time, and each branch will be managed by one of the employees that work there. We’ll also want to keep track of when the current manager started as manager.

An employee can act as a supervisor for other employees at the branch, an employee may also act as the supervisor for employees at other branches. An employee can have at most one supervisor.

A branch may handle a number of clients, with each client having a name and a unique number to identify it. A single client may only be handled by one branch at a time.

Employees can work with clients controlled by their branch to sell them stuff. If nescessary multiple employees can work with the same client. We’ll want to keep track of how many dollars worth of stuff each employee sells to each client they work with.

Many branches will need to work with suppliers to buy inventory. For each supplier we’ll keep track of their name and the type of product they’re selling the branch. A single supplier may supply products to multiple branches.
"""



#Key points while creating the ER diagram from above document
"""
1. first find entities in the document
2. find attributes of each entiies and their attribute type
3. create clear relationship between entities
4. find relationship attributes
"""



# After creating the ER diagram use that to create database schema
"""
1. Mapping of regular entity types:
    For each regular entity type create a relation(table) that includes all the simple attributes of that entity.
2. Mapping of weak entity types:
    For each weak entity create a relation (table) that includes all simple attributesof the weak entity
    The primary key of the new relation/table should be the partial key of the weak entity Plus the primary keu of its owner
3. Mapping of binary 1:1 relationship types:
    Include one side of therelationship as a foreign key in the other favor total participation.
4. Mapping of binary 1:N relationship types:
    Include the 1 side's primary key as foreign key on the N side relation table.
5. Mapping of binary N:M relationship types:
    Create a new relation/table who's primary key is a combination of both entities primary key's. 
    Also include any relationship attributes.
"""