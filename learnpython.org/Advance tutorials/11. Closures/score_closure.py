def score_manager(initial_score):
    def add_score(points):
        total = initial_score + points
        print("Total Score: ", total)
    return add_score

my_score = score_manager(100)

my_score(50)
my_score(20)