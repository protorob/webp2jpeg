# webp2jpeg: A simple script to convert all *.webp images in a directory to *.jpg

## Installation:

- Create a virtual environment

```
$ python.exe -m venv venv
```

- Mount the virtual environment

```
$ .\venv\Scripts\Activate.ps1
```

- Install requirements.txt

```
$ pip install -r requirements.txt
```

- Replace the path in line 5 of webp2jpeg.py to the folder containing your webp images
- Run the script

```
$ python.exe webp2jpeg.py
```

- Enjoy.

## To-Do

- Add the path as an argument or add a flag to run on the current directory
- Add an argument for removing the original webp image after conversion
