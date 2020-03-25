# -*- coding: utf-8 -*-
# Copyright 2020 Aneior Studio, SL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from airflow.operators.bash_operator import BashOperator
from airflow.plugins_manager import AirflowPlugin
from airflow_pentaho.hooks.PentahoHook import PentahoHook
from airflow_pentaho.operators.PanOperator import PanOperator
from airflow_pentaho.operators.KitchenOperator import KitchenOperator
BashOperator


class PentahoPlugin(AirflowPlugin):
    name = "pentaho"
    operators = [KitchenOperator, PanOperator]
    hooks = [PentahoHook]
