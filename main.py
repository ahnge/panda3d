from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

from math import pi, sin, cos


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        # Create the lerp intervals needed for the panda to
        # walk in square.
        walkForwardToNY = self.pandaActor.posInterval(
            5, Point3(0, -5, 0), startPos=Point3(0, 5, 0)
        )
        turnLeftInterval1 = self.pandaActor.hprInterval(
            2, Point3(90, 0, 0), startHpr=Point3(0, 0, 0)
        )
        walkForwardToPX = self.pandaActor.posInterval(
            5, Point3(10, -5, 0), startPos=Point3(0, -5, 0)
        )
        turnLeftInterval2 = self.pandaActor.hprInterval(
            2, Point3(180, 0, 0), startHpr=Point3(90, 0, 0)
        )
        walkForwardToPY = self.pandaActor.posInterval(
            5, Point3(10, 5, 0), startPos=Point3(10, -5, 0)
        )
        turnLeftInterval3 = self.pandaActor.hprInterval(
            2, Point3(270, 0, 0), startHpr=Point3(180, 0, 0)
        )
        walkForwardToNX = self.pandaActor.posInterval(
            5, Point3(0, 5, 0), startPos=Point3(10, 5, 0)
        )
        turnLeftInterval4 = self.pandaActor.hprInterval(
            2, Point3(360, 0, 0), startHpr=Point3(270, 0, 0)
        )

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(
            walkForwardToNY,
            turnLeftInterval1,
            walkForwardToPX,
            turnLeftInterval2,
            walkForwardToPY,
            turnLeftInterval3,
            walkForwardToNX,
            turnLeftInterval4,
            name="pandaPace",
        )
        self.pandaPace.loop()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
