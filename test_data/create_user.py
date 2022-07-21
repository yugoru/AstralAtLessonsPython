from faker import Faker

faker = Faker('ru-RU')
SCENARIO = {
    "email": faker.email(),
    "password": "Test123",
    "confirmPassword": "Test123",
    "lastName": faker.first_name(),
    "firstName": faker.last_name(),
    "patronymic": faker.first_name() + "ович",
    "phoneNumber": "+79999999999"
}
