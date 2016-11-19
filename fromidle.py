Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
python
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> import turtle
>>> t=turtle
>>> turtle.pen()
{'pencolor': 'black', 'pendown': True, 'pensize': 1, 'shearfactor': 0.0, 'fillcolor': 'black', 'resizemode': 'noresize', 'speed': 3, 'shown': True, 'stretchfactor': (1.0, 1.0), 'outline': 1, 'tilt': 0.0}
>>> turtle.color()
('black', 'black')
>>> turtle.color(green)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    turtle.color(green)
NameError: name 'green' is not defined
>>> turtle.stamp()
5
>>> fillcolor()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fillcolor()
NameError: name 'fillcolor' is not defined
>>> turtle.fillcolot()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    turtle.fillcolot()
AttributeError: 'module' object has no attribute 'fillcolot'
>>> turtle.fillcolor()
'black'
>>> t.forward(5)
>>> turtle.stamp()
6
>>> t.forward(5)
>>> turtle.stamp()
7
>>> t.forward(5)
>>> t.forward(20)
>>> t.forward(40)
>>> File "<pyshell#0>", line 1, in <module>
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> t.forward(5)6
SyntaxError: invalid syntax
t.forward(5)6
>>> 
>>> 
