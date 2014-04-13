

class TaskModel(object):
    """
    @brief Small structure that describes tasks in human readable form before converting them to DBObjects to be inserted
    in to the dictionary.
    """
    def __init__(self, scaled_model_id=[], name=[], world=[], wrench = []):
        """
        @param scaled_model_id - The scaled model id of the target object in the database.
        @param name - The name of the target object. Mostly just for convenience.
        @param world - The relative URL of the world file for a scene with the planning object. This is
                       what will be loaded, so if the scaled_model_id is set incorrectly, it will not correspond
                       properly to the planned grasp when the grasp is stored in the database
        @param wrench - This is an applied wrench that the grasp metrics may use to calculate the fitness of a grasp
                        to produce or resist a particular force/wrench on the object.
    
         """
        self.scaled_model_id = scaled_model_id
        self.name = name
        self.world = world
        self.wrench = wrench



"""
Create a TaskModel for each model
"""
models = dict()
models['hammer'] = TaskModel(18548,'harvard_hammer','worlds/HammerWorld.xml',[0,0,3.5,0,-4.55,0])
models['drill'] = TaskModel(18547,'harvard_drill','worlds/DrillWorld2.xml',[0,0,24.52,.0,-2.25,0])
models['doorknob'] = TaskModel(18546,'harvard_doorknob','worlds/DoorknobWorld.xml',[0,0,3.45,-.25,0,0])
models['laptop'] = TaskModel(18545,'harvard_laptop','worlds/LaptopWorld.xml',[0,0,31.75,0,0,0])
models['beerbottle'] = TaskModel(18544,'harvard_beerbottle','worlds/BeerbottleWorld.xml',[0,0,9.05,0,-0.45,0])
models['sodabottle'] = TaskModel(18543,'harvard_sodabottle','worlds/TwoliterWorld.xml',[0,0,21.12,0,-1.57,0])
models['wrench'] = TaskModel(18542,'harvard_wrench','worlds/WrenchWorld.xml',[0,3.25,0,-3.25,0])
models['coffeemug'] = TaskModel(18541,'harvard_coffeemug','worlds/CoffeemugWorld.xml',[0,0,3.5,0,-4.55,0])
models['bowl'] = TaskModel(18540,'harvard_bowl','worlds/BowlWorld.xml',[0,0,3.45,0,0,0])
models['aerosol'] = TaskModel(18539,'harvard_aersol','worlds/AerosolcanWorld.xml',[0,0,3.55,0,0,0])

def model_set(keys):
    safe_keys = list(set(keys) & set(models.keys()))
    return dict((k, models[k]) for k in safe_keys)
       

small_keys = ['hammer','drill','aerosol','doorknob','laptop']
tiny_keys = ['drill','aerosol']
