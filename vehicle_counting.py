import cv2
import glob
from vehicle_detector import VehicleDetector


def detectVehicle(imagepath):
    vd = VehicleDetector()
    img = cv2.imread("static/uploaded/"+imagepath)

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    print(vehicle_count)

    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imwrite("static/processed/"+imagepath,img)



