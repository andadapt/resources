[drag=100, drop=center, flow=col true]


### Starter

On your MWB write the output for the following code:

```basic 
TextWindow.WriteLine("hello, world!")
TextWindow.Write("Basic is ")
TextWindow.WriteLine("awesome")
TextWindow.WriteLine("!!!")
```

---

[drag=99, drop=center, flow=stack]
# Small Basic - Lesson 3 
## Input / Output

**ASPIRE to:**
apply the methods of input and output in a variety of scenarios

**CHALLENGE to:**
construct a program that allows the user to input and output data
---
[drag=99, drop=center, flow=col]
## Taking Input

So you now know how to display text on screen, but what about taking input from the user, you can do this will the following command.
```basic
TextWindow.Read()
```
This will create a flashing cursor so the user can type something in.

## Storing the Input
It is really important that when you use this command, you store what they type somewhere. To do this you use a variable. This is a name that will be used to refer to what they have entered, e.g.:

```basic
TextWindow.WriteLine(“Enter your name: “)
name = TextWindow.Read()
TextWindow.WriteLine(“Your name is “ + name)
```
---
[drag=100, drop=center, flow=col true]

[drag=50, drop=left, flow=col true]
## Task

Try to complete Task 2 - Shopping List.

Use the code that is given to get started and then continue creating the program so it works like the example shown.

**Done?**
Screenshot your code and add it to your programming diary

[drag=50,drop=right]
![](assets/img/slide11right.gif)


---
[drag=99, drop=center, flow=column]

[drag=50, drop=left, flow=column]
## Task

Try to complete Task 3 - Chat Bot


Use the code that is given to get started and then continue creating the program so it works like the example shown.

**Done? **
Screenshot your code and add it to your programming diary
[drag=50,drop=right]
![](assets/img/slide12right.gif)

---
[drag=100, drop=center, flow=stack]

## Extension

🌈🌈🌈🌈🌈🌈🌈🌈

Using:

```basic
TextWindow.BackgroundColor="red"
TextWindow.ForegroundColor="yellow"
```

Create some rainbow output!

black, darkBlue, darkGreen, darkCyan, darkRed, darkMagenta, darkYellow, gray, darkGray, blue, green, cyan, red, magenta, yellow, white


---
[drag=99, drop=center, flow=column]

## Plenary

**On your mini-whiteboards answer the following questions:**

What would the following program display if the user entered Pizza

```basic
TextWindow.WriteLine(“What is your favourite food?”)
food = TextWindow.Read()
TextWindow.WriteLine(“You said “ + food + “ is your fav”)
```

---

## Plenary

**On your mini-whiteboards answer the following questions:**

Why would this program not make sense?

```basic
age = TextWindow.Read()
TextWindow.WriteLine(“What is your age?”)
```
---
[drag=99, drop=center, flow=column]

## Plenary
**On your mini-whiteboards answer the following questions:**

What is wrong with this code? Rewrite it so that it would work
```basic
Text.WriteLine(“What day is it?)
TextWindow.Read()
TextWindow.Write”Today is “ + day)
```
