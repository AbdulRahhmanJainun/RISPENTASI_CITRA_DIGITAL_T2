import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def load_image(image_path):
    """Memuat gambar dari path yang diberikan."""
    img = imageio.imread(image_path)
    return img

def display_blue_channel(images, titles):
    """Menampilkan channel biru (Blue) dari gambar dan menyimpannya ke file."""
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, (image, title) in enumerate(zip(images, titles)):
        B = image[:, :, 2]
        axs[i].imshow(B, cmap='Blues')
        axs[i].set_title(f'{title} - Channel B (Blue)')
        axs[i].axis('off')

    plt.tight_layout()
    plt.savefig('channel_blue.png')  # Abdul Rahman Jainun
    plt.show()

if __name__ == "__main__":
    image_paths = [
       "C:\\gambar\\DaunPepaya.jpg",
        "C:\\gambar\\singkong.jpeg",
        "C:\\gambar\\kenikir.jpeg"
    ]
    
    titles = ['Daun Pepaya', 'Singkong', 'Kenikir']
    
    images = [load_image(path) for path in image_paths]
    display_blue_channel(images, titles)
