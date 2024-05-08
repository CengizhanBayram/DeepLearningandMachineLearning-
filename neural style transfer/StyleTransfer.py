import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import vgg19
from tensorflow.keras.preprocessing import image as kp_image
from tensorflow.keras import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError

# Resim yolu ve tarz resmi yolu
content_path = 'icerik_goruntu.jpg'
style_path = 'stil_goruntu.jpg'

# Resim boyutları
width, height = kp_image.load_img(content_path).size
img_size = 400
content_img = kp_image.load_img(content_path, target_size=(img_size, img_size))
style_img = kp_image.load_img(style_path, target_size=(img_size, img_size))

# Görüntüyü numpy dizisine dönüştürme
def preprocess_img(img):
    img = kp_image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    return img

# Görüntüyü geri dönüştürme
def deprocess_img(processed_img):
    x = processed_img.copy()
    if len(x.shape) == 4:
        x = np.squeeze(x, 0)
    assert len(x.shape) == 3, ("Görüntü boyutları yanlış", x.shape)
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype('uint8')
    return x

# İçerik ve stil görüntülerini işleme
content_img = preprocess_img(content_img)
style_img = preprocess_img(style_img)

# İçerik görüntüsü için VGG19 modelinden belirli katmanları çıkarma
content_layers = ['block5_conv2'] 

# Stil görüntüsü için VGG19 modelinden belirli katmanları çıkarma
style_layers = ['block1_conv1',
                'block2_conv1',
                'block3_conv1', 
                'block4_conv1', 
                'block5_conv1']

# Stil ve içerik görüntülerinin çıkarılacak katmanları
num_content_layers = len(content_layers)
num_style_layers = len(style_layers)

# İçerik ve stil görüntüleri için VGG19 modelini yükleme
vgg = vgg19.VGG19(include_top=False, weights='imagenet')
vgg.trainable = False

# İçerik ve stil görüntüleri için belirli katmanları seçme
style_outputs = [vgg.get_layer(name).output for name in style_layers]
content_outputs = [vgg.get_layer(name).output for name in content_layers]

# Model oluşturma
model_outputs = style_outputs + content_outputs
style_model = Model(vgg.input, model_outputs)

# Stil matrisi oluşturma
def gram_matrix(input_tensor):
    result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)
    input_shape = tf.shape(input_tensor)
    num_locations = tf.cast(input_shape[1]*input_shape[2], tf.float32)
    return result/(num_locations)

# Stil kaybı
def style_loss(style, style_pred):
    return tf.reduce_mean(tf.square(gram_matrix(style) - gram_matrix(style_pred)))

# İçerik kaybı
def content_loss(base, target):
    return tf.reduce_mean(tf.square(base - target))

# Stil ağırlıkları
style_weight = 1e-2
content_weight = 1e4

# Optimizasyon
opt = Adam(learning_rate=0.02, beta_1=0.99, epsilon=1e-1)

# Hesaplanan stil ve içerik kaybı
def compute_loss(model, loss_weights, init_image, gram_style_features, content_features):
    style_weight, content_weight = loss_weights

    model_outputs = model(init_image)

    style_output_features = model_outputs[:num_style_layers]
    content_output_features = model_outputs[num_style_layers:]

    style_score = 0
    content_score = 0

    weight_per_style_layer = 1.0 / float(num_style_layers)
    for target_style, comb_style in zip(gram_style_features, style_output_features):
        style_score += weight_per_style_layer * style_loss(target_style, comb_style)

    weight_per_content_layer = 1.0 / float(num_content_layers)
    for target_content, comb_content in zip(content_features, content_output_features):
        content_score += weight_per_content_layer* content_loss(target_content, comb_content)

    style_score *= style_weight
    content_score *= content_weight

    loss = style_score + content_score
    return loss, style_score, content_score

# Gradyan inişi
@tf.function()
def compute_grads(cfg):
    with tf.GradientTape() as tape:
        all_loss = compute_loss(**cfg)
    total_loss = all_loss[0]
    return tape.gradient(total_loss, cfg['init_image']), all_loss

# Stil ve içerik görüntülerinden özellik haritalarını al
style_features = style_model(style_img)
content_features = style_model(content_img)

# Stil görüntülerinden Gram matrislerini al
gram_style_features = [gram_matrix(style_feature) for style_feature in style_features[:num_style_layers]]

# Başlangıç görüntüsü oluşturma
init_image = tf.Variable(content_img)

# İterasyon sayısı ve güncelleme sıklığı
iterations = 1000
show_iterations = 100

# Stil aktarımı için optimizasyon döngüsü
best_loss, best_img = float('inf'), None
cfg = {
    'model': style_model,
    'loss_weights': (style_weight, content_weight),
    'init_image': init_image,
    'gram_style_features': gram_style_features,
    'content_features': content_features
}

for i in range(1, iterations+1):
    grads, all_loss = compute_grads(cfg)
    loss, style_score, content_score = all_loss
    opt.apply_gradients([(grads, init_image)])
    if loss < best_loss:
        best_loss = loss
        best_img = deprocess_img(init_image.numpy())
    if i % show_iterations == 0:
        print("Iteration:", i)
        print("Total loss:", loss.numpy())
        print("Style loss:", style_score.numpy())
        print("Content loss:", content_score.numpy())

# Sonuçları gösterme
plt.figure(figsize=(10, 5))
plt.imshow(best_img)
plt.axis('off')
plt.show()
