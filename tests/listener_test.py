# -*- coding: utf-8 -*-

import unittest
import mock
import pytest
from sure import expect
from syriarightnow.app.tasks.twitter.listener import Listener

class ListenerTest(unittest.TestCase):
    def test_on_data(obj):
        data = { "user": { "screen_name": "something" }, "text": "some tweet" }
        listener = Listener("twitter_api")
        listener.on_data(data)

        expect(listener.verify).to.be.called_with(data)

    def test_verify(obj):
        data = { "user": { "screen_name": "something" }, "text": "some tweet" }
        listener = Listener("twitter_api")
        listener.verify(data)

        expect(listener.tweet).to.be.called_with("some tweet")
