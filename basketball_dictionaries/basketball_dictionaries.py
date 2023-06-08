
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "Small Forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "Small Forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, 
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, 
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "Sams Frank", 
    	"age":29, 
    	"position": "Center",
    	"team": "Portland Trailblazers"
    }
]

class Player:

    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    def get_players(self):

        print("This is all the players we have right now : ", players)

        new_team = []

        for each_player in players:
            if each_player["team"] == "Brooklyn Nets":
                new_team.append(each_player)
        print("Let's build a new team! Let's start with these two players first : ", new_team)
            
        return self

    @classmethod

    def get_team(cls, team_list):

        print("Let's get one more player!")

        team_list = []

        for another_player in players:
            if another_player["team"] == "Boston Celtics":
                team_list.append(another_player)
        print("The third player can be : ", team_list)
        print("Now we have a team! Let's see who they are : ")

        return cls

    def team_dojo(self):
        print(f'Name: {self.name}, \n Age: {self.age}, \n Position: {self.position}, \n Team: {self.team}')
        
        return self



player_kevin = Player("Kevin Durant", 34, "Small Forward", "Brooklyn Nets")
player_jason = Player("Jason Tatum", 24, "Small Forward", "Boston Celtics")
player_kyrie = Player("Kyrie Irving", 32, "Point Guard", "Brooklyn Nets")




player_kevin.get_players()
player_kevin.get_team(players)
player_kevin.team_dojo()
player_jason.team_dojo()
player_kyrie.team_dojo()
