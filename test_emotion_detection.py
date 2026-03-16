import unittest
from EmotionDetection import emotion_detector


class TestEmotion(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertTrue("joy" in result)

    def test_sad(self):
        result = emotion_detector("I am sad")
        self.assertTrue("sadness" in result)


if __name__ == "__main__":
    unittest.main()