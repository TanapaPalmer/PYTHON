class User:	


    def __init__(self, first_name, last_name, email, age, gold__card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = gold__card_points
        

    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')



    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = self.gold_card_points + 200
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')



    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')



    def already_members(self, first_name, last_name):
        if (first_name, last_name) == (first_name, last_name):
            print("You're already a member!")



    def over_spend(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        if amount >= 161:
            raise Exception ("Over spending!")

    
    def re_enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')

        
user1 = User('Sabrina', 'Sams', 'SabrinaSams@gmail.com', 28, 0)
user2 = User('Timothy', 'Johnson', 'TimJ@gmail.com', 35, 0)
user3 = User('Babara', 'Boon', 'BabaraBooN@gmail.com', 47, 0)

user1.display_info()
user1.enroll()
user1.spend_points(50)
user1.re_enroll()


user2.enroll()
user2.spend_points(80)
user2.already_members("Timothy", "Johnson")


user3.enroll()
user3.spend_points(40)

try:
    user3.over_spend(170)
except Exception as a:
    print(a)

