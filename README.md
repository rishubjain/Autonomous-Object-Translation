# Autonomous-Object-Translation
Currently most object translation tasks within an image require tedious human input. I propose a system that attempts to perform this object translation task from a sentence describing the object and how it is manipulated. I explore and compare different models for this task.

**The final report can be found here: [autonomous-object-translation.pdf](autonomous-object-translation.pdf)**

[make_images.py](make_images.py), [unit_tests.py](unit_tests.py), [constants.py](constants.py) include the code for generating the dataset, and the train\*.ipynb notebooks include the code to create, train, and evaluate the different models (They all use the file [my_nn_lib.py](my_nn_lib.py) which was adapted from code found [here](https://gist.github.com/tomokishii/7ddde510edb1c4273438ba0663b26fc6#file-my_nn_lib-py)). [train808GAN.ipynb](train808GAN.ipynb) is still in development. 

