"""Using the classify_text method to find content categories of text files,
Then use the content category labels to compare text similarity.
"""

# [START classify_text_tutorial_import]
import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six
# [END classify_text_tutorial_import]


# [START def_classify]
def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result
# [END def_classify]
classify("Scientists at the National Center for Supercomputing Applications (NCSA), located at the University of Illinois at Urbana-Champaign used GPUs and deep learning to rapidly detect and characterize.")
