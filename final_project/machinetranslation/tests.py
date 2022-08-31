import unittest
import translator

class TestTranslate( unittest.TestCase):
    def testEnglishToFrench( self):
        self.assertIsNotNone( translator.englishToFrench( ''))
        self.assertEqual( translator.englishToFrench("Hello"),  "Bonjour")

    def testFrenchToEnglish( self):
        self.assertIsNotNone( translator.frenchToEnglish( ''))
        self.assertEqual( translator.frenchToEnglish("Bonjour"),"Hello")

unittest.main()