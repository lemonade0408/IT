
import requests
import cv2
from ultralytics import YOLO


image_url = "https://ultralytics.com/images/bus.jpg"

response = requests.get(image_url, timeout=30)
response.raise_for_status()

with open("bus.jpg", "wb") as file:
    file.write(response.content)


image = cv2.imread("bus.jpg")

if image is None:
    raise ValueError("Не удалось открыть изображение!")


models = [
    ("YOLO26n", YOLO("yolo26n.pt")),
    ("YOLO11n", YOLO("yolo11n.pt"))
]


target_classes = ["person", "bus"]


for model_name, model in models:

    result_image = image.copy()

    results = model.predict(
        source="bus.jpg",
        conf=0.35,
        verbose=False
    )

    found_objects = []

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0].item())
            class_name = result.names[class_id]

            if class_name in target_classes:

                x1, y1, x2, y2 = map(
                    int, box.xyxy[0].tolist()
                )

                cv2.rectangle(
                    result_image,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    result_image,
                    class_name,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

                found_objects.append(class_name)

    output_name = f"result_{model_name.lower()}.jpg"

    cv2.imwrite(output_name, result_image)

    print("\nМодель:", model_name)
    print("Найдено объектов:", len(found_objects))
    print("Объекты:", found_objects)
    print("Изображение сохранено:", output_name)


print("\nРабота программы завершена!")
