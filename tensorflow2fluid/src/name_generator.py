#   Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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


class NameGenerator(object):
    def __init__(self):
        self.param_index = 0
        self.input_index = 0
        self.net_index = 0
        self.const_index = 0
        self.names = dict()

    def get_name(self, node):
        ref_name = None
        op_name = node.layer_type

        if node.layer.name in self.names:
            return self.names[node.layer.name]

        if op_name == "variablev2":
            ref_name = "param_" + str(self.param_index)
            self.param_index += 1
        elif op_name == "placeholder":
            ref_name = "input_" + str(self.input_index)
            self.input_index += 1
        elif op_name == "const":
            ref_name = "const_" + str(self.const_index)
            self.const_index += 1
        elif op_name.lower() == "identity":
            ref_name = self.names[node.layer.input[0]]
        else:
            ref_name = "net_" + str(self.net_index)
            self.net_index += 1
        self.names[node.layer.name] = ref_name
        return ref_name