# Unrestricted-Resource-Consumption

## Overview
This project focuses on addressing **OWASP Top 10 API Security Risks** for the year 2023. Specifically, it targets the issue of **Unrestricted Resource Consumption**. In this README, we delve into the scenario of a **GraphQL API Endpoint** allowing users to upload profile pictures, which inherently poses risks associated with Unrestricted Resource Consumption 🚀🔒👨‍💻.


## Features
- Web server implementation using **Apache** in **Ubuntu** within a **VMware** environment.
- Python script creation for simulating attacks on the server.
- Simulated scenarios:
  - Continuous session creation leading to server downtime.
  - Uninterrupted download from the server.
  - Ceaseless upload to the server.

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Ensure you have **Apache2** installed on your Ubuntu server.

3. Set up the network between the Ubuntu server in VMware and your local Windows machine.

## Usage
1. Start the Apache server on Ubuntu:

    ```bash
    sudo service apache2 start
    ```

2. Run the Python script for simulating attacks. Modify the script according to your specific scenario requirements.

    ```bash
    python data.py
    script_scnario_3
    session_2
    ```

3. Monitor server performance and behavior during attacks.

## Configuration
Ensure that Apache server configurations are appropriately set to handle potential resource consumption issues. Implement throttling mechanisms or request limiting where necessary.


## Note
In this project, I primarily focused on addressing one of the three scenarios outlined in **OWASP's Scenario #2**. Specifically, the scenario revolves around a **GraphQL API Endpoint** allowing users to upload profile pictures, which inherently poses risks related to Unrestricted Resource Consumption.

