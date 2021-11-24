from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price:
            if self.__animal_capacity > len(self.animals):
                self.__budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            else:
                return "Not enough space for animal"
        else:
            return "Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__worker_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
            else:
                "There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        total_lions = 0
        lions_info = []
        for animal in self.animals:
            if type(animal) == Lion:
                total_lions += 1
                lions_info.append(repr(animal))

        total_tigers = 0
        tigers_info = []
        for animal in self.animals:
            if type(animal) == Tiger:
                total_tigers += 1
                tigers_info.append(repr(animal))

        total_cheetahs = 0
        cheetahs_info = []
        for animal in self.animals:
            if type(animal) == Cheetah:
                total_cheetahs += 1
                cheetahs_info.append(repr(animal))

        result += f"----- {total_lions} Lions:\n"
        lions_more_info = "\n".join(lions_info)
        result += lions_more_info + "\n"

        result += f"----- {total_tigers} Tigers:\n"
        tigers_more_info = "\n".join(tigers_info)
        result += tigers_more_info + "\n"

        result += f"----- {total_cheetahs} Cheetahs:\n"
        cheetahs_more_info = "\n".join(cheetahs_info)
        result += cheetahs_more_info

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        total_keepers = 0
        keepers_info = []
        for worker in self.workers:
            if type(worker) == Keeper:
                total_keepers += 1
                keepers_info.append(repr(worker))

        total_caretakers = 0
        caretakers_info = []
        for worker in self.workers:
            if type(worker) == Caretaker:
                total_caretakers += 1
                caretakers_info.append(repr(worker))

        total_vets = 0
        vets_info = []
        for worker in self.workers:
            if type(worker) == Vet:
                total_vets += 1
                vets_info.append(repr(worker))

        result += f"----- {total_keepers} Keepers:\n"
        keepers_more_info = "\n".join(keepers_info)
        result += keepers_more_info + "\n"

        result += f"----- {total_caretakers} Caretakers:\n"
        caretakers_more_info = "\n".join(caretakers_info)
        result += caretakers_more_info + "\n"

        result += f"----- {total_vets} Vets:\n"
        vets_more_info = "\n".join(vets_info)
        result += vets_more_info

        return result











