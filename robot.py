import time
from ultralytics import YOLO

def brain():
    print("Robot Brain Simulator")

    # Use a model that ultralytics definitely supports (v8/v11 style)
    # If you already have yolov8n.pt it will download automatically if missing.
    model = YOLO("yolov8n.pt")
    print("Robot Brain is Loaded")

    scenarios = [
        {
            "scene": "Empty hallway ahead",
            "objects": [],
            "ultrasonic_distance": 50,
            "expected_action": "MOVE FORWARD",
        },
        {
            "scene": "Person walking in front",
            "objects": [{"name": "person", "position": "center", "distance": 25}],
            "ultrasonic_distance": 45,
            "expected_action": "STOP and TURN RIGHT",
        },
        {
            "scene": "Chair blocking path",
            "objects": [{"name": "chair", "position": "center", "distance": 15}],
            "ultrasonic_distance": 18,
            "expected_action": "EMERGENCY STOP and TURN LEFT",
        },
        {
            "scene": "Cat walking to the side",
            "objects": [{"name": "cat", "position": "left", "distance": 30}],
            "ultrasonic_distance": 60,
            "expected_action": "MOVE FORWARD",
        },
        {
            "scene": "Table in front, book on side",
            "objects": [
                {"name": "dining table", "position": "center", "distance": 20},
                {"name": "book", "position": "right", "distance": 40},
            ],
            "ultrasonic_distance": 25,
            "expected_action": "STOP and TURN RIGHT",
        },
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📸 SCENARIO {i}: {scenario['scene']}")
        print("-" * 40)

        print("👁️  ROBOT'S VISION:")
        if scenario["objects"]:
            for obj in scenario["objects"]:
                print(f"   • {obj['name']} detected at {obj['position']} ({obj['distance']}cm away)")
        else:
            print("   • No objects detected")

        print(f"📡 ULTRASONIC SENSOR: {scenario['ultrasonic_distance']}cm")

        print("🧠 ROBOT THINKING...")
        time.sleep(1)

        print("⚙️  DECISION LOGIC:")

        if scenario["ultrasonic_distance"] < 20:
            decision = "EMERGENCY STOP and TURN LEFT"
            reason = f"Ultrasonic detected obstacle at {scenario['ultrasonic_distance']}cm (< 20cm)"
        elif any(obj["position"] == "center" and obj["distance"] < 30 for obj in scenario["objects"]):
            decision = "STOP and TURN RIGHT"
            reason = "Vision detected object in center within 30cm"
        else:
            decision = "MOVE FORWARD"
            reason = "Path clear"

        print(f"   Reason: {reason}")
        print(f"🤖 ROBOT ACTION: {decision}")

        if decision == scenario["expected_action"]:
            print("✅ Decision matches expected behavior!")
        else:
            print(f"⚠️  Expected: {scenario['expected_action']}")

        input("\nPress Enter to continue to next scenario...")

    print("\n" + "=" * 60)
    print("🎓 WHAT YOU LEARNED:")
    print("End of Simulation")
if __name__ == "__main__":
    brain()
