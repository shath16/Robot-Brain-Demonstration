# 🤖 AI Robot Brain Simulator (Simulated Sensor Fusion with YOLO)

## 📖 Overview

This project implements a simulated autonomous robot decision system that demonstrates how AI vision and sensor data can be combined to guide robot navigation.

The system simulates a robot's perception pipeline by integrating:

* Simulated YOLO-based object detection
* Simulated ultrasonic distance sensing
* Rule-based decision logic

Instead of using real hardware or live camera input, predefined scenarios are used to emulate environmental conditions, allowing safe testing and development of robot navigation behaviour.

---

## 🧠 Key Concepts

* Simulated AI perception using YOLO framework structure
* Sensor fusion principles (vision + distance sensors)
* Priority-based safety decision making
* Autonomous navigation logic design
* Robotics control architecture simulation

---

## ⚙️ How It Works

The robot processes simulated sensor data through a decision pipeline:

1️⃣ **Ultrasonic Safety Check**

* Emergency stop triggered if an object is too close.

2️⃣ **Vision-Based Analysis**

* Simulated object detection identifies obstacles and positions.

3️⃣ **Decision Layer**

* Move forward when path is clear.
* Stop and turn when obstacles appear in front.
* Emergency stop when safety threshold is exceeded.

---

## 🎓 Purpose

This project demonstrates foundational robotics and AI navigation concepts, focusing on how autonomous systems integrate multiple sensor inputs to make safe movement decisions.

---

## 🚀 Future Improvements

* Real-time camera integration using YOLO
* Real ultrasonic sensor hardware
* Motor control and physical robot movement
* ROS-style modular robot architecture


👉 *“make it look pro”*.
