# とりま iphone se でSCした画像から
# iphonese settings
# SOURCE_IMG_W = 750
# SOURCE_IMG_H = 1623
# OFFSET_X = 30
# OFFSET_Y = 435
# TROOPS_SIZE_W = 95
# TROOPS_SIZE_H = 149

# Huawei P30 Pro settings
SOURCE_IMG_W = 1080
SOURCE_IMG_H = 2340
OFFSET_X = 84
OFFSET_Y = 720
TROOPS_SIZE_W = 140
TROOPS_SIZE_H = 198



formation_array = [ 
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
    ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
]

# 表示座標から 7x7 キャラクタ位置を返す
def calc_disploc2charloc(disp_loc_x, disp_loc_y):
    x = int(((disp_loc_x+TROOPS_SIZE_W/2) - OFFSET_X) / TROOPS_SIZE_W)
    y = int(((disp_loc_y+TROOPS_SIZE_H/2) - OFFSET_Y) / TROOPS_SIZE_H)
    return x, y

def set_char(loc_x, loc_y, troop):
    if loc_x >= 0 and loc_x <= 6 and loc_y >= 0 and loc_y <= 6:
        formation_array[loc_x][loc_y] = troop

def get_formation_array():
    return formation_array

def print_formation():
    for y in range(0,7):
        line_char = ""
        for x in range(0,7):
            line_char += (formation_array[x][y] + " ")
        print(line_char)