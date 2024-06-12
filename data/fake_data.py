from faker import Faker


class FakeData:
    fake = Faker("en_US")

    @property
    def name(self):
        return self.fake.first_name
