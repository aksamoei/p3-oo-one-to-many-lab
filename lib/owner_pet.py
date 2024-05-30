class Pet:
    '''templates a pet'''
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        '''initialize attributes'''
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Pet type not in allowed types")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            owner.add_pet(self)

    @property
    def pet_type(self):
        '''get pet_type'''
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, type):
        '''set pet_type'''
        if type not in Pet.PET_TYPES:
            raise Exception("Pet type not in allowed types")
        else:
            self._pet_type = type


class Owner:
    '''templates a pet owner'''
    def __init__(self, name):
        '''initialize attributes'''
        self.name = name
        self._pets = []
    
    def pets(self):
        '''return all pets for this owner'''
        return self._pets
    
    def add_pet(self, pet):
        '''adds a pet to this owner'''
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        '''returns pets sorted by name'''
        return sorted(self._pets, key=lambda pet: pet.name)