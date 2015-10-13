#!/usr/bin/python



import os
import cv2
import numpy
from scipy.ndimage import label

def segment_on_dt(img):
    """ takes an openvc image, extracts the central segment, then returns the image
        with only the central segment, and all other segments colored out(white)
        args:
            img: and opencv image object
        returns:
            img: and opencv image object of the first segment
    """

    # code from:
    # http://stackoverflow.com/questions/11294859/how-to-define-the-markers-for-watershed-in-opencv
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        
    _, img_bin = cv2.threshold(img_gray, 0, 255,cv2.THRESH_OTSU)
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN,numpy.ones((3, 3), dtype=int))
    border = cv2.dilate(img_bin, None, iterations=5)
    border = border - cv2.erode(border, None)

    dt = cv2.distanceTransform(img_bin, 2, 3)
    dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(numpy.uint8)
    _, dt = cv2.threshold(dt, 180, 255, cv2.THRESH_BINARY)
    lbl, ncc = label(dt)
    lbl = lbl * (255/ncc)
    # Completing the markers now. 
    lbl[border == 255] = 255 

    lbl = lbl.astype(numpy.int32)
    cv2.watershed(img, lbl)

    lbl[lbl == -1] = 0 
    lbl = lbl.astype(numpy.uint8)
    result = 255 - lbl 
    result[result != 255] = 0 
    result = cv2.dilate(result, None)
    img[result == 255] = (0, 0, 255)
    return img 

def get_hom_grid_logo(img):
    """ takes the logo image, determines the homography grid 
    Args:
         img: an opencv image object of only the can
    Return:
         a collection of pts specifying the grid over the logo"""
    pass
    # apply a uniform grid over the logo

def get_hom_grid_can(img):
    """ takes the segmented can image, determines the homography grid 
    Args:
         img: an opencv image object of only the can
    Return:
         a collection of pts specifying the grid over the can"""
    pass
    # 1) get ellipse formed by the top of the can
    # 2) get the sides of the can
    # 3) given the sides of the can, iterate the ellipse in uniform intervals between the 
    #    sides N times to create a grid of evenly spaced(in 'can' space) points
def apply_logo_to_can(toimg,fromimg,togird,fromgrid):
    """ take two images, and their grids and transfers from the toimg onto the fromimg
        Args:

            toimg: the opencv object to transfer onto
            fromimg: the opencv object to transfer from
            togrid: the grid corresponding to the toimg
            fromgrid: the grid corresponding to the fromimg
        Return:
            opencv image of the peicewise affine transform"""
    pass
    # to implement, see http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf, page 85


def get_basename(input_file):
    """ get the basename for a file
        example '/home/a/b/c.jpg' -> 'c'
    """
    return os.path.splitext(os.path.basename(input_file))[0]


class template_logos():
    """ the object for initiated the application of logos to template images
        Args:
            tempates (list of str): the templates which images are applied to
            logos    (list of str): the logo images which are applied to the template
            output_dir (str)       : the output directory 
            bounding_box (list of (x-min,x-max,y-min,ymax) || None) the bounding box for
            the template. If list is None, or None is a value in the list, no bounding
            box is assumed for the template image.
    """
    def __init__(self, templates logos, ouputdir,bounding_box=None):
        self.templates = templates
        self.logos     = logos
        self.ouputdir = outputdir
        self.templates = templates
    def run_over_imgs(self):
    """ The function for taking logos and matching them to can typed objects
        within the template image"""
        for idx,tmp in enumerate(self.template_logos):
            box = self.templates[idx[
            for logo in self.logos:
                # implement worker queue here
                output_file = self.outputdir + '/' +  get_basename(tmp) + '_' + get_basename(logo) + '.jpg'
                status = self.match_logo_to_template(template=tmp, logo=logo, box=box, output_file = output_file)
                if status is True:
                    print "PASSED: \n\ttmp: " + tmp + " logo: " + logo + "\toutput: " + output_file
                else:
                    print "FAILED: \n\ttmp: " + tmp + " logo: " + logo + "\toutput: " + output_file

    def match_logo_to_template(template,logo,box,output_file)
    """ object method to apply logo to template"""
    ### apply box to template(not implemented)
        try:
            img_tmp = cv2.imread(template)
            img_logo = cv2.imread(logo)
        except e:
            print "failed to open template/log" + '\ttemplate: ' + tmp + '\n\tlogo: ' + logo
            return None
        img_tmp_seg = segment_on_dt(tmp)
        ## get the homography grid on the template
        img_tmp_grid = get_hom_grid_can(img_tmp_seg)        
        img_logo_grid  = get_hom_grid_log(img_logo)
        img_can_logo  = apply_logo_to_can(toimg=img_tmp,fromimg=img_logo,togrid=img_tmp_grid,fromgrid=img_logo_grid)
        cv2.imwrite(output_file, img_can_logo)
        return True

