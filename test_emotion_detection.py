from EmotionPredict.emotions_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotions"], "joy")
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotions"], "anger")
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotions"], "disgust")
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotions"], "sadness")
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotions"], "fear")

unittest.main()