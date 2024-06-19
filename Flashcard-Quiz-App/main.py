class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardQuizApp:
    def __init__(self):
        self.flashcards = []
        self.score = 0

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)
        print("Flashcard added.")

    def take_quiz(self):
        if not self.flashcards:
            print("No flashcards available. Please add some flashcards first.")
            return

        self.score = 0
        for flashcard in self.flashcards:
            print(f"Question: {flashcard.question}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {flashcard.answer}")

        self.display_score()

    def display_score(self):
        total_questions = len(self.flashcards)
        print(f"\nYour score: {self.score}/{total_questions}")
        if total_questions > 0:
            print(f"Percentage: {(self.score / total_questions) * 100:.2f}%")

def main():
    app = FlashcardQuizApp()

    while True:
        print("\nFlashcard Quiz App")
        print("1. Add flashcard")
        print("2. Take quiz")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            app.add_flashcard(question, answer)
        elif choice == '2':
            app.take_quiz()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
