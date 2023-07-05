from panda3d.core import ConfigVariableInt
from Color import ColorGroup
from Map import Map, MapNode


min_pos_x = ConfigVariableInt('min-pos-x', -1000).getValue()
max_pos_x = ConfigVariableInt('max-pos-x', 1000).getValue()
min_pos_y = ConfigVariableInt('min-pos-y', 1000).getValue()
max_pos_y = ConfigVariableInt('max-pos-y', 5000).getValue()
min_pos_z = ConfigVariableInt('min-pos-z', -1000).getValue()
max_pos_z = ConfigVariableInt('max-pos-z', 1000).getValue()
min_hpr_x = ConfigVariableInt('min-hpr-x', -100).getValue()
max_hpr_x = ConfigVariableInt('max-hpr-x', 300).getValue()
min_hpr_y = ConfigVariableInt('min-hpr-y', -25).getValue()
max_hpr_y = ConfigVariableInt('max-hpr-y', 25).getValue()
rotate_time = ConfigVariableInt('rotate-time', 5).getValue()

color_groups = {
    "Blue": ColorGroup("Blue", (13, 152, 186), (13, 81, 118), (93, 53, 252), (47, 10, 196)),
    "Green": ColorGroup("Green", (37, 162, 43), (1, 113, 1), (14, 115, 17), (2, 82, 5)),
    "Yellow": ColorGroup("Yellow", (255, 223, 0), (215, 242, 78), (218, 255, 28)),
    "White": ColorGroup("White", (248, 245, 250), (245, 247, 230)),
    "Brown": ColorGroup("Brown", (136, 104, 73), (136, 104, 73), (94, 72, 30), (84, 42, 14),
                        (99, 57, 15)),
    "Sand": ColorGroup("Sand", (246, 215, 176), (242, 210, 169), (231, 196, 150),
                       (225, 191, 146)),
    "Black": ColorGroup("Black", (19, 28, 27), (8, 7, 10), (29, 28, 31)),
    "Purple": ColorGroup("Purple", (82, 47, 129), (139, 139, 219), (48, 37, 95), (95, 44, 163),
                         (67, 13, 140)),
    "Gray": ColorGroup("Gray", (89, 82, 90), (171, 167, 181), (207, 205, 212)),
    "Light Blue": ColorGroup("Light Blue", (96, 194, 240), (22, 222, 240), (126, 228, 237),
                             (73, 112, 184)),
    "Dark Green": ColorGroup("Dark Green", (7, 38, 16), (8, 18, 11), (3, 43, 23)),
    "Red": ColorGroup("Red", (245, 41, 22), (163, 45, 34)),
    "Skin Color": ColorGroup("Skin Color", (141, 85, 36), (198, 134, 66), (224, 172, 105))
}

maps = [
    # Sunny Day
    Map(MapNode(color_groups["Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, 0.7, 0.75),
        MapNode(color_groups["Yellow"], 0.5, 1, 0.5, 1),
        MapNode(color_groups["Yellow"], -1, 1, -0.5, -0.35),
        MapNode(color_groups["Red"], -1, 1, -0.5, -0.35),
        MapNode(color_groups["White"], -1, 1, 0.2, 0.75),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Brown"], -1, 1, -0.5, 0.5),
        fuzz=0.25, weight=60, name="Sunny Day"
        ),
    # Desert
    Map(MapNode(color_groups["Light Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Light Blue"], -1, 1, -0.4, 1),
        MapNode(color_groups["Sand"], -1, 1, -1, -0.35),
        MapNode(color_groups["Sand"], -1, 1, -1, -0.35),
        MapNode(color_groups["Gray"], -1, 1, -1, -0.35),
        MapNode(color_groups["Yellow"], -1, -0.5, 0.5, 1),
        MapNode(color_groups["White"], -1, 1, 0.2, 0.75),
        MapNode(color_groups["Black"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Black"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        MapNode(color_groups["Green"], -1, 1, -0.5, 0.5),
        fuzz=0.25, weight=60, name="Desert"
        ),
    # Stormy
    Map(MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Purple"], -1, 1, -0.4, 1),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Green"], -1, 1, -1, -0.35),
        MapNode(color_groups["Dark Green"], -1, 1, -0.55, -0.35),
        MapNode(color_groups["Gray"], -1, 1, 0.2, 0.75),
        MapNode(color_groups["Yellow"], -1, 1, -0.5, 0.6),
        MapNode(color_groups["Black"], -1, 1, 0.4, 1),
        fuzz=0.25, weight=60, name="Stormy"
        ),
    # Mountain
    Map(MapNode(color_groups["Gray"], -0.75, 0.75, -1, -0.75),
        MapNode(color_groups["Black"], -0.5, 0.5, -1, -0.75),
        MapNode(color_groups["Gray"], -0.65, 0.65, -0.75, -0.5),
        MapNode(color_groups["Gray"], -0.5, 0.5, -0.5, -0.25),
        MapNode(color_groups["Gray"], -0.25, 0.25, -0.25, 0),
        MapNode(color_groups["Gray"], -0.1, 0.1, 0, 0.25),
        MapNode(color_groups["Gray"], -0.75, 0.75, -1, -0.75),
        MapNode(color_groups["Gray"], -0.65, 0.65, -0.75, -0.5),
        MapNode(color_groups["Gray"], -0.5, 0.5, -0.5, -0.25),
        MapNode(color_groups["Gray"], -0.25, 0.25, -0.25, 0),
        MapNode(color_groups["Gray"], -0.1, 0.1, 0, 0.25),
        MapNode(color_groups["Gray"], -0.75, 0.75, -1, -0.75),
        MapNode(color_groups["Gray"], -0.65, 0.65, -0.75, -0.5),
        MapNode(color_groups["Gray"], -0.5, 0.5, -0.5, -0.25),
        MapNode(color_groups["Gray"], -0.25, 0.25, -0.25, 0),
        MapNode(color_groups["Gray"], -0.1, 0.1, 0, 0.25),
        MapNode(color_groups["Blue"], -1, 1, -1, 1),
        MapNode(color_groups["Yellow"], -0.25, 0.25, 0.6, 1),
        MapNode(color_groups["White"], -1, -0.5, 0, 0.5),
        MapNode(color_groups["White"], 0.5, 1, 0, 0.5),
        MapNode(color_groups["Purple"], -1, 1, -1, 0.25),
        fuzz=0.15, weight=60, name="Mountain"
        ),
    # Love Heart
    Map(MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Red"], -0.05, 0.05, -0.6, -0.5),
        MapNode(color_groups["Red"], -0.15, 0.15, -0.5, -0.25),
        MapNode(color_groups["Red"], -0.35, 0.35, -0.25, 0),
        MapNode(color_groups["Red"], -0.6, -0.35, 0, 0.25),
        MapNode(color_groups["Red"], -0.55, -0.25, 0.25, 0.5),
        MapNode(color_groups["Red"], 0.35, 0.6, 0, 0.25),
        MapNode(color_groups["Red"], 0.3, 0.5, 0.25, 0.5),
        MapNode(color_groups["Light Blue"], -1, 1, -1, 1),
        MapNode(color_groups["Gray"], -1, 1, -1, 1),
        MapNode(color_groups["White"], 0.65, 0.75, 0.5, 0.65),
        fuzz=0.15, weight=60, name="Love Heart"
        )
]
