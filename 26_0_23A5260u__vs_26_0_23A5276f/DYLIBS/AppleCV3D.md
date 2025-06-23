## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-8.25.5.7.1
-  __TEXT.__text: 0x1efb6a8
-  __TEXT.__auth_stubs: 0x3900
+8.25.5.28.1
+  __TEXT.__text: 0x1f4772c
+  __TEXT.__auth_stubs: 0x3910
   __TEXT.__init_offsets: 0x8
-  __TEXT.__gcc_except_tab: 0x108a80
-  __TEXT.__const: 0x168dec
-  __TEXT.__cstring: 0xa4938
-  __TEXT.__oslogstring: 0x1159a
-  __TEXT.__unwind_info: 0x3e440
+  __TEXT.__gcc_except_tab: 0x10b680
+  __TEXT.__const: 0x16aebc
+  __TEXT.__cstring: 0xa5751
+  __TEXT.__oslogstring: 0x117f0
+  __TEXT.__unwind_info: 0x3e8b8
   __TEXT.__eh_frame: 0x2328
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x74f
   __TEXT.__objc_stubs: 0xba0
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x32c0
+  __DATA_CONST.__const: 0x3308
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e8
-  __AUTH_CONST.__auth_got: 0x1c90
-  __AUTH_CONST.__const: 0x7a2d8
+  __AUTH_CONST.__auth_got: 0x1c98
+  __AUTH_CONST.__const: 0x7a7f8
   __AUTH_CONST.__cfstring: 0x1980
-  __AUTH.__data: 0x30
+  __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30
-  __DATA.__data: 0x89e8
+  __DATA.__data: 0x8a68
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xf6d8
-  __DATA.__common: 0x2008
+  __DATA.__bss: 0x11d08
+  __DATA.__common: 0x2068
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6F82FD3-2B23-3472-9984-8637836D3DC0
-  Functions: 47511
-  Symbols:   2052
-  CStrings:  14482
+  UUID: 813BAE8D-D7E0-3F5A-AC7C-00F3CC2D49EB
+  Functions: 47686
+  Symbols:   2055
+  CStrings:  14547
 
Symbols:
+ _CV3DSLAMConfigEnableOneTimePrioritizedMapLoading
+ _CV3DSLAMSessionRemoveAnchorFromGroupWithRequest
+ __tlv_atexit
CStrings:
+ " is processing only the first encountered timestamp, which was '"
+ " offsets)."
+ "!located_submap_toc_.contains(metadata.session_id)"
+ "(config_.imu_filter_switch_config.enable_imu_filter_motion_switch && (config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode == RLSTrainingFilterModes::MotionIMUFilteringSmooth || check1 || check1b || check3)) || (!config_.imu_filter_switch_config.enable_imu_filter_motion_switch && config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode != RLSTrainingFilterModes::MotionIMUFilteringSmooth) || check2 || check2b || check4"
+ "(output[i].timestamp - output[i - 1].timestamp) <= max_IMU_data_gap"
+ ", VIOIMUFactorBase imu data. "
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/IMUSampleBuffer.h"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/OdometryKernels/src/Shims.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/include/VIO/Odometry/LowPowerEpipolarOutlierRejection.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/include/VIO/Odometry/OutlierRejectionUtil.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/OdometryUnsanitized/include/VIO/OdometryUnsanitized/IMUSynchronizerLP.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/OdometryUnsanitized/src/IMUSynchronizerUtil.cpp"
+ "Adaptive IMU sampling is not supported on LACC."
+ "Anchors: unable to save NRAnchor %s"
+ "BA WARNING: successfulIterations: %d, correction: %f, gradient: %f, inertial: %f, map: %f, vision: %f, prior: %f, total: %f."
+ "Classify"
+ "Enforce uniform distribution across all bins in area binning filter."
+ "Exceeding max gap for %.*s timestamps: prev=%lf, cur=%lf. Dropping this sample."
+ "Failed to save submap metadata to latest with msg. "
+ "Filter must not be initialized yet."
+ "GeneralizedP3POutlierRejectionConfig.min_num_2d3d_inliers_from_2nd_estimate"
+ "Got %u point correspondences and %u line correspondences to reference frame (which is %zu frames back)"
+ "IMU sample timestamp is not increasing."
+ "IMU state timestamp is not associate with last IMU sample timestamp."
+ "IMUSampleBuffer is empty."
+ "LPMaximumParameterMagnitudeSq: "
+ "Last IMU sample offset incorrect."
+ "Map data must have a vio database"
+ "MappingIO:LoadingPriorityBump:Constructor"
+ "MappingIO:LoadingPriorityBump:LoadedMap"
+ "MappingIO:LoadingPriorityBump:ReInit"
+ "MappingIOMapLoad:NR:All:NumAreas%zu, NumKFSize:%zu"
+ "MappingIOMapLoad:NR:RecentLocation:NumAreas%zu, NumKFSize:%zu"
+ "MappingIOSave:NumUpdatedSubmapMetadata:%u"
+ "MappingManagerConfig.max_non_removable_area_range_m"
+ "MappingManagerConfig.max_num_non_removable_area_relocalization_request"
+ "Maximum allowed magnitude of the parameter updates."
+ "Maximum distance range of a non removable area. It is used for deciding which NR-area to associate with current pose, and also the lever-arm distance allowed for pruning map containing NR anchor."
+ "Minimum number of 2D3D inilier from 2nd estimater to consider it."
+ "NR:NumAreas: %d|Loc: %d|Ext: %d|states: %u|w_neighbor: %u"
+ "NR:UpdateNRSubmapAreaNeighbots"
+ "No segmentation inputs found, did you mean to disable segmentation with `enable_mpc_and_segmentation: false`?"
+ "Non-monotonic %.*s timestamps: prev=%lf, cur=%lf. Dropping this sample."
+ "Number of maximum non-removable area relocalization request."
+ "P192Tracker200HzFilter"
+ "Per-HWFP Intrinsics: Fx: %f, Fy: %f, Cx: %f, Cy: %f"
+ "R_gyro_prev_to_cur_cam_frame_t.size() == camera_sensor_models[config_.primary_stereo_primary_stream_id.camera_id]->NumStreams()"
+ "Stored timestamp does not match the buffer 2."
+ "Stored timestamp does not match the buffer."
+ "Structure filtering chi square 2d threshold"
+ "System"
+ "The IMU sample buffer cannot be empty!"
+ "The bundle does not have accel to gyro time-offset (have "
+ "The camera set features must exist for the already estimated state."
+ "The last IMU sample timestamp of a state overlaps with a previous state first timestamp."
+ "The request ID can not be null when removing an anchor"
+ "Toggle LowPowerSlamEngine prototype."
+ "Too many feature points detected. Be sure to set 'VFusionTrackerConfig.max_features' in your config"
+ "Update norm is too large. Skip it"
+ "VisualInertialBundleAdjusterConfig.maximum_parameter_magnitude"
+ "WaveRender"
+ "[IMUSynchronization] Large accel gap (likely due to frame is behind IMU data): "
+ "[IMUSynchronization] Large gyro gap (likely due to frame is behind IMU data): "
+ "[LPS] WindowStats: frameid: {}, camera: {}, num_continued: {}, num_created: {}, num_invalid: {}."
+ "[LPS] too many camera models."
+ "`calibrated_to_distorted` must succeed."
+ "accel"
+ "accel_it != accel.cend()"
+ "accel_it - accel.cbegin() <= IMU_BUFFER_SIZE"
+ "area_binning_enforce_uniform_distribution"
+ "calibrated_location[2] > 1e-8"
+ "config_.imu_extrapolation_config.accel_filter_config.RLS_filter_mode != RLSTrainingFilterModes::WaveMotionAdaptive"
+ "exporter"
+ "external_reloc_result.relocalization_type() == RelocalizationType::kVisionStateToStateRelocalization || external_reloc_result.relocalization_type() == RelocalizationType::kUnknown || external_reloc_result.relocalization_type() == RelocalizationType::kOdometryEdge"
+ "gyro"
+ "gyro_it != gyro.cend()"
+ "gyro_it - gyro.cbegin() <= IMU_BUFFER_SIZE"
+ "imu accels: "
+ "imu gyros: "
+ "imu timestamp: "
+ "kMaxNumberOfHypothesesLP >= config.ransac_max_num_hypotheses"
+ "lens_model.image_to_calibrated(calibrated_location.data(), obs.data())"
+ "nfde_rskwfdpih8_sparse.mlmodelc/"
+ "point_store->keypoints().size() <= odometry::LowPowerSlamState::WindowTraits::kMaxTracks"
+ "ret.second && \"must successful adding the NR_area_info\""
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kBADeltaNormTooLarge]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::batch_least_squares::MetricName::kBANoSuccessfulIteration]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kCMFirstJoinedUsersBandwidthKBPriorMerge]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kDurationOfMergingFirstJoinCMUserWithWarmStart]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kNumStatesFromNonRemovableAreasAndNeighbor]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kUpdateAllNRSubmapNeighbors]"
+ "std::string_view lacc::function_name() [F = &ComputePoseFromLatestFrame]"
+ "this->data_->viodatabase()"
+ "use_low_power_slam_engine"
- "!m_data.second.location_data.has_value()"
- "(config_.imu_filter_switch_config.enable_imu_filter_motion_switch && (config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode == RLSTrainingFilterModes::MotionIMUFilteringSmooth || check1 || check3)) || (!config_.imu_filter_switch_config.enable_imu_filter_motion_switch && config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode != RLSTrainingFilterModes::MotionIMUFilteringSmooth) || check2 || check4"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/LPFGContainers.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/BatchLeastSquaresUnsanitized/src/IMUSampleBuffer.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/include_private/VIO/Odometry/OutlierRejectionUtil.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/SlamEngineNodeGroup/src/include_private/SlamEngineNodeGroup.cpp"
- "; exporter is exporting only the first encountered timestamp, which was '"
- "Error the IMU sample buffer cannoty be empty!\n"
- "Exceeding max gap for accel timestamps: prev=%lf, cur=%lf. Dropping this sample."
- "Exceeding max gap for gyro timestamps: prev=%lf, cur=%lf. Dropping this sample."
- "Filter must not be initialized yet"
- "IMU sample timestamp is not increasing"
- "IMU state timestamp is not associate with last imu sample timestamp"
- "Last imu sample offset incorrect"
- "Map Data must have a vio database."
- "MappingManagerConfig.max_nonremovable_area_distance_to_current_pose_m"
- "MappingManagerConfig.max_nonremovable_area_lever_arm_distance_m"
- "Maximum allowed distance (in meters) for lever-arm distance to allow pruning map containing NR anchor."
- "Maximum distance (in meters) allowed for a candidate NR-area to be corresponded assigned to current pose."
- "NR:NumAreas: %d|Loc: %d|Ext: %d|states: %u"
- "Non-monotonic accel timestamps: prev=%lf, cur=%lf. Dropping this sample."
- "Non-monotonic gyro timestamps: prev=%lf, cur=%lf. Dropping this sample."
- "Our frame predates our oldest IMU data. Time to die"
- "Query submap does not exist"
- "R_gyro_prev_to_cur_cam_frame.size() == camera_sensor_models[config_.primary_stereo_primary_stream_id.camera_id]->NumStreams()"
- "Received Accel measurement exceeds maximum gap."
- "Received Gyro measurement exceeds maximum gap."
- "Structure filtering chi square 2d threshold \n"
- "The IMU sample buffer cannoty be empty!"
- "The bundle does not have accel to gyro time-offset."
- "The camera set features must exist for the already estimated state"
- "buffer is empty"
- "first IMU sample timestamp overlaps with previous imu_state last imu sample"
- "gyros_.back().timestamp < oldest_frame_ts && accels_.front().timestamp"
- "iter == located_submap_toc_.end()"
- "map_data.viodatabase()"
- "map_interface_node_ != nullptr"
- "nfde_rskwfdpih8_sparse.mlmodelc/model.mil"
- "opt_query_submap"
- "std::fabs(anchor_direction().norm2() - 1) <= 1e-6"

```
