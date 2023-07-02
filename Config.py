from panda3d.core import ConfigVariableInt

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
