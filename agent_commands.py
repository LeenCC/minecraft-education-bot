
def blossom_walk():
    if blocks.test_for_block(GRASS, pos(0, -1, 0)):
        blocks.place(YELLOW_FLOWER, pos(1, 0, 0))
        blocks.place(OXEYE_DAISY, pos(0, 0, 0))
        blocks.place(POPPY, pos(-1, 0, 0))

def move_forward(blocks:int):
    for _ in range(blocks):
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        if agent.detect(AgentDetection.BLOCK, UP):
            agent.destroy(UP)

def turn_left():
    agent.turn(LEFT_TURN)

def turn_right():
    agent.turn(RIGHT_TURN)

def move_up(blocks:int):
    for _ in range(blocks):
        if agent.detect(AgentDetection.BLOCK, UP):
            agent.destroy(UP)
        agent.move(UP, 1)
        
def dig_down(blocks:int):
    for _ in range(blocks):
        if agent.detect(AgentDetection.BLOCK, DOWN):
            agent.destroy(DOWN)
        agent.move(DOWN, 1)

def build_tower():
    agent.teleport_to_player()
    agent.move(FORWARD, 5)
    agent.set_slot(1)
    agent.set_assist(PLACE_ON_MOVE, True)
    agent.set_assist(DESTROY_OBSTACLES, True)
    for _ in range(10):
        for _ in range(4):
            agent.set_item(SANDSTONE, 16, 1)
            agent.move(FORWARD, 4)
            agent.turn(LEFT_TURN)
        agent.move(UP, 1)

def build_wall(width:int, height:int):
    for _ in range(height):
        builder.move(FORWARD, width)
        builder.move(UP, 1)
        builder.turn(LEFT_TURN)
        builder.turn(LEFT_TURN)
    builder.trace_path(MOSSY_STONE_BRICKS)

def build_house(width:int, height:int):
    layer = 0
    roofLayers = 0
    j = 0
    builder.teleport_to(pos(0, -1, -5))
    while j <= height - 1:
        builder.move(UP, 1)
        builder.mark()
        for _ in range(4):
            builder.move(FORWARD, width - 1)
            builder.turn(LEFT_TURN)
        builder.trace_path(STONE)
        j += 1
    builder.shift(-1, 1, -1)
    if width % 2 == 0:
        roofLayers = width / 2 - 1
    else:
        roofLayers = width / 2
    while layer <= roofLayers + 1:
        builder.mark()
        for _ in range(4):
            builder.move(FORWARD, width + 1 - layer * 2)
            builder.turn(LEFT_TURN)
        builder.trace_path(PLANKS_OAK)
        builder.shift(1, 1, 1)
        layer += 1
    builder.move(DOWN, roofLayers + height + 2)
    builder.mark()
    builder.move(FORWARD, width / 2 + 1)
    builder.move(UP, 1)
    builder.fill(AIR)
    builder.shift(width * -1 + 1, 0, width / 2 - 1)
    builder.place(GLASS)
    builder.move(RIGHT, width - 1)
    builder.place(GLASS)

def build_pyramid(size:int):
    if size > 0:
        agent.set_item(SANDSTONE, size * size, 1)
        agent.set_slot(1)
        agent.set_assist(PLACE_ON_MOVE, True)
        i = 0
        while i <= 4 - 1:
            agent.move(FORWARD, size)
            agent.turn(LEFT_TURN)
            i += 1
        agent.move(UP, 1)
        agent.set_assist(PLACE_ON_MOVE, False)
        agent.move(FORWARD, 1)
        player.run_chat_command("pyramid " + ("" + str((size - 2))))

def build_cave():
    agent.teleport_to_player()
    for _ in range(10):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
    bat_cave = agent.get_position()
    agent.destroy(FORWARD)
    agent.set_item(TNT, 1, 1)
    agent.place(FORWARD)
    agent.set_item(REDSTONE_WIRE, 10, 1)
    for _ in range(9):
        agent.move(BACK, 1)
        agent.place(FORWARD)
    agent.set_item(LEVER, 1, 1)
    agent.move(BACK, 1)
    agent.place(FORWARD)
    agent.interact(FORWARD)
    loops.pause(10000)
    for _ in range(200):
        mobs.spawn(BAT, bat_cave)


def earthquake():
    center = positions.add(player.position(), pos(-30, 0, 0))
    for _ in range(30):
        center = positions.add(center, pos(1, 0, Math.random_range(0, 2)))
        blocks.fill(AIR,
            positions.add(center, pos(0, 0, -1)),
            positions.add(center, pos(0, -4, 1)),
            FillOperation.REPLACE)
        blocks.place(LAVA, positions.add(center, pos(0, -3, 0)))



player.on_travelled(WALK, blossom_walk)

player.on_chat("fd", move_forward)
player.on_chat("lt", turn_left)
player.on_chat("rt", turn_right)
player.on_chat("up", move_up)
player.on_chat("down", dig_down)

player.on_chat("cave", build_cave)
player.on_chat("wall", build_wall)
player.on_chat("house", build_house)
player.on_chat("pyramid", build_pyramid)
player.on_chat("tower", build_tower)

player.on_chat("earthquake", earthquake)

