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

obj = APIBase("torch.sigmoid")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.sigmoid(torch.tensor([ 0.9213,  1.0887, -0.8858, -1.7683]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([ 0.9213,  1.0887, -0.8858, -1.7683])
        result = torch.sigmoid(a)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = [ 0.9213,  1.0887, -0.8858, -1.7683]
        out = torch.tensor(a)
        result = torch.sigmoid(torch.tensor(a), out=out)
        """
    )
    obj.run(pytorch_code, ["out"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        a = torch.tensor([ 0.9213,  1.0887, -0.8858, -1.7683])
        result = torch.sigmoid(input=a)
        """
    )
    obj.run(pytorch_code, ["result"])
