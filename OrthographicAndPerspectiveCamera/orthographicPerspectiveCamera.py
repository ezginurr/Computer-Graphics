import numpy
import json
import math
from PIL import Image

screenSize=200

#Read the scene1_diffuse
with open('scene1_diffuse.json') as f:
      data = json.load(f)

s1orthocamCenter=numpy.array(data['orthocamera']['center'])
s1orthocamDirection=numpy.array(data['orthocamera']['direction'])
s1orthocamUp=numpy.array(data['orthocamera']['up'])
s1orthocamSize=numpy.array(data['orthocamera']['size'])
s1backgroundColor=numpy.array(data['background']['color'])
s1backgroundAmbient=numpy.array(data['background']['ambient'])
s1lightDirection=numpy.array(data['light']['direction'])
s1lightColor=numpy.array(data['light']['color'])
s1SphereCenter=numpy.array(data['group'][0]['sphere']['center'])
s1SphereRadius=numpy.array(data['group'][0]['sphere']['radius'])
s1SphereColor=numpy.array(data['group'][0]['sphere']['color'])

#Read the scene2_ambient
with open('scene2_ambient.json') as f2:
    data2=json.load(f2)

s2orthocamCenter=numpy.array(data2['orthocamera']['center'])
s2orthocamDirection=numpy.array(data2['orthocamera']['direction'])
s2orthocamUp=numpy.array(data2['orthocamera']['up'])
s2orthocamSize=numpy.array(data2['orthocamera']['size'])
s2backgroundColor=numpy.array(data2['background']['color'])
s2backgroundAmbient=numpy.array(data2['background']['ambient'])
s2lightDirection=numpy.array(data2['light']['direction'])
s2lightColor=numpy.array(data2['light']['color'])
s2SphereCenter=numpy.array(data2['group'][0]['sphere']['center'])
s2SphereRadius=numpy.array(data2['group'][0]['sphere']['radius'])
s2SphereColor=numpy.array(data2['group'][0]['sphere']['color'])

#Read the scene3_perspective
with open('scene3_perspective.json') as f3:
    data3=json.load(f3)

s3perscamCenter=numpy.array(data3['perspectivecamera']['center'])
s3perscamDirection=numpy.array(data3['perspectivecamera']['direction'])
s3perscamUp=numpy.array(data3['perspectivecamera']['up'])
s3perscamAngle=numpy.array(data3['perspectivecamera']['angle'])
s3backgroundColor=numpy.array(data3['background']['color'])
s3backgroundAmbient=numpy.array(data3['background']['ambient'])
s3lightDirection=numpy.array(data3['light']['direction'])
s3lightColor=numpy.array(data3['light']['color'])
s3SphereCenter0=numpy.array(data3['group'][0]['sphere']['center'])
s3SphereRadius0=numpy.array(data3['group'][0]['sphere']['radius'])
s3SphereColor0=numpy.array(data3['group'][0]['sphere']['color'])
s3SphereCenter1=numpy.array(data3['group'][1]['sphere']['center'])
s3SphereRadius1=numpy.array(data3['group'][1]['sphere']['radius'])
s3SphereColor1=numpy.array(data3['group'][1]['sphere']['color'])
s3SphereCenter2=numpy.array(data3['group'][2]['sphere']['center'])
s3SphereRadius2=numpy.array(data3['group'][2]['sphere']['radius'])
s3SphereColor2=numpy.array(data3['group'][2]['sphere']['color'])
s3SphereCenter3=numpy.array(data3['group'][3]['sphere']['center'])
s3SphereRadius3=numpy.array(data3['group'][3]['sphere']['radius'])
s3SphereColor3=numpy.array(data3['group'][3]['sphere']['color'])
s3SphereCenter4=numpy.array(data3['group'][4]['sphere']['center'])
s3SphereRadius4=numpy.array(data3['group'][4]['sphere']['radius'])
s3SphereColor4=numpy.array(data3['group'][4]['sphere']['color'])

#Read the scene4_plane
with open('scene4_plane.json') as f4:
    data4=json.load(f4)

s4perscamCenter=numpy.array(data4['perspectivecamera']['center'])
s4perscamDirection=numpy.array(data4['perspectivecamera']['direction'])
s4perscamUp=numpy.array(data4['perspectivecamera']['up'])
s4perscamAngle=numpy.array(data4['perspectivecamera']['angle'])
s4backgroundColor=numpy.array(data4['background']['color'])
s4backgroundAmbient=numpy.array(data4['background']['ambient'])
s4lightDirection=numpy.array(data4['light']['direction'])
s4lightColor=numpy.array(data4['light']['color'])
s4SphereCenter0=numpy.array(data4['group'][0]['sphere']['center'])
s4SphereRadius0=numpy.array(data4['group'][0]['sphere']['radius'])
s4SphereColor0=numpy.array(data4['group'][0]['sphere']['color'])
s4SphereCenter1=numpy.array(data4['group'][1]['sphere']['center'])
s4SphereRadius1=numpy.array(data4['group'][1]['sphere']['radius'])
s4SphereColor1=numpy.array(data4['group'][1]['sphere']['color'])
s4SphereCenter2=numpy.array(data4['group'][2]['sphere']['center'])
s4SphereRadius2=numpy.array(data4['group'][2]['sphere']['radius'])
s4SphereColor2=numpy.array(data4['group'][2]['sphere']['color'])
s4SphereCenter3=numpy.array(data4['group'][3]['sphere']['center'])
s4SphereRadius3=numpy.array(data4['group'][3]['sphere']['radius'])
s4SphereColor3=numpy.array(data4['group'][3]['sphere']['color'])
s4SphereCenter4=numpy.array(data4['group'][4]['sphere']['center'])
s4SphereRadius4=numpy.array(data4['group'][4]['sphere']['radius'])
s4SphereColor4=numpy.array(data4['group'][4]['sphere']['color'])
s4PlaneNormal=numpy.array(data4['group'][5]['plane']['normal'])
s4PlaneOffset=numpy.array(data4['group'][5]['plane']['offset'])
s4PlaneColor=numpy.array(data4['group'][5]['plane']['color'])

#Read the scene5_sphere_triangle
with open('scene5_sphere_triangle.json') as f5:
    data5=json.load(f5)

s5perscamCenter=numpy.array(data5['perspectivecamera']['center'])
s5perscamDirection=numpy.array(data5['perspectivecamera']['direction'])
s5perscamUp=numpy.array(data5['perspectivecamera']['up'])
s5perscamAngle=numpy.array(data5['perspectivecamera']['angle'])
s5backgroundColor=numpy.array(data5['background']['color'])
s5backgroundAmbient=numpy.array(data5['background']['ambient'])
s5lightDirection=numpy.array(data5['light']['direction'])
s5lightColor=numpy.array(data5['light']['color'])
s5SphereCenter=numpy.array(data5['group'][0]['sphere']['center'])
s5SphereRadius=numpy.array(data5['group'][0]['sphere']['radius'])
s5SphereColor=numpy.array(data5['group'][0]['sphere']['color'])
s5TriangleV1=numpy.array(data5['group'][1]['triangle']['v1'])
s5TriangleV2=numpy.array(data5['group'][1]['triangle']['v2'])
s5TriangleV3=numpy.array(data5['group'][1]['triangle']['v3'])
s5TriangleColor=numpy.array(data5['group'][1]['triangle']['color'])

#Read the scene6_squashed_sphere
with open('scene6_squashed_sphere.json') as f6:
    data6=json.load(f6)

s6orthocamCenter=numpy.array(data6['orthocamera']['center'])
s6orthocamDirection=numpy.array(data6['orthocamera']['direction'])
s6orthocamUp=numpy.array(data6['orthocamera']['up'])
s6orthocamSize=numpy.array(data6['orthocamera']['size'])
s6backgroundColor=numpy.array(data6['background']['color'])
s6backgroundAmbient=numpy.array(data6['background']['ambient'])
s6lightDirection=numpy.array(data6['light']['direction'])
s6lightColor=numpy.array(data6['light']['color'])
s6transScale=numpy.array(data6['group'][0]['transform']['transformations'][0]['scale'])
s6transSphereCenter=numpy.array(data6['group'][0]['transform']['object']['sphere']['center'])
s6transSphereRadius=numpy.array(data6['group'][0]['transform']['object']['sphere']['radius'])
s6transSphereColor=numpy.array(data6['group'][0]['transform']['object']['sphere']['color'])


#Read the scene7_squashed_rotated_sphere
with open('scene7_squashed_rotated_sphere.json') as f7:
    data7=json.load(f7)

s7orthocamCenter=numpy.array(data7['orthocamera']['center'])
s7orthocamDirection=numpy.array(data7['orthocamera']['direction'])
s7orthocamUp=numpy.array(data7['orthocamera']['up'])
s7orthocamSize=numpy.array(data7['orthocamera']['size'])
s7backgroundColor=numpy.array(data7['background']['color'])
s7backgroundAmbient=numpy.array(data7['background']['ambient'])
s7lightDirection=numpy.array(data7['light']['direction'])
s7lightColor=numpy.array(data7['light']['color'])
s7transScale=numpy.array(data7['group'][0]['transform']['transformations'][1]['scale'])
s7transZrotate=data7['group'][0]['transform']['transformations'][0]['zrotate']
s7transSphereCenter=numpy.array(data7['group'][0]['transform']['object']['sphere']['center'])
s7transSphereRadius=numpy.array(data7['group'][0]['transform']['object']['sphere']['radius'])
s7transSphereColor=numpy.array(data7['group'][0]['transform']['object']['sphere']['color'])



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

    def intersect(self, ray, hit, tmin):

        oc=ray.origin - self.center
        a=numpy.dot(ray.direction, ray.direction)
        b=2.0*numpy.dot(oc, ray.direction)
        c=numpy.dot(oc, oc)-self.radius*self.radius
        discriminant=b*b-4*a*c

        if discriminant<0:
          return math.inf
        else:
            t=(-b-numpy.sqrt(discriminant))/(2.0*a)
            t2=(-b+numpy.sqrt(discriminant))/(2.0*a)
            if t>0 and t<tmin:
                if t2<t and t2>0 and t<tmin:
                    t=t2
            elif t2>0 and t<tmin:
                t=t2
            if(t>0 and t<tmin):
                m=ray.origin+ray.direction*t
                n=(m-self.center)/numpy.linalg.norm(m-self.center)
                hit.setNewValues(t, self.color, n)

                return t
            return math.inf

    
class Triangle(Object3D):
    def __init__(self, vertex1, vertex2, vertex3, color):
        self.v1=vertex1
        self.v2=vertex2
        self.v3=vertex3
        self.color=color

    def intersect(self, ray, hit, tmin):
        v0v1=self.v2-self.v1
        v0v2=self.v3-self.v1
        pvec=numpy.cross(ray.direction, v0v2)
        det=numpy.dot(v0v1, pvec)
        if(det<1e-8):
            return math.inf
        if(math.fabs(det)<1e-8):
            return math.inf
        invDet=1/det
        tvec=ray.origin-self.v1
        u=numpy.dot(tvec, pvec)*invDet
        if(u<0 or u>1):
            return math.inf
        qvec=numpy.cross(tvec, v0v1)
        v=numpy.dot(ray.direction, qvec)*invDet
        if(v<0 or v+u>1):
            return math.inf
        t=numpy.dot(v0v2, qvec)*invDet

        if(t>0 and t<tmin):
            n=numpy.cross(v0v1, v0v2)/numpy.linalg.norm(numpy.cross(v0v1, v0v2))
            hit.setNewValues(t, self.color, n)
            return t
        return math.inf
       

class Plane(Object3D):
    
    def __init__(self, normal, d, color):
        self.normal=normal
        self.d=d
        self.color=color

    def intersect(self,ray, hit, tmin):

        denom=numpy.dot(self.normal, ray.direction)
        if(denom>1e-6):
            return math.inf
        t=-(numpy.dot(self.normal, ray.origin)+self.d*-1)/numpy.dot(self.normal, ray.direction)
        if(t>=0 and t<tmin):
            hit.setNewValues(t, self.color, self.normal)
            return t
        
        return math.inf



class Group(Object3D):
    def __init__(self):
        self.objects=[]

    def adding(self, object):
        self.objects.append(object)

    def intersects(self, ray, hit, tmin):
        for k in self.objects:
            t=k.intersect(ray, hit, tmin)
            if t<tmin and t!=math.inf:
                tmin=t
                hit.setValues(t, hit.color)
        return tmin


class Transformation(Object3D):
    def __init__(self, object):
        self.matrix=numpy.eye(4)
        self.object=object

    def rotate(self, rotate):
        theta=numpy.radians(rotate)
        c=numpy.cos(theta)
        s=numpy.sin(theta)
        self.matrix=numpy.dot(self.matrix, numpy.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
      
        
    def scale(self, scale):
        self.matrix=numpy.dot(self.matrix, numpy.array([[scale[0], 0, 0, 0], [0, scale[1], 0, 0], [0, 0, scale[2], 0], [0, 0, 0, 1]]))
        

    def intersect(self, ray, hit, tmin):
        o=numpy.dot(numpy.linalg.inv(self.matrix), numpy.append(ray.origin, [1]))
        d=numpy.dot(numpy.linalg.inv(self.matrix), numpy.append(ray.direction, [0]))
        newray=Ray()
        newray.setValues(numpy.delete(o, 3), numpy.delete(d, 3))
        result=self.object.intersect(newray, hit, tmin)
        if result!=math.inf:
            n=numpy.dot(self.matrix, numpy.append(hit.normal, [1]))/numpy.linalg.norm(numpy.dot(self.matrix,numpy.append(hit.normal, [1])))
            hit.setNormal(numpy.delete(n, 3)/numpy.linalg.norm(numpy.delete(n, 3)))

        return result
        

class Camera:
    def __init__(self):
        self.cam=0

    def generateRay(x, y):
        print()


class PerspectiveCamera(Camera):

    def __init__(self, perscamCenter, perscamDirection, perscamUp, perscamAngle):
        self.center=perscamCenter
        self.direction=perscamDirection
        self.up=perscamUp
        self.angle=perscamAngle

    def generateRay(self, x=0.5, y=0.5):
        ray=Ray()
        right=numpy.cross(self.direction, self.up)/(numpy.linalg.norm(numpy.cross(self.direction, self.up)))
        trueUp=numpy.cross(right, self.direction)/(numpy.linalg.norm(numpy.cross(right, self.direction)))
        height=2*1*math.tan(self.angle*math.pi/180)
        width=height*1
        widthPixel=width/screenSize
        heightPixel=height/screenSize
        lowerleft=self.center+self.direction*1-(width/2)*right-(height/2)*trueUp
        position=lowerleft+(x+0.5)*widthPixel*right+(y+0.5)*heightPixel*trueUp
        direct=position-self.center
        ray.setValues(position,direct)
        return ray


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
        self.normal=numpy.array([])

    def setValues(self, newt, newcolor):
        self.t=newt
        self.color=newcolor

    def setNormal(self, normal):
        self.normal=normal

    def setNewValues(self, newt, newcolor, newNormal):
        self.t=newt
        self.color=newcolor
        self.normal=newNormal

   
if __name__ == '__main__':

    inputt=input("for the scene1, enter 1 \nfor the scene2, enter 2 \nfor the scene3, enter 3 \nfor the scene4, enter 4 \nfor the scene5, enter 5 \nfor the scene6, enter 6 \nfor the scene7, enter 7 \n")
    inp=input("for colored image, enter 1 \nfor depth image, enter 2\n")

    ray=Ray()
    hit=Hit()
    tmin=screenSize

    img=Image.new('RGB',(screenSize, screenSize))
    pix=img.load()

    if inputt=="1":
        camera=OrthographicCamera(s1orthocamCenter, s1orthocamDirection, s1orthocamUp, s1orthocamSize)
        sphere=Sphere(s1SphereRadius, s1SphereCenter, s1SphereColor)
        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                h=sphere.intersect(ray, hit, tmin)
                if h!=math.inf:
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((((hit.color*s1backgroundAmbient)+max(numpy.dot(-1*s1lightDirection, hit.normal), 0)*(hit.color*s1lightColor))*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s1backgroundAmbient*s1backgroundColor*255).astype(int))

    elif inputt=="2":
        camera=OrthographicCamera(s2orthocamCenter, s2orthocamDirection, s2orthocamUp, s2orthocamSize)
        sphere=Sphere(s2SphereRadius, s2SphereCenter, s2SphereColor)
        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                h=sphere.intersect(ray, hit, tmin)
                if h!=math.inf: 
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((hit.color*s2backgroundAmbient*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s2backgroundColor*s2backgroundAmbient*255).astype(int))
                    

    elif inputt=="3":
        camera=PerspectiveCamera(s3perscamCenter, s3perscamDirection, s3perscamUp, s3perscamAngle)
        group=Group()
        group.adding(Sphere(s3SphereRadius0, s3SphereCenter0, s3SphereColor0))
        group.adding(Sphere(s3SphereRadius1, s3SphereCenter1, s3SphereColor1))
        group.adding(Sphere(s3SphereRadius2, s3SphereCenter2, s3SphereColor2))
        group.adding(Sphere(s3SphereRadius3, s3SphereCenter3, s3SphereColor3))
        group.adding(Sphere(s3SphereRadius4, s3SphereCenter4, s3SphereColor4))
        
        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                h=group.intersects(ray, hit, tmin)
                if h!=screenSize: 
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((((hit.color*s3backgroundAmbient)+max(numpy.dot(-1*s3lightDirection, hit.normal), 0)*(hit.color*s3lightColor))*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s3backgroundColor*s3backgroundAmbient*255).astype(int))
                    
                    
    elif inputt=="4":
        camera=PerspectiveCamera(s4perscamCenter, s4perscamDirection, s4perscamUp, s4perscamAngle)
        group=Group()
        group.adding(Sphere(s4SphereRadius0, s4SphereCenter0, s4SphereColor0))
        group.adding(Sphere(s4SphereRadius1, s4SphereCenter1, s4SphereColor1))
        group.adding(Sphere(s4SphereRadius2, s4SphereCenter2, s4SphereColor2))
        group.adding(Sphere(s4SphereRadius3, s4SphereCenter3, s4SphereColor3))
        group.adding(Sphere(s4SphereRadius4, s4SphereCenter4, s4SphereColor4))
        group.adding(Plane(s4PlaneNormal, s4PlaneOffset, s4PlaneColor))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                h=group.intersects(ray, hit, tmin)
                if h!=screenSize: 
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((((hit.color*s4backgroundAmbient)+max(numpy.dot(-1*s4lightDirection, hit.normal), 0)*(hit.color*s4lightColor))*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s4backgroundColor*s4backgroundAmbient*255).astype(int))


    elif inputt=="5":
        camera=PerspectiveCamera(s4perscamCenter, s4perscamDirection, s4perscamUp, s4perscamAngle)
        group=Group()
        group.adding(Sphere(s5SphereRadius, s5SphereCenter, s5SphereColor))
        group.adding(Triangle(s5TriangleV1, s5TriangleV2, s5TriangleV3, s5TriangleColor))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                h=group.intersects(ray, hit, tmin)
                if h!=screenSize: 
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((((hit.color*s5backgroundAmbient)+max(numpy.dot(-1*s5lightDirection, hit.normal), 0)*(hit.color*s5lightColor))*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s5backgroundColor*s5backgroundAmbient*255).astype(int))

    elif inputt=="6":
        camera=OrthographicCamera(s6orthocamCenter, s6orthocamDirection, s6orthocamUp, s6orthocamSize)
        sphere=Sphere(s6transSphereRadius, s6transSphereCenter, s6transSphereColor)
        transformation=Transformation(sphere)
        transformation.scale(s6transScale)
        group=Group()
        group.adding(transformation)
        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                h=group.intersects(ray, hit, tmin)
                if h!=screenSize:
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((((hit.color*s6backgroundAmbient)+max(numpy.dot(-1*s6lightDirection, hit.normal), 0)*(hit.color*s6lightColor))*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s6backgroundAmbient*s6backgroundColor*255).astype(int))

    elif inputt=="7":
        camera=OrthographicCamera(s7orthocamCenter, s7orthocamDirection, s7orthocamUp, s7orthocamSize)
        sphere=Sphere(s7transSphereRadius, s7transSphereCenter, s7transSphereColor)
        transformation=Transformation(sphere)
        transformation.rotate(s7transZrotate)
        transformation.scale(s7transScale)
        group=Group()
        group.adding(transformation)
        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                h=group.intersects(ray, hit, tmin)
                if h!=screenSize: 
                    if(inp=="1"):
                        pix[i,screenSize-j-1]=tuple((((hit.color*s7backgroundAmbient)+max(numpy.dot(-1*s7lightDirection, hit.normal), 0)*(hit.color*s7lightColor))*255).astype(int))
                    else:
                        nf=int(((12-hit.t)/(12-8))*255)
                        pix[i,screenSize-j-1]=tuple(numpy.array([nf, nf, nf]))
                else:
                    pix[i,screenSize-j-1]=tuple((s7backgroundAmbient*s7backgroundColor*255).astype(int))
                    
    img.show()