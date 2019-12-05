from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import LerpHprInterval, Func, Sequence


def createCube(parent, x, y, z, position, cubeMembership, walls):

    vertexFormat = GeomVertexFormat.getV3n3cp()
    vertexData = GeomVertexData("cube_data", vertexFormat, Geom.UHStatic)
    tris = GeomTriangles(Geom.UHStatic)

    posWriter = GeomVertexWriter(vertexData, "vertex")
    colWriter = GeomVertexWriter(vertexData, "color")
    normalWriter = GeomVertexWriter(vertexData, "normal")

    vertexCount = 0

    for direction in (-1, 1):

        for i in range(3):

            normal = VBase3()
            normal[i] = direction
            rgb = [0., 0., 0.]
            rgb[i] = 1.

            if direction == 1:
                rgb[i-1] = 1.

            r, g, b = rgb
            color = (r, g, b, 1.)

            for a, b in ( (-1., -1.), (-1., 1.), (1., 1.), (1., -1.) ):

                pos = VBase3()
                pos[i] = direction
                pos[(i + direction) % 3] = a
                pos[(i + direction * 2) % 3] = b

                posWriter.addData3f(pos)
                colWriter.addData4f(color)
                normalWriter.addData3f(normal)

            vertexCount += 4

            tris.addVertices(vertexCount - 2, vertexCount - 3, vertexCount - 4)
            tris.addVertices(vertexCount - 4, vertexCount - 1, vertexCount - 2)

    geom = Geom(vertexData)
    geom.addPrimitive(tris)
    node = GeomNode("cube_node")
    node.addGeom(geom)
    cube = parent.attachNewNode(node)
    cube.setScale(.4)
    cube.setPos(x, y, z)
    membership = set() # the walls this cube belongs to
    position[cube] = [x, y, z]
    cubeMembership[cube] = membership
    # In Panda3D, X axis straightly points to right.
    # Y axis goes inside perpendicular to the screen.
    # Z axis is pointing up.


    if x == 1:
        walls["right"].append(cube)
        membership.add("right")
    elif x == -1:
        walls["left"].append(cube)
        membership.add("left")
    elif x == 0:
        walls["center"].append(cube)
        membership.add("center")

    if y == 1:
        walls["back"].append(cube)
        membership.add("back")
    elif y == -1:
        walls["front"].append(cube)
        membership.add("front")
    elif y==0:
        walls["standing"].append(cube)
        membership.add("standing")

    if z == -1:
        walls["down"].append(cube)
        membership.add("down")
    elif z == 1:
        walls["up"].append(cube)
        membership.add("up")
    elif z==0:
        walls["equator"].append(cube)
        membership.add("equator")

    return cube

class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)


        walls = {}
        pivots = {}
        rotations = {}
        position = {}
        cubeMembership = {}
        #Equator slice is the slice between up and down faces, center slice between left and right faces, standing slice the left one,
        wallIDs = ("front", "back", "left", "right", "down", "up", "equator", "center", "standing")
        hprs = {}
        # VBase(Z,X,Y) if spin around Z, VBase3(90., 0., 0.).
        # The degree is positive following the right hand rule.
        hprs["right"] = VBase3(0., -90., 0.)
        hprs["center"] = VBase3(0., -90., 0.) # The ratation direction of the standing slice follows the front face.
        hprs["left"] = VBase3(0., 90., 0.)
        hprs["back"] = VBase3(0., 0., -90.)
        hprs["front"] = VBase3(0., 0., 90.)
        hprs["standing"] = VBase3(0., 0., 90.)# The ratation direction of the center slice follows the right face.
        hprs["down"] = VBase3(90., 0., 0.)
        hprs["up"] = VBase3(-90., 0., 0.)
        hprs["equator"] = VBase3(-90., 0., 0.) # The ratation direction of the equator slice follows the up face.
        wallRotate = {}
        wallNegRotate = {}
        # Each rotation is a matrix.
        # The positive front rotation and the negative back rotation have the same matrix.
        # The standing slice follows the rules of the front face.

        wallRotate["right"] = wallRotate["center"] = wallNegRotate["left"] = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
        wallRotate["left"] = wallNegRotate["right"] = wallNegRotate["center"] = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]

        wallRotate["back"] = wallNegRotate["standing"] = wallNegRotate["front"] = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
        wallRotate["front"] = wallRotate["standing"] = wallNegRotate["back"] = [[0, 0, -1], [0, 1, 0], [1, 0, 0]]

        wallRotate["up"] = wallRotate["equator"] = wallNegRotate["down"] = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        wallRotate["down"] = wallNegRotate["equator"] = wallNegRotate["up"] = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]


        for wallID in wallIDs:
            walls[wallID] = []
            pivots[wallID] = self.render.attachNewNode('pivot_%s' % wallID)
            rotations[wallID] = {"hpr": hprs[wallID]}
        #print walls
        #print pivots
        #print rotations
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                for z in (-1, 0, 1):
                    createCube(self.render, x, y, z, position, cubeMembership, walls)

        self.directionalLight = DirectionalLight('directionalLight')
        self.directionalLightNP = self.cam.attachNewNode(self.directionalLight)
        self.directionalLightNP.setHpr(20., -20., 0.)
        self.render.setLight(self.directionalLightNP)
        self.cam.setPos(7., -10., 4.)
        self.cam.lookAt(0., 0., 0.)


app = MyApp()
app.run()
