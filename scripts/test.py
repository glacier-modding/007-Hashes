from common import GAME_FLAGS

def decode_flags(value):
    active_flags = []
    for name, mask in GAME_FLAGS.items():
        if value & mask:  # check if bit is set
            active_flags.append(name)
    return active_flags

game_flag = 38
print(f"Decimal: {game_flag}")
print("Active flags:", decode_flags(game_flag))
