import numpy
import json
import math
from PIL import Image

screenSize=300

#Read the scene1_exponent_variations
with open('scene1_exponent_variations.json') as f:
      data = json.load(f)

s1orthocamCenter=numpy.array(data['orthocamera']['center'])
s1orthocamDirection=numpy.array(data['orthocamera']['direction'])
s1orthocamUp=numpy.array(data['orthocamera']['up'])
s1orthocamSize=numpy.array(data['orthocamera']['size'])
s1backgroundColor=numpy.array(data['background']['color'])
s1backgroundAmbient=numpy.array(data['background']['ambient'])
s1lightDirection=numpy.array(data['light']['direction'])
s1lightColor=numpy.array(data['light']['color'])

s1SphereCenter0=numpy.array(data['group'][0]['sphere']['center'])
s1SphereRadius0=numpy.array(data['group'][0]['sphere']['radius'])
s1SphereMaterial0=data['group'][0]['sphere']['material']
s1SphereCenter1=numpy.array(data['group'][1]['sphere']['center'])
s1SphereRadius1=numpy.array(data['group'][1]['sphere']['radius'])
s1SphereMaterial1=data['group'][1]['sphere']['material']
s1SphereCenter2=numpy.array(data['group'][2]['sphere']['center'])
s1SphereRadius2=numpy.array(data['group'][2]['sphere']['radius'])
s1SphereMaterial2=data['group'][2]['sphere']['material']
s1SphereCenter3=numpy.array(data['group'][3]['sphere']['center'])
s1SphereRadius3=numpy.array(data['group'][3]['sphere']['radius'])
s1SphereMaterial3=data['group'][3]['sphere']['material']
s1SphereCenter4=numpy.array(data['group'][4]['sphere']['center'])
s1SphereRadius4=numpy.array(data['group'][4]['sphere']['radius'])
s1SphereMaterial4=data['group'][4]['sphere']['material']
s1SphereCenter5=numpy.array(data['group'][5]['sphere']['center'])
s1SphereRadius5=numpy.array(data['group'][5]['sphere']['radius'])
s1SphereMaterial5=data['group'][5]['sphere']['material']
s1SphereCenter6=numpy.array(data['group'][6]['sphere']['center'])
s1SphereRadius6=numpy.array(data['group'][6]['sphere']['radius'])
s1SphereMaterial6=data['group'][6]['sphere']['material']
s1SphereCenter7=numpy.array(data['group'][7]['sphere']['center'])
s1SphereRadius7=numpy.array(data['group'][7]['sphere']['radius'])
s1SphereMaterial7=data['group'][7]['sphere']['material']
s1SphereCenter8=numpy.array(data['group'][8]['sphere']['center'])
s1SphereRadius8=numpy.array(data['group'][8]['sphere']['radius'])
s1SphereMaterial8=data['group'][8]['sphere']['material']

s1PhongMatDiffuse0=numpy.array(data['materials'][0]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular0=numpy.array(data['materials'][0]['phongMaterial']['specularColor'])
s1PhongMatExponent0=data['materials'][0]['phongMaterial']['exponent']
s1PhongMatDiffuse1=numpy.array(data['materials'][1]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular1=numpy.array(data['materials'][1]['phongMaterial']['specularColor'])
s1PhongMatExponent1=data['materials'][1]['phongMaterial']['exponent']
s1PhongMatDiffuse2=numpy.array(data['materials'][2]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular2=numpy.array(data['materials'][2]['phongMaterial']['specularColor'])
s1PhongMatExponent2=data['materials'][2]['phongMaterial']['exponent']
s1PhongMatDiffuse3=numpy.array(data['materials'][3]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular3=numpy.array(data['materials'][3]['phongMaterial']['specularColor'])
s1PhongMatExponent3=data['materials'][3]['phongMaterial']['exponent']
s1PhongMatDiffuse4=numpy.array(data['materials'][4]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular4=numpy.array(data['materials'][4]['phongMaterial']['specularColor'])
s1PhongMatExponent4=data['materials'][4]['phongMaterial']['exponent']
s1PhongMatDiffuse5=numpy.array(data['materials'][5]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular5=numpy.array(data['materials'][5]['phongMaterial']['specularColor'])
s1PhongMatExponent5=data['materials'][5]['phongMaterial']['exponent']
s1PhongMatDiffuse6=numpy.array(data['materials'][6]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular6=numpy.array(data['materials'][6]['phongMaterial']['specularColor'])
s1PhongMatExponent6=data['materials'][6]['phongMaterial']['exponent']
s1PhongMatDiffuse7=numpy.array(data['materials'][7]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular7=numpy.array(data['materials'][7]['phongMaterial']['specularColor'])
s1PhongMatExponent7=data['materials'][7]['phongMaterial']['exponent']
s1PhongMatDiffuse8=numpy.array(data['materials'][8]['phongMaterial']['diffuseColor'])
s1PhongMatSpecular8=numpy.array(data['materials'][8]['phongMaterial']['specularColor'])
s1PhongMatExponent8=data['materials'][8]['phongMaterial']['exponent']


#Read the scene2_plane_sphere
with open('scene2_plane_sphere.json') as f2:
    data2=json.load(f2)

s2perscamCenter=numpy.array(data2['perspectivecamera']['center'])
s2perscamDirection=numpy.array(data2['perspectivecamera']['direction'])
s2perscamUp=numpy.array(data2['perspectivecamera']['up'])
s2perscamAngle=numpy.array(data2['perspectivecamera']['angle'])
s2backgroundColor=numpy.array(data2['background']['color'])
s2backgroundAmbient=numpy.array(data2['background']['ambient'])
s2lightDirection=numpy.array(data2['lights'][0]['directionalLight']['direction'])
s2lightColor=numpy.array(data2['lights'][0]['directionalLight']['color'])
s2SphereCenter=numpy.array(data2['group'][0]['sphere']['center'])
s2SphereRadius=numpy.array(data2['group'][0]['sphere']['radius'])
s2SphereMaterial=data2['group'][0]['sphere']['material']
s2PlaneNormal=numpy.array(data2['group'][1]['plane']['normal'])
s2PlaneOffset=numpy.array(data2['group'][1]['plane']['offset'])
s2PlaneMaterial=data2['group'][1]['plane']['material']
s2PhongMatDiffuse1=numpy.array(data2['materials'][0]['phongMaterial']['diffuseColor'])
s2PhongMatDiffuse2=numpy.array(data2['materials'][1]['phongMaterial']['diffuseColor'])

#Read the scene3_colored_lights
with open('scene3_colored_lights.json') as f3:
    data3=json.load(f3)

s3perscamCenter=numpy.array(data3['perspectivecamera']['center'])
s3perscamDirection=numpy.array(data3['perspectivecamera']['direction'])
s3perscamUp=numpy.array(data3['perspectivecamera']['up'])
s3perscamAngle=numpy.array(data3['perspectivecamera']['angle'])
s3backgroundColor=numpy.array(data3['background']['color'])
s3backgroundAmbient=numpy.array(data3['background']['ambient'])
s3SphereCenter=numpy.array(data3['group'][0]['sphere']['center'])
s3SphereRadius=numpy.array(data3['group'][0]['sphere']['radius'])
s3SphereMaterial=data3['group'][0]['sphere']['material']
s3PlaneNormal=numpy.array(data3['group'][1]['plane']['normal'])
s3PlaneOffset=numpy.array(data3['group'][1]['plane']['offset'])
s3PlaneMaterial=data3['group'][1]['plane']['material']

s3PhongMatDiffuse=numpy.array(data3['materials'][0]['phongMaterial']['diffuseColor'])

s3lightDirection1=numpy.array(data3['lights'][0]['directionalLight']['direction'])
s3lightColor1=numpy.array(data3['lights'][0]['directionalLight']['color'])
s3lightDirection2=numpy.array(data3['lights'][1]['directionalLight']['direction'])
s3lightColor2=numpy.array(data3['lights'][1]['directionalLight']['color'])
s3lightDirection3=numpy.array(data3['lights'][2]['directionalLight']['direction'])
s3lightColor3=numpy.array(data3['lights'][2]['directionalLight']['color'])

#Read the scene4_reflective_sphere
with open('scene4_reflective_sphere.json') as f4:
    data4=json.load(f4)

s4perscamCenter=numpy.array(data4['perspectivecamera']['center'])
s4perscamDirection=numpy.array(data4['perspectivecamera']['direction'])
s4perscamUp=numpy.array(data4['perspectivecamera']['up'])
s4perscamAngle=numpy.array(data4['perspectivecamera']['angle'])
s4backgroundColor=numpy.array(data4['background']['color'])
s4backgroundAmbient=numpy.array(data4['background']['ambient'])
s4lightDirection=numpy.array(data4['lights'][0]['directionalLight']['direction'])
s4lightColor=numpy.array(data4['lights'][0]['directionalLight']['color'])

s4PhongMatDiffuse0=numpy.array(data4['materials'][0]['phongMaterial']['diffuseColor'])
s4PhongMatSpecular0=numpy.array(data4['materials'][0]['phongMaterial']['specularColor'])
s4PhongMatExponent0=data4['materials'][0]['phongMaterial']['exponent']
s4PhongMatTransparent0=numpy.array(data4['materials'][0]['phongMaterial']['transparentColor'])
s4PhongMatReflective0=numpy.array(data4['materials'][0]['phongMaterial']['reflectiveColor'])
s4PhongMatIndex0=data4['materials'][0]['phongMaterial']['indexOfRefraction']
s4PhongMatDiffuse1=numpy.array(data4['materials'][1]['phongMaterial']['diffuseColor'])
s4PhongMatSpecular1=numpy.array(data4['materials'][1]['phongMaterial']['specularColor'])
s4PhongMatExponent1=data4['materials'][1]['phongMaterial']['exponent']
s4PhongMatTransparent1=numpy.array(data4['materials'][1]['phongMaterial']['transparentColor'])
s4PhongMatReflective1=numpy.array(data4['materials'][1]['phongMaterial']['reflectiveColor'])
s4PhongMatIndex1=data4['materials'][1]['phongMaterial']['indexOfRefraction']
s4PhongMatDiffuse2=numpy.array(data4['materials'][2]['phongMaterial']['diffuseColor'])

s4SphereCenter0=numpy.array(data4['group'][0]['sphere']['center'])
s4SphereRadius0=numpy.array(data4['group'][0]['sphere']['radius'])
s4SphereMaterial0=data4['group'][0]['sphere']['material']
s4SphereCenter1=numpy.array(data4['group'][1]['sphere']['center'])
s4SphereRadius1=numpy.array(data4['group'][1]['sphere']['radius'])
s4SphereMaterial1=data4['group'][1]['sphere']['material']
s4PlaneNormal=numpy.array(data4['group'][2]['plane']['normal'])
s4PlaneOffset=numpy.array(data4['group'][2]['plane']['offset'])
s4PlaneMaterial=data4['group'][2]['plane']['material']


#Read the scene5_transparent_sphere
with open('scene5_transparent_sphere.json') as f5:
    data5=json.load(f5)

s5perscamCenter=numpy.array(data5['perspectivecamera']['center'])
s5perscamDirection=numpy.array(data5['perspectivecamera']['direction'])
s5perscamUp=numpy.array(data5['perspectivecamera']['up'])
s5perscamAngle=numpy.array(data5['perspectivecamera']['angle'])
s5backgroundColor=numpy.array(data5['background']['color'])
s5backgroundAmbient=numpy.array(data5['background']['ambient'])
s5lightDirection1=numpy.array(data5['lights'][0]['directionalLight']['direction'])
s5lightColor1=numpy.array(data5['lights'][0]['directionalLight']['color'])
s5lightDirection2=numpy.array(data5['lights'][1]['directionalLight']['direction'])
s5lightColor2=numpy.array(data5['lights'][1]['directionalLight']['color'])

s5PhongMatDiffuse1=numpy.array(data5['materials'][0]['phongMaterial']['diffuseColor'])
s5PhongMatDiffuse2=numpy.array(data5['materials'][1]['phongMaterial']['diffuseColor'])
s5PhongMatDiffuse3=numpy.array(data5['materials'][2]['phongMaterial']['diffuseColor'])
s5PhongMatDiffuse4=numpy.array(data5['materials'][3]['phongMaterial']['diffuseColor'])
s5PhongMatDiffuse5=numpy.array(data5['materials'][4]['phongMaterial']['diffuseColor'])
s5PhongMatSpecular5=numpy.array(data5['materials'][4]['phongMaterial']['specularColor'])
s5PhongMatExponent5=data5['materials'][4]['phongMaterial']['exponent']
s5PhongMatTransparent5=numpy.array(data5['materials'][4]['phongMaterial']['transparentColor'])
s5PhongMatReflective5=numpy.array(data5['materials'][4]['phongMaterial']['reflectiveColor'])
s5PhongMatIndex5=data5['materials'][4]['phongMaterial']['indexOfRefraction']

s5PlaneNormal=numpy.array(data5['group'][0]['plane']['normal'])
s5PlaneOffset=numpy.array(data5['group'][0]['plane']['offset'])
s5PlaneMaterial=data5['group'][0]['plane']['material']

s5transTranslate1=numpy.array(data5['group'][1]['transform']['transformations'][0]['translate'])
s5transScale1=numpy.array(data5['group'][1]['transform']['transformations'][1]['scale'])
s5transSphereCenter1=numpy.array(data5['group'][1]['transform']['object']['sphere']['center'])
s5transSphereRadius1=data5['group'][1]['transform']['object']['sphere']['radius']
s5transSphereMaterial1=data5['group'][1]['transform']['object']['sphere']['material']
s5transTranslate2=numpy.array(data5['group'][2]['transform']['transformations'][0]['translate'])
s5transScale2=numpy.array(data5['group'][2]['transform']['transformations'][1]['scale'])
s5transSphereCenter2=numpy.array(data5['group'][2]['transform']['object']['sphere']['center'])
s5transSphereRadius2=data5['group'][2]['transform']['object']['sphere']['radius']
s5transSphereMaterial2=data5['group'][2]['transform']['object']['sphere']['material']
s5transTranslate3=numpy.array(data5['group'][3]['transform']['transformations'][0]['translate'])
s5transScale3=numpy.array(data5['group'][3]['transform']['transformations'][1]['scale'])
s5transSphereCenter3=numpy.array(data5['group'][3]['transform']['object']['sphere']['center'])
s5transSphereRadius3=data5['group'][3]['transform']['object']['sphere']['radius']
s5transSphereMaterial3=data5['group'][3]['transform']['object']['sphere']['material']

s5SphereCenter=numpy.array(data5['group'][4]['sphere']['center'])
s5SphereRadius=numpy.array(data5['group'][4]['sphere']['radius'])
s5SphereMaterial=data5['group'][4]['sphere']['material']

#Read the scene6_transparent_sphere2
with open('scene6_transparent_sphere2.json') as f6:
    data6=json.load(f6)

s6perscamCenter=numpy.array(data6['perspectivecamera']['center'])
s6perscamDirection=numpy.array(data6['perspectivecamera']['direction'])
s6perscamUp=numpy.array(data6['perspectivecamera']['up'])
s6perscamAngle=numpy.array(data6['perspectivecamera']['angle'])
s6backgroundColor=numpy.array(data6['background']['color'])
s6backgroundAmbient=numpy.array(data6['background']['ambient'])
s6lightDirection1=numpy.array(data6['lights'][0]['directionalLight']['direction'])
s6lightColor1=numpy.array(data6['lights'][0]['directionalLight']['color'])
s6lightDirection2=numpy.array(data6['lights'][1]['directionalLight']['direction'])
s6lightColor2=numpy.array(data6['lights'][1]['directionalLight']['color'])

s6PhongMatDiffuse1=numpy.array(data6['materials'][0]['phongMaterial']['diffuseColor'])
s6PhongMatDiffuse2=numpy.array(data6['materials'][1]['phongMaterial']['diffuseColor'])
s6PhongMatDiffuse3=numpy.array(data6['materials'][2]['phongMaterial']['diffuseColor'])
s6PhongMatDiffuse4=numpy.array(data6['materials'][3]['phongMaterial']['diffuseColor'])
s6PhongMatDiffuse5=numpy.array(data6['materials'][4]['phongMaterial']['diffuseColor'])
s6PhongMatSpecular5=numpy.array(data6['materials'][4]['phongMaterial']['specularColor'])
s6PhongMatExponent5=data6['materials'][4]['phongMaterial']['exponent']
s6PhongMatTransparent5=numpy.array(data6['materials'][4]['phongMaterial']['transparentColor'])
s6PhongMatReflective5=numpy.array(data6['materials'][4]['phongMaterial']['reflectiveColor'])
s6PhongMatIndex5=data6['materials'][4]['phongMaterial']['indexOfRefraction']

s6PlaneNormal=numpy.array(data6['group'][0]['plane']['normal'])
s6PlaneOffset=numpy.array(data6['group'][0]['plane']['offset'])
s6PlaneMaterial=data6['group'][0]['plane']['material']

s6transTranslate1=numpy.array(data6['group'][1]['transform']['transformations'][0]['translate'])
s6transScale1=numpy.array(data6['group'][1]['transform']['transformations'][1]['scale'])
s6transSphereCenter1=numpy.array(data6['group'][1]['transform']['object']['sphere']['center'])
s6transSphereRadius1=data6['group'][1]['transform']['object']['sphere']['radius']
s6transSphereMaterial1=data6['group'][1]['transform']['object']['sphere']['material']
s6transTranslate2=numpy.array(data6['group'][2]['transform']['transformations'][0]['translate'])
s6transScale2=numpy.array(data6['group'][2]['transform']['transformations'][1]['scale'])
s6transSphereCenter2=numpy.array(data6['group'][2]['transform']['object']['sphere']['center'])
s6transSphereRadius2=data6['group'][2]['transform']['object']['sphere']['radius']
s6transSphereMaterial2=data6['group'][2]['transform']['object']['sphere']['material']
s6transTranslate3=numpy.array(data6['group'][3]['transform']['transformations'][0]['translate'])
s6transScale3=numpy.array(data6['group'][3]['transform']['transformations'][1]['scale'])
s6transSphereCenter3=numpy.array(data6['group'][3]['transform']['object']['sphere']['center'])
s6transSphereRadius3=data6['group'][3]['transform']['object']['sphere']['radius']
s6transSphereMaterial3=data6['group'][3]['transform']['object']['sphere']['material']

s6SphereCenter=numpy.array(data6['group'][4]['sphere']['center'])
s6SphereRadius=numpy.array(data6['group'][4]['sphere']['radius'])
s6SphereMaterial=data6['group'][4]['sphere']['material']


class Light():
    def __init__(self, color):
        self.color=color
    
class DirectionalLight(Light):
    def __init__(self, color, direction):
        self.color=color
        self.direction=direction
  
class Material():
    def __init__(self, diffuseColor, reflectiveColor, transparentColor, indexOfRefraction):
        self.diffuseColor=diffuseColor
        self.reflectiveColor=reflectiveColor
        self.transparentColor=transparentColor
        self.indexOfRefraction=indexOfRefraction

    def shade(self, ray, hit, light):
        return color

class PhongMaterial(Material):
    def __init__(self, diffuseColor, reflectiveColor, transparentColor, indexOfRefraction, specularColor, exponent):
        self.diffuseColor=diffuseColor
        self.reflectiveColor=reflectiveColor
        self.transparentColor=transparentColor
        self.indexOfRefraction=indexOfRefraction
        self.specularColor=specularColor
        self.exponent=exponent

    def shade(self, ray, hit, i):
        
        color=numpy.array([0, 0, 0])
        diffuseC=max(numpy.dot(-i.direction, hit.normal), 0)*(self.diffuseColor*i.color)
        if(self.specularColor.size!=0):
            R=hit.normal*2*(numpy.dot(hit.normal, i.direction))-i.direction
            R=R/numpy.linalg.norm(R)
            specularC=pow(max(numpy.dot(R, ray.direction), 0), self.exponent)*(self.specularColor*i.color)
            color=color+diffuseC+specularC
        else:
            color=color+diffuseC
        return color

class Object3D:
    def __init_(self, metarial):
        self.color=numpy.array([])
        self.metarial=metarial

    def intersect(ray, hit, tmin):
        print()

class Sphere(Object3D):
    def __init__(self, groupSphereRadius, groupSphereCenter, material):
        self.radius=groupSphereRadius
        self.center=groupSphereCenter
        self.material=material

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
            if(t>tmin):
                m=ray.origin+ray.direction*t
                n=(m-self.center)/numpy.linalg.norm(m-self.center)
                hit.setHitValues(t, n, self.material)

                return t
            return math.inf

class Triangle(Object3D):
    def __init__(self, vertex1, vertex2, vertex3, metarial):
        self.v1=vertex1
        self.v2=vertex2
        self.v3=vertex3
        self.metarial=metarial


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

        if(t>tmin):
            n=numpy.cross(v0v1, v0v2)/numpy.linalg.norm(numpy.cross(v0v1, v0v2))
            hit.setHitValues(t, n, self.material)
            return t
        return math.inf
       
class Plane(Object3D):
    
    def __init__(self, normal, d, material):
        self.normal=normal
        self.d=d
        self.material=material

    def intersect(self,ray, hit, tmin):

        denom=numpy.dot(self.normal, ray.direction)
        if(denom>1e-6):
            return math.inf
        t=-(numpy.dot(self.normal, ray.origin)+self.d*-1)/numpy.dot(self.normal, ray.direction)
        if(t>tmin):
            hit.setHitValues(t, self.normal, self.material)
            return t
        
        return math.inf

class Group(Object3D):
    def __init__(self):
        self.objects=[]

    def adding(self, object):
        self.objects.append(object)

    def intersects(self, ray, hit, tmin, lights):
        mint=math.inf
        for k in self.objects:
            t=k.intersect(ray, hit, tmin)
            if t>tmin and t!=math.inf and t<mint:
                mint=t
                tmin=t
                if(isinstance(k, Transformation)):
                    color=k.object.material.shade(ray, hit, lights, self.objects, k)
                    #color=ray_tarce(ray, hit, lights, self.objects, k.object)
                else:
                    color=k.material.shade(ray, hit, lights)
                    #color=ray_tarce(ray, hit, lights, self.objects, k)
                hit.setValues(t, color)
        return mint

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
        

    def translate(self, translate):
        self.matrix=numpy.dot(self.matrix, numpy.array([[1, 0, 0, translate[0]], [0, 1, 0, translate[1]], [0, 0, 1, translate[2]], [0, 0, 0, 1]]))
        

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
        self.material=PhongMaterial(numpy.array([]), numpy.array([]), numpy.array([]), 0, numpy.array([]), 0)

    def setValues(self, newt, newcolor):
        self.t=newt
        self.color=newcolor
        #self.normal=newnormal
        #self.material=newmaterial

    def setNormal(self, normal):
        self.normal=normal

    def setT(self, t):
        self.t=t

    def setHitValues(self, newt, newNormal, metarial):
        self.t=newt
        self.normal=newNormal
        self.material=metarial

def ray_trace(ray, hit, tmin, lights, objs, depth, ambient):
    
    obj=0
    mint=math.inf
    for o in objs:
        t=o.intersect(ray, hit, tmin)
        if t>tmin and t!=math.inf and t<mint:
            mint=t
            obj=o
    
    if(obj!=0):
        obj.intersect(ray, hit, tmin)

        if(isinstance(obj, Transformation)):
            obj=obj.object

        color=shadow(ray, hit, lights, objs, obj, ambient)
        if(depth>0):
            depth=depth-1
            if(obj.material.reflectiveColor.size!=0):
                rr=mirrorDirection(ray, hit)
                color=color+obj.material.reflectiveColor*ray_trace(rr, hit, tmin, lights, objs, depth, ambient)
    
            if(obj.material.transparentColor.size!=0):
                rr=transmittedDirection(ray, hit, obj.material.indexOfRefraction)
                if(rr!=0):
                    color=color+obj.material.transparentColor*ray_trace(rr, hit, tmin, lights, objs, depth, ambient)
    

        return color

    else:
        return numpy.array([0, 0, 0])

def mirrorDirection(incidentRay, hit):
    
    refRay=Ray()
    r=incidentRay.direction-2.0*numpy.dot(incidentRay.direction, hit.normal)*hit.normal
    refRay.setValues((incidentRay.origin+incidentRay.direction*hit.t), r)
    return refRay

def transmittedDirection(incidentRay, hit, u):
    refRay=Ray()
    if(1-u*u*(1-numpy.dot(hit.normal, incidentRay.direction)*numpy.dot(hit.normal, incidentRay.direction))<0):
        return 0
    t=(u*numpy.dot(hit.normal, incidentRay.direction)-math.sqrt(1-u*u*(1-numpy.dot(hit.normal, incidentRay.direction)*numpy.dot(hit.normal, incidentRay.direction))))*hit.normal-u*incidentRay.direction
    #t=(u*numpy.dot(hit.normal, incidentRay.direction))*hit.normal-u*incidentRay.direction
    t=t/numpy.linalg.norm(t)
    refRay.setValues((incidentRay.origin+incidentRay.direction*hit.t), t)
    return refRay

def shadow(ray, hit, lights, objs, obj, ambient):
    
    color=numpy.array([0, 0, 0])
    color=color+ambient*hit.material.diffuseColor
    for i in lights:
        ray2=Ray()
        ray2.setValues((ray.origin+ray.direction*hit.t), -i.direction)
        hit2=Hit()
        t2=math.inf
        flag=math.inf
        for o in objs:
            if(o!=obj):
                t2=o.intersect(ray2, hit2, 0)
            if(t2!=math.inf):
                flag=1
        if(flag==math.inf):
            color=color+hit.material.shade(ray, hit, i)
    
    return color

if __name__ == '__main__':

    input=input("for the scene1, enter 1 \nfor the scene2, enter 2 \nfor the scene3, enter 3 \nfor the scene4, enter 4 \nfor the scene5, enter 5 \nfor the scene6, enter 6 \n")
    
    ray=Ray()
    hit=Hit()
    tmin=0.0001

    img=Image.new('RGB',(screenSize, screenSize))
    pix=img.load()


    if input=="1":
        camera=OrthographicCamera(s1orthocamCenter, s1orthocamDirection, s1orthocamUp, s1orthocamSize)

        lights=[]
        lights.append(DirectionalLight(s1lightColor, s1lightDirection))

        material=[]
        material.append(PhongMaterial(s1PhongMatDiffuse0, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular0, s1PhongMatExponent0))
        material.append(PhongMaterial(s1PhongMatDiffuse1, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular1, s1PhongMatExponent1))
        material.append(PhongMaterial(s1PhongMatDiffuse2, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular2, s1PhongMatExponent2))
        material.append(PhongMaterial(s1PhongMatDiffuse3, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular3, s1PhongMatExponent3))
        material.append(PhongMaterial(s1PhongMatDiffuse4, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular4, s1PhongMatExponent4))
        material.append(PhongMaterial(s1PhongMatDiffuse5, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular5, s1PhongMatExponent5))
        material.append(PhongMaterial(s1PhongMatDiffuse6, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular6, s1PhongMatExponent6))
        material.append(PhongMaterial(s1PhongMatDiffuse7, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular7, s1PhongMatExponent7))
        material.append(PhongMaterial(s1PhongMatDiffuse8, numpy.array([]), numpy.array([]), 0, s1PhongMatSpecular8, s1PhongMatExponent8))

        group=Group()
        group.adding(Sphere(s1SphereRadius0, s1SphereCenter0, material[s1SphereMaterial0]))
        group.adding(Sphere(s1SphereRadius1, s1SphereCenter1, material[s1SphereMaterial1]))
        group.adding(Sphere(s1SphereRadius2, s1SphereCenter2, material[s1SphereMaterial2]))
        group.adding(Sphere(s1SphereRadius3, s1SphereCenter3, material[s1SphereMaterial3]))
        group.adding(Sphere(s1SphereRadius4, s1SphereCenter4, material[s1SphereMaterial4]))
        group.adding(Sphere(s1SphereRadius5, s1SphereCenter5, material[s1SphereMaterial5]))
        group.adding(Sphere(s1SphereRadius6, s1SphereCenter6, material[s1SphereMaterial6]))
        group.adding(Sphere(s1SphereRadius7, s1SphereCenter7, material[s1SphereMaterial7]))
        group.adding(Sphere(s1SphereRadius8, s1SphereCenter8, material[s1SphereMaterial8]))

        for i in range(screenSize):
            for  j in range(screenSize):
                x=(i+0.5)/screenSize
                y=(j+0.5)/screenSize
                ray=camera.generateRay(x,y)
                #h=group.intersects(ray, hit, tmin, lights)
                color=ray_trace(ray, hit, tmin, lights, group.objects, 3, s1backgroundAmbient)
                if color.all!=0:#h!=math.inf: 
                    #pix[i,screenSize-j-1]=tuple(((hit.color+s4backgroundAmbient)*255).astype(int))
                    pix[i,screenSize-j-1]=tuple(((color)*255).astype(int))
                else:
                    pix[i,screenSize-j-1]=tuple((s1backgroundAmbient*s1backgroundColor*255).astype(int))

    elif input=="2":
        camera=PerspectiveCamera(s2perscamCenter, s2perscamDirection, s2perscamUp, s2perscamAngle)

        lights=[]
        lights.append(DirectionalLight(s2lightColor, s2lightDirection))

        material=[]
        material.append(PhongMaterial(s2PhongMatDiffuse1, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s2PhongMatDiffuse2, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        
        group=Group()
        group.adding(Sphere(s2SphereRadius, s2SphereCenter, material[s2SphereMaterial]))
        group.adding(Plane(s2PlaneNormal, s2PlaneOffset, material[s2PlaneMaterial]))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                color=ray_trace(ray, hit, tmin, lights, group.objects, 3, s2backgroundAmbient)
                if color.all!=0:
                    pix[i,screenSize-j-1]=tuple(((color)*255).astype(int))
                else:
                    pix[i,screenSize-j-1]=tuple((s2backgroundColor*s2backgroundAmbient*255).astype(int))
                    

    elif input=="3":
        camera=PerspectiveCamera(s3perscamCenter, s3perscamDirection, s3perscamUp, s3perscamAngle)

        lights=[]
        lights.append(DirectionalLight(s3lightColor1, s3lightDirection1))
        lights.append(DirectionalLight(s3lightColor2, s3lightDirection2))
        lights.append(DirectionalLight(s3lightColor3, s3lightDirection3))

        material=[]
        material.append(PhongMaterial(s3PhongMatDiffuse, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        
        group=Group()
        group.adding(Sphere(s3SphereRadius, s3SphereCenter, material[s3SphereMaterial]))
        group.adding(Plane(s3PlaneNormal, s3PlaneOffset, material[s3PlaneMaterial]))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                color=ray_trace(ray, hit, tmin, lights, group.objects, 3, s3backgroundAmbient)
                if color.all!=0:
                    pix[i,screenSize-j-1]=tuple(((color)*255).astype(int))
                else:
                    pix[i,screenSize-j-1]=tuple((s3backgroundColor*s3backgroundAmbient*255).astype(int))
                    
                    
    elif input=="4":
        camera=PerspectiveCamera(s4perscamCenter, s4perscamDirection, s4perscamUp, s4perscamAngle)

        lights=[]
        lights.append(DirectionalLight(s4lightColor, s4lightDirection))

        material=[]
        material.append(PhongMaterial(s4PhongMatDiffuse0, s4PhongMatReflective0, s4PhongMatTransparent0, s4PhongMatIndex0, s4PhongMatSpecular0, s4PhongMatExponent0))
        material.append(PhongMaterial(s4PhongMatDiffuse1, s4PhongMatReflective1, s4PhongMatTransparent1, s4PhongMatIndex1, s4PhongMatSpecular1, s4PhongMatExponent1))
        material.append(PhongMaterial(s4PhongMatDiffuse2, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))

        group=Group()
        group.adding(Sphere(s4SphereRadius0, s4SphereCenter0, material[s4SphereMaterial0]))
        group.adding(Sphere(s4SphereRadius1, s4SphereCenter1, material[s4SphereMaterial1]))
        group.adding(Plane(s4PlaneNormal, s4PlaneOffset, material[s4PlaneMaterial]))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                color=ray_trace(ray, hit, tmin, lights, group.objects, 3, s4backgroundAmbient)
                if color.all!=0:
                    pix[i,screenSize-j-1]=tuple(((color)*255).astype(int))
                else:
                    pix[i,screenSize-j-1]=tuple((s4backgroundColor*s4backgroundAmbient*255).astype(int))


    elif input=="5":
        camera=PerspectiveCamera(s5perscamCenter, s5perscamDirection, s5perscamUp, s5perscamAngle)

        lights=[]
        lights.append(DirectionalLight(s5lightColor1, s5lightDirection1))
        lights.append(DirectionalLight(s5lightColor2, s5lightDirection2))

        material=[]
        material.append(PhongMaterial(s5PhongMatDiffuse1, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s5PhongMatDiffuse2, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s5PhongMatDiffuse3, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s5PhongMatDiffuse4, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s5PhongMatDiffuse5, s5PhongMatReflective5, s5PhongMatTransparent5, s5PhongMatIndex5, s5PhongMatSpecular5, s5PhongMatExponent5))

        transformation1=Transformation(Sphere(s5transSphereRadius1, s5transSphereCenter1, material[s5transSphereMaterial1]))
        transformation1.scale(s5transScale1)
        transformation1.translate(s5transTranslate1)
        transformation2=Transformation(Sphere(s5transSphereRadius2, s5transSphereCenter2, material[s5transSphereMaterial2]))
        transformation2.translate(s5transTranslate2)
        transformation2.scale(s5transScale2)
        transformation3=Transformation(Sphere(s5transSphereRadius3, s5transSphereCenter3, material[s5transSphereMaterial3]))
        transformation3.translate(s5transTranslate3)
        transformation3.scale(s5transScale3)
        group=Group()
        group.adding(Plane(s5PlaneNormal, s5PlaneOffset, material[s5PlaneMaterial]))
        group.adding(transformation1)
        group.adding(transformation2)
        group.adding(transformation3)
        group.adding(Sphere(s5SphereRadius, s5SphereCenter, material[s5SphereMaterial]))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                color=ray_trace(ray, hit, tmin, lights, group.objects, 3, s5backgroundAmbient)
                if color.all!=0:
                    pix[i,screenSize-j-1]=tuple(((color)*255).astype(int))
                else:
                    pix[i,screenSize-j-1]=tuple((s5backgroundColor*s5backgroundAmbient*255).astype(int))

    elif input=="6":
        camera=PerspectiveCamera(s6perscamCenter, s6perscamDirection, s6perscamUp, s6perscamAngle)

        lights=[]
        lights.append(DirectionalLight(s6lightColor1, s6lightDirection1))
        lights.append(DirectionalLight(s6lightColor2, s6lightDirection2))

        material=[]
        material.append(PhongMaterial(s6PhongMatDiffuse1, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s6PhongMatDiffuse2, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s6PhongMatDiffuse3, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s6PhongMatDiffuse4, numpy.array([]), numpy.array([]), 0, numpy.array([]), 0))
        material.append(PhongMaterial(s6PhongMatDiffuse5, s6PhongMatReflective5, s6PhongMatTransparent5, s6PhongMatIndex5, s6PhongMatSpecular5, s6PhongMatExponent5))

        transformation1=Transformation(Sphere(s6transSphereRadius1, s6transSphereCenter1, material[s6transSphereMaterial1]))
        transformation1.scale(s6transScale1)
        transformation1.translate(s6transTranslate1)
        transformation2=Transformation(Sphere(s6transSphereRadius2, s6transSphereCenter2, material[s6transSphereMaterial2]))
        transformation2.translate(s6transTranslate2)
        transformation2.scale(s6transScale2)
        transformation3=Transformation(Sphere(s6transSphereRadius3, s6transSphereCenter3, material[s6transSphereMaterial3]))
        transformation3.translate(s6transTranslate3)
        transformation3.scale(s6transScale3)
        group=Group()
        group.adding(Plane(s6PlaneNormal, s6PlaneOffset, material[s6PlaneMaterial]))
        group.adding(transformation1)
        group.adding(transformation2)
        group.adding(transformation3)
        group.adding(Sphere(s6SphereRadius, s6SphereCenter, material[s6SphereMaterial]))

        for i in range(screenSize):
            for  j in range(screenSize):
                ray=camera.generateRay(i,j)
                color=ray_trace(ray, hit, tmin, lights, group.objects, 3, s6backgroundAmbient)
                if color.all!=0:
                    pix[i,screenSize-j-1]=tuple(((color)*255).astype(int))
                else:
                    pix[i,screenSize-j-1]=tuple((s6backgroundColor*s6backgroundAmbient*255).astype(int))

                    
    img.show()

