"""
Assignment: Creating Class Diagrams and Implementing Dog Classes

Objective
This assignment aims to help you understand and apply the concepts of inheritance and polymorphism by creating class diagrams and implementing additional dog classes based on the American Kennel Club (AKC) dog groups.

Instructions
1. Create a Class Diagram
    - Using a tool of your choice (such as draw.io, Lucidchart, or any other diagramming software), create a class diagram for the provided Dog class and two additional dog classes you will implement.

        - Include all attributes and methods for each class.
        - Show the relationships between the classes (inheritance).

2. Copy the Provided Dog Class
    - Start by copying the provided Dog class code:

class Dog:
    def __init__(self, average_weight, height_range, life_span, color):
        self.average_weight = average_weight
        self.height_range = height_range
        self.life_span = life_span
        self.color = color
        
3. Implement Two Additional Dog Classes
    - Choose two different groups from the AKC dog groups list and implement new classes for each. Your classes should inherit from the Dog class and add specific characteristics and methods for each group.

    - The AKC dog groups are:

-Sporting
-Hound
-Working
-Terrier
-Toy
-Non-Sporting
-Herding
-Miscellaneous

    - Here is an example of how to implement the HerdingDog class:

'''
class HerdingDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, herding_ability):
        super().__init__(average_weight, height_range, life_span, color)
        self.herding_ability = herding_ability

    def herd(self):
        return "This dog is herding sheep!"
'''
        
    - Similarly, two other dog classes should be implemented, each with at least one unique attribute and one unique method.

4. Provide Sample Output
    - Write a script that creates instances of each class and demonstrates their attributes and methods. Here is an example of what your script might look like:

'''
if __name__ == "__main__":
    collie = HerdingDog(average_weight=60, height_range="22-26 inches", life_span="12-14 years", color="various", herding_ability="excellent")
    print(f"Collie: {collie.herd()}")
    
    # Add similar blocks for your other two dog classes
'''

Submission
    - Submit your completed assignment by uploading the following to your GitHub directory for the course:

        - The class diagram file
        - The Python script file with the implemented classes and sample output

    - Provide the link to your GitHub repository when submitting the assignment on Canvas.

Sample Output

Collie: This dog is herding sheep!
# Additional output for the other two dog classes

"""
