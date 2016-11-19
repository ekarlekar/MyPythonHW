Last login: Sun Aug 21 11:01:11 on ttys000
Eshas-Air:~ eshak$ python
Python 2.7.12 |Anaconda 4.1.1 (x86_64)| (default, Jul  2 2016, 17:43:17) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> input numpy
  File "<stdin>", line 1
    input numpy
              ^
SyntaxError: invalid syntax
>>> 8 * 3.57
28.56
>>> 10*365
3650
>>> 20 + 3650
3670
>>> 3*52
156
>>> 3670-156
3514
>>> 100/20
5
>>> 5+30*20
605
>>> (5+30)*20
700
>>> ((5+30)*20)/10
70
>>> 5+30*20/10
65
>>> fred=100
>>> print(fred)
100
>>> fred=200
>>> print(fred)
200
>>> fred=200
>>> john=fred
>>> print(john)
200
>>> number_of_coins=200
>>> print(number_of_coins)
200
>>> 20+10*365
3670
>>> 3852
3852
>>> 3*52
156
>>> 3670-156
3514
>>> 20=10*356-3*52
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> 20+10*365-3*52
3514
>>> found_coins+20
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'found_coins' is not defined
>>> foun_coins=20
>>> found_coins+20
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'found_coins' is not defined
>>> found_coins=20
>>> magic_coins=10
>>> stolen_coins+3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'stolen_coins' is not defined
>>> stolen_coins=3
>>> found_coins+magic_coins *365-stolen_coins*52
3514
>>> stolen_coins=2
>>> found_coins+magic_coins *365-stolen_coins*52
3566
>>> magic_coins=13
>>> found_coins+magic_coins *365-stolen_coins*52
4661
>>> fred="Why do gorillas have big nostrils? Big fingers!!"
>>> print(fred)
Why do gorillas have big nostrils? Big fingers!!
>>> fred= 'What is pink and fluffy? Pink fluff!!'
>>> print(fred)
What is pink and fluffy? Pink fluff!!
>>> fred= "How do dinosaurs pay their bills?
  File "<stdin>", line 1
    fred= "How do dinosaurs pay their bills?
                                           ^
SyntaxError: EOL while scanning string literal
>>> fred= '''How do dinosaurs pay their bills?
... With tyrannosaurus checks!'''
>>> print(fred)
How do dinosaurs pay their bills?
With tyrannosaurus checks!
>>> silly_string='He said, "Aren't can't shouldn't wouldn't."'
  File "<stdin>", line 1
    silly_string='He said, "Aren't can't shouldn't wouldn't."'
                                 ^
SyntaxError: invalid syntax
>>> silly_string="He said, "Aren't can't shouldn't wouldn't.""
  File "<stdin>", line 1
    silly_string="He said, "Aren't can't shouldn't wouldn't.""
                               ^
SyntaxError: invalid syntax
>>> silly_string='''He said, "Aren't can't shouldn't wouldn't"'''
>>> silly_string
'He said, "Aren\'t can\'t shouldn\'t wouldn\'t"'
>>> single_quote_str='He said, "Aren\'t can\'t shouldn\'t wouldn\'t.'
>>> print(single_quote_str)
He said, "Aren't can't shouldn't wouldn't.
>>> single_quote_str='He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
>>> print(single_quote_str)
He said, "Aren't can't shouldn't wouldn't."
>>> double_quote_str="He said, "Aren\'t can\'t shouldn\'t wouldn\'t.""
  File "<stdin>", line 1
    double_quote_str="He said, "Aren\'t can\'t shouldn\'t wouldn\'t.""
                                   ^
SyntaxError: invalid syntax
>>> double_quote_str="He said, \"Aren't can't shouldn't wouldn't.\""
>>> double_quote_str
'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
>>> myscore=1000
>>> message= 'I scored %s points
  File "<stdin>", line 1
    message= 'I scored %s points
                               ^
SyntaxError: EOL while scanning string literal
>>> print (message % myscore)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'message' is not defined
>>> myscore=1000
>>> message= 'I scored %s points'
>>> print (message % myscore)
I scored 1000 points
>>> joke_text='%s: a device for findin furniture in the dark'
>>> bodypart1='Knee'
>>> bodypart2='Shin'
>>> print(joke_text % bodypart1)
Knee: a device for findin furniture in the dark
>>> joke_text='%s: a device for finding furniture in the dark'
>>> print(joke_text % bodypart1)
Knee: a device for finding furniture in the dark
>>> print(joke_text % bodypart2)
Shin: a device for finding furniture in the dark
>>> nums='What did the number %s say to the number %s? Nice belt!!'
>>> print(nums % (0,8))
What did the number 0 say to the number 8? Nice belt!!
>>> print(10*a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> print(10*'a')
aaaaaaaaaa
>>> print(1000*'snirt')
snirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirtsnirt
>>> wizard_list='spider legs, toe of forg, eye of newt, bat wing, slug butter, snake dandruff'
>>> print(wizard_list)
spider legs, toe of forg, eye of newt, bat wing, slug butter, snake dandruff
>>> wizard_list='spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
>>> print(wizard_list)
spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff
>>> wizard_list=['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
>>> print(wizard_list)
['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
>>> print(wizard_list[2])
eye of newt
>>> wizard_list[2]=snail tongue
  File "<stdin>", line 1
    wizard_list[2]=snail tongue
                              ^
SyntaxError: invalid syntax
>>> wizard_list[2]='snail tongue'
>>> print(wizard_list[2:5])
['snail tongue', 'bat wing', 'slug butter']
>>> some_number=[1,2,5,10,20]
>>> some_strings=['Which','Witch','Is', 'Which']
>>> numbers_and_strings= ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
>>> print(number_and_strings)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number_and_strings' is not defined
>>> print(numbers_and_strings)
['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
>>> 
>>> numbers=[1,2,3,4]
>>> strings=['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
>>> mylist=[number,strings]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number' is not defined
>>> mylist=[numbers,strings]
>>> print(mylist)
[[1, 2, 3, 4], ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']]
>>> wizard_list.append('bear burp')
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff', 'bear burp']
>>> wizard_list.append('mandrake')
>>> wizard_list.append('hemlock')
>>> wizard_list.append('swamp gas')
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'snake dandruff', 'bear burp', 'mandrake', 'hemlock', 'swamp gas']
>>> del wizard_list[5]
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp', 'mandrake', 'hemlock', 'swamp gas']
>>> del wizard_list[8]
>>> del wizard_list[7]
>>> del wizard_list[6]
>>> print(wizard_list)
['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
>>> list1=[1,2,3,4]
>>> list2=['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> print( list1+list2
... )
[1, 2, 3, 4, 'I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> list1=[1,2,3,4]
>>> list2=['I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
>>> list3=list1+list2
>>> list3
[1, 2, 3, 4, 'I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
>>> list1=[1,2]
>>> print(list1*5)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> list1/20
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> list1-20
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> list1+50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list
>>> fibs=(1,1,2,3)
>>> print(fibs[3])
3
>>> fibs=(0,1,1,2,3)
>>> print(fibs[3])
2
>>> fibs[0]=4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> favorite_sports=['Ralph Williams, Football', 'Michael Tippett, Basketball','Edward Elgar, Baseball', 'Rebecca Clarke, Netball', 'Ethel Smyth, Badminton', 'Frank Bridge, Rugby']
>>> favorite_sports=['Ralph Williams, Football', 'Michael Tippett, Basketball','Edward Elgar, Baseball', 'Rebecca Clarke, Netball', 'Ethel Smyth, Badminton', 'Frank Bridge, Rugby']
>>> favorite_sports={'Ralph Williams':' Football', 'Michael Tippett': 'Basketball','Edward Elgar':' Baseball', 'Rebecca Clarke': 'Netball', 'Ethel Smyth': 'Badminton', 'Frank Bridge': 'Rugby'}
>>> print(favorite_sports['Rebecca Clarke'])
Netball
>>> del favorie_sports['Ethel Smyth']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'favorie_sports' is not defined
>>> del favorite_sports['Ethel Smyth']
>>> print(favorite_sports)
{'Rebecca Clarke': 'Netball', 'Michael Tippett': 'Basketball', 'Ralph Williams': ' Football', 'Edward Elgar': ' Baseball', 'Frank Bridge': 'Rugby'}
>>> favorite_sports[Ralph Williams']='Ice Hockey'
  File "<stdin>", line 1
    favorite_sports[Ralph Williams']='Ice Hockey'
                                 ^
SyntaxError: invalid syntax
>>> favorite_sports['Ralph Williams']='Ice Hockey'
>>> print(favorite_sports)
{'Rebecca Clarke': 'Netball', 'Michael Tippett': 'Basketball', 'Ralph Williams': 'Ice Hockey', 'Edward Elgar': ' Baseball', 'Frank Bridge': 'Rugby'}
>>> favorite_colors={'Malcolm Warner':'Pink polka dots','James Baxter':'Orange Stripes', 'Sue Lee':'Purple Paisley'}
>>> favorite_sports+favorite_colors
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(#1: Favorites)
... )
()
>>> print('#1: Favorites')
#1: Favorites
>>> games=['reading', 'drawing', 'singing', 'dancing','playing music', 'writing', 'programming']
>>> games
['reading', 'drawing', 'singing', 'dancing', 'playing music', 'writing', 'programming']
>>> foods=['pizza', 'pau bhaji', 'chinese food', 'tacos', 'paninis','lasagna','mashed potatoes']
>>> print(games+foods)
['reading', 'drawing', 'singing', 'dancing', 'playing music', 'writing', 'programming', 'pizza', 'pau bhaji', 'chinese food', 'tacos', 'paninis', 'lasagna', 'mashed potatoes']
>>> games+foods=favorites
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> favorites=games+foods
>>> print(favorites)
['reading', 'drawing', 'singing', 'dancing', 'playing music', 'writing', 'programming', 'pizza', 'pau bhaji', 'chinese food', 'tacos', 'paninis', 'lasagna', 'mashed potatoes']
>>> 
>>> 
>>> 
>>> 
>>> print('#2:Counting Combatants')
#2:Counting Combatants
>>> 25*3+2*40
155
>>> 
>>> 
>>> 
>>> 
>>> print('#3:Greetings!')
#3:Greetings!
>>> first_name='Esha'
>>> last_name='Karlekar'
>>> print('Hi there, first_name last_name')
Hi there, first_name last_name
>>> print('Hi there, %s %s)
  File "<stdin>", line 1
    print('Hi there, %s %s)
                          ^
SyntaxError: EOL while scanning string literal
>>> print('Hi there, %s %s')
Hi there, %s %s
>>> message= 'Hi there, %s %s')
  File "<stdin>", line 1
    message= 'Hi there, %s %s')
                              ^
SyntaxError: invalid syntax
>>> message= 'Hi there, %s %s'
>>> print(% message first_name last_name)
  File "<stdin>", line 1
    print(% message first_name last_name)
          ^
SyntaxError: invalid syntax
>>> print( message first_name last_name)
  File "<stdin>", line 1
    print( message first_name last_name)
                            ^
SyntaxError: invalid syntax
>>> print( message % first_name % last_name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string
>>> message= 'Hi there, %s!'
>>> print(message %first_name+last_name)
Hi there, Esha!Karlekar
>>> last_name=' Karlekar'
>>> message= 'Hi there, %s'
>>> print(message %first_name+last_name)
Hi there, Esha Karlekar
>>> 
