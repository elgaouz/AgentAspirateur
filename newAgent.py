import time
from IPython.display import clear_output

# Dimensions de l'environnement
ENV_WIDTH = 5
ENV_HEIGHT = 5

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_down(self):
        if self.y < ENV_HEIGHT - 1:
            self.y += 1
    def move_up(self):
        if self.y > 0:
            self.y -= 1
            
    def move_left(self):
        if self.x > 0:
            self.x -= 1
            
    def move_right(self):
        if self.x < ENV_WIDTH - 1:
            self.x += 1

class Environment:
    def __init__(self):
        self.environment =  [
                            ['0', ' ', ' ', ' ', '0'],
                            [' ', ' ', ' ', ' ', '0'],
                            ['0', ' ', ' ', ' ', '0'],
                            [' ', ' ', ' ', ' ', '0'],
                            [' ', ' ', ' ', ' ', '0']
                        ]

    def clean_dirt(self, x, y):
        self.environment[x][y] = ' '

    def print_environment(self, agent):
        clear_output(wait=True)
        print("----------")
        for i in range(len(self.environment)):
            for j in range(len(self.environment[0])):
                if i == agent.y and j == agent.x:
                    self.clean_dirt(i, j)
                    print('A', end=' ')  
                else:
                    print(self.environment[i][j], end=' ')
            print()
        print("----------")
    


# Création de l'agent et de l'environnement
agent = Agent(0, 0)

env = Environment()

env.print_environment(agent)

for i in range(len(env.environment)):
    if i % 2 == 0:
        for j in range(len(env.environment[0]) - 1):
            agent.move_right();
            env.print_environment(agent);
            time.sleep(1);
            clear_output(wait=True);
        agent.move_down();
        env.print_environment(agent);
        time.sleep(1);
        clear_output(wait=True);
    else:
        for j in range(len(env.environment[0]) - 1):
            agent.move_left();
            env.print_environment(agent);
            time.sleep(1);
            clear_output(wait=True);
        agent.move_down();
        env.print_environment(agent);
        time.sleep(1);
        clear_output(wait=True);