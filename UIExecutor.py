import eel
import directory_singler
import renamer
import effects

eel.init('pages')

@eel.expose
def applyEffects(input_folder_path,output_folder_path,effects_input):
    effects.applyEffects(input_folder_path,output_folder_path,effects_input)
    eel.completed()

@eel.expose
def renaming(path,no_space,prefix,suffix):
    renamer.renaming(path,no_space,prefix,suffix)
    eel.completed()

@eel.expose
def singler(input_folder,output_folder,moveOrCopy,folder_suffix):
    directory_singler.singler(input_folder,output_folder,moveOrCopy,folder_suffix)
    eel.completed()

eel.start('home.html',size=(800,900))
eel.close()