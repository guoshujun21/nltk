# -*- coding: utf-8 -*-

"""
Mock test for Stanford CoreNLP wrappers.
"""

import sys
from itertools import chain
from unittest import TestCase, skipIf
from unittest.mock import patch

from nltk.tag.stanford import CoreNLPPOSTagger, CoreNLPNERTagger
from nltk.tokenize.stanford import CoreNLPTokenizer

@skipIf(sys.version_info[0] < 3, 'unittest.mock no supported in Python2')
class TestTokenizerAPI(TestCase):
    @patch('nltk.tokenize.stanford.CoreNLPTokenizer')
    def test_tokenize(self, MockTokenizer):
        corenlp_tokenizer = MockTokenizer()
        input_string = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks."
        corenlp_tokenizer.api_call.return_value = {
        u'sentences': [   {   u'index': 0,
                          u'tokens': [   {   u'after': u' ',
                                             u'before': u'',
                                             u'characterOffsetBegin': 0,
                                             u'characterOffsetEnd': 4,
                                             u'index': 1,
                                             u'originalText': u'Good',
                                             u'word': u'Good'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 5,
                                             u'characterOffsetEnd': 12,
                                             u'index': 2,
                                             u'originalText': u'muffins',
                                             u'word': u'muffins'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 13,
                                             u'characterOffsetEnd': 17,
                                             u'index': 3,
                                             u'originalText': u'cost',
                                             u'word': u'cost'},
                                         {   u'after': u'',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 18,
                                             u'characterOffsetEnd': 19,
                                             u'index': 4,
                                             u'originalText': u'$',
                                             u'word': u'$'},
                                         {   u'after': u'\n',
                                             u'before': u'',
                                             u'characterOffsetBegin': 19,
                                             u'characterOffsetEnd': 23,
                                             u'index': 5,
                                             u'originalText': u'3.88',
                                             u'word': u'3.88'},
                                         {   u'after': u' ',
                                             u'before': u'\n',
                                             u'characterOffsetBegin': 24,
                                             u'characterOffsetEnd': 26,
                                             u'index': 6,
                                             u'originalText': u'in',
                                             u'word': u'in'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 27,
                                             u'characterOffsetEnd': 30,
                                             u'index': 7,
                                             u'originalText': u'New',
                                             u'word': u'New'},
                                         {   u'after': u'',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 31,
                                             u'characterOffsetEnd': 35,
                                             u'index': 8,
                                             u'originalText': u'York',
                                             u'word': u'York'},
                                         {   u'after': u'  ',
                                             u'before': u'',
                                             u'characterOffsetBegin': 35,
                                             u'characterOffsetEnd': 36,
                                             u'index': 9,
                                             u'originalText': u'.',
                                             u'word': u'.'}]},
                      {   u'index': 1,
                          u'tokens': [   {   u'after': u' ',
                                             u'before': u'  ',
                                             u'characterOffsetBegin': 38,
                                             u'characterOffsetEnd': 44,
                                             u'index': 1,
                                             u'originalText': u'Please',
                                             u'word': u'Please'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 45,
                                             u'characterOffsetEnd': 48,
                                             u'index': 2,
                                             u'originalText': u'buy',
                                             u'word': u'buy'},
                                         {   u'after': u'\n',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 49,
                                             u'characterOffsetEnd': 51,
                                             u'index': 3,
                                             u'originalText': u'me',
                                             u'word': u'me'},
                                         {   u'after': u' ',
                                             u'before': u'\n',
                                             u'characterOffsetBegin': 52,
                                             u'characterOffsetEnd': 55,
                                             u'index': 4,
                                             u'originalText': u'two',
                                             u'word': u'two'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 56,
                                             u'characterOffsetEnd': 58,
                                             u'index': 5,
                                             u'originalText': u'of',
                                             u'word': u'of'},
                                         {   u'after': u'',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 59,
                                             u'characterOffsetEnd': 63,
                                             u'index': 6,
                                             u'originalText': u'them',
                                             u'word': u'them'},
                                         {   u'after': u'\n',
                                             u'before': u'',
                                             u'characterOffsetBegin': 63,
                                             u'characterOffsetEnd': 64,
                                             u'index': 7,
                                             u'originalText': u'.',
                                             u'word': u'.'}]},
                      {   u'index': 2,
                          u'tokens': [   {   u'after': u'',
                                             u'before': u'\n',
                                             u'characterOffsetBegin': 65,
                                             u'characterOffsetEnd': 71,
                                             u'index': 1,
                                             u'originalText': u'Thanks',
                                             u'word': u'Thanks'},
                                         {   u'after': u'',
                                             u'before': u'',
                                             u'characterOffsetBegin': 71,
                                             u'characterOffsetEnd': 72,
                                             u'index': 2,
                                             u'originalText': u'.',
                                             u'word': u'.'}]}]
                                             }
        # Should return the mocked json.
        api_call_output = corenlp_tokenizer.api_call(input_string)
        self.assertIsInstance(api_call_output, dict)
        # Emulates the tokenization process.
        # Note: We're not calling the corenlpt_tokenizer.tokenize() directly because
        #       it will not return the desired value but a MagicMock object.
        # >>> corenlp_tokenizer.tokenize(input_string)
        # >>> <MagicMock name='CoreNLPTokenizer().tokenize()' id='140308440963224'>
        print (corenlp_tokenizer.tokenize(input_string))
        tokenized_output = [token['originalText'] or token['word']
                            for sentence in api_call_output['sentences']
                            for token in sentence['tokens']]
        expected_output = [u'Good', u'muffins', u'cost', u'$', u'3.88', u'in',
                           u'New', u'York', u'.', u'Please', u'buy', u'me',
                           u'two', u'of', u'them', u'.', u'Thanks', u'.']
        self.assertEqual(expected_output, tokenized_output)


@skipIf(sys.version_info[0] < 3, 'unittest.mock no supported in Python2')
class TestTaggerAPI(TestCase):
    @patch('nltk.tag.stanford.CoreNLPTagger')
    def test_blog_posts(self, MockTagger):
        corenlp_tagger = MockTagger()
        input_tokens = 'What is the airspeed of an unladen swallow ?'.split()
        corenlp_tagger.api_call.return_value = {
        u'sentences': [   {   u'basicDependencies': [   {   u'dep': u'ROOT',
                                                        u'dependent': 1,
                                                        u'dependentGloss': u'What',
                                                        u'governor': 0,
                                                        u'governorGloss': u'ROOT'},
                                                    {   u'dep': u'cop',
                                                        u'dependent': 2,
                                                        u'dependentGloss': u'is',
                                                        u'governor': 1,
                                                        u'governorGloss': u'What'},
                                                    {   u'dep': u'det',
                                                        u'dependent': 3,
                                                        u'dependentGloss': u'the',
                                                        u'governor': 4,
                                                        u'governorGloss': u'airspeed'},
                                                    {   u'dep': u'nsubj',
                                                        u'dependent': 4,
                                                        u'dependentGloss': u'airspeed',
                                                        u'governor': 1,
                                                        u'governorGloss': u'What'},
                                                    {   u'dep': u'case',
                                                        u'dependent': 5,
                                                        u'dependentGloss': u'of',
                                                        u'governor': 8,
                                                        u'governorGloss': u'swallow'},
                                                    {   u'dep': u'det',
                                                        u'dependent': 6,
                                                        u'dependentGloss': u'an',
                                                        u'governor': 8,
                                                        u'governorGloss': u'swallow'},
                                                    {   u'dep': u'compound',
                                                        u'dependent': 7,
                                                        u'dependentGloss': u'unladen',
                                                        u'governor': 8,
                                                        u'governorGloss': u'swallow'},
                                                    {   u'dep': u'nmod',
                                                        u'dependent': 8,
                                                        u'dependentGloss': u'swallow',
                                                        u'governor': 4,
                                                        u'governorGloss': u'airspeed'},
                                                    {   u'dep': u'punct',
                                                        u'dependent': 9,
                                                        u'dependentGloss': u'?',
                                                        u'governor': 1,
                                                        u'governorGloss': u'What'}],
                          u'enhancedDependencies': [   {   u'dep': u'ROOT',
                                                           u'dependent': 1,
                                                           u'dependentGloss': u'What',
                                                           u'governor': 0,
                                                           u'governorGloss': u'ROOT'},
                                                       {   u'dep': u'cop',
                                                           u'dependent': 2,
                                                           u'dependentGloss': u'is',
                                                           u'governor': 1,
                                                           u'governorGloss': u'What'},
                                                       {   u'dep': u'det',
                                                           u'dependent': 3,
                                                           u'dependentGloss': u'the',
                                                           u'governor': 4,
                                                           u'governorGloss': u'airspeed'},
                                                       {   u'dep': u'nsubj',
                                                           u'dependent': 4,
                                                           u'dependentGloss': u'airspeed',
                                                           u'governor': 1,
                                                           u'governorGloss': u'What'},
                                                       {   u'dep': u'case',
                                                           u'dependent': 5,
                                                           u'dependentGloss': u'of',
                                                           u'governor': 8,
                                                           u'governorGloss': u'swallow'},
                                                       {   u'dep': u'det',
                                                           u'dependent': 6,
                                                           u'dependentGloss': u'an',
                                                           u'governor': 8,
                                                           u'governorGloss': u'swallow'},
                                                       {   u'dep': u'compound',
                                                           u'dependent': 7,
                                                           u'dependentGloss': u'unladen',
                                                           u'governor': 8,
                                                           u'governorGloss': u'swallow'},
                                                       {   u'dep': u'nmod:of',
                                                           u'dependent': 8,
                                                           u'dependentGloss': u'swallow',
                                                           u'governor': 4,
                                                           u'governorGloss': u'airspeed'},
                                                       {   u'dep': u'punct',
                                                           u'dependent': 9,
                                                           u'dependentGloss': u'?',
                                                           u'governor': 1,
                                                           u'governorGloss': u'What'}],
                          u'enhancedPlusPlusDependencies': [   {   u'dep': u'ROOT',
                                                                   u'dependent': 1,
                                                                   u'dependentGloss': u'What',
                                                                   u'governor': 0,
                                                                   u'governorGloss': u'ROOT'},
                                                               {   u'dep': u'cop',
                                                                   u'dependent': 2,
                                                                   u'dependentGloss': u'is',
                                                                   u'governor': 1,
                                                                   u'governorGloss': u'What'},
                                                               {   u'dep': u'det',
                                                                   u'dependent': 3,
                                                                   u'dependentGloss': u'the',
                                                                   u'governor': 4,
                                                                   u'governorGloss': u'airspeed'},
                                                               {   u'dep': u'nsubj',
                                                                   u'dependent': 4,
                                                                   u'dependentGloss': u'airspeed',
                                                                   u'governor': 1,
                                                                   u'governorGloss': u'What'},
                                                               {   u'dep': u'case',
                                                                   u'dependent': 5,
                                                                   u'dependentGloss': u'of',
                                                                   u'governor': 8,
                                                                   u'governorGloss': u'swallow'},
                                                               {   u'dep': u'det',
                                                                   u'dependent': 6,
                                                                   u'dependentGloss': u'an',
                                                                   u'governor': 8,
                                                                   u'governorGloss': u'swallow'},
                                                               {   u'dep': u'compound',
                                                                   u'dependent': 7,
                                                                   u'dependentGloss': u'unladen',
                                                                   u'governor': 8,
                                                                   u'governorGloss': u'swallow'},
                                                               {   u'dep': u'nmod:of',
                                                                   u'dependent': 8,
                                                                   u'dependentGloss': u'swallow',
                                                                   u'governor': 4,
                                                                   u'governorGloss': u'airspeed'},
                                                               {   u'dep': u'punct',
                                                                   u'dependent': 9,
                                                                   u'dependentGloss': u'?',
                                                                   u'governor': 1,
                                                                   u'governorGloss': u'What'}],
                          u'index': 0,
                          u'parse': u'(ROOT\n  (SBARQ\n    (WHNP (WP What))\n    (SQ (VBZ is)\n      (NP\n        (NP (DT the) (NN airspeed))\n        (PP (IN of)\n          (NP (DT an) (NN unladen) (NN swallow)))))\n    (. ?)))',
                          u'tokens': [   {   u'after': u' ',
                                             u'before': u'',
                                             u'characterOffsetBegin': 0,
                                             u'characterOffsetEnd': 4,
                                             u'index': 1,
                                             u'lemma': u'what',
                                             u'originalText': u'What',
                                             u'pos': u'WP',
                                             u'word': u'What'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 5,
                                             u'characterOffsetEnd': 7,
                                             u'index': 2,
                                             u'lemma': u'be',
                                             u'originalText': u'is',
                                             u'pos': u'VBZ',
                                             u'word': u'is'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 8,
                                             u'characterOffsetEnd': 11,
                                             u'index': 3,
                                             u'lemma': u'the',
                                             u'originalText': u'the',
                                             u'pos': u'DT',
                                             u'word': u'the'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 12,
                                             u'characterOffsetEnd': 20,
                                             u'index': 4,
                                             u'lemma': u'airspeed',
                                             u'originalText': u'airspeed',
                                             u'pos': u'NN',
                                             u'word': u'airspeed'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 21,
                                             u'characterOffsetEnd': 23,
                                             u'index': 5,
                                             u'lemma': u'of',
                                             u'originalText': u'of',
                                             u'pos': u'IN',
                                             u'word': u'of'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 24,
                                             u'characterOffsetEnd': 26,
                                             u'index': 6,
                                             u'lemma': u'a',
                                             u'originalText': u'an',
                                             u'pos': u'DT',
                                             u'word': u'an'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 27,
                                             u'characterOffsetEnd': 34,
                                             u'index': 7,
                                             u'lemma': u'unladen',
                                             u'originalText': u'unladen',
                                             u'pos': u'JJ',
                                             u'word': u'unladen'},
                                         {   u'after': u' ',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 35,
                                             u'characterOffsetEnd': 42,
                                             u'index': 8,
                                             u'lemma': u'swallow',
                                             u'originalText': u'swallow',
                                             u'pos': u'VB',
                                             u'word': u'swallow'},
                                         {   u'after': u'',
                                             u'before': u' ',
                                             u'characterOffsetBegin': 43,
                                             u'characterOffsetEnd': 44,
                                             u'index': 9,
                                             u'lemma': u'?',
                                             u'originalText': u'?',
                                             u'pos': u'.',
                                             u'word': u'?'}]}]
                                        }
        expected_output = [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'),
                           ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'),
                           ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]
        tagged_data = corenlp_tagger.api_call(input_tokens,
                                              properties={'ssplit.isOneSentence': 'true',
                                                          'annotators': 'tokenize,ssplit,pos' })
        # Emulates the tagging function.
        # Note: We're not calling the corenlp_tagger.tag() directly because
        #       it will not return the desired value but a MagicMock object.
        # >>> corenlp_tagger.tag(input_tokens)
        # >>> <MagicMock name='CoreNLPTagger().tag()' id='140395802719848'>
        tagged_output = [(token['word'], token['pos'])
                         for token in tagged_data['sentences'][0]['tokens']]
        self.assertEqual(expected_output, tagged_output)
