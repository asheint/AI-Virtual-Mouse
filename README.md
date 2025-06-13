# AI Virtual Mouse

Control your computer mouse with hand gestures using your webcam. No need to touch anything - just move your hand!

## What it does

This program lets you control your mouse cursor, click, scroll, and adjust volume using simple hand gestures. It uses your webcam to track your hand movements in real-time.

## What you need

- Python 3.7 or newer
- A webcam (built-in or USB)
- Windows (some features work on other systems too)

## How to install

1. Download or clone this project:

```bash
git clone https://github.com/asheint/AI-Virtual-Mouse.git
cd AI-Virtual-Mouse
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

That's it! You're ready to go.

## How to use

1. Run the program:

```bash
python AiVirtualMouseProject.py
```

2. A window will open showing your camera feed. You'll see your hand being tracked with dots and lines.

3. Make hand gestures to control your mouse:

**Mouse movement**: Point with just your index finger
**Left click**: Put up index and middle finger, then bring them close together
**Right click**: Put up index, middle, and ring finger, then bring them close
**Scroll**: Put up index finger and pinky, then move your index finger up/down
**Drag and drop**: Put up thumb and index finger, then move around
**Volume control**: Put up thumb and pinky, change distance between them

4. Press 'q' to quit

## Tips for better results

- Use good lighting
- Keep your hand 1-2 feet from the camera
- Try to have a plain background behind your hand
- Make clear, distinct finger positions
- If the camera doesn't work, the program will automatically try different camera numbers (0, 1, 2)

## How it works

The program detects which fingers are up (1) or down (0). For example:

- `[0,1,0,0,0]` means only index finger is up → moves mouse
- `[0,1,1,0,0]` means index and middle up → ready to click
- `[1,0,0,0,1]` means thumb and pinky up → volume control

## Common problems

**Camera not found**: Make sure no other programs are using your camera. The program tries camera indices 0, 1, 2 automatically.

**Volume control not working**: Try running as administrator.

**Gestures not detected well**: Improve lighting and use a plain background.

**Package installation errors**: Use a virtual environment or update pip.

## Files in this project

- `AiVirtualMouseProject.py` - Main program
- `HandTrackingModule.py` - Hand detection code
- `requirements.txt` - List of packages needed
- `README.md` - This file

## Settings you can change

You can edit these values in `AiVirtualMouseProject.py`:

```python
wCam, hCam = 640, 480      # Camera resolution
frameR = 100               # Mouse control area border
smoothening = 7            # How smooth mouse movement is
scroll_sensitivity = 20    # How sensitive scrolling is
```

## Contributing

Feel free to improve this project! Just fork it, make your changes, and submit a pull request.

## License

MIT License - you can use this code however you want.

## Support the project

If this project helped you, consider buying me a coffee! ☕

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/asheint)

---

Made by [Ashen Thilakarathna](https://github.com/asheint) - Hope you find it useful!
