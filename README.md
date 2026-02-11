# 🎮 LAN Multiplayer Game using Python & Pygame

A real-time 2-player LAN multiplayer game built using **Python sockets**, **multithreading**, and **Pygame**.

This project demonstrates client-server architecture, real-time position synchronization, and LAN networking.

---

## 🚀 Features

- Real-time multiplayer over LAN
- Client-server socket communication
- Multithreaded server handling
- Player boundary restriction
- Smooth 60 FPS rendering
- Lightweight and simple architecture

---

## 🧠 Technologies Used

- Python 3
- Pygame
- Socket Programming (TCP)
- Multithreading (`_thread`)

---

## 📂 Project Structure
    server.py
    client.py
    network.py
    Requirements.txt


## ⚙️ How to Run (Same WiFi / LAN)

### On Server PC

- Open server.py
- Set: server="0.0.0.0"
- Run server.py

### Find Server IP

- On Server PC in CMD run ipconfig and copy the IPv4 Address 

### On Client PC

- Open network.py and past that Server's IPv4 Address to send connection request to Server PC.
- Run client.py


***Author - Pravir Nihar Maity***
