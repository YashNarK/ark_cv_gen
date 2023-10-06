#adding the root directory to sys path
import os, sys
current_path = os.path.normpath(os.getcwd())
root_path = os.path.join(current_path.split(os.sep + 'ark_cv_gen')[0], 'ark_cv_gen')
sys.path.append(root_path)