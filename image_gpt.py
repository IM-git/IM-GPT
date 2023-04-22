# Sourse information: https://github.com/openai/openai-cookbook/blob/main/examples/dalle/Image_generations_edits_and_variations_with_DALL-E.ipynb
import openai
import requests
import os

from settings import TOKEN_GPT


openai.api_key = TOKEN_GPT

# set a directory to save DALL-E images to
image_dir_name = "images"
image_dir = os.path.join(os.curdir, image_dir_name)

# create the directory if it doesn't yet exist
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# print the directory to save to
print(f"{image_dir=}")

####################################################################################################
# create an image
# set the prompt
prompt = "A QA-cyberpunk cat hacker dreaming of the amazing game, neon light digital art"

# call the OpenAI API
generation_response = openai.Image.create(
    prompt=prompt,
    n=1,    # quantity images
    size="1024x1024",   # also: "256x256", "512x512"
    response_format="url",
)

# print response
print(generation_response)

# save the image
generated_image_name = "generated_image.png"  # any name you like; the filetype should be .png
generated_image_filepath = os.path.join(image_dir, generated_image_name)
generated_image_url = generation_response["data"][0]["url"]  # extract image URL from response
generated_image = requests.get(generated_image_url).content  # download the image

with open(generated_image_filepath, "wb") as image_file:
    image_file.write(generated_image)  # write the image to the file

# print the image
# print(generated_image_filepath)
####################################################################################################


####################################################################################################
# Creating variation
variation_response = openai.Image.create_variation(
    image=generated_image,  # generated_image is the image generated above
    n=2,
    size="1024x1024",
    response_format="url",
)

# print response
print(variation_response)


# save the images
variation_urls = [datum["url"] for datum in variation_response["data"]]  # extract URLs
variation_images = [requests.get(url).content for url in variation_urls]  # download images
variation_image_names = [f"variation_image_{i}.png" for i in range(len(variation_images))]  # create names
variation_image_filepaths = [os.path.join(image_dir, name) for name in variation_image_names]  # create filepaths
for image, filepath in zip(variation_images, variation_image_filepaths):  # loop through the variations
    with open(filepath, "wb") as image_file:  # open the file
        image_file.write(image)  # write the image to the file

# print the original image
print(generated_image_filepath)

# print the new variations
for variation_image_filepaths in variation_image_filepaths:
    print(variation_image_filepaths)
####################################################################################################
