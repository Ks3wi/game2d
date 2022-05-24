class Scoreboard:
    def __init__(self):
        self.__scoreboard = {}
        self.FillTheScoreboard()
    def FillTheScoreboard(self):
        file = open("score.txt", "r")
        content = file.read()
        content = content[:-1]
        file.close()
        list_content = content.split(' ')
        i = 0
        while i < len(list_content):
            self.__scoreboard[list_content[i]] = int(list_content[i + 1])
            i += 2
    def Display(self):
        for key in self.__scoreboard:
            print(key + ": " + str(self.__scoreboard[key]))
    def Save(self, name, score):
        if name in self.__scoreboard:
            if self.__scoreboard[name] < score:
                self.__scoreboard[name] = score
        else:
            self.__scoreboard[name] = score

        file = open("score.txt", "w")
        for key in self.__scoreboard:
            file.write(key + " " + str(self.__scoreboard[key])+" ")
        file.close()



    