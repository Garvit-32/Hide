from PIL import Image
import stepic

print("1 : Encode")
print("2 : Decode")

x = int(input('Enter your number : '))
if x == 1:
    #Open Image or file in which you want to hide your data
    a=input('Enter the file name in which u want to hide data : ')
    im = Image.open(a)

    #Encode some text into your Image file and save it in another file    
    b=input('Enter the text u want to hide : ')
    res=bytes(b,'utf-8')
    im1 = stepic.encode(im,res)
    c=input('Enter the name of the file in which u want to save data : ') 
    im1.save(c, 'PNG')

if x== 2:
    #Decode the image so as to extract the hidden data from the image
    d=input('Enter the name of the file which u want to decode : ')
    im2 = Image.open(d)
    stegoImage = stepic.decode(im2)
    print(stegoImage)