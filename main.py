from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

from panda3d.core import WindowProperties, AmbientLight, Vec4, DirectionalLight


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.disableMouse()

        # Load the environment model
        self.environment = loader.loadModel("Models/Misc/Environment/environment")
        # Attach it to Parent NodePath - global render NodePath
        self.environment.reparentTo(render)

        # Load the actor and attach
        self.tempActor = Actor(
            "Models/models/act_p3d_chan", {"walk": "Models/models/a_p3d_chan_run"}
        )
        self.tempActor.reparentTo(render)

        self.tempActor.setPos(0, 0, 0)
        self.tempActor.getChild(0).setH(90)
        self.tempActor.loop("walk")

        # Lighting

        # AmbientLight returs Node
        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))

        # This time we take the parent NodePath and attach the node to it.
        # `parent.attachNewNode(node)` returns the NodePath of the node
        self.ambientLightNodePath = render.attachNewNode(ambientLight)

        # Indicate which nodes we want to affect. In this case `render` NodePath
        render.setLight(self.ambientLightNodePath)

        # This is direction light
        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = render.attachNewNode(mainLight)
        # Turn it around by 45 degrees, and tilt it down by 45 degrees
        self.mainLightNodePath.setHpr(45, -45, 0)
        render.setLight(self.mainLightNodePath)

        render.setShaderAuto()

        # Move the camera to a position high above the screen
        # --that is, offset it along the z-axis.
        self.camera.setPos(0, 0, 32)
        # Tilt the camera down by setting its pitch.
        self.camera.setP(-90)


game = Game()
game.run()
