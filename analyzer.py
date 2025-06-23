import cv2
import numpy as np
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="pose_landmark_cpu.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
h, w = input_details[0]['shape'][1:3]

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    results = []
    frame_num = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        input_image = cv2.resize(image_rgb, (w, h))
        input_image = (input_image.astype(np.float32) - 127.5) / 127.5
        input_data = np.expand_dims(input_image, axis=0)

        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        results.append({
            "frame": frame_num,
            "landmarks": output_data[0].tolist()
        })
        frame_num += 1

    cap.release()
    return results
