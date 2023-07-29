import dataclasses


@dataclasses.dataclass
class User:
    zip_code: int = 72716
    first_name: str = "Meerim"
    last_name: str = "Sk"
    username: str = "standard_user"
    invalid_email: str = "skmeerim@mail.ru"
    wrong_password: str = "secret_sauc"
    password: str = "secret_sauce"


user = User()