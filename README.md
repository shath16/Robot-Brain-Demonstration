# 🤖 AI Robot Brain Simulator

### Simulated Perception Pipeline with YOLO and Sensor Fusion

---

## 📖 Overview

This project implements a simulated autonomous robot decision system that demonstrates how AI perception and sensor data can be combined to guide navigation behaviour.

The system models a **simulated perception pipeline**, inspired by real robotics architectures, where multiple sensor inputs are processed and prioritised to produce safe movement decisions.

Rather than using real hardware or live camera feeds, predefined scenarios simulate environmental conditions, allowing controlled testing and development of robot decision logic.

---

## 🧠 Key Concepts

* Simulated perception pipeline
* AI vision framework integration (Ultralytics YOLO)
* Sensor fusion principles
* Rule-based autonomous decision making
* Robotics navigation logic
* Safety-priority control systems

---

## ⚙️ Architecture

The system follows a simplified robotics pipeline:

```
Simulated Sensors → Perception Layer → Decision Logic → Robot Action
```

### 1️⃣ Perception Layer (Simulated)

* Simulates YOLO-based object detection results.
* Objects include position and distance information.
* Models how a robot would interpret camera-based AI detections.

### 2️⃣ Ultrasonic Sensor Simulation

* Provides distance measurements.
* Used as a safety override mechanism.

### 3️⃣ Decision Logic

Priority-based behaviour:

* 🚨 Emergency stop when ultrasonic distance is below safety threshold.
* 🛑 Stop and turn when obstacle detected in front path.
* ✅ Move forward when path is clear.

---

## 💻 Example Output

```
SCENARIO: Chair blocking path
ROBOT'S VISION:
• chair detected at center (15cm away)

ULTRASONIC SENSOR: 18cm

ROBOT ACTION: EMERGENCY STOP and TURN LEFT
```

---

## 🎓 Learning Objectives

* Understanding perception pipelines in robotics
* Applying sensor fusion concepts
* Designing decision-making systems
* Structuring modular Python robotics code
* Preparing for real-world autonomous navigation systems

---

## 🚀 Future Improvements

* Real-time camera integration with YOLO detection
* Hardware implementation (Raspberry Pi / Arduino)
* Motor control and physical robot navigation
* ROS-style architecture
* Machine learning-based path planning

---

## 🛠️ Installation

```bash
pip install ultralytics
```

---

## ▶️ Run

```bash
python robot.py
```

---

