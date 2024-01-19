import imagehash
from PIL import Image
import cv2

a = imagehash.dhash(cv2.imread('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489.jpeg'))
a_copy = imagehash.dhash(cv2.imread('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489 - Copy.jpeg'))
a_gray = imagehash.dhash(cv2.imread('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_Gray.jpeg'))
a_changed = imagehash.dhash(cv2.imread('acoustic_guitar_musician_music_girl_woman_people_sunshine-fake.jpg'))
b = imagehash.dhash(cv2.imread('agriculture_asia_cat_china_cloud_colorful_the_country_district-70998.jpeg'))
a_croped = imagehash.dhash(cv2.imread('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_Croped.jpeg'))
a_10rotated = imagehash.dhash(cv2.imread('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_10rotated.jpeg'))
print("a = ", a)
print("a_copy = ", a_copy)
print("a_gray = ", a_gray)
print("a_changed = ", a_changed)
print("a_croped = ", a_croped)
print("a_10rotated = ", a_10rotated)
print("b = ", b)

print(a - a_10rotated) # Hamming distance
print(a - b) # Hamming distance

# a = imagehash.average_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489.jpeg'))
# a_copy = imagehash.average_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489 - Copy.jpeg'))
# a_gray = imagehash.average_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_Gray.jpeg'))
# a_changed = imagehash.average_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-fake.jpg'))
# b = imagehash.average_hash(Image.open('agriculture_asia_cat_china_cloud_colorful_the_country_district-70998.jpeg'))
# a_croped = imagehash.average_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_Croped.jpeg'))
# a_10rotated = imagehash.average_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_10rotated.jpeg'))
# print("a = ", a)
# print("a_copy = ", a_copy)
# print("a_gray = ", a_gray)
# print("a_changed = ", a_changed)
# print("a_croped = ", a_croped)
# print("a_10rotated = ", a_10rotated)
# print("b = ", b)

# print(a - a_10rotated) # Hamming distance
# print(a - b) # Hamming distance

# a = imagehash.crop_resistant_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489.jpeg'))
# a_copy = imagehash.crop_resistant_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489 - Copy.jpeg'))
# a_gray = imagehash.crop_resistant_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_Gray.jpeg'))
# a_changed = imagehash.crop_resistant_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-fake.jpg'))
# b = imagehash.crop_resistant_hash(Image.open('agriculture_asia_cat_china_cloud_colorful_the_country_district-70998.jpeg'))
# a_croped = imagehash.crop_resistant_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_Croped.jpeg'))
# a_10rotated = imagehash.crop_resistant_hash(Image.open('acoustic_guitar_musician_music_girl_woman_people_sunshine-860489_10rotated.jpeg'))
# print("a = ", a)
# print("a_copy = ", a_copy)
# print("a_gray = ", a_gray)
# print("a_changed = ", a_changed)
# print("a_croped = ", a_croped)
# print("a_10rotated = ", a_10rotated)
# print("b = ", b)