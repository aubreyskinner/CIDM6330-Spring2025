import csv
from typing import List, Optional
from repositories.base import BaseRepository

class CSVRepository(BaseRepository):
    
    def __init__(self, filename: str):
        self.filename = filename
    
    #create
    def create(self, item) -> None:
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(item)
    
    #read
    def read(self, id: int) -> Optional[object]:
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == str(id):
                    return row  
        return None
    
    #update
    def update(self, item) -> None:
        rows = []
        updated = False
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        for idx, row in enumerate(rows):
            if row[0] == str(item[0]): 
                rows[idx] = item
                updated = True
                break
        
        if updated:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    
    #delete
    def delete(self, id: int) -> None:
        rows = []
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        rows = [row for row in rows if row[0] != str(id)] 
        
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    
    # List
    def list(self) -> List[object]:
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
