bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy


#Button 1

def button_01(context):

    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(1, 0, 2), scale=(1, 1, 1))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(1, 0, 1), scale=(1, 1, 1))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 1, 1), scale=(1, 1, 1))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(1, 1, 1), scale=(1, 1, 1))
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 1, 2), scale=(1, 1, 1))

    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_ssr_refraction = True
    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 0



class Add_Environment(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "nik.add_environment"
    bl_label = "Add Environment"


    def execute(self, context):
        button_01(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(Add_Environment.bl_idname, text=Add_Environment.bl_label)


#Button 2     

def button_02(context):
    bpy.ops.object.select_by_type(type='LIGHT')
    bpy.ops.object.delete(use_global=False)
    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 1





class Remove_Environment(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "nik.remove_environment"
    bl_label = "Remove Environment"


    def execute(self, context):
        button_02(context)
        return {'FINISHED'}

    # test call
    #bpy.ops.object.simple_operator()
  
    
#bpy.ops.object.select_by_type(type='LIGHT')
#bpy.ops.object.delete(use_global=False)
    
    
class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Add Quick Environment"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

       

        # button 01
       
        row = layout.row()
        row.scale_y = 2.0
        row.operator("nik.add_environment")

        # button 02
       
        row = layout.row()
        row.scale_y = 2.0
        row.operator("nik.remove_environment")
       


def register():
    
    bpy.utils.register_class(Add_Environment)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.utils.register_class(Remove_Environment)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(Add_Environment)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(Remove_Environment)


if __name__ == "__main__":
    register()
