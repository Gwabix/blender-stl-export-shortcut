bl_info = {
    "name": "Export Selection to STL Shortcut",
    "author": "Gwabix",
    "version": (1, 2),
    "blender": (4, 50, 0),
    "location": "File > Export > STL (or shortcut)",
    "description": "Export selected objects to STL with keyboard shortcut",
    "category": "Import-Export",
}

import bpy
import os

class EXPORT_OT_stl_shortcut(bpy.types.Operator):
    """Export selected objects to STL"""
    bl_idname = "export_scene.stl_shortcut"
    bl_label = "Export Selection to STL"
    bl_options = {'REGISTER'}

    def get_vertex_count(self, obj):
        """Retourne le nombre de vertices d'un objet mesh"""
        if obj.type == 'MESH':
            # Utiliser evaluated pour obtenir le mesh après modificateurs
            depsgraph = bpy.context.evaluated_depsgraph_get()
            obj_eval = obj.evaluated_get(depsgraph)
            return len(obj_eval.data.vertices)
        return 0

    def get_main_object(self, objects):
        """Trouve l'objet avec le plus de vertices"""
        max_vertices = 0
        main_obj = objects[0]
        
        for obj in objects:
            vertex_count = self.get_vertex_count(obj)
            if vertex_count > max_vertices:
                max_vertices = vertex_count
                main_obj = obj
        
        return main_obj

    def execute(self, context):
        # Vérifier qu'il y a une sélection
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        # Définir le nom par défaut selon le nombre d'objets sélectionnés
        if len(context.selected_objects) == 1:
            # Un seul objet sélectionné
            obj_name = bpy.path.clean_name(context.selected_objects[0].name)
            
            # Si fichier sauvegardé : [nom fichier] - [nom objet]
            # Sinon : [nom objet]
            if bpy.data.filepath:
                blend_filename = os.path.splitext(bpy.path.basename(bpy.data.filepath))[0]
                default_name = f"{blend_filename} - {obj_name}"
            else:
                default_name = obj_name
        else:
            # Plusieurs objets : trouver celui avec le plus de vertices
            main_obj = self.get_main_object(context.selected_objects)
            obj_name = bpy.path.clean_name(main_obj.name)
            
            # Si fichier sauvegardé : [nom fichier] - [nom objet principal]
            # Sinon : [nom objet principal]
            if bpy.data.filepath:
                blend_filename = os.path.splitext(bpy.path.basename(bpy.data.filepath))[0]
                default_name = f"{blend_filename} - {obj_name}"
            else:
                default_name = obj_name
            
            # Afficher une info sur l'objet principal choisi
            vertex_count = self.get_vertex_count(main_obj)
            self.report({'INFO'}, 
                f"Main object: '{main_obj.name}' ({vertex_count} vertices)")
        
        # Définir le chemin par défaut
        if bpy.data.filepath:
            blend_dir = os.path.dirname(bpy.data.filepath)
        else:
            blend_dir = os.path.expanduser("~")
        
        default_filepath = os.path.join(blend_dir, default_name + ".stl")
        
        # Appeler l'opérateur d'export STL avec les options
        bpy.ops.wm.stl_export(
            'INVOKE_DEFAULT',
            filepath=default_filepath,
            export_selected_objects=True
        )
        
        return {'FINISHED'}

# Enregistrement du raccourci clavier
addon_keymaps = []

def register():
    bpy.utils.register_class(EXPORT_OT_stl_shortcut)
    
    # Ajouter le raccourci clavier
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(
            EXPORT_OT_stl_shortcut.bl_idname,
            type='E',
            value='PRESS',
            ctrl=True,
            shift=True
        )
        addon_keymaps.append((km, kmi))

def unregister():
    # Retirer le raccourci clavier
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(EXPORT_OT_stl_shortcut)

if __name__ == "__main__":
    register()

