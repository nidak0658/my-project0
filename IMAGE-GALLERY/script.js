// Array of image URLs
const images = [
    'images/image1.jpg',
    'images/image2.jpg',
    'images/image3.jpg',
    // Add more images as needed
];

let currentIndex = 0;
const totalImages = images.length;
const currentImageElem = document.getElementById('current-image');

function changeImage(direction) {
    currentIndex += direction;

    // Wrap around if index goes out of bounds
    if (currentIndex < 0) {
        currentIndex = totalImages - 1;
    } else if (currentIndex >= totalImages) {
        currentIndex = 0;
    }

    // Update the image source
    currentImageElem.src = images[currentIndex];
}
