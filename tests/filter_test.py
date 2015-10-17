# -*- coding: utf-8 -*-

import pytest
from sure import expect
import syriarightnow.app.tasks.filter as filter

def test_call_with_match():
    sentence = "may the force be with you"
    keywords = ["may", "force", "some other thing", "be with"]
    result = filter.call(sentence, keywords)

    expect(result).to.equal(["may", "force", "be with"])

def test_call_without_match():
    sentence = "may the force be with you"
    result = filter.call(sentence)

    expect(result).to.equal([])
