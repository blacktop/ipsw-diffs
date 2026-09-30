## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-8.25.5.28.1
-  __TEXT.__text: 0x1f4772c
-  __TEXT.__auth_stubs: 0x3910
+8.25.6.11.0
+  __TEXT.__text: 0x1f9576c
+  __TEXT.__auth_stubs: 0x3920
   __TEXT.__init_offsets: 0x8
-  __TEXT.__gcc_except_tab: 0x10b680
-  __TEXT.__const: 0x16aebc
-  __TEXT.__cstring: 0xa5751
-  __TEXT.__oslogstring: 0x117f0
-  __TEXT.__unwind_info: 0x3e8b8
+  __TEXT.__gcc_except_tab: 0x10ce54
+  __TEXT.__const: 0x16b3bc
+  __TEXT.__cstring: 0xa6519
+  __TEXT.__oslogstring: 0x11895
+  __TEXT.__unwind_info: 0x3ea98
   __TEXT.__eh_frame: 0x2328
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x74f
   __TEXT.__objc_stubs: 0xba0
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x3308
+  __DATA_CONST.__const: 0x3318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e8
-  __AUTH_CONST.__auth_got: 0x1c98
-  __AUTH_CONST.__const: 0x7a7f8
+  __AUTH_CONST.__auth_got: 0x1ca0
+  __AUTH_CONST.__const: 0x7ac38
   __AUTH_CONST.__cfstring: 0x1980
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30
-  __DATA.__data: 0x8a68
+  __DATA.__data: 0x8868
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x11d08
-  __DATA.__common: 0x2068
+  __DATA.__bss: 0x11d88
+  __DATA.__common: 0x2060
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 813BAE8D-D7E0-3F5A-AC7C-00F3CC2D49EB
-  Functions: 47686
-  Symbols:   2055
-  CStrings:  14547
+  UUID: A3F450E4-7E5C-3518-A410-175BF43BDFB3
+  Functions: 47782
+  Symbols:   2056
+  CStrings:  14626
 
Symbols:
+ _e5rt_e5_compiler_options_set_mil_entry_points
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
+ " is not compatible with "
+ " is out of bounds for tracks vector size: "
+ "!kMaxTracks || kMaxTracks >= max_observations"
+ "!kMaxTracks || kMaxTracks >= num_observations"
+ "', it already has an active configuration '"
+ ", %u"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/Image.h:1193"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/Image.h:1199"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/BundleSeeding.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/Triangulator.h"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/include/VIO/Odometry/InMotionInitialization.h"
+ "Accel: %d. Gyro: %d. Vision: %d (%d). Inlier fraction %f (%u/%u)\n\n"
+ "Can't reconfigure VisualLogger with config '"
+ "Flag to output front-end point cloud."
+ "FlatWorld (%u B, overwrite guard: %s)\n\tsz: %u\n\tnt: %u\n\tnlt: %u\n\tnumExtrinsics: %u update: %d update-pos: %d\n\tnumIntrinsics: %u update: %d\n\tupdateIMUIntrinsics: %d haveVelocityAndBiases: %d\n\tconditioner: %.5g\n\tmaxUpdateMagnitudeSq: %.5g, maxTimeOffsetDelta: %.5g\n"
+ "Invalid CameraStreamId (source ID: %u)."
+ "It's impossible to propagate the first frame."
+ "LPb"
+ "LPdelta"
+ "LPdeltaElim"
+ "LPhpp"
+ "LPrcs"
+ "LPrcsFactor"
+ "LPrhs"
+ "Local point cloud quality metric configuration (in degrees)."
+ "Minimum number of 2D3D inlier from 2nd estimater to consider it."
+ "Minimum number of points to output in OdometryMetadata."
+ "OdometryMetadataConfig"
+ "OdometryMetadataConfig.output_front_end_point_cloud"
+ "OdometryMetadataConfig.output_sliding_window_estimate_in_pose_metadata"
+ "OdometryMetadataConfig.point_cloud_quality_cos_thresh"
+ "OdometryMetadataConfig.point_cloud_quality_num_pts_thresh"
+ "Optionally output sliding-window estiamte in the OdometryMetadata."
+ "REPEATED_NR_ANCH:%u"
+ "Unable to set compiler options for compute device types mask: "
+ "Unable to set compiler options for mil entry points: "
+ "Updated relocalization type: %d to %d"
+ "VIOPoseMetadata has no camera_calibration_parameters (while processing source ID: %u). Will not warn again."
+ "VIO_OdometryEstimatorKernels.elf"
+ "[lpfg] successfuly initialized at %.g5\n"
+ "[lpsba] BA step: %s, cost before: %.3g, cost after: %.3g, costs before: %s, costs after: %s\n"
+ "[lpsba] Extracted %u tracks for camera %u (w/ %u streams) CameraIndex %u\n"
+ "[lpsba] Propagating %u of %u frames ...\n"
+ "[lpsba] Triangulated %u of %u tracks ...\n"
+ "[lpsba] assigned variable offsets (total DoF: %u): %s\n"
+ "[lpsba] prepared a full bundle with %u states (%s)\n"
+ "[lpsba] there are %u frames in window [%d @%.5f ... %d @%.5f]\n"
+ "[lpsba] use default prior: %s\n"
+ "calibIMUIntrinsicsLeadingColumn"
+ "calibIntrinsicsLeadingColumn"
+ "calibPositionLeadingColumn"
+ "calibRotationLeadingColumn"
+ "config == active_config_.lock()"
+ "corrupt"
+ "ext_nr_submap_iter != this->external_submaps_.end()"
+ "fail"
+ "imu_sample_buffer.NumBufferedIMUStates() >= bundle.num_states()"
+ "m_imuIntrinsicIDAtIndex"
+ "nfde_image"
+ "nfde_pred"
+ "statePositionLeadingColumn"
+ "stateRotationLeadingColumn"
+ "stateVelocityBiasLeadingColumn"
+ "std::isfinite(depth)"
+ "std::string_view lacc::function_name() [F = &RunBA]"
+ "timeOffsetLeadingColumn"
+ "track_slot < tracks.size()"
+ "track_slot: "
+ "warning: late motion too big for initialization."
+ "warning: motion too big for initialization."
+ "yes"
+ "{%u"
- " is not compatiable with "
- "!kMaxObservations || kMaxObservations >= max_observations"
- "!kMaxObservations || kMaxObservations >= num_observations"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/Image.h:1192"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/Image.h:1198"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/ImageView.h:1289"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/ImageView.h:1299"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/Kit/Image/include/Kit/Image/SharedImage.h:1236"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/BatchLeastSquaresUnsanitized/include/VIO/BatchLeastSquaresUnsanitized/InitializationHelper.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/include_private/VIO/Odometry/InMotionInitialization.h"
- "::"
- "Accel: %d. Gyro: %d. Vision: %d (%d). Inlier fraction %f (%zu/%zu)\n\n"
- "Got a CM data that was not meant for user anchors"
- "Insufficient kMaxObservations."
- "Invalid CameraStreamId (source ID: %d)"
- "Minimum number of 2D3D inilier from 2nd estimater to consider it."
- "Unable to set compiler options: "
- "inertial_measurements.NumFrames() == propagate_mask.size()"
- "initial_velocity_variance_imu.size() == cv_types::InertialCovariance::kVelocityDof"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::kit::viz::UnknownPackage]"

```
