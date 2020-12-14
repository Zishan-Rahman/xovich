# [*X*ovich](https://github.com/Zishan-Rahman/xovich)

"This is a fun little program I made to test my knowledge of programming," said [Kabilan Thesingarajah](https://github.com/KabilanThesingarajah/).
"I don't care about doing this in one line, I just want this as a GUI," said me, when I found his ovich repository.

So I set out to create a GUI version of his ovich program with some additional features. This is the result: *X*ovich!

## Features

- GUI made in tkinter brings Kabilan's ovich functionality outside of your command line inferface!
- Add "Ilya" as a middle name (between a first and last name)!
- You can have:
  - Only one name + "ovich"
  - A first name + A last name + "ovich" (at the end of the last name)
  - The same name twice + "ovich" at the last instance

## Scenario (originally by Kabilan, edited and added to by me)

Kabilan's best friend was cold-texted by a random number. This person was presumably a Chinese Lady, but with doubt, so they wanted to proxy their identity. They wanted to be Russian.
He then advised his best friend to change his name *very* slightly. Whereby his surname is his first name, with "ovich" concatenated to it.
This was a simple task, so to test their patience, and their Python programming skills, they initially endeavoured to do this in one line. They eventually managed to do it in one afternoon at a Starbucks, and, without knowing what anyone would do with it, [Kabilan released it as a gift to the so-called "interwebs" through a simple GitHub repository, consisting of only the ```ivanovichFinal.py``` file and a ```README.md``` file.](https://github.com/KabilanThesingarajah/ovich)

Three months later, his *other* best friend (aka [**me**](https://github.com/Zishan-Rahman)) came across his one-line program, and was impressed by the way Kabilan was able to do all of this in one line.
However, he felt that this was not enough. He wanted to spread this novetly further than his mate did. He wanted other people to revel at the massive stereotyping in display, without having to make the end user endure the command line. He *liked* and *enjoyed using* the command line, but, the thing is, **many** (*if not most*) **people don't**. So he decided to fork Kabilan's GitHub repo and create his own "*X*ovich" program that would run as a GUI with some extra features. He also edited the ```README.md``` file to reflect this, hence this gargantuan second paragraph (and a puny third paragraph (consisting of just three sentences)).
He also did this to practice some of the knowledge he had been tought in Computer Science at university recently. Namely, unit testing; the repository also includes a unit test file (```testing.py```) that may (or may not) also be built onto along with the main ```xovich.py``` file in the future. He still hasn't found a use for lambdas here, however. Oh, well, maybe somewhere else they could be implemented (by him)!
Following his mate's example, he (aka **moi**) decided to release the new and improved program on "da webbings" for anyone who sees this to use. Now, he thought, in retrospect, that this program shouldn't've been a fork of his original program, since it is so wildly different; in fact, he had no idea what to do with the original file, so he made the ```xovich.py``` file pretty much from scratch. However, he kept the original ```ivanovichFinal.py``` file from his original project for reference (he edited it quite a bit with comments, and moved the actual line to a function so it can be called in the future by any other program), and at least the ```README.md``` file in this repo has some similarities with the original one!

And, yes, I know, I was referring to myself in the third person! You don't need to point that out to me, I already know that! **I'm self-aware, please don't judge!**

## TODO

This is where I show y'all the roadmap of this program:

- I need to fix some of the if statements (in ```xovich.py```) and unit tests (in ```testing.py```) so that the program works better (and *more* properly).
- I may or may not want to add a LICENSE file in the future, ideally for a permissive license (i.e. MIT, Apache, BSD, Unlicense, CC0, Public Domain, zlib et cetera).
- I also want to add a "Story" button that displays the "Scenario" section of this README.md file in a messagebox *that also shows up before the program starts*.
- Once all of the above is done, I'll be ready to compile it for Windows and (maybe) other platforms too.
- I don't know what to do with the ```ivanovichFinal.py``` file yet...
