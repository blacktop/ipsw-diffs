## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-8.25.6.25.11
-  __TEXT.__text: 0x1f90b68
+8.25.6.25.71
+  __TEXT.__text: 0x1fb88e8
   __TEXT.__auth_stubs: 0x3910
   __TEXT.__init_offsets: 0x8
-  __TEXT.__gcc_except_tab: 0x10d484
-  __TEXT.__const: 0x16c1bc
-  __TEXT.__cstring: 0xa81a1
-  __TEXT.__oslogstring: 0x11ae4
-  __TEXT.__unwind_info: 0x3eb70
+  __TEXT.__gcc_except_tab: 0x10ea48
+  __TEXT.__const: 0x16c97c
+  __TEXT.__cstring: 0xa9d3a
+  __TEXT.__oslogstring: 0x11ddc
+  __TEXT.__unwind_info: 0x3ee88
   __TEXT.__eh_frame: 0x2200
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x713
-  __TEXT.__objc_stubs: 0xb60
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x3420
+  __TEXT.__objc_methname: 0x732
+  __TEXT.__objc_stubs: 0xba0
+  __DATA_CONST.__got: 0x5c0
+  __DATA_CONST.__const: 0x3458
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d8
+  __DATA_CONST.__objc_selrefs: 0x2e8
   __AUTH_CONST.__auth_got: 0x1c98
-  __AUTH_CONST.__const: 0x7abc0
-  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__const: 0x7afa8
+  __AUTH_CONST.__cfstring: 0x19a0
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30
-  __DATA.__data: 0x8a08
+  __DATA.__data: 0x8a48
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x11e88
-  __DATA.__common: 0x21d0
+  __DATA.__bss: 0x121c8
+  __DATA.__common: 0x2300
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91E21D9D-BBEE-3081-87A0-88BC68E909F3
-  Functions: 47870
-  Symbols:   2055
-  CStrings:  14733
+  UUID: 944B0B2C-7765-36E1-B8C5-4B81835AC98D
+  Functions: 48002
+  Symbols:   2056
+  CStrings:  14841
 
Symbols:
+ _OBJC_CLASS_$_PSBarrier
CStrings:
+ " inlier_clique: "
+ " num_pairs: "
+ " num_pts_subset: "
+ " ref_imgs: "
+ " relative_pose_pair_size: "
+ " scene_size: "
+ "!config_.skip_transition_mode_in_camera_allocation || !from_transition_to_target"
+ "!line_detector_->Enabled()"
+ "!target_query_image_ids.empty()"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/AreaMapping/src/MultiRelativePoseAggregation.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/HarrisDetector/src/HarrisDetectionModel.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/src/CameraAllocatorBase.cpp"
+ "Anchors:CM removing anchor with ID: %s..."
+ "Attempting to load the model "
+ "CameraAllocatorConfig.minimal_frames_to_switch_to_next_state"
+ "CameraAllocatorConfig.skip_transition_mode_in_camera_allocation"
+ "Cosine of maximum difference between average gradient and current edgel gradient when tracking edgel chains."
+ "Dropping HarrisDetectionOutput at %f because frame expired"
+ "Flag to aggregate only relative poses from target external submaps."
+ "Flag to aggregate only relative poses from target localized submaps."
+ "Flag to not removing cached relative poses after a successful relocalization."
+ "Flag to only accept aggregated relocalization results if it contains query images. This is only used when evaluating re-localization FOM."
+ "HarrisDetectionModel Run Error: "
+ "LineDetectorConfig.cos_angle_threshold"
+ "LineMatchingConfig.point_distance_sq_threshold"
+ "Minimal number of frames to switch to next camera allocation state."
+ "MpcControllerDonResetMode"
+ "MultiFramePoseRefinerConfig.skip_matching_if_found_cached_relative_pose_info"
+ "MultiRelativePoseAggregationConfig parameters"
+ "MultiRelativePoseAggregationConfig.aggregate_only_from_target_external_submap"
+ "MultiRelativePoseAggregationConfig.aggregate_only_from_target_localized_submap"
+ "MultiRelativePoseAggregationConfig.eval_only_from_query_images"
+ "MultiRelativePoseAggregationConfig.eval_only_keep_cached_relative_poses_after_success"
+ "MultiRelativePoseAggregationConfig.num_cached_relative_poses"
+ "MultiRelativePoseAggregationConfig.only_use_ext_submap_connected_via_odometry"
+ "NR:MultiRelPoseSucceeded %u"
+ "Not running DMS detector due to APPLE_FEATURE_DMS_DETECTION flag: %d"
+ "Number of cached relative poses overtime."
+ "PoseController(%s) device not worn"
+ "PoseController(%s) reset"
+ "PoseController(%s) temp disabled"
+ "Should not be light_ba_mode_ if bad_geometry_in_last_frame_"
+ "Skip matching if found cached relative pose info."
+ "T_seed_to_curr_submap_iter != T_seed_to_other_submap_origin.end()"
+ "Tolerance in matching pixel distance per end point, 1.0 is too strict for fisheye"
+ "Use only odometry edge when aggregating neighbor external submap from target external submap."
+ "We should not hit transition mode when we already enable skipping transition mode."
+ "Whether driver monitoring system (DMS) detection should be performed in Polaris. Disabled by default on visionOS."
+ "Whether or not skip `CameraAllocationState::TransitionCameraMode`."
+ "Whether to run lines inference only when DMS is detected. Enabled by default on visionOS."
+ "[AllocateCameraUsage] Regular stereo mode."
+ "[AllocateCameraUsage] SCAML Mono mode."
+ "[AllocateCameraUsage] SCAMR Mono mode."
+ "[AllocateCameraUsage] adaptive stereo mode."
+ "[AllocateCameraUsage] dcam-l | dcam-r | scam-l | scam-r weight=%.3f, %.3f, %.3f, %.3f"
+ "[CreateCameraUsageRequests] primary_stereo_inliers=%u, left_stereo_percentage=%u, right_stereo_percentage=%u"
+ "[DistributeMonoCameraRatio] left_inliers=%u, right_inliers=%u, ratio=%d:1, left_share=%.3f, right_share=%.3f"
+ "curr_state"
+ "enable_dms_detection"
+ "harris_corner_detector_NMP.mlmodelc/"
+ "input_buffer"
+ "iter != T_seed_to_other_submap_origin.end()"
+ "iter != cached_relative_pose_info_vec_.end()"
+ "latest_pose_pair size: "
+ "max lux level thresholds cannot be negative."
+ "max_period, min_period, and confirmation_frames must be positive."
+ "min_peaks_in_window must be at least 3 for robust stats."
+ "min_period must be less than max_period."
+ "neighbor_state"
+ "peak_valley_depth_cv_threshold must be between 0 and 1."
+ "prominence thresholds cannot be negative."
+ "run_lines_inference_only_dms_detected"
+ "slam-lines-barrier"
+ "src_ext_submap->session_hash_ == target_ref_submap_id"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::applecv3d::slam::OpaqueTypeWithSessionID<cv3d::vio::harris::HarrisDetectionOutput>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera0InlierMatchedStereoLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera0InlierTemporalLineMatches]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera0MatchedLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera0NumFeaturesForMatching]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera0NumLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera1InlierMatchedStereoLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera1InlierTemporalLineMatches]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera1MatchedLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera1NumFeaturesForMatching]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera1NumLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera2InlierMatchedStereoLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera2InlierTemporalLineMatches]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera2MatchedLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera2NumFeaturesForMatching]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera2NumLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera3InlierMatchedStereoLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera3InlierTemporalLineMatches]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera3MatchedLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera3NumFeaturesForMatching]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera3NumLineFeatures]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kLowFrequencyFlickerDetectionState]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kNumberOfVIOLineFactors]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::harris::HarrisDetectionOutput]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kNRAreaMultiRelativePoseSucceeded]"
+ "std::all_of(target_query_image_ids.begin(), target_query_image_ids.end(), [target_query_submap_id](const auto& target_query_image_id) { return target_query_image_id.view.uuid_hash() == target_query_submap_id; })"
+ "std::find(cached_relative_pose_info_vec_.begin(), cached_relative_pose_info_vec_.end(), relative_pose_info) == cached_relative_pose_info_vec_.end()"
+ "updateBarrier:"
+ "waitForBarrier:"
+ "window_size should be at least 2 times max_period."
- "!use_lens_model_during_detection_"
- "Currently not supported"
- "LineDetectorConfig.angle_threshold"
- "Maximum difference between average gradient and current edgel gradient when tracking edgel chains."
- "Should not have bad_geometry_in_last_frame_"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::applecv3d::slam::LinesMLData]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::applecv3d::slam::OpaqueTypeWithSessionID<cv3d::applecv3d::slam::LinesMLData>]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera0NumStaticFeatures]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera1NumStaticFeatures]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera2NumStaticFeatures]"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kCamera3NumStaticFeatures]"

```
