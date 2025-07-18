from experta import *

# Define the facts class
class StudentFacts(Fact):
    """ A fact class to hold user interests """
    pass

# Expert system class
class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

# Main function to interact with the user
def main():
    engine = CareerExpertSystem()
    engine.reset()  # Initialize the expert system

    print("Welcome to the Career Path Expert System!")

    # Taking input from the user and ensuring no extra spaces are left
    interests_input = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ")
    interests = [interest.strip() for interest in interests_input.split(',')]

    # Declare facts based on user input
    for interest in interests:
        engine.declare(StudentFacts(likes=interest))

    # Run the engine to process the facts and apply rules
    engine.run()

if __name__ == "__main__":
    main()

