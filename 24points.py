import random
import itertools
import math
import sys

class twentyfour_points():
    def __init__(self):
        self.problem=[]
        self.has_solution = False
        self.solution=''
        self.find_solution(self.generate_numbers())


    def generate_numbers(self):
        all_numbers = []
        for i in range(0,4):
            all_numbers.append(random.randint(1, 24))
        self.problem = all_numbers
        # print("four numbers are:",all_numbers)
        all_permutations = list(itertools.permutations(all_numbers))
        return all_permutations


    def try_all_four_operations(self,string):
        # operations = ['+','-','*','/']
        operations = '+-*/'
        all_operations = list(itertools.product(operations, repeat = 3))
        for i in all_operations:
            expression = (string.format(*i))
            try:
                calculation = eval(expression)
            except ZeroDivisionError:
                return False
            if math.isclose(calculation,24,rel_tol=1e-4):
                # print("one possible solution is:", expression)
                self.solution='one possible solution is: '+expression
                return True
        return False

    def add_one_parenthesis(self,ele1,ele2,ele3,ele4):
        permutation_list = []
        permutation_list.append('('+ele1+'{}'+ele2+')'+'{}'+ele3+'{}'+ele4)
        permutation_list.append('('+ele1+'{}'+ele2+'{}'+ele3+')'+'{}'+ele4)
        permutation_list.append(ele1+'{}'+'('+ele2+'{}'+ele3+')'+'{}'+ele4)
        permutation_list.append(ele1+'{}'+'('+ele2+'{}'+ele3+')'+'{}'+ele4)
        permutation_list.append(ele1+'{}'+'('+ele2+'{}'+ele3+'{}'+ele4+')')
        for i in permutation_list:
            if self.try_all_four_operations(i):
                return True
        return False

    def add_two_parenthesis(self,ele1,ele2,ele3,ele4):
        permutation_list = []
        permutation_list.append('('+ele1+'{}'+ele2+')'+'{}'+'('+ele3+'{}'+ele4+')')
        permutation_list.append('('+'('+ele1+'{}'+ele2+')'+'{}'+ele3+')'+'{}'+ele4)
        permutation_list.append('('+ele1+'{}'+'('+ele2+'{}'+ele3+')'+')'+'{}'+ele4)
        permutation_list.append(ele1+'{}'+'('+'('+ele2+'{}'+ele3+')'+'{}'+ele4+')')
        permutation_list.append(ele1+'{}'+'('+ele2+'{}'+'('+ele3+'{}'+ele4+')'+')')
        for i in permutation_list:
            if self.try_all_four_operations(i):
                return True
        return False


    def test_validity(self,one_permutation):
        ele1 = str(one_permutation[0])
        ele2 = str(one_permutation[1])
        ele3 = str(one_permutation[2])
        ele4 = str(one_permutation[3])
        list_no_parenthesis = ele1+'{}'+ele2+'{}'+ele3+'{}'+ele4
        if self.try_all_four_operations(list_no_parenthesis) or self.add_one_parenthesis(ele1, ele2, ele3, ele4) or self.add_two_parenthesis(ele1, ele2, ele3, ele4):
            return True
        return False


    def find_solution(self,list_of_permutations):
        for i in list_of_permutations:
            if self.test_validity(i):
                self.has_solution = True
                # return True
        # return False
    
    def check_solution(self):
        return self.has_solution

    def get_solution(self):
        return self.solution

    def get_question(self):
        return self.problem


print("This is the 24-points game! Allowed operations are: +, -, * and /. Numbers are integers ranging from 1 to 24 inclusively.")
print("All problems has a solution. Enter your expression to answer. If the expression calculates to 24, then you win.")
print("To peek at the answer, enter 'help'. To skip to the next question, enter 'skip'.")
start = input("Enter 'y' to start the game. The game will keep going unless 'stop' is entered:")
stop = False
if start == 'y':
    while not stop:
        valid = False
        while not valid:
            obj = twentyfour_points()
            valid = obj.check_solution()
        print(obj.get_question())
        ans = input("your answer: ")
        if ans == 'stop':
            stop = True
        elif ans == 'help':
            print(obj.get_solution())
        elif ans == 'skip':
            pass
        else:
            while not math.isclose(eval(ans),24,rel_tol=1e-4):
                ans = input("try again: ")
            print("Bingo! Next one!")


