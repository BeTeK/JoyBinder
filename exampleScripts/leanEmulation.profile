{"version": "1.0", "type": "expert", "code": "enterPos = 20000\n\nonJoyAxisEnters(axis(1, 1), enterPos, 100000, setKeyDown(\"q\"))\nonJoyAxisExits(axis(1, 1), enterPos, 100000, setKeyUp(\"q\"))\nonJoyAxisEnters(axis(1, 2), enterPos, 100000, setKeyDown(\"e\"))\nonJoyAxisExits(axis(1, 2), enterPos, 100000, setKeyUp(\"e\"))\nonAlways(setJoyAxis(1, 4, getJoyAxis(axis(1, 3))))", "joyMappings": {"1": "YHk9g8OK6BGAC0RFU1Q="}}