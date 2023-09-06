from imageai.Classification import ImageClassification
import os

# predict the category of image in  image_file
# display predictions
def predict(base_path : str,image_name):
    print("\n---Starting Prediction---\n")
    print(f"Predictions of model for object {image_name}")
    predictions, probabilities = prediction.classifyImage(base_path, result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)


# import the model
execution_path = os.getcwd()
prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()

# import images from "images" folder
base_path = os.path.join(execution_path,"images")

# test images
for image_file in os.listdir(os.path.join(execution_path, "images")):
    image_name = image_file[:-4]
    predict(base_path+"\\"+image_file, image_name)

