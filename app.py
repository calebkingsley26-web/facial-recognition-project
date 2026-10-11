
import os
import cv2
import face_recognition as fr

# Get the folder where this Python file is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Add your image filenames here
image_names = [
    'my_image.jpg',
    'f60189d1-195f-4c7e-8610-770087649117.JPG',
    'person3.JPG'
]

# Store face encodings and image names
known_face_encodings = []
known_face_names = []

# Process each image
for image_name in image_names:

    image_path = os.path.join(base_dir, image_name)

    # Check whether the image exists
    if not os.path.exists(image_path):
        print(f"Image not found: {image_name}")
        continue

    # Load the image
    image = fr.load_image_file(image_path)

    # Detect faces
    face_locations = fr.face_locations(image)

    if not face_locations:
        print(f"No faces detected in {image_name}.")
        continue

    print(f"Found {len(face_locations)} face(s) in {image_name}.")

    # Get face encodings
    face_encodings = fr.face_encodings(image, face_locations)

    # Store face encodings
    for face_encoding in face_encodings:
        known_face_encodings.append(face_encoding)
        known_face_names.append(image_name)

    # Convert RGB to BGR
    color_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw green rectangles around faces
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(
            color_image,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            3
        )

    # Display the image
    cv2.imshow(f'Face Detection - {image_name}', color_image)

# Compare faces and calculate distances
print("\n--- Face Comparison Results ---")

for i in range(len(known_face_encodings)):
    for j in range(i + 1, len(known_face_encodings)):

        # Skip faces from the same image
        if known_face_names[i] == known_face_names[j]:
            continue

        # Calculate face distance
        distance = fr.face_distance(
            [known_face_encodings[i]],
            known_face_encodings[j]
        )[0]

        # Compare faces
        results = fr.compare_faces(
            [known_face_encodings[i]],
            known_face_encodings[j]
        )

        print(f"\nImage 1: {known_face_names[i]}")
        print(f"Image 2: {known_face_names[j]}")
        print(f"Face distance: {distance:.4f}")

        if results[0]:
            print("Result: Same person (match)")
        else:
            print("Result: Different people (no match)")

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
