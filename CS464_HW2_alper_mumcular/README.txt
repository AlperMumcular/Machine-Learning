1- Open Anaconda Prompt
2- type cd "Path-of-folder"  --- For example in my computer it was: cd C:\Users\ALPER\Untitled Folder
3- type conda env create -f environment.yml

	If it says prefix already exists then
	4- type conda remove -n cs464_hw2 --all
	5- Proceed --> type "y"
	6- type conda env create -f environment.yml

7- Please wait for the environment to be created
8- type conda activate cs464_hw2
9- type jupyter notebook (Opens Jupyter Notebook on the browser)
10- Open "q1main.ipynb"
11- In the second cell, please update "your_path" variable, it should be the path of the cat folder
12- Click on kernel --> Choose Restart & Run All --> click the red button
13- Wait until the execution of the code is terminated 
14- Once you are done with grading, you can open "q1delete.ipynb"
15- Run q1delete.ipynb to delete created images.

I hope these will help you and you won't encounter with any problems :)