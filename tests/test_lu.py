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

obj = APIBase("torch.lu")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch

        A = torch.tensor(
            [
                [
                    [0.3591, -0.0479, -0.2174],
                    [-0.6957, -1.4667, 1.4384],
                    [0.0735, 0.1147, 0.0513],
                ],
                [
                    [-1.2565, -2.1263, 0.8075],
                    [-0.3665, -3.3540, -0.9417],
                    [-0.1299, -0.0689, -0.6207],
                ],
            ]
        )
        A_LU, pivots = torch.lu(A)
        """
    )
    obj.run(pytorch_code, ["A_LU", "pivots"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch

        A = torch.tensor(
            [
                [
                    [0.3591, -0.0479, -0.2174],
                    [-0.6957, -1.4667, 1.4384],
                    [0.0735, 0.1147, 0.0513],
                ],
                [
                    [-1.2565, -2.1263, 0.8075],
                    [-0.3665, -3.3540, -0.9417],
                    [-0.1299, -0.0689, -0.6207],
                ],
            ]
        )
        A_LU, pivots, info = torch.lu(A, get_infos=True)
        """
    )
    obj.run(pytorch_code, ["A_LU", "pivots", "info"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch

        A = torch.tensor(
            [
                [
                    [0.3591, -0.0479, -0.2174],
                    [-0.6957, -1.4667, 1.4384],
                    [0.0735, 0.1147, 0.0513],
                ],
                [
                    [-1.2565, -2.1263, 0.8075],
                    [-0.3665, -3.3540, -0.9417],
                    [-0.1299, -0.0689, -0.6207],
                ],
            ]
        )
        A_LU, pivots, info = torch.lu(A, pivot=True, get_infos=True)
        """
    )
    obj.run(pytorch_code, ["A_LU", "pivots", "info"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch

        A = torch.tensor(
            [
                [
                    [0.3591, -0.0479, -0.2174],
                    [-0.6957, -1.4667, 1.4384],
                    [0.0735, 0.1147, 0.0513],
                ],
                [
                    [-1.2565, -2.1263, 0.8075],
                    [-0.3665, -3.3540, -0.9417],
                    [-0.1299, -0.0689, -0.6207],
                ],
            ]
        )
        A_LU = torch.empty_like(A)
        pivots = torch.empty((2, 3), dtype=torch.int32)
        info = torch.empty((2, ), dtype=torch.int32)
        torch.lu(A, pivot=True, get_infos=True, out=(A_LU, pivots, info))
        """
    )
    obj.run(pytorch_code, ["A_LU", "pivots", "info"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch

        A = torch.tensor(
            [
                [
                    [0.3591, -0.0479, -0.2174],
                    [-0.6957, -1.4667, 1.4384],
                    [0.0735, 0.1147, 0.0513],
                ],
                [
                    [-1.2565, -2.1263, 0.8075],
                    [-0.3665, -3.3540, -0.9417],
                    [-0.1299, -0.0689, -0.6207],
                ],
            ]
        )
        A_LU = torch.empty_like(A)
        pivots = torch.empty((2, 3), dtype=torch.int32)
        torch.lu(A, pivot=True, get_infos=False, out=(A_LU, pivots))
        """
    )
    obj.run(pytorch_code, ["A_LU", "pivots"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch

        A = torch.tensor(
            [
                [
                    [0.3591, -0.0479, -0.2174],
                    [-0.6957, -1.4667, 1.4384],
                    [0.0735, 0.1147, 0.0513],
                ],
                [
                    [-1.2565, -2.1263, 0.8075],
                    [-0.3665, -3.3540, -0.9417],
                    [-0.1299, -0.0689, -0.6207],
                ],
            ]
        )
        A_LU = torch.empty_like(A)
        pivots = torch.empty((2, 3), dtype=torch.int32)
        LU = torch.lu(A, pivot=True, get_infos=False, out=(A_LU, pivots))
        """
    )
    obj.run(pytorch_code, ["A_LU", "pivots", "LU"])
