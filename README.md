# Coordinate Generator & Socket Communication Project

## 📌 Overview
This project demonstrates how to generate geographical coordinate data using Python and transfer that data between two programs using socket communication (client-server model).

- Coordinate generation simulates longitude and latitude values.
- A server listens on a port and accepts incoming data.
- A client generates coordinates and sends them to the server.

---

## 📂 Project Structure
```
project-folder/
├── generate_float_coords.py  # Coordinate generator script
├── server.py                 # Socket server script
├── client.py                 # Socket client script
└── README.md                 # Project documentation
```

---

## ⚙️ Requirements
- Python 3.x

If Python isn't installed:
```bash
brew install python
```

---

## 📍 Coordinate Generator
File: `generate_float_coords.py`

Generates an array of coordinate pairs (longitude, latitude) using random floats within valid ranges:
- Longitude: `-180` to `180`
- Latitude: `-90` to `90`

### Example Output:
```python
Generated Coordinates:
[(-73.56, 45.50), (151.21, -33.86), ...]
```

---

## 🔌 Socket Communication

### Server
File: `server.py`
- Listens for incoming client connections on a specified port.
- Receives coordinate data in JSON format.
- Prints the data.

### Client
File: `client.py`
- Imports coordinate generator.
- Sends generated coordinates to the server via socket.

### Running Locally
1. Open Terminal #1:
```bash
python3 server.py
```
2. Open Terminal #2:
```bash
python3 client.py
```

### Example Server Output:
```
Connected by ('127.0.0.1', 56342)
Received Coordinates:
Point 0: Longitude -73.56, Latitude 45.50
...
```

---

## 🌐 Find Your Local IP Address
```bash
ipconfig getifaddr en0
```
Use this IP if you want to test on multiple devices in your local network.

---

## ✅ Future Improvements
- Add graceful shutdown functionality to the server.
- Enable two-way communication.
- Store data to file or database.
- Visualize coordinates on a map.

---

## 📧 Contact
Feel free to reach out if you need help or enhancements!

---

Happy Coding! 🚀

