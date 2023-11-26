from dataclasses import dataclass


@dataclass
class Users:
    User_id: int

    def get_user_id(self) -> str:
        print(Users.get_user_id.__annotations__)
        return f'User id is {self.User_id}'


if __name__ == "__main__":
    user1 = Users(142)
    print(user1.get_user_id())