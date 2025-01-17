# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
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

from __future__ import absolute_import
import logging
from ... import c_lib_wrap as C


def vis_detection(im_data,
                  det_result,
                  score_threshold=0.0,
                  line_size=1,
                  font_size=0.5):
    return C.vision.Visualize.vis_detection(
        im_data, det_result, score_threshold, line_size, font_size)


def vis_face_detection(im_data, face_det_result, line_size=1, font_size=0.5):
    return C.vision.Visualize.vis_face_detection(im_data, face_det_result,
                                                 line_size, font_size)


def vis_segmentation(im_data, seg_result):
    return C.vision.Visualize.vis_segmentation(im_data, seg_result)


def vis_matting_alpha(im_data,
                      matting_result,
                      remove_small_connected_area=False):
    return C.vision.Visualize.vis_matting_alpha(im_data, matting_result,
                                                remove_small_connected_area)


def swap_background_matting(im_data,
                            background,
                            result,
                            remove_small_connected_area=False):
    assert isinstance(
        result,
        C.vision.MattingResult), "The result must be MattingResult type"
    return C.vision.Visualize.swap_background_matting(
        im_data, background, result, remove_small_connected_area)


def swap_background_segmentation(im_data, background, background_label,
                                 result):
    assert isinstance(
        result, C.vision.
        SegmentationResult), "The result must be SegmentaitonResult type"
    return C.vision.Visualize.swap_background_segmentation(
        im_data, background, background_label, result)


def remove_small_connected_area(alpha_pred_data, threshold):
    assert len(alpha_pred_data.shape) == 3, "alpha has a (h, w, 1) shape"
    return C.vision.Visualize.remove_small_connected_area(alpha_pred_data,
                                                          threshold)
def vis_ppocr(im_data, det_result):
    return C.vision.Visualize.vis_ppocr(im_data, det_result)
