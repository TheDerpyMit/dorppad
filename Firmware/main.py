import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.keys import KC

keyboard = KMKKeyboard()

# =====================
# BUTTONS (6 total)
# =====================
keyboard.matrix = KeysScanner(
    pins=[
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
    ],
    value_when_pressed=False,
)

# =====================
# ROTARY ENCODER
# =====================
keyboard.encoders = [
    RotaryioEncoder(
        pin_a=board.GP26,
        pin_b=board.GP27,
        resolution=2,
    )
]

# =====================
# KEYMAP
# =====================
keyboard.keymap = [
    [
        KC.A,          # SW1
        KC.B,          # SW2
        KC.C,          # SW3
        KC.D,          # SW4
        KC.E,          # SW5
        KC.MUTE,       # Encoder push button (SW)
    ]
]

# Encoder actions
keyboard.encoder_map = [
    (
        KC.VOLU,
        KC.VOLD,
    )
]

# =====================
# START
# =====================
if __name__ == "__main__":
    keyboard.go()

#i had to use chatgpt to figure this out 🥹