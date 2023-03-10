from faker import Faker
import uuid

fake = Faker()
for i in range(493):
     # Raises a UniquenessException
     print(fake.boolean(chance_of_getting_true=75))