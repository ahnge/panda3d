from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.actor.Actor import Actor


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.disableMouse()

        # Load the environment model
        self.environment = loader.loadModel("Models/Misc/Environment/environment")
        # Attach it to Parent NodePath - global render variable
        self.environment.reparentTo(render)

        # Load the actor and attach
        self.tempActor = Actor(
            "Models/models/act_p3d_chan", {"walk": "Models/models/a_p3d_chan_run"}
        )
        self.tempActor.reparentTo(render)

        self.tempActor.setPos(0, 0, 0)
        self.tempActor.getChild(0).setH(90)
        self.tempActor.loop("walk")

        # Move the camera to a position high above the screen
        # --that is, offset it along the z-axis.
        self.camera.setPos(0, 0, 32)
        # Tilt the camera down by setting its pitch.
        self.camera.setP(-90)


game = Game()
game.run()
