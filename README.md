# 🚗 ROS 2 Autonomous Vehicle Architecture & Control System

<div align="left">
  <img src="https://img.shields.io/badge/ROS%202-Humble%20%7C%20Foxy-22314E?style=for-the-badge&logo=ros&logoColor=white" alt="ROS 2">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Under%20Development-success?style=for-the-badge" alt="Status">
</div>

<br>

## 🌟 Overview
This repository serves as a foundational software architecture for Autonomous Driving Systems and Advanced Driver Assistance Systems (ADAS) using **ROS 2 (Robot Operating System)**. It is designed to bridge the gap between isolated path-planning algorithms and real-time, scalable vehicle integration.

### Why ROS 2 in Autonomous Vehicles?
In the modern automotive and defense industries, a self-driving car is not a single script. It is a complex network of independent micro-systems (Cameras, LiDARs, Path Planners, Motor Controllers) running simultaneously. **ROS 2** is the industry-standard middleware that allows these systems to communicate securely, in real-time, and without crashing the entire vehicle if one single module fails. It provides the robust Publish/Subscribe architecture required for mission-critical autonomous navigation.

---

## 🏗️ System Architecture & Features
This project simulates a complete end-to-end autonomous driving pipeline, transitioning theoretical algorithms into a node-based ecosystem. The following features are being implemented:

* **🧠 Central Vehicle Brain (Decision Node):** The core decision-making unit. It subscribes to multiple sensor topics, processes the environment, and dictates the vehicle's high-level state.
* **📡 Sensor Fusion & Perception (Publishers):** Nodes dedicated to broadcasting simulated hardware data into the ROS 2 network (e.g., LiDAR distance broadcasts, Camera object detection arrays).
* **⚙️ Control & Path Planning Integration:** Wrapping advanced geometric and optimal control algorithms (such as Pure Pursuit, Stanley, or LQR) into autonomous ROS 2 Nodes that actively publish steering and acceleration commands (`/cmd_vel`).
* **🛑 Emergency Intervention (ROS 2 Services):** Implementing synchronous Request-Response service calls for critical safety overrides, such as Automatic Emergency Braking (AEB).
* **🎛️ Dynamic Parameter Management:** Utilizing the ROS 2 Parameter Server for real-time tuning of vehicle constraints (e.g., maximum velocity, steering limits, lookahead distances) without recompiling the system.
* **📨 Custom Interface Definitions:** Creating custom `.msg` and `.srv` files tailored for specific vehicle telemetry and sensor fusion data structures.

---

## 🛠️ Tech Stack & Concepts Covered
- **Framework:** ROS 2 (rclpy)
- **Architecture:** Publish/Subscribe Pattern, ROS 2 Services, Parameter Server, Node Composition
- **Target Domains:** Sensor Fusion, Embedded AI Integration, Autonomous Navigation, ADAS

---

## 🚀 Getting Started

### Prerequisites
- Ubuntu 22.04 / 20.04
- ROS 2 (Humble or Foxy) installed
- Python 3.x

### Build & Run
```bash
# Clone the repository into your ROS 2 workspace
cd ~/ros2_ws/src
git clone [https://github.com/recepyalcinkaya/ROS2-Autonomous-Driving-Foundations.git](https://github.com/recepyalcinkaya/ROS2-Autonomous-Driving-Foundations.git)

# Build the package
cd ~/ros2_ws
colcon build --packages-select autonomous_driving_pkg

# Source the environment
source install/setup.bash

# Run the nodes (in separate terminals)
ros2 run autonomous_driving_pkg vehicle_brain
ros2 run autonomous_driving_pkg sensor_publisher
