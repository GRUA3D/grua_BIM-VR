import unreal
import pandas as pd

#Seleccionar Actores en Nivel
EAS = unreal.EditorActorSubsystem()
actors = EAS.get_all_level_actors()



#Agrupando Actores Clase 'StaticMeshActor'
actorsStaticMesh = []

for num in actors:
    if num.get_class().get_name() == 'StaticMeshActor':
        actorsStaticMesh.append(num)

# print (actorsStaticMesh[1])

# Reasignar la etiqueta a todos los elementor de revit 
def TagsID ():
    for tagActor in actorsStaticMesh:
        a = tagActor.tags
        IDRevit = "Revit.Element.UniqueId."

    for i in a:

        if str(i)[0:23] == IDRevit:
            tagID = str(i)[23:]
            print (tagID)
    tagActor.set_editor_property('tags',{tagID})

for MeshA in actorsStaticMesh:
    Component = MeshA.static_mesh_component
    StaticMesh = Component.static_mesh
    print (StaticMesh.get_name())



