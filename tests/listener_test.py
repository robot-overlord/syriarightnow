# -*- coding: utf-8 -*-

import unittest
import mock
import pytest
from sure import expect
from syriarightnow.app.tasks.twitter.listener import Listener

class ListenerTest(unittest.TestCase):
    def test_on_data(obj):
        data = { "user": { "screen_name": "something" }, "text": "some tweet" }
        listener = Listener()

        expect(listener.on_data(data)).to.be.true

    def test_verify(obj):
        data = { "user": { "screen_name": "something" }, "text": "some tweet" }
        listener = Listener()
        listener.verify(data)

        expect(listener.channel.basic_publish).to.be.called
