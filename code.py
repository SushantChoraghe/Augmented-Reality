import cv2
import numpy as np

# Load the image with markers and the poster image
class_img = cv2.imread('classroom_image.jpg')
poster_img = cv2.imread('poster_image.jpg')

# ArUco marker detection
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_1000)
parameters = cv2.aruco.DetectorParameters_create()
marker_corners, marker_ids, _ = cv2.aruco.detectMarkers(class_img, aruco_dict, parameters=parameters)

# Assuming the first detected marker
marker_corners = marker_corners[0].reshape(4, 2)

# Dimensions of the poster
poster_height, poster_width = poster_img.shape[:2]

# Coordinates of the full poster corners
full_poster_coords = np.array([[0, 0], [poster_width, 0], [poster_width, poster_height], [0, poster_height]], dtype=np.float32)

# Calculate the center of the poster
poster_center = np.mean(full_poster_coords, axis=0)

# Calculate the smaller portion of the poster
small_w = poster_width / 9
small_h = poster_height / 6
small_poster_coords = np.array([
    [poster_center[0] - small_w / 2, poster_center[1] - small_h / 2],
    [poster_center[0] + small_w / 2, poster_center[1] - small_h / 2],
    [poster_center[0] + small_w / 2, poster_center[1] + small_h / 2],
    [poster_center[0] - small_w / 2, poster_center[1] + small_h / 2]
], dtype=np.float32)

# Perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(small_poster_coords, marker_corners)

# Warp the perspective of the poster image
transformed_poster = cv2.warpPerspective(poster_img, perspective_matrix, (class_img.shape[1], class_img.shape[0]))

# Create a mask of the transformed poster
mask = np.zeros_like(class_img, dtype=np.uint8)
cv2.fillPoly(mask, [marker_corners.astype(np.int32)], (255, 255, 255))

# Invert the mask
inverse_mask = cv2.bitwise_not(mask)

# Black out the area of the poster in the classroom image
class_img_blackout = cv2.bitwise_and(class_img, inverse_mask)

# Combine the classroom image with the transformed poster
final_image = cv2.bitwise_or(class_img_blackout, transformed_poster)

# Save or display the result
cv2.imwrite('final_image.jpg', final_image)
cv2.imshow('Final Image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
