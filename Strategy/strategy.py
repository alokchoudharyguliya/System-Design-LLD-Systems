from abc import ABC, abstractmethod
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self,array):
        pass

class BubbleSortStrategy(SortingStrategy):
    def sort(self,array):
        print("Sorting using Bubble Sort")

class MergeSortStrategy(SortingStrategy):
    def sort(self,array):
        print("Sorting using Merge Sort")
class SortingContext:
    def __init__(self,sorting_strategy):
        self.sorting_strategy=sorting_strategy
    
    def set_sorting_strategy(self,sorting_strategy):
        self.sorting_strategy=sorting_strategy
    
    def perform_sort(self,array):
        self.sorting_strategy.sort(array)

array1 = ["cpp","c","java","python3","csharp","html","css","javascript","php","cpp14","cobol","dart","go","julia","kotlin","lisp","matlab","node","objc","perl","r","rust","ruby","scala","swift","solidity","xml"]

sorting_context=SortingContext(BubbleSortStrategy())
sorting_context.perform_sort(array1)

sorting_context.set_sorting_strategy(MergeSortStrategy())
array2 = ["cpp","c","java","python3","csharp","html","css","javascript","php","cpp14","cobol","dart","go","julia","kotlin","lisp","matlab","node","objc","perl","r","rust","ruby","scala","swift","solidity","xml"]

sorting_context.perform_sort(array2)
