bl_info = {
    "name": "Export Selection to STL Shortcut",
    "author": "Votre nom",
    "version": (1, 1),
    "blender": (2, 80, 0),
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

    def execute(self, context):
        # Vérifier qu'il y a une sélection
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        # Définir le nom par défaut
        default_name = "export"
        
        # Si un seul objet sélectionné, utiliser son nom
        if len(context.selected_objects) == 1:
            default_name = bpy.path.clean_name(context.selected_objects[0].name)
        # Si plusieurs objets ET fichier .blend sauvegardé, utiliser le nom du fichier
        elif len(context.selected_objects) > 1 and bpy.data.filepath:
            blend_filename = bpy.path.basename(bpy.data.filepath)
            # Retirer l'extension .blend
            default_name = os.path.splitext(blend_filename)[0]
        
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