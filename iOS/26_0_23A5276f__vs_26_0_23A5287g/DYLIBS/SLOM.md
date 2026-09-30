## SLOM

> `/System/Library/PrivateFrameworks/SLOM.framework/SLOM`

```diff

-1.10.0.0.0
-  __TEXT.__text: 0x14bbbe8
+1.11.0.0.0
+  __TEXT.__text: 0x14cd0d0
   __TEXT.__auth_stubs: 0x2150
-  __TEXT.__const: 0xe1910
-  __TEXT.__gcc_except_tab: 0x8bd2c
-  __TEXT.__cstring: 0x4cb6c
-  __TEXT.__oslogstring: 0x3597
-  __TEXT.__unwind_info: 0x20e70
+  __TEXT.__const: 0xe2010
+  __TEXT.__gcc_except_tab: 0x8c0ec
+  __TEXT.__cstring: 0x4d844
+  __TEXT.__oslogstring: 0x360f
+  __TEXT.__unwind_info: 0x21098
   __TEXT.__eh_frame: 0x1dc0
   __TEXT.__objc_methname: 0x24e
   __TEXT.__objc_stubs: 0x300
   __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0x1780
+  __DATA_CONST.__const: 0x1798
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc0
   __AUTH_CONST.__auth_got: 0x10b8
-  __AUTH_CONST.__const: 0x2fa00
+  __AUTH_CONST.__const: 0x2fc00
   __AUTH_CONST.__cfstring: 0x100
   __AUTH.__data: 0x18
-  __DATA.__data: 0x8588
+  __DATA.__data: 0x85c8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xede0
-  __DATA.__common: 0x1d58
+  __DATA.__common: 0x1d78
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36C77ABB-4527-3E39-B81B-ABEB573C0B65
-  Functions: 23790
+  UUID: AF3E2B7B-8BD6-394D-9AAC-157624EEBB1D
+  Functions: 23903
   Symbols:   681
-  CStrings:  6197
+  CStrings:  6265
 
CStrings:
+ "!cached_vio_kf_data_vector_.empty()"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/SlomMappingVIO/src/OccupancyRasterizer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Util/include/SLOM/Util/SensorBuffer.h"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Util/src/SensorBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/Triangulator.h"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/EstimatorKernels/include/VIO/EstimatorKernels/ComputePose.h"
+ "CoordinateTransformer::IsPositionInBound(local_mask_size_, local_mask_size_, l0, l1)"
+ "DeleteBadlyTrackedSubmaps"
+ "DeleteCorruptedStates"
+ "ExactlyEqual(opt_npdr_base_state_and_timestamp_->timestamp, last_kf_timestamp)"
+ "IMUSync"
+ "Invalid feature_container provided"
+ "Logic error: confident walking not accounted for."
+ "MapKeyframe:R:%u|W:%u|S:%u"
+ "NR:AddNonRemovableAnchor: %{public}s | %d"
+ "NR:AreaInfo: Loc_area:%{public}s Ext_area:%{public}s"
+ "NR:Downgrade|%s: %{public}s"
+ "NR:LocalizedDuration|avg: %f| max: %f"
+ "Near(sync_time, *last_input_time + input_imu_interval_, kTimeEps)"
+ "Near(w_older + w_newer, 1.0, kTimeEps)"
+ "Network type is not supported by our IMULandmark interface"
+ "Occupancy should be valid"
+ "Odometry"
+ "OutsideLimit"
+ "REPEATED_NR_ANCH:%u"
+ "Relative pose between frames must exit"
+ "Should be init'ed"
+ "Should be valid"
+ "Should have state."
+ "Solve"
+ "VIO Timestamp has to be monotonically increasing"
+ "VerifyAndDeleteCorruptedExternalSubmaps"
+ "We should always have relative poses"
+ "Wrong marginalized indices."
+ "Wrong reduced indices."
+ "[lpsba] Extracted %u tracks for camera %u (w/ %u streams) CameraIndex %u\n"
+ "[lpsba] Triangulated %u of %u tracks ...\n"
+ "[lpsba] batched marginalization reduced order: %s (size %u)\n"
+ "[lpsba] estimator kernel marginalization: reducedDoF: %u, norm2: %g, nnz: %u, diag30: %s\n"
+ "[lpsba] marginalization from last frame: reduced order: %s (size %u)\n"
+ "[lpsba] marginalization from last frame: reducedDoF: %u, norm2: %g, nnz: %u, diag30: %s\n"
+ "[lpsba] marginalization from last frame: target order: %s (size %u)\n"
+ "[lpsba] marginalization injected prior: %u x %u norm2: %g, nnz: %u, diag30: %s\n"
+ "[lpsba] successfuly initialized at %.5g\n"
+ "base_to_oldest_state_rel_pose_and_cov.state_id0 == opt_last_create_map_keyframe_state_id->key()"
+ "base_to_oldest_state_rel_pose_and_cov.state_id1 == oldest_state_id"
+ "cached_npdr_state_vector_.front().timestamp <= vio_keyframe_timestamp"
+ "cached_npdr_state_vector_.size() == 1"
+ "cached_vio_kf_data_vector_.front()->vio_state.timestamp > last_kf_timestamp"
+ "config().ml_desc_config.feature_type != vio::feature_detection::FeatureType::DetectorNoneDescriptorATUHardNetGlobalFeat"
+ "epipolar_algorithm == EpipolarAlgorithm::TwoPoint"
+ "ext_nr_submap_iter != this->external_submaps_.end()"
+ "feature_container"
+ "kf_data_ptr->opt_old_to_second_rel_pose_cov"
+ "motion_engine_ != nullptr"
+ "motion_engine_ret.imu_pose_refined.has_value()"
+ "motion_engine_ret.npdr_fast.has_value()"
+ "motion_engine_ret.npdr_refined.has_value()"
+ "new_kf_data_ptr->opt_old_to_second_rel_pose_cov"
+ "new_kf_data_ptr->vio_state.timestamp > latest_kf_data_ptr->vio_state.timestamp"
+ "next_npdr_state_iter->timestamp > vio_keyframe_timestamp"
+ "num_regular_states_to_remove < submap.NumberOfRegularStates()"
+ "occupancy.occupancy_grid_.rows() != 0 && occupancy.occupancy_grid_.columns() != 0"
+ "opt_last_npdr_kf_state"
+ "opt_last_slom_kf_info_"
+ "opt_last_slom_kf_info_->opt_npdr_state"
+ "opt_npdr_base_state_and_timestamp_"
+ "prev_npdr_state_iter != cached_npdr_state_vector_.end()"
+ "prev_npdr_state_iter->timestamp < vio_keyframe_timestamp"
+ "ptr > activity_period_queue_.begin()"
+ "ptr->confidence <= config_.walking_confidence_threshold"
+ "ptr_1->activity == repeated_event_for_removal_"
+ "ptr_2 >= activity_period_queue_.begin()"
+ "slom_kf_data_from_vio.front_end_kf_data->opt_rel_pose_info"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kLocalizedNonRemovableAreasDuration]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kMaxLocalizedNonRemovableAreasDuration]"
+ "std::isfinite(depth)"
+ "std::ranges::equal(offsetsMarg, intermediates.offsetsMarg)"
+ "std::ranges::equal(offsetsRed, intermediates.offsetsRed)"
+ "svk != nullptr"
+ "vio_pose_accumulator_info_.base_state_timestamp"
+ "vio_pose_accumulator_info_.prev_bundle_oldest_state_id_and_pose->first[1] == kf_data_ptr->opt_old_to_second_rel_pose_cov->state_id0"
+ "warning: acceleration too big for init."
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Util/include/SLOM/Util/SlomUtilities.h"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Util/src/SlomUtilities.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/OdometryKernels/src/Shims.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/include/VIO/Odometry/LowPowerEpipolarOutlierRejection.hpp"
- "IsParticleInBound(local_mask_size_, local_mask_size_, l0, l1)"
- "NR:AddNonRemovableAnchor: %s | %d"
- "NR:AreaInfo: Loc_area:%s Ext_area:%s"
- "NR:Downgrade: %s"
- "Near(sync_time, *last_input_time + input_imu_interval_, motion_engine::kTimeEps)"
- "Near(w_older + w_newer, 1.0, motion_engine::kTimeEps)"
- "Network type is not supported by IMULandmark interface"
- "[lpfg] successfuly initialized at %.g5\n"
- "kMaxNumberOfHypothesesLP >= config.ransac_max_num_hypotheses"
- "num_states_to_remove < submap.NumberOfRegularStates()"
- "opt_oldest_state_rel_pose_and_cov_->state_id0 == opt_last_create_map_keyframe_state_id->key()"
- "opt_oldest_state_rel_pose_and_cov_->state_id1 == oldest_state_id"
- "this->config_.epipolar_algorithm == EpipolarAlgorithm::TwoPoint"
- "warning: motion too big for initialization."

```
