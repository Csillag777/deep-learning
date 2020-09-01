from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np

# include_top=True，表示會載入完整的 VGG16 模型，包括加在最後3層的卷積層
# include_top=False，表示會載入 VGG16 的模型，不包括加在最後3層的卷積層，通常是取得 Features
# 若下載失敗，請先刪除 c:\<使用者>\.keras\models\vgg16_weights_tf_dim_ordering_tf_kernels.h5
model = VGG16(weights='imagenet', include_top=True) 

# Input：要辨識的影像
img_path = 'tiger.jpg'
#img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# 預測，取得features，維度為 (1,7,7,512)
features = model.predict(x)
# 取得前三個最可能的類別及機率

print('Predicted:', decode_predictions(features, top=3)[0])
l = decode_predictions(features, top=1)[0]
def find_match_ans(l):
    sl = str(l)
    index2_find = sl.split("',")
    ans = index2_find[1][2:len(index2_find[1])]
    #print(index2_find)
    return ans
ans = find_match_ans(l)
print(ans)
#print(model.summary())