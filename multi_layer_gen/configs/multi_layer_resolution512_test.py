_base_ = "./base.py"

### path & device settings

output_path_base = "./output/"
cache_dir = None


### wandb settings
wandb_job_name = "flux_" + '{{fileBasenameNoExtension}}'

resolution = 512

### Model Settings
rank = 64
text_encoder_rank = 64
train_text_encoder = False
max_layer_num = 50 + 2
learnable_proj = True

### Training Settings
weighting_scheme = "none"
logit_mean = 0.0
logit_std = 1.0
mode_scale = 1.29
guidance_scale = 1.0 ###IMPORTANT
layer_weighting = 5.0

# steps
train_batch_size = 1
num_train_epochs = 1
max_train_steps = None
checkpointing_steps = 2000
resume_from_checkpoint = "latest"
gradient_accumulation_steps = 1

# lr
optimizer = "prodigy"
learning_rate = 1.0
scale_lr = False
lr_scheduler = "constant"
lr_warmup_steps = 0
lr_num_cycles = 1
lr_power = 1.0

# optim
adam_beta1 = 0.9
adam_beta2 = 0.999
adam_weight_decay = 1e-3
adam_epsilon = 1e-8
prodigy_beta3 = None
prodigy_decouple = True
prodigy_use_bias_correction = True
prodigy_safeguard_warmup = True
max_grad_norm = 1.0

# logging
tracker_task_name = '{{fileBasenameNoExtension}}'
output_dir = output_path_base + "{{fileBasenameNoExtension}}"

### Validation Settings
num_validation_images = 1
validation_steps = 2000
validation_prompts = [
    'The image features a background with a soft, pastel color gradient that transitions from pink to purple. There are abstract floral elements scattered throughout the background, with some appearing to be in full bloom and others in a more delicate, bud-like state. The flowers have a watercolor effect, with soft edges that blend into the background.\n\nCentered in the image is a quote in a serif font that reads, "You\'re free to be different." The text is black, which stands out against the lighter background. The overall style of the image is artistic and inspirational, with a motivational message that encourages individuality and self-expression. The image could be used for motivational purposes, as a background for a blog or social media post, or as part of a personal development or self-help theme.',
    'The image features a logo for a company named "Bull Head Party Adventure." The logo is stylized with a cartoon-like depiction of a bull\'s head, which is the central element of the design. The bull has prominent horns and a fierce expression, with its mouth slightly open as if it\'s snarling or roaring. The color scheme of the bull is a mix of brown and beige tones, with the horns highlighted in a lighter shade.\n\nBelow the bull\'s head, the company name is written in a bold, sans-serif font. The text is arranged in two lines, with "Bull Head" on the top line and "Party Adventure" on the bottom line. The font color matches the color of the bull, creating a cohesive look. The overall style of the image is playful and energetic, suggesting that the company may offer exciting or adventurous party experiences.',
    'The image features a festive and colorful illustration with a theme related to the Islamic holiday of Eid al-Fitr. At the center of the image is a large, ornate crescent moon with intricate patterns and decorations. Surrounding the moon are several smaller stars and crescents, also adorned with decorative elements. These smaller celestial motifs are suspended from the moon, creating a sense of depth and dimension.\n\nBelow the central moon, there is a banner with the text "Eid Mubarak" in a stylized, elegant font. The text is in a bold, dark color that stands out against the lighter background. The background itself is a gradient of light to dark green, which complements the golden and white hues of the celestial motifs.\n\nThe overall style of the image is celebratory and decorative, with a focus on the traditional symbols associated with Eid al-Fitr. The use of gold and white gives the image a luxurious and festive feel, while the green background is a color often associated with Islam. The image appears to be a digital artwork or graphic design, possibly intended for use as a greeting card or a festive decoration.',
    'The image is a festive graphic with a dark background. At the center, there is a large, bold text that reads "Happy New Year 2023" in a combination of white and gold colors. The text is surrounded by numerous white balloons with gold ribbons, giving the impression of a celebratory atmosphere. The balloons are scattered around the text, creating a sense of depth and movement. Additionally, there are small gold sparkles and confetti-like elements that add to the celebratory theme. The overall design suggests a New Year\'s celebration, with the year 2023 being the focal point.',
    'The image is a stylized illustration with a flat design aesthetic. It depicts a scene related to healthcare or medical care. In the center, there is a hospital bed with a patient lying down, appearing to be resting or possibly receiving treatment. The patient is surrounded by three individuals who seem to be healthcare professionals or caregivers. They are standing around the bed, with one on each side and one at the foot of the bed. The person at the foot of the bed is holding a clipboard, suggesting they might be taking notes or reviewing medical records.\n\nThe room has a window with curtains partially drawn, allowing some light to enter. The color palette is soft, with pastel tones dominating the scene. The text "INTERNATIONAL CANCER DAY" is prominently displayed at the top of the image, indicating that the illustration is related to this event. The overall impression is one of care and support, with a focus on the patient\'s well-being.',
    'The image features a stylized illustration of a man with a beard and a tank top, drinking from a can. The man is depicted in a simplified, cartoon-like style with a limited color palette. Above him, there is a text that reads "Happy Eating, Friends" in a bold, friendly font. Below the illustration, there is another line of text that states "Food is a Necessity That is Not Prioritized," which is also in a bold, sans-serif font. The background of the image is a gradient of light to dark blue, giving the impression of a sky or a calm, serene environment. The overall style of the image is casual and approachable, with a focus on the message conveyed by the text.',
    'The image is a digital illustration with a pastel pink background. At the top, there is a text that reads "Sending you my Easter wishes" in a simple, sans-serif font. Below this, a larger text states "May Your Heart be Happy!" in a more decorative, serif font. Underneath this main message, there is a smaller text that says "Let the miracle of the season fill you with hope and love."\n\nThe illustration features three stylized flowers with smiling faces. On the left, there is a purple flower with a yellow center. In the center, there is a blue flower with a green center. On the right, there is a pink flower with a yellow center. Each flower has a pair of eyes and a mouth, giving them a friendly appearance. The flowers are drawn with a cartoon-like style, using solid colors and simple shapes.\n\nThe overall style of the image is cheerful and whimsical, with a clear Easter theme suggested by the text and the presence of flowers, which are often associated with spring and new beginnings.',
    'The image is a vibrant and colorful graphic with a pink background. In the center, there is a photograph of a man and a woman embracing each other. The man is wearing a white shirt, and the woman is wearing a patterned top. They are both smiling and appear to be in a joyful mood.\n\nSurrounding the photograph are various elements that suggest a festive or celebratory theme. There are three hot air balloons in the background, each with a different design: one with a heart, one with a gift box, and one with a basket. These balloons are floating against a clear sky.\n\nAdditionally, there are two gift boxes with ribbons, one on the left and one on the right side of the image. These gift boxes are stylized with a glossy finish and are placed at different heights, creating a sense of depth.\n\nAt the bottom of the image, there is a large red heart, which is a common symbol associated with love and Valentine\'s Day.\n\nFinally, at the very bottom of the image, there is a text that reads "Happy Valentine\'s Day," which confirms the theme of the image as a Valentine\'s Day greeting. The text is in a playful, cursive font that matches the overall cheerful and romantic tone of the image.',
    'The image depicts a stylized illustration of two women sitting on stools, engaged in conversation. They are wearing traditional attire, with headscarves and patterned dresses. The woman on the left is wearing a brown dress with a purple pattern, while the woman on the right is wearing a purple dress with a brown pattern. Between them is a purple flower. Above the women, the text "INTERNATIONAL WOMEN\'S DAY" is written in bold, uppercase letters. The background is a soft, pastel pink, and there are abstract, swirling lines in a darker shade of pink above the women. The overall style of the image is simplistic and cartoonish, with a warm and friendly tone.',
    'The image is a stylized illustration with a warm, peach-colored background. At the center, there is a vintage-style radio with a prominent dial and antenna. The radio is emitting a blue, star-like burst of light or energy from its top. Surrounding the radio are various objects and elements that seem to be floating or suspended in the air. These include a brown, cone-shaped object, a blue, star-like shape, and a brown, wavy, abstract shape that could be interpreted as a flower or a wave.\n\nAt the top of the image, there is text that reads "World Radio Day" in a bold, serif font. Below this, in a smaller, sans-serif font, is the date "13 February 2022." The overall style of the image is playful and cartoonish, with a clear focus on celebrating World Radio Day.',
    'The image is a graphic design of a baby shower invitation. The central focus is a cute, cartoon-style teddy bear with a friendly expression, sitting upright. The bear is colored in a soft, light brown hue. Above the bear, there is a bold text that reads "YOU\'RE INVITED" in a playful, sans-serif font. Below this, the words "BABY SHOWER" are prominently displayed in a larger, more decorative font, suggesting the theme of the event.\n\nThe background of the invitation is a soft, light pink color, which adds to the gentle and welcoming atmosphere of the design. At the bottom of the image, there is additional text providing specific details about the event. It reads "27 January, 2022 - 8:00 PM" followed by "FAUGET INDUSTRIES CAFE," indicating the date, time, and location of the baby shower.\n\nThe overall style of the image is warm, inviting, and child-friendly, with a clear focus on the theme of a baby shower celebration. The use of a teddy bear as the central image reinforces the baby-related theme. The design is simple yet effective, with a clear hierarchy of information that guides the viewer\'s attention from the top to the bottom of the invitation.',
]

validation_boxes = [
    [(0, 0, 512, 512), (0, 0, 512, 512), (368, 0, 512, 272), (0, 272, 112, 512), (160, 208, 352, 304)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (128, 128, 384, 304), (96, 288, 416, 336), (128, 336, 384, 368)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (112, 48, 400, 368), (0, 48, 96, 176), (128, 336, 384, 384), (240, 384, 384, 432)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (32, 32, 480, 480), (80, 176, 432, 368), (64, 176, 448, 224), (144, 96, 368, 224)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (0, 64, 176, 272), (0, 400, 512, 512), (16, 160, 496, 512), (224, 48, 464, 112), (208, 96, 464, 160)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (112, 224, 512, 512), (0, 0, 240, 160), (144, 144, 512, 512), (48, 64, 432, 208), (48, 400, 256, 448)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (160, 48, 352, 80), (64, 80, 448, 192), (128, 208, 384, 240), (320, 240, 512, 512), (80, 272, 368, 512), (0, 224, 192, 512)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (48, 0, 464, 304), (128, 144, 384, 400), (288, 288, 384, 368), (336, 304, 400, 368), (176, 432, 336, 480), (224, 400, 288, 432)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (32, 288, 448, 512), (144, 176, 336, 400), (224, 208, 272, 256), (160, 128, 336, 192), (192, 368, 304, 400), (368, 80, 448, 224), (48, 160, 128, 256)],
   [(0, 0, 512, 512), (0, 0, 512, 512), (0, 352, 512, 512), (112, 176, 368, 432), (48, 176, 128, 256), (48, 368, 128, 448), (384, 192, 480, 272), (384, 336, 432, 384), (80, 80, 432, 128), (176, 128, 336, 160)],
    [(0, 0, 512, 512), (0, 0, 512, 512), (0, 0, 512, 352), (144, 384, 368, 448), (160, 192, 352, 432), (368, 0, 512, 144), (0, 0, 144, 144), (128, 80, 384, 208), (128, 448, 384, 496), (176, 48, 336, 80)],
]