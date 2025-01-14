import unreal
import pandas as pd

#Seleccionar Actores por library

EAL = unreal.EditorAssetLibrary()

actors = EAL.list_assets('/Game/Modelo_ARQ/MOB/MODELO_CASA3D_Mobiliario/Geometries/')
# actors = EAL.list_assets('/Game/00Prueba/')
staticMeshWalls = []

# Seleccionar Static Mesh de Walls
for num in actors:   
 
    pathnum = str(num.split('.')[0])
    findclases = EAL.find_asset_data(pathnum)
    nameMesh = findclases.get_asset().get_name().split('_')[0]

    if nameMesh == "Walls":
        staticMeshWalls.append(num)

    
#Agregar collision simple

for wall in staticMeshWalls:
    # Cargar Librerias de editor y type_shape
    ESML = unreal.EditorStaticMeshLibrary
    shape_type = unreal.ScriptingCollisionShapeType.NDOP10_Z
    
    pathwall = str(wall.split('.')[0])
    findwall = EAL.find_asset_data(pathwall)
    ESML.add_simple_collisions(findwall.get_asset(),shape_type)
    nameWall = findwall.get_class().get_name()
    
    # print(nameWall)
