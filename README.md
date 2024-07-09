# chatUwU
**chatUwU** is a simple command-line based chat application that allows communication between different PCs over a network using Python's socket programming.
This simple project demonstrates basic client-server architecture and multi-threading to handle multiple clients simultaneously.

# Features
- **Simple Setup:** Easy to set up and run using Python.
- **Multi-client Support:** Supports multiple clients communicating with each other through a single server.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

# Getting Started
**Prerequisites**

1.   Python (any 3.x+ versions) installed on all machines.

2.   Basic knowledge of using command-line interface (CMD, UwU-Terminal).

# Installation

Commands: 

> _git clone https://github.com/PhitzZ/chatUwu_

> _cd chat-cmd-uwu_

**Install dependencies**

> _pip install -r requirements.txt_

> _pip install colorama_

# Usage

**START SERVER**

1.) Open a terminal (CMD on Windows).

2.) Navigate to the project directory.

3.) Start the server by specifying the host and port:

>_python server.py 0.0.0.0 9999_

This starts the server listening on all network interfaces at port 9999.




**CONNECTING CLIENTS**

1.) Open another terminal for each client.

2.) Navigate to the project directory.

3.) Start the client by specifying the server's IP address and port:

>_python client.py <server_ip> 9999_

Replace <server_ip> with the actual IP address of the machine running the server.

Type messages in the client terminal to send them to the server, which will broadcast them to all connected clients. 

Type **exit** to disconnect.


# Example

**Server:**

>_python server.py 0.0.0.0 9999_


**Client 1:**

>_python client.py 192.168.1.100 9999_

chatUwU Interface:

![](https://pandao.github.io/editor.md/examples/images/4.jpg)



# Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.
EHE!
