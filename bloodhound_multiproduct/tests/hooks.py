# -*- coding: utf-8 -*-
#
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.


try:
    import unittest2 as unittest
except ImportError:
    import unittest

from trac.web.href import Href

from multiproduct.hooks import ProductizedHref


class ProductizedHrefTestCase(unittest.TestCase):

    def test_params_is_dictionary(self):
        ghref = Href('/base')
        phref = ProductizedHref(ghref, '/product')
        self.assertIn(phref({'param': 'value', 'other': 'other value'}),
                      ['/product?param=value&other=other+value',
                       '/product?other=other+value&param=value'])


def test_suite():
    return unittest.TestSuite([
        unittest.makeSuite(ProductizedHrefTestCase, 'test')
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
