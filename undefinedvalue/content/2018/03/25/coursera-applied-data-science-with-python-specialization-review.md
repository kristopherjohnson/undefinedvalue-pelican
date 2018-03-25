Title: Review: Coursera's "Applied Data Science with Python" Specialization
Slug: coursera-applied-data-science-with-python-specialization-review
Date: 2018-03-25 12:58:42.518611
Category: Blog
Tags: datascience, machinelearning, coursera, mooc

I recently completed Coursera's [Applied Data Science with Python][specialization] specialization, and received the [accompanying certificate][certificate]. This is a review of my experience with the online courses.

This specialization is a series of five courses, each of which focuses on some aspect of using Python for data-science applications.  Each course is focused on use of one or more free Python libraries. The courses and the libraries covered by each are

1. Introduction to Data Science in Python: [NumPy][numpy], [SciPy][scipy], and [Pandas][pandas]
2. Applied Plotting, Charting, & Data Representation in Python: [Matplotlib][matplotlib]
3. Applied Machine Learning in Python: [scikit-learn][sklearn]
4. Applied Text Mining in Python: [NLTK][nltk] and [Gensim][gensim]
5. Applied Social Network Analysis in Python: [NetworkX][networkx]

The courses build on one another. For example, all the courses after the first assume that you are proficient with NumPy and Pandas, and all courses after the second assume you are proficient at creating plots with Matplotlib, and the last two courses assume you know how to train a machine-learning model.  So you should take the courses consecutively in the specified order, although you could take the last two at the same time.

This is an intermediate-level specialization, and it is assumed you already know how to write programs in Python.  It also assumes some elementary knowledge of statistics and discrete mathematics, but nothing too advanced.  I had previously taken Andrew Ng's [Machine Learning][machinelearning] course, so I already had some familiarity with the terminology and the math.  I just needed to do a little googling once in a while to refresh my memory or get an introduction to unfamiliar concepts.

As hinted at by the word "Applied" in the specialization and course titles, there is not much theory presented in these courses.  There is just enough theory to understand the exercises.  I took the specialization concurrently with Andrew Ng's [deeplearning.ai][deeplearning] specialization, so I got a nice dose of neural-network theory mixed in with my data science, but people who want to understand the algorithms in detail will need further study.

The programming assignments are both good and terrible.  They are good in that I feel like I got a solid introduction to what libraries are available and how to use them, with enough challenge to make me dig into the documentation and Stack Overflow a lot, but they were not so difficult that I didn't know what to do.  They are terrible in that the exercises are automatically graded, and the auto-grader has a lot of problems.  Assignments that should take an hour or two instead take two or three times that due to the auto-grader rejecting correct answers with a "wrong" data type, or "wrong" number of significant figures, or expecting a different result than what the assignment's instructions specify.  After doing each assignment, one has to spend an hour reading the course forums to find out the tricks to getting correct work accepted.  If these were brand-new courses, I could excuse the auto-grader imperfections, but these courses have all been run multiple times, so it's very frustrating that the bugs haven't been worked out and the teaching assistants don't understand the issues.

Most of the courses include some lectures or assignments dealing with the ethics of data science.  I was glad to see that.  We all need to be thinking about the consequences of these technologies.

I found the courses in this specialization useful.  It was nice to find a set of courses in Python; I've abandoned a few other courses that use [R][rproject] or [Octave][octave], because I found learning and writing code in those languages while also learning new concepts to be too frustrating.  I especially liked that the later courses used the tools and techniques introduced in earlier courses, and a few of the later assignments had the feel of doing real work.  More than once, I was amazed at how easy it was to do things that I would have said were impossible before I took the courses.

I think the complete specialization is roughly equivalent to a one-semester college course.  I know I don't know enough to call myself a competent data-science practitioner, but I do feel like I would at least know where to start looking if faced with a data-science task.

[specialization]: https://www.coursera.org/specializations/data-science-python
[certificate]: https://www.coursera.org/account/accomplishments/specialization/certificate/HFVQHV6Q3B4B
[numpy]: http://www.numpy.org
[scipy]: https://www.scipy.org
[pandas]: https://pandas.pydata.org
[matplotlib]: https://matplotlib.org
[sklearn]: http://scikit-learn.org/
[nltk]: https://www.nltk.org
[gensim]: https://radimrehurek.com/gensim/
[networkx]: https://networkx.github.io
[machinelearning]: https://www.coursera.org/learn/machine-learning
[deeplearning]: https://www.deeplearning.ai
[rproject]: https://www.r-project.org
[octave]: https://www.gnu.org/software/octave/

