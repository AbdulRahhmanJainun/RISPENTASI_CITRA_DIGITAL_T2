import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def load_image(image_path):
    """Memuat gambar dari path yang diberikan."""
    img = imageio.imread(image_path)
    return img

def display_red_channel(images, titles):
    """Menampilkan channel merah (Red) dari gambar dan menyimpannya ke file."""
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, (image, title) in enumerate(zip(images, titles)):
        R = image[:, :, 0]
        axs[i].imshow(R, cmap='Reds')
        axs[i].set_title(f'{title} - Channel R (Red)')
        axs[i].axis('off')

    plt.tight_layout()
    plt.savefig('channel_red.png')  # Abdul Rahman Jainun
    plt.show()

if __name__ == "__main__":
    image_paths = [
        "C:\\gambar\\DaunPepaya.jpg",
        "C:\\gambar\\singkong.jpeg",
        "C:\\gambar\\kenikir.jpeg"
    ]
    
    titles = ['Daun Pepaya', 'Singkong', 'Kenikir']
    
    images = [load_image(path) for path in image_paths]
    display_red_channel(images, titles)
