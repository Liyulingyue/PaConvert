# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase
from optimizer_helper import generate_optimizer_test_code

obj = APIBase("torch.optim.SGD")


def test_case_1():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code("torch.optim.SGD(conv.parameters(), lr=0.1)")
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


def test_case_2():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code(
            "torch.optim.SGD(conv.parameters(), lr=0.8, weight_decay=0.1)"
        )
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


def test_case_3():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code("torch.optim.SGD(conv.parameters(), lr=0.5)")
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


# if `weight_decay` set as int rather than float,
# paddle will raise TypeError: 'int' object is not callable
def _test_case_4():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code(
            "torch.optim.SGD(conv.parameters(), lr=0.1, weight_decay=0)"
        )
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


def test_case_5():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code(
            "torch.optim.SGD(params=conv.parameters(), lr=0.8, weight_decay=0.1)"
        )
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


def test_case_6():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code("torch.optim.SGD(conv.parameters(), 0.5)")
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


def test_case_7():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code(
            "torch.optim.SGD(weight_decay=0.1, params=conv.parameters(), lr=0.8)"
        )
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5)


def test_case_8():
    pytorch_code = textwrap.dedent(
        generate_optimizer_test_code(
            "torch.optim.SGD(params=conv.parameters(), lr=0.8, momentum=0, dampening=0, weight_decay=0, nesterov=False, maximize=False, foreach=None, differentiable=False)"
        )
    )
    obj.run(
        pytorch_code,
        unsupport=True,
        reason="`momentum`, `dampening`, `nesterov`, `maximize`, `foreach` and `differentiable` is not supported.",
    )
