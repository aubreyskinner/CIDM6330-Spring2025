from typing import List, Optional
from repositories.base import BaseRepository

class MemoryRepository(BaseRepository):
    
    def __init__(self):
        self.data = []
    
    #create
    def create(self, item) -> None:
        self.data.append(item)
    
    #read
    def read(self, id: int) -> Optional[object]:
        return next((item for item in self.data if item[0] == id), None)  

    #update
    def update(self, item) -> None:
        for idx, existing_item in enumerate(self.data):
            if existing_item[0] == item[0]: 
                self.data[idx] = item
                break
    
    #delete
    def delete(self, id: int) -> None:
        self.data = [item for item in self.data if item[0] != id]  
    
    #list
    def list(self) -> List[object]:
        return self.data
