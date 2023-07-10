class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population


    def description(self):
        return f'{self.name}, {self.population}'
    
    @classmethod
    def create_country(cls, name='Standard name',population=0):
        instance = cls(name, population)
        return instance
    
    def add(self, other,):
        if not isinstance(other, Country):
            return TypeError('other must be a Country instance')
        
        new = Country
        new.create_country()
        new.name = ' '.join([self.name, other.name])
        new.population = self.population + other.population
        return new
        

        

bosnia = Country('Bosnia', 10_000_000)

herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzogovina = bosnia.add(herzegovina)
print(bosnia_herzogovina.name)
print(bosnia_herzogovina.population)
