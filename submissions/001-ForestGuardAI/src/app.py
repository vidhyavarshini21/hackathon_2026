from satellite_module import detect_deforestation
from acoustic_module import detect_gunshot
from drone_module import detect_intruder
from risk_engine import calculate_risk
from alert_system import send_alert

def main():
    print("🌲 ForestGuard AI Initializing...\n")

    forest_loss = detect_deforestation(
        "data_samples/before_forest.jpg",
        "data_samples/after_forest.jpg"
    )

    gunshot = detect_gunshot("data_samples/gunshot_sample.wav")

    intruder = detect_intruder("data_samples/after_forest.jpg")

    risk_score = calculate_risk(forest_loss, gunshot, intruder)

    print(f"\n🔥 Final Risk Score: {risk_score}/100")

    if risk_score > 60:
        send_alert(risk_score)

if __name__ == "__main__":
    main()
