## SLOM

> `/System/Library/PrivateFrameworks/SLOM.framework/SLOM`

```diff

-1.7.6.0.0
-  __TEXT.__text: 0x145acb8
+1.10.0.0.0
+  __TEXT.__text: 0x14bbbe8
   __TEXT.__auth_stubs: 0x2150
-  __TEXT.__const: 0xdfdb0
-  __TEXT.__gcc_except_tab: 0x8a1d0
-  __TEXT.__cstring: 0x4b8eb
+  __TEXT.__const: 0xe1910
+  __TEXT.__gcc_except_tab: 0x8bd2c
+  __TEXT.__cstring: 0x4cb6c
   __TEXT.__oslogstring: 0x3597
-  __TEXT.__unwind_info: 0x20b68
+  __TEXT.__unwind_info: 0x20e70
   __TEXT.__eh_frame: 0x1dc0
   __TEXT.__objc_methname: 0x24e
   __TEXT.__objc_stubs: 0x300

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc0
   __AUTH_CONST.__auth_got: 0x10b8
-  __AUTH_CONST.__const: 0x2f5f0
+  __AUTH_CONST.__const: 0x2fa00
   __AUTH_CONST.__cfstring: 0x100
   __AUTH.__data: 0x18
-  __DATA.__data: 0x86c8
+  __DATA.__data: 0x8588
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xc8a0
-  __DATA.__common: 0x1d60
+  __DATA.__bss: 0xede0
+  __DATA.__common: 0x1d58
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AAC8790F-ACA3-3C0A-A307-D3C61BC45EBF
-  Functions: 23664
-  Symbols:   682
-  CStrings:  6095
+  UUID: 36C77ABB-4527-3E39-B81B-ABEB573C0B65
+  Functions: 23790
+  Symbols:   681
+  CStrings:  6197
 
Symbols:
- _kSLOMConfigPresetOnlyOdometryLite
CStrings:
+ "\t\t\t         noise: {%.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g}\n"
+ "\t\t\tintrinsic %u [%u:%u]: mean: {%.5g, %.5g, %.5g, %.5g, %.5g, %.5g}, sigma: {%.5g, %.5g, %.5g, %.5g, %.5g, %.5g}\n"
+ "\t\t\tintrinsic %u [%u:%u]: mean: {%.5g, %.5g, %.5g, %.5g}, sigma: {%.5g, %.5g, %.5g, %.5g}\n"
+ "\t\t\tstate %u: mean: {%.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g, %.5g}\n"
+ "\t\textrinsicsCalibPriors: %u\n"
+ "\t\timuIntrinsicsCalibPriors: %u\n"
+ "\t\tinertial sensor: noise: {%.5g, %.5g, %.5g, %.5g}, gravity: {%.5g, %.5g, %.5g}, accel ts correction: %.5g\n"
+ "\t\tintrinsicsCalibPriors: %u\n"
+ "\t\tpoints: %u, depth(min: %.5g, mean: %.5g, max: %.5g) anchorDirection(mean: {%.5g, %.5g, %.5g}, denormalization: %.5g), %u were NaN\n"
+ "\t\tstate %u: IMU velocity: {%.5g, %.5g, %.5g}, accel bias: {%.5g, %.5g, %.5g}, gyro bias: {%.5g, %.5g, %.5g}\n"
+ "\t\tstateAndIMUTimeOffsetPriors: %u\n"
+ "\t\tstatePriors: %u\n"
+ "\t\tstationaryPriors: zeroVelocityInfo: %.5g zeroDisplacementInfo: %.5g\n"
+ "\t\tzeroDisplacementStates"
+ "\t\tzeroVelocityStates"
+ "\t%s: "
+ "\t%s: %u x %u %s, norm2: %.5g, %u nonzeros\n"
+ "\t%s: %u x %u %s, norm2: %.5g, %u nonzeros, %u upper, %u lower\n"
+ "\thaveInjectedCosts: %d haveInjectedHessian: %d (batched marginalization: %d injectedPrior: %d)\n\tfactors: %u landmark, %u map, %u IMU, %u preIMU\n\tinvalidateIMUCache: %d\n"
+ "\n\tbundle:"
+ "\n\tpriors:"
+ " is out of bounds for tracks vector size: "
+ "!data_->dense_point_cloud.contains(image_id)"
+ "!kMaxTracks || kMaxTracks >= max_observations"
+ "!kMaxTracks || kMaxTracks >= num_observations"
+ "', it already has an active configuration '"
+ "(config_.imu_filter_switch_config.enable_imu_filter_motion_switch && (config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode == RLSTrainingFilterModes::MotionIMUFilteringSmooth || check1 || check1b || check3)) || (!config_.imu_filter_switch_config.enable_imu_filter_motion_switch && config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode != RLSTrainingFilterModes::MotionIMUFilteringSmooth) || check2 || check2b || check4"
+ ", %u"
+ ", VIOIMUFactorBase imu data. "
+ ".architectra"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/Image.h:1193"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/Image.h:1199"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Architectra/src/ArchitectraInstance.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Architectra/src/MilBNNSArchitectraBackend.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/MotionEngine/src/MotionEngine.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/SlomMappingVIO/src/SlomMapDataController.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/SlomMappingVIO/src/SlomMapKeyframeGenerator.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/SlomMappingVIO/src/SlomMapManager.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/UtilVisualization/src/DrawingInterface.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/UtilVisualization/src/ImageFormatConverter.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/BundleSeeding.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/IMUSampleBuffer.h"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/include/VIO/Odometry/InMotionInitialization.h"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/include/VIO/Odometry/LowPowerEpipolarOutlierRejection.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/include/VIO/Odometry/OutlierRejectionUtil.hpp"
+ "20250408-architectra-v0.mlmodelc"
+ "BNNS graph compile error."
+ "Can't reconfigure VisualLogger with config '"
+ "Failed to execute MilBNNS Architectra."
+ "Failed to find the state"
+ "Filter must not be initialized yet."
+ "FlatWorld (%u B, overwrite guard: %s)\n\tsz: %u\n\tnt: %u\n\tnlt: %u\n\tnumExtrinsics: %u update: %d update-pos: %d\n\tnumIntrinsics: %u update: %d\n\tupdateIMUIntrinsics: %d haveVelocityAndBiases: %d\n\tconditioner: %.5g\n\tmaxUpdateMagnitudeSq: %.5g, maxTimeOffsetDelta: %.5g\n"
+ "ImageID does not belong to this mapdata"
+ "It's impossible to propagate the first frame."
+ "ItoC_iter != const_primary_submap().data()->viodatabase()->state_set()->endTransformItoC()"
+ "ItoC_iter->first == cv_types::CameraSourceID{0}"
+ "LPb"
+ "LPdelta"
+ "LPdeltaElim"
+ "LPhpp"
+ "LPrcs"
+ "LPrcsFactor"
+ "LPrhs"
+ "Map data must have a vio database"
+ "Mismatch in relative pose info"
+ "Model_output and sample should be non-empty and have same size"
+ "NPDR_refined is not assigned"
+ "Network type is not supported by our Architectra interface"
+ "Number of steps needs to be in [1, timesteps] and timesteps is dividable by it; For timesteps=1000, examples steps are 1, 5, 10, 20, 50, ..."
+ "Only single camera supported"
+ "Point-cloud is already in the map data"
+ "R_gyro_prev_to_cur_cam_frame_t.size() == camera_sensor_models[config_.primary_stereo_primary_stream_id.camera_id]->NumStreams()"
+ "Requested stream ID not found."
+ "Should have state"
+ "The IMU sample buffer cannot be empty!"
+ "The camera set features must exist for the already estimated state."
+ "Timestamp of the VIO point cloud and the last added keyframe must match"
+ "Timesteps should be at least 2."
+ "Variable prev_t must be within [0, timesteps_-1]"
+ "Variable t must be within [0, timesteps_-1]"
+ "[lpfg] successfuly initialized at %.g5\n"
+ "[lpsba] BA step: %s, cost before: %.3g, cost after: %.3g, costs before: %s, costs after: %s\n"
+ "[lpsba] Propagating %u of %u frames ...\n"
+ "[lpsba] assigned variable offsets (total DoF: %u): %s\n"
+ "[lpsba] prepared a full bundle with %u states (%s)\n"
+ "[lpsba] there are %u frames in window [%d @%.5f ... %d @%.5f]\n"
+ "[lpsba] use default prior: %s\n"
+ "`calibrated_to_distorted` must succeed."
+ "add_kf_output.new_base_state_id == kf_data.opt_rel_pose_info->state_id1"
+ "calibIMUIntrinsicsLeadingColumn"
+ "calibIntrinsicsLeadingColumn"
+ "calibPositionLeadingColumn"
+ "calibRotationLeadingColumn"
+ "camera_frame"
+ "config == active_config_.lock()"
+ "config_.imu_extrapolation_config.accel_filter_config.RLS_filter_mode != RLSTrainingFilterModes::WaveMotionAdaptive"
+ "config_.steps >= 1 && config_.steps <= timesteps_ && timesteps_ % config_.steps == 0"
+ "corrupt"
+ "cva::exactlyEqual(orig_timestamp, kf_timestamp)"
+ "did_update"
+ "explored_ratio"
+ "fail"
+ "image_id.view.uuid_hash() == data_->session_hash_"
+ "imu accels: "
+ "imu gyros: "
+ "imu timestamp: "
+ "imu_sample_buffer.NumBufferedIMUStates() >= bundle.num_states()"
+ "kMaxNumberOfHypothesesLP >= config.ransac_max_num_hypotheses"
+ "latest_neuralpdr_refined_"
+ "m_imuIntrinsicIDAtIndex"
+ "model_output.size() != 0 && sample.size() != 0 && model_output.size() == sample.size()"
+ "no"
+ "opt_oldest_state_rel_pose_and_cov_->state_id0 == opt_last_create_map_keyframe_state_id->key()"
+ "opt_oldest_state_rel_pose_and_cov_->state_id1 == oldest_state_id"
+ "opt_state_id"
+ "prev_t >= 0 && prev_t < timesteps_ - 1"
+ "statePositionLeadingColumn"
+ "stateRotationLeadingColumn"
+ "stateVelocityBiasLeadingColumn"
+ "t >= 0 && t < timesteps_ - 1"
+ "this->data_->viodatabase()"
+ "timeOffsetLeadingColumn"
+ "timesteps_ >= 2"
+ "track_slot < tracks.size()"
+ "track_slot: "
+ "warning: late motion too big for initialization."
+ "warning: motion too big for initialization."
+ "yes"
+ "{%u"
- "!kMaxObservations || kMaxObservations >= max_observations"
- "!kMaxObservations || kMaxObservations >= num_observations"
- "(config_.imu_filter_switch_config.enable_imu_filter_motion_switch && (config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode == RLSTrainingFilterModes::MotionIMUFilteringSmooth || check1 || check3)) || (!config_.imu_filter_switch_config.enable_imu_filter_motion_switch && config_.imu_extrapolation_config.gyro_filter_config.RLS_filter_mode != RLSTrainingFilterModes::MotionIMUFilteringSmooth) || check2 || check4"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/Image.h:1192"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/Image.h:1198"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/ImageView.h:1289"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/ImageView.h:1299"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/Kit/Image/include/Kit/Image/SharedImage.h:1236"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/MotionEngine/src/MotionEngineConfig.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Util/src/DrawingInterface.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/SLOM/Util/src/ImageFormatConverter.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/InitializationHelper.h"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/LPFGContainers.h"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/BatchLeastSquaresUnsanitized/src/IMUSampleBuffer.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/include_private/VIO/Odometry/InMotionInitialization.h"
- "/Library/Caches/com.apple.xbs/Sources/SLOM/library/VIO/Odometry/include_private/VIO/Odometry/OutlierRejectionUtil.hpp"
- "::"
- "Error the IMU sample buffer cannoty be empty!\n"
- "Filter must not be initialized yet"
- "Insufficient kMaxObservations."
- "Map Data must have a vio database."
- "R_gyro_prev_to_cur_cam_frame.size() == camera_sensor_models[config_.primary_stereo_primary_stream_id.camera_id]->NumStreams()"
- "The IMU sample buffer cannoty be empty!"
- "The camera set features must exist for the already estimated state"
- "Unsupported preset when constructing MotionEngineConfig."
- "inertial_measurements.NumFrames() == propagate_mask.size()"
- "initial_velocity_variance_imu.size() == cv_types::InertialCovariance::kVelocityDof"
- "map_data.viodatabase()"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UnknownPackage]"
- "std::fabs(anchor_direction().norm2() - 1) <= 1e-6"

```
