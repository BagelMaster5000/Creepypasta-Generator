import random

def PrintInfo():
    print("Creepypasta Story Generator!")
    print()
    print("By BagelMaster5000(Sammy Mahmoudi)")
    print()
    print()

def ReadStoryLinesFromFile(fileName):
    print("Generating story using data from " + fileName + ":")
    print()

    readFile = open(fileName, 'r')
    Lines = readFile.readlines()

    return Lines

def GenerateStory(StoryLines):
    List = []
    story = ""
    for line in StoryLines:
        if (len(line) > 1):
            List.append(line[0:len(line) - 1])
        else:
            story += List[random.randint(0, len(List) - 1)]
            List.clear()

    return story

def OutputStoryToFile(fileName, story):
    print()
    print("Story also output to " + fileName)
    print()

    writeFile = open(fileName, 'w')
    writeFile.write(story)
    writeFile.close()


PrintInfo()

Lines = ReadStoryLinesFromFile("Lines for random generation.txt")
story = GenerateStory(Lines)
print(story)
OutputStoryToFile("Creepypasta Story.txt", story)