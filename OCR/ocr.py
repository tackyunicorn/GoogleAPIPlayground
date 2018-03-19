import io
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

for i in range(1 , 61):
    print('Processing ' + str(int((i/60)*100)) + '%...', end='\r')
    
    inputfile = './img/SIOAS'+str(i)+'.jpg'
    outputfile = './txt/SIOAS'+str(i)+'.txt'

    with io.open(inputfile , 'rb') as image_file:
        content = image_file.read();

    image = types.Image(content = content)
    response = client.document_text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        with io.open(outputfile , 'w') as text_file:
            text_file.write(text.description)
        break
