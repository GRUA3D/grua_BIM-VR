import unreal
import pandas as pd

#Seleccionar Actores en Nivel
EAS = unreal.EditorActorSubsystem()
actors = EAS.get_all_level_actors()

actorsStaticMesh = []

for num in actors:
    # if num.actor_has_tag("IsElement") == 'Truer'
    
#    print (num.get_class().get_name()) 
#    print (num.get_actor_label()) 
#    print (num.actor_has_tag("IsElement"))

   if num.actor_has_tag("IsElement") == True:
        actorsStaticMesh.append(num)
        # print (num.get_actor_label())


# Reasignar la etiqueta a todos los elementor de revit     

for tagActor in actorsStaticMesh:
        a = tagActor.tags
        IDRevit = "Revit.Element.UniqueId."
        for i in a:
         if str(i)[0:23] == IDRevit:
            tagID = str(i)[23:]
            print (tagID)
        tagActor.set_editor_property('tags',{tagID})
