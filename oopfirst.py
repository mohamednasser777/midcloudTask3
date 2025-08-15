class VotingSystem:
    def __init__(self):
        
        self.__candidates = {}  

    def add_candidate(self, name):
        if name not in self.__candidates:
            self.__candidates[name] = 0
            print(f"Candidate '{name}' added.")
        else:
            print(f"Candidate '{name}' already exists.")

    def remove_candidate(self, name):
        if name in self.__candidates:
            del self.__candidates[name]
            print(f"Candidate '{name}' removed.")
        else:
            print(f"Candidate '{name}' not found.")

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1
            print(f"Vote cast for '{name}'.")
        else:
            print(f"Candidate '{name}' not found.")

    def display_winner(self):
        if not self.__candidates:
            print("No candidates available.")
            return

        max_votes = max(self.__candidates.values())
        winners = [name for name, votes in self.__candidates.items() if votes == max_votes]

        if len(winners) == 1:
            print(f"The winner is '{winners[0]}' with {max_votes} votes!")
        else:
            print(f"It's a tie between: {', '.join(winners)} with {max_votes} votes each!")

   
    def show_candidates(self):
        for name, votes in self.__candidates.items():
            print(f"{name}: {votes} votes")


vs = VotingSystem()
vs.add_candidate("Alice")
vs.add_candidate("Bob")
vs.vote_to_candidate("Alice")
vs.vote_to_candidate("Bob")
vs.vote_to_candidate("Alice")
vs.show_candidates()
vs.display_winner()
