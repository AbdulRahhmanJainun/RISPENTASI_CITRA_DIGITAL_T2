import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def load_image(image_path):
    """Memuat gambar dari path yang diberikan."""
    img = imageio.imread(image_path)
    return img

def convert_to_binary(grayscale_image, threshold=128):
    """Mengonversi gambar grayscale ke biner berdasarkan threshold."""
    binary_image = (grayscale_image > threshold) * 255
    return binary_image

def display_binary(images, titles):
    """Menampilkan gambar biner dan menyimpannya ke file."""
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, (image, title) in enumerate(zip(images, titles)):
        grayscale = np.dot(image[...,:3], [0.299, 0.587, 0.114])
        binary = convert_to_binary(grayscale, threshold=128)

        axs[i].imshow(binary, cmap='gray')
        axs[i].set_title(f'{title} - Binary Image')
        axs[i].axis('off')

    plt.tight_layout()
    plt.savefig('binary_images.png')  # Simpan sebagai file gambar
    plt.show()

if __name__ == "__main__":
    image_paths = [
         "C:\\gambar\\DaunPepaya.jpg",
        "C:\\gambar\\singkong.jpeg",
        "C:\\gambar\\kenikir.jpeg"
    ]
    
    titles = ['Daun Pepaya', 'Singkong', 'Kenikir']
    
    images = [load_image(path) for path in image_paths]
    display_binary(images, titles)
