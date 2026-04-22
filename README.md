# WeApRous - Lightweight Python Web Framework & Proxy

## Overview
WeApRous is a custom-built, dependency-free Python web framework and reverse proxy server. Originally designed for educational purposes (CO3093/CO3094 course at HCMUT), it provides a robust foundation for building RESTful APIs, peer-to-peer trackers, and load-balanced proxy architectures utilizing only Python's built-in `socket` and `threading` standard libraries.

## Key Features
* **Decorator-Based Routing:** Easily map HTTP methods and URLs to specific Python functions using the intuitive `@app.route` decorator.
* **Reverse Proxy & Load Balancing:** Includes a built-in proxy server capable of forwarding requests to multiple backend servers using a "round-robin" distribution policy.
* **Middleware Support:** Allows developers to intercept incoming requests for tasks like cookie-based authentication before they hit the main route logic.
* **Zero External Dependencies:** Runs purely on Python standard libraries, eliminating the need for `pip install` or virtual environments.
* **Multithreaded:** Spawns individual threads for each client connection to handle concurrent HTTP requests efficiently.

## Installation
Because WeApRous relies entirely on standard Python libraries, no additional dependencies are required. Just clone the repository and run the scripts directly.

## How to Run

To run the complete architecture, you need to configure your proxy settings, start your backend server(s), and then launch the proxy server.

### 1. Configure the Proxy
Before starting the proxy, define your routing rules and load balancing policies in the configuration file located at `config/proxy.conf`. 

### 2. Start the Proxy
`python start_proxy.py`

### 2. Start the Backend Server
Run your backend application by specifying the IP address and port it should listen on. You can spawn multiple backend instances on different ports if you are using the proxy for load balancing.
* `python start_backend.py --server-ip <your_ip> --server-port <your_port>`
