import Image
import copy
def roll(image, delta):
    xsize, ysize = image.size
    delta = delta % xsize
    if delta == 0:
        return image
    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    return image

im = Image.open('/home/adam/sandbox/dress.jpg')
im.save('/home/adam/sandbox/saved_dress.jpg')


from subprocess import call
def view_gnome(image):
    num_str = [x.split('_')[1] for x in os.listdir('/tmp/') if 'view_' in x]
    dummy_numer  = str(max([int(x) for x in num_str if x.isdigit()]) + 1)
    f = '/tmp/view_'+dummy_numer+'_.jpeg'
    im.save(f)
    call(['gnome-open', f])



