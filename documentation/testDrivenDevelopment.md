# Test-Driven Development (TDD)
Since we were talking about unit testing today, I thought I would bring up the topic of Test-Driven Development (TDD).

### The basics of TDD are as follows:
- Write your unit test first
- Make sure that whatever it tests, fails (very important!)
- Write the minimal amount of code needed to make it pass
- Repeat

The general idea is that by writing your tests first (and making sure that they fail), you are giving yourself some guiderails when it comes to actually writing the code. You no long need to draft out the problem in your head, because you have a tangible goal-- making the unit test pass!

### Example
1 - First we write a test that describes a very basic use case.
`import unittest

class TestFreeFall(unittest.TestCase):

    def test_falling_distance(self):
        g = 9.81  # gravity (m/s^2)
        t = 2  # time in seconds
        expected_distance = 0.5 * g * t ** 2  # The correct answer we expect
        result = falling_distance(t)
        self.assertAlmostEqual(result, expected_distance, places=2)
`

2 - Next we run the test and make sure that it fails

3 - Then we write the least amount of code needed to make the test pass

`def falling_distance(t):
    g = 9.81  # gravity (m/s^2)
    return 0.5 * g * t ** 2
`

4 - Now we test it again to make sure that it passes.

There is a ton of literature on the topic (especially if you are interested in web development) but for now I'll just link these:
- [Simple Intro to TDD](https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/)
- [TDD in Python: A Beginner's Guide](https://www.datacamp.com/tutorial/test-driven-development-in-python)

If there's questions regarding how/why it works, feel free to comment or reach out to me directly.

![goat](https://github.com/user-attachments/assets/fe25a5e2-70e9-4b3b-80da-485c2e2f7433)

> Obey the [Goat](https://www.obeythetestinggoat.com/)
