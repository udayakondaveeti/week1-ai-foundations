# Abstraction using an abstract base class
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass


class CSVProcessor(DataProcessor):
    def process(self, data):
        return f"Processed CSV: {data}"


processor = CSVProcessor()
print(processor.process("employee_data"))
