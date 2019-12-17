/*
 * Copyright (C) 2019 Open Source Robotics Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/

#include "layer.h"
using std::string;
using std::vector;

Layer::Layer()
{
}

Layer::~Layer()
{
}

bool Layer::from_yaml(const std::string &_name, const YAML::Node &y)
{
  if (!y.IsMap())
    throw std::runtime_error("Layer::from_yaml() expected a map");
  name = _name;
  filename = y["filename"].as<string>();
  meters_per_pixel = y["meters_per_pixel"].as<double>();
  translation_x = y["translation_x"].as<double>();
  translation_y = y["translation_y"].as<double>();
  rotation = y["rotation"].as<double>();
  return true;
}

YAML::Node Layer::to_yaml() const
{
  YAML::Node y;
  y["name"] = name;
  y["filename"] = filename;
  y["meters_per_pixel"] = meters_per_pixel;
  y["translation_x"] = translation_x;
  y["translation_y"] = translation_y;
  y["rotation"] = rotation;
  return y;
}
