#pip install Algorithmia for installing algorithmia
import Algorithmia
#get algorithmia key
client = Algorithmia.client('Add Algorithmia key here')
algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/1.0.1')

foo = client.dir("data://owais/data")
foo.file("test.jpg").putFile("./test2.jpg")

input = {
  "image": "data://owais/data/test.jpg",
   "numResults": 7
}
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)
