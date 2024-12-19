class collage:
    def __init__(self,studentname,room,roll):
        self.studentname=studentname
        self.room=room
        self.roll=roll

    def __str__(self):
        return "student={0},room={1},roll={2}".format(self.studentname,self.room,self.roll)

    t= collage=("rahul","1","100")
    print(t)