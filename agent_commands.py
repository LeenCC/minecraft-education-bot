def on_on_chat(width2, height2):
    global j, roofLayers, layer
    builder.teleport_to(pos(0, -1, -5))
    while j <= height2 - 1:
        builder.move(UP, 1)
        builder.mark()
        for index in range(4):
            builder.move(FORWARD, width2 - 1)
            builder.turn(LEFT_TURN)
        builder.trace_path(STONE)
        j += 1
    builder.shift(-1, 1, -1)
    if width2 % 2 == 0:
        roofLayers = width2 / 2 - 1
    else:
        roofLayers = width2 / 2
    while layer <= roofLayers + 1:
        builder.mark()
        for index2 in range(4):
            builder.move(FORWARD, width2 + 1 - layer * 2)
            builder.turn(LEFT_TURN)
        builder.trace_path(PLANKS_OAK)
        builder.shift(1, 1, 1)
        layer += 1
    builder.move(DOWN, roofLayers + height2 + 2)
    builder.mark()
    builder.move(FORWARD, width2 / 2 + 1)
    builder.move(UP, 1)
    builder.fill(AIR)
    builder.shift(width2 * -1 + 1, 0, width2 / 2 - 1)
    builder.place(GLASS)
    builder.move(RIGHT, width2 - 1)
    builder.place(GLASS)
player.on_chat("house", on_on_chat)

def on_on_chat2(size):
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
player.on_chat("pyramid", on_on_chat2)

def on_on_chat3():
    agent.turn(RIGHT_TURN)
player.on_chat("rt", on_on_chat3)

def on_on_chat4(blocks23):
    for index3 in range(blocks23):
        if agent.detect(AgentDetection.BLOCK, UP):
            agent.destroy(UP)
        agent.move(UP, 1)
player.on_chat("up", on_on_chat4)

def on_on_chat5():
    global bat_cave
    agent.teleport_to_player()
    for index4 in range(10):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
    bat_cave = agent.get_position()
    agent.destroy(FORWARD)
    agent.set_item(TNT, 1, 1)
    agent.place(FORWARD)
    agent.set_item(REDSTONE_WIRE, 10, 1)
    for index5 in range(9):
        agent.move(BACK, 1)
        agent.place(FORWARD)
    agent.set_item(LEVER, 1, 1)
    agent.move(BACK, 1)
    agent.place(FORWARD)
    agent.interact(FORWARD)
    loops.pause(10000)
    for index6 in range(200):
        mobs.spawn(BAT, bat_cave)
player.on_chat("cave", on_on_chat5)

def on_on_chat6(blocks2):
    for index7 in range(blocks2):
        if agent.detect(AgentDetection.BLOCK, DOWN):
            agent.destroy(DOWN)
        agent.move(DOWN, 1)
player.on_chat("down", on_on_chat6)

def on_on_chat7(width, height):
    for index8 in range(height):
        builder.move(FORWARD, width)
        builder.move(UP, 1)
        builder.turn(LEFT_TURN)
        builder.turn(LEFT_TURN)
    builder.trace_path(MOSSY_STONE_BRICKS)
player.on_chat("wall", on_on_chat7)

def on_travelled_walk():
    if blocks.test_for_block(GRASS, pos(0, -1, 0)):
        blocks.place(YELLOW_FLOWER, pos(1, 0, 0))
        blocks.place(OXEYE_DAISY, pos(0, 0, 0))
        blocks.place(POPPY, pos(-1, 0, 0))
player.on_travelled(WALK, on_travelled_walk)

def on_on_chat8():
    global location
    location = positions.add(player.position(), pos(1, 0, 0))
    for index9 in range(10):
        for value in rainbow:
            blocks.place(value, location)
            location = positions.add(location, pos(0, 1, 0))
player.on_chat("rainbow", on_on_chat8)

def on_on_chat9(blocks22):
    for index10 in range(blocks22):
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        if agent.detect(AgentDetection.BLOCK, UP):
            agent.destroy(UP)
player.on_chat("fd", on_on_chat9)

def on_on_chat10():
    global center
    center = positions.add(player.position(), pos(-30, 0, 0))
    for index11 in range(30):
        center = positions.add(center, pos(1, 0, Math.random_range(0, 2)))
        blocks.fill(AIR,
            positions.add(center, pos(0, 0, -1)),
            positions.add(center, pos(0, -4, 1)),
            FillOperation.REPLACE)
        blocks.place(LAVA, positions.add(center, pos(0, -3, 0)))
player.on_chat("earthquake", on_on_chat10)

def on_on_chat11():
    agent.teleport_to_player()
    agent.move(FORWARD, 5)
    agent.set_slot(1)
    agent.set_assist(PLACE_ON_MOVE, True)
    agent.set_assist(DESTROY_OBSTACLES, True)
    for index12 in range(10):
        for index13 in range(4):
            agent.set_item(SANDSTONE, 16, 1)
            agent.move(FORWARD, 4)
            agent.turn(LEFT_TURN)
        agent.move(UP, 1)
player.on_chat("tower", on_on_chat11)

def on_on_chat12():
    agent.turn(LEFT_TURN)
player.on_chat("lt", on_on_chat12)

def on_item_interacted_apple():
    mobs.clear_effect(mobs.target(LOCAL_PLAYER))
player.on_item_interacted(APPLE, on_item_interacted_apple)

center: Position = None
location: Position = None
bat_cave: Position = None
layer = 0
roofLayers = 0
j = 0
rainbow: List[number] = []
rainbow = [RED_CONCRETE,
    ORANGE_CONCRETE,
    YELLOW_CONCRETE,
    LIME_CONCRETE,
    GREEN_CONCRETE,
    LIGHT_BLUE_CONCRETE,
    BLUE_CONCRETE,
    MAGENTA_CONCRETE,
    PURPLE_CONCRETE,
    PINK_CONCRETE]
