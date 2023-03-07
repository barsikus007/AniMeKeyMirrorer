from functools import partial

from pynput.keyboard import Key, KeyCode, Listener

from buffer import Buffer


def on_press(key: KeyCode, buffer: Buffer, debug=False):
    """
    place to test
    """
    if hasattr(key, "char") and key.char and len(key.char) == 1:
        buffer.add(key.char)
    elif key == Key.space:
        buffer.add(" ")
    elif key == Key.enter:
        buffer.add("\n")
    elif key == Key.backspace:
        buffer.pop()
    else:
        if debug:
            print(f"!{key}!")
        return
    buffer.show()


with Listener(on_press=partial(on_press, buffer=Buffer())) as listener:  # type: ignore
    try:
        listener.join()
    except KeyboardInterrupt:
        print("KIss")
