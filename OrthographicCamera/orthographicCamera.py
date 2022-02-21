import numpy
import json
from PIL import Image

#Read the scene1
with open('scene1.json') as f:
      data = json.load(f)

orthocamCenter=numpy.array(data['orthocamera']['center'])
orthocamDirection=numpy.array(data['orthocamera']['direction'])
orthocamUp=numpy.array(data['orthocamera']['up'])
orthocamSize=numpy.array(data['orthocamera']['size'])
backgroundColor=numpy.array(data['background']['color'])
groupSphereCenter=numpy.array(data['group'][0]['sphere']['center'])
groupSphereRadius=numpy.array(data['group'][0]['sphere']['radius'])
groupSphereColor=numpy.array(data['group'][0]['sphere']['color'])

#Read the scene2
with open('scene2.json') as f2:
    data2=json.load(f2)

orthocamCenter2=numpy.array(data2['orthocamera']['center'])
orthocamDirection2=numpy.array(data2['orthocamera']['direction'])
orthocamUp2=numpy.array(data2['orthocamera']['up'])
orthocamSize2=numpy.array(data2['orthocamera']['size'])
backgroundColor2=numpy.array(data2['background']['color'])
groupSphereCenter0=numpy.array(data2['group'][0]['sphere']['center'])
groupSphereRadius0=numpy.array(data2['group'][0]['sphere']['radius'])
groupSphereColor0=numpy.array(data2['group'][0]['sphere']['color'])
groupSphereCenter1=numpy.array(data2['group'][1]['sphere']['center'])
groupSphereRadius1=numpy.array(data2['group'][1]['sphere']['radius'])
groupSphereColor1=numpy.array(data2['group'][1]['sphere']['color'])
groupSphereCenter2=numpy.array(data2['group'][2]['sphere']['center'])
groupSphereRadius2=numpy.array(data2['group'][2]['sphere']['radius'])
groupSphereColor2=numpy.array(data2['group'][2]['sphere']['color'])
groupSphereCenter3=numpy.array(data2['group'][3]['sphere']['center'])
groupSphereRadius3=numpy.array(data2['group'][3]['sphere']['radius'])
groupSphereColor3=numpy.array(data2['group'][3]['sphere']['color'])
groupSphereCenter4=numpy.array(data2['group'][4]['sphere']['center'])
groupSphereRadius4=numpy.array(data2['group'][4]['sphere']['radius'])
groupSphereColor4=numpy.array(data2['group'][4]['sphere']['color'])




     
class Object3D:
    def __init_(self):
        self.color=groupSphereColor

    def intersect(ray, hit, tmin):
        print()

    


class Sphere(Object3D):
    def __init__(self, groupSphereRadius, groupSphereCenter, groupSphereColor):
        self.radius=groupSphereRadius
        self.center=groupSphereCenter
        self.color=groupSphereColor

    def intersectWithColor(self, ray, hit, tmin):

        oc=ray.origin - self.center
        a=numpy.dot(ray.direction, ray.direction)
        b=2.0*numpy.dot(oc, ray.direction)
        c=numpy.dot(oc, oc)-self.radius*self.radius
        discriminant=b*b-4*a*c

        if discriminant<0:
            return -1.0
        else:
            t=(-b-numpy.sqrt(discriminant))/(2.0*a)
            if t<tmin and t>-1:
                tmin=t
                hit.setValues(t,self.color)
            return t

    def intersectWithDepth(self, ray, hit, tmin, near, far):

        oc=ray.origin - self.center
        a=numpy.dot(ray.direction, ray.direction)
        b=2.0*numpy.dot(oc, ray.direction)
        c=numpy.dot(oc, oc)-self.radius*self.radius
        discriminant=b*b-4*a*c

        if discriminant<0:
            return -1.0
        else:
            t=(-b-numpy.sqrt(discriminant))/(2.0*a)
            if t<tmin and t>-1:
                tmin=t
                nf=int(((far-t)/(far-near))*255)
                color=numpy.array([nf, nf, nf])
                hit.setValues(t,color)
            return t





class Group(Object3D):
    def __init__(self):
        self.objects=[]

    def adding(self, object):
        self.objects.append(object)

    def intersectColor(self, ray, hit, tmin):
        tmin=100
        for k in self.objects:
            t=k.intersectWithColor(ray, hit, tmin)
            if t<tmin and t>-1:
                tmin=t
                hit.setValues(t, hit.color)
        return tmin

    def intersectDepth(self, ray, hit, tmin, near, far):
        tmin=100
        for k in self.objects:
            t=k.intersectWithDepth(ray, hit, tmin, near, far)
            if t<tmin and t>-1:
                tmin=t
                hit.setValues(t, hit.color)
        return tmin



class Camera:
    def __init__(self):
        self.cam=0

    def generateRay(x, y):
        print()



class OrthographicCamera(Camera):
    
    def __init__(self, orthocamCenter, orthocamDirection, orthocamUp, orthocamSize):
        self.center=orthocamCenter
        self.direction=orthocamDirection
        self.up=orthocamUp
        self.size=orthocamSize

    def generateRay(self, x=0.5, y=0.5):
        ray=Ray()
        horizontal=numpy.cross(self.direction, self.up)
        ray.setValues(self.center+(x-0.5)*self.size*horizontal+(y-0.5)*self.size*self.up, self.direction)
        return ray



class Ray:
    def __init__(self):
        self.origin=numpy.array([])
        self.direction=numpy.array([])

    def setValues(self, neworigin, newdirection):
        self.origin=neworigin
        self.direction=newdirection
    


class Hit:
    
    def __init__(self):
        self.t=0
        self.color=numpy.array([])

    def setValues(self, newt, newcolor):
        self.t=newt
        self.color=newcolor

   

    
if __name__ == '__main__':

    input=input("for the sphere which is colered, enter 1 \nfor the sphere which has depth, enter 2 \nfor the spheres which are colored, enter 3 \nfor the spheres which have depth, enter 4 \n")

    camera=OrthographicCamera(orthocamCenter, orthocamDirection, orthocamUp, orthocamSize)
    camera2=OrthographicCamera(orthocamCenter2, orthocamDirection2, orthocamUp2, orthocamSize2)
    ray=Ray()
    hit=Hit()
    tmin=500
    screenSize=500

    img=Image.new('RGB',(screenSize, screenSize))
    pix=img.load()

    if input=="1":
        sphere=Sphere(groupSphereRadius, groupSphereCenter, groupSphereColor)
        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                h=sphere.intersectWithColor(ray, hit, tmin)
                if h!=-1.0:
                    pix[i,j]=tuple(hit.color)
                else:
                    pix[i, j]=tuple(backgroundColor)

    elif input=="2":
        sphere=Sphere(groupSphereRadius, groupSphereCenter, groupSphereColor)
        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                h=sphere.intersectWithDepth(ray, hit, tmin, 9, 11)
                if h!=-1.0:
                    pix[i,j]=tuple(hit.color)
                else:
                    pix[i, j]=tuple(backgroundColor)
    else:
        group=Group()
        group.adding(Sphere(groupSphereRadius0, groupSphereCenter0, groupSphereColor0))
        group.adding(Sphere(groupSphereRadius1, groupSphereCenter1, groupSphereColor1))
        group.adding(Sphere(groupSphereRadius2, groupSphereCenter2, groupSphereColor2))
        group.adding(Sphere(groupSphereRadius3, groupSphereCenter3, groupSphereColor3))
        group.adding(Sphere(groupSphereRadius4, groupSphereCenter4, groupSphereColor4))

        if input=="3":
            for i in range(screenSize):
                for  j in range(screenSize):
                    x=(i+0.5)/screenSize
                    y=(j+0.5)/screenSize
                    ray=camera2.generateRay(x,y)
                    h=group.intersectColor(ray, hit, tmin)
                    if h!=100:
                        pix[i,j]=tuple(hit.color)
                    else:
                        pix[i, j]=tuple(backgroundColor2)

        elif input=="4":
            for i in range(screenSize):
                for  j in range(screenSize):
                    x=(i+0.5)/screenSize
                    y=(j+0.5)/screenSize
                    ray=camera2.generateRay(x,y)
                    h=group.intersectDepth(ray, hit, tmin, 8, 11.5)
                    if h!=100:
                        pix[i,j]=tuple(hit.color)
                    else:
                        pix[i, j]=tuple(backgroundColor2)

    img.show()



