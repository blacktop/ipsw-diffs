## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-8.25.6.25.1
-  __TEXT.__text: 0x1f8b178
-  __TEXT.__auth_stubs: 0x3920
+8.25.6.25.4
+  __TEXT.__text: 0x1f8847c
+  __TEXT.__auth_stubs: 0x3910
   __TEXT.__init_offsets: 0x8
-  __TEXT.__gcc_except_tab: 0x10d2fc
-  __TEXT.__const: 0x16b73c
-  __TEXT.__cstring: 0xa74e1
-  __TEXT.__oslogstring: 0x11b2a
-  __TEXT.__unwind_info: 0x3eb10
+  __TEXT.__gcc_except_tab: 0x10d494
+  __TEXT.__const: 0x16b8bc
+  __TEXT.__cstring: 0xa7d09
+  __TEXT.__oslogstring: 0x11b77
+  __TEXT.__unwind_info: 0x3eb60
   __TEXT.__eh_frame: 0x2328
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x74f
-  __TEXT.__objc_stubs: 0xba0
-  __DATA_CONST.__got: 0x5c8
+  __TEXT.__objc_methname: 0x713
+  __TEXT.__objc_stubs: 0xb60
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__const: 0x3330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e8
-  __AUTH_CONST.__auth_got: 0x1ca0
-  __AUTH_CONST.__const: 0x7ac88
+  __DATA_CONST.__objc_selrefs: 0x2d8
+  __AUTH_CONST.__auth_got: 0x1c98
+  __AUTH_CONST.__const: 0x7abf0
   __AUTH_CONST.__cfstring: 0x1980
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D0475B46-AA0F-356B-864C-3AF31DED8DF2
-  Functions: 47841
-  Symbols:   2056
-  CStrings:  14694
+  UUID: 4E49775A-E179-3831-8E58-E44353808A7C
+  Functions: 47836
+  Symbols:   2055
+  CStrings:  14721
 
Symbols:
+ _CV3DSLAMSessionSimulateLowFrequencyFlickerDetected
+ _CV3DSLAMStateIsLowFrequencyFlickerDetected
- _DRSubmitLogs
- _NSTemporaryDirectory
- _OBJC_CLASS_$_DRClientLog
CStrings:
+ "!optimized_key_submap_T_G_to_O.empty()"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/MappingTypes/src/CollaborativeMapping/UserOriginAnchorInfo.cpp"
+ "AdaptiveRatio parameters"
+ "AdaptiveRatioConfig.high_inlier_threshold"
+ "AdaptiveRatioConfig.log_input_offset"
+ "AdaptiveRatioConfig.log_input_scale"
+ "AdaptiveRatioConfig.log_output_offset"
+ "AdaptiveRatioConfig.log_scale_factor"
+ "AdaptiveRatioConfig.maximum_ratio"
+ "AdaptiveRatioConfig.minimum_input_value"
+ "AdaptiveRatioConfig.minimum_ratio"
+ "AdaptiveRatioConfig.ratio_lower_bound"
+ "CM:Merge: hot merge duration: %f s | user %llu | history: %d"
+ "CM:UserOrigin: reject merge user %llu with anchor %s"
+ "CMUA:Optimizer converged: %d"
+ "CMUA:Submap:%llu pos: %f,%f,%f"
+ "CameraAllocatorConfig.visual_slam_inlier_ratio_good_quality_threshold"
+ "Logarithmic input offset. This offset is added to the scaled input before taking the logarithm. It helps position the curve appropriately on the input domain."
+ "Logarithmic input scaling factor. This parameter scales the input (number of inliers) before applying the logarithmic transformation."
+ "Logarithmic output offset. This offset is added to the logarithmic result to position the curve appropriately on the output range."
+ "Logarithmic scaling factor for the adaptive curve. This parameter controls the steepness of the logarithmic curve. Negative values create a decreasing function as inliers increase."
+ "Lower bound for the ratio calculation (prevents negative values). The final calculated ratio is clamped to be at least this value, ensuring the output is always within a valid range."
+ "MPC freed."
+ "MPC re-allocated."
+ "Maximum ratio value returned when inliers are very low. This serves as an upper bound for the calculated ratio and is returned for zero inliers or when the logarithmic calculation would exceed this value."
+ "Minimum ratio value returned when inliers are above threshold. This is the constant value returned for high inlier counts (>= high_inlier_threshold)."
+ "Minimum valid input value (prevents invalid logarithm calculations). Input values below this threshold are clamped to this value to prevent invalid logarithm calculations (log of non-positive numbers)."
+ "MpcControllerDonResetMode"
+ "OutlierRejectionConfig.ransac_desired_confidence"
+ "PoseController(%s) device not worn"
+ "PoseController(%s) reset"
+ "PoseController(%s) temp disabled"
+ "The desired probability (confidence level) of finding at least one correct model hypothesis."
+ "Threshold above which the ratio becomes constant at minimum value. When the number of inliers is greater than or equal to this threshold, the function returns the minimum_ratio value."
+ "VisualSLAM minimum inlier ratio for primary stereo camera stability. Below this threshold, mono camera usage is increased to support SLAM."
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kDurationOfMergingCMUserWithHotMergeFromHistory]"
+ "this->primary_user_origin_anchor.UserSessionID() != cv_types::kInvalidUserSessionID"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Geometry/src/RANSAC/GeneralizedP3PPreemptiveRansac.cpp"
- "AutomaticDiagnostics"
- "CM:Merge: feasible hot merge duration: %f s | user %llu"
- "CM:Merge: hot merge duration: %f s | user %llu"
- "CM:UserOrigin: reject merge user %llu with anchor %s <-> %s"
- "Data Collection Diagnostics creation completed in %f ms"
- "DataCollectionDiagnostics-Automatic"
- "DataCollectionDiagnostics-Manual"
- "ManualDiagnostics"
- "arrayWithCapacity:"
- "config.automatic_data_prior_active_duration < config.automatic_data_minimum_duration && \"We need this property to guarantee that a dataset's recording is only initiated when \" \"there is enough budget left to accommodate the window of buffered data.\""
- "diagnostics"
- "initWithPath:transferOwnership:errorOut:"
- "session->mpc_algorithm_"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kDurationOfFeasibleMergingCMUserWithHotMerge]"

```
