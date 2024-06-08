
```
class NovaCore:
    def __init__(self):
        self.ideas = []

    def generate_idea(self):
        idea = "A novel concept: " + str(len(self.ideas) + 1)
        self.ideas.append(idea)
        return idea

# Create an instance of the NovaCore
nova = NovaCore()
```
