from django.shortcuts import render
from django.conf import settings
#from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from snake_app.models import*
from django.shortcuts import render, redirect
from snake_app.forms import ImageUploadForm
from .models import DeepLearningModel
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import numpy as np
import requests
from PIL import Image
from io import BytesIO
import os



# Create your views here.
def welcome (request):
    return render(request,'welcome.html')


def second(request):
    if request.method == 'POST':
        form = ImageUploadForm(data=request.POST,files= request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            img_url = obj.image.url
            return render(request,'submit.html',{"obj":obj})  # Redirect to a success page or wherever you need
    else:
        form = ImageUploadForm()
    img=snake.objects.all()
    return render(request, 'second.html', {"img":img,"form": form})
    
def submit(request):
    loaded_model = load_model(os.path.join(settings.BASE_DIR, 'models', 'Snake_prediction_model.h5'))
    image_url = request.FILES.get('img_url', '')
    print("Image_URL", image_url)


    try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img = img.convert('RGB')
            img = img.resize((224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array/255.0

            # Make predictions
            predictions = loaded_model.predict(img_array)
            class_index = np.argmax(predictions[0])
            result = ""

            if class_index == 1:
                result = "Poisonous"
            else:
                result = "Not poisonous"

            # Debugging statements
            print("Image URL:", image_url)
            print("Predictions:", predictions)
            print("Class Index:", class_index)
            print("Result:", result)

    except Exception as e:
            # Handle any exceptions that might occur
            print("Error:", e)
            result = "Error during prediction"

        # Pass the result to the template
    print("Result:", result)
    return render(request, 'submit.html', result)




