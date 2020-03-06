from PIL import Image

num_key_frames = 74

with Image.open('Aquarium_.gif') as im:
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save('{}.gif'.format(i))
