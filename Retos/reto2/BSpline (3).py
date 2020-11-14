from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL as vis
import numpy as np

# Create a BSpline surface instance
surf = BSpline.Surface()

surf.delta = 0.01

surf.degree_u = 3
surf.degree_v = 3

# Puntos del jarron
z = [
    0.1988,0.18526,0.35347,
    0.21423,0.003247,0.002165,
    0.4252,0.63618,2.0627,
    0.52168,0.68988,1.0994,
    3.1588,5.1613,7.163,
    2.7907,5.171,7.2384,
    8.8926,9.0838,10.081,
    8.6903,8.9817,10.392,
    11.254,12.245,12.251,
    11.734,12.265,12.258
]

y = [
    2.1815,2.1736,1.4535,
    2.6212,2.6253,1.7502,
    2.6171,2.613,3.7783,
    2.1894,2.1974,2.5691,
    4.4202,4.4135,4.3967,
    3.9925,4.1688,4.0651,
    2.1953,1.621,1.805,
    1.9034,1.3175,1.4575,
    2.524,3.2296,3.0753,
    2.4197,2.7665,2.9209
]


cp_o = [
    [-1.9611,-0.099176,10.616],[-1.4244,-0.098825,10.591],[-0.88771,-0.098474,10.565],
    [-4.2049,-0.099243,10.765],[-3.0346,-0.099877,10.667],[-2.4679,-0.099526,10.641],
    [-4.4799,-0.08618,9.1687],[-4.4646,-0.092291,9.8178],[-4.3808,-0.095872,10.313],
    [-4.3992,-0.064652,6.9192],[-4.5106,-0.073958,7.8705],[-4.5551,-0.080947,8.7061],
    [-3.6382,-0.039965,4.776],[-3.8563,-0.048463,5.5496],[-4.4061,-0.056926,6.3034]
]

n = int(len(cp_o)/2)

control_points = [[0,0,0]] * n

for i in range(len(y)):
    ang = np.linspace(0,2*np.pi,n)
    for th in ang:
        control_points.append([y[i]*np.cos(th),y[i]*np.sin(th),z[i]])

for c in cp_o:
    control_points.append(c)

t = int(len(control_points)/n)

surf.set_ctrlpts(control_points,t,n)

surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, t)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, n)

surf.evaluate()

# Visualization config
vis_config = vis.VisConfig(figure_size=[30,15])
# Visualization component
vis_comp = vis.VisSurface(vis_config)
# Set visualization component of the surface
surf.vis = vis_comp
# Render the surface
surf.render()