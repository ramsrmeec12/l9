import cv2
image = cv2.imread(&quot;input_image.jpg&quot;)
if image is None:
print(&quot;Error: Image not loaded&quot;)
exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier(&quot;haarcascade_frontalface_default.xml&quot;)
objects = cascade.detectMultiScale(
gray,
scaleFactor=1.1,
minNeighbors=5,
minSize=(30, 30)
)
for (x, y, w, h) in objects:
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow(&quot;Object Detection Result&quot;, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
