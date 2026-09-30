## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-7.19.58.0.0
-  __TEXT.__text: 0x1c8236c
-  __TEXT.__auth_stubs: 0x3300
+7.25.50.0.0
+  __TEXT.__text: 0x1c88094
+  __TEXT.__auth_stubs: 0x32e0
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x1344
-  __TEXT.__cstring: 0x92c75
+  __TEXT.__cstring: 0x93461
   __TEXT.__const: 0x1492ab
-  __TEXT.__oslogstring: 0xd313
-  __TEXT.__gcc_except_tab: 0xfa528
-  __TEXT.__unwind_info: 0x3d9e0
+  __TEXT.__oslogstring: 0xd7a4
+  __TEXT.__gcc_except_tab: 0xfa7e4
+  __TEXT.__unwind_info: 0x3da18
   __TEXT.__eh_frame: 0x1004
   __TEXT.__objc_classname: 0x3ae
   __TEXT.__objc_methname: 0x1847

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4e8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x1990
-  __AUTH_CONST.__auth_ptr: 0x1f0
-  __AUTH_CONST.__const: 0x729b8
+  __AUTH_CONST.__auth_got: 0x1980
+  __AUTH_CONST.__auth_ptr: 0x1f8
+  __AUTH_CONST.__const: 0x72a98
   __AUTH_CONST.__cfstring: 0x5b40
   __AUTH_CONST.__objc_const: 0x5828
   __AUTH.__objc_data: 0x910
-  __AUTH.__data: 0x90
+  __AUTH.__data: 0x98
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30
   __DATA.__objc_ivar: 0x110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45260
-  Symbols:   1852
-  CStrings:  12918
+  Functions: 45290
+  Symbols:   1850
+  CStrings:  12954
 
Symbols:
+ _exit
- _cblas_dgemv$NEWLAPACK
- _cblas_dger$NEWLAPACK
- _cblas_sgemv$NEWLAPACK
CStrings:
+ " BLAS error: Parameter %!s(MISSING)"
+ " BLAS error: Parameter number %!l(MISSING)d"
+ " passed to %!s(MISSING) was %!l(MISSING)d, which is invalid.\n"
+ " readd_vairable: "
+ " reason_for_reinit_ts_queue_[i]: "
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Calibration/src/CameraToIMUTranslation.cpp"
+ "ACCEL MANY GOOD UPDATES - RESET CHI SQ MULT to 1, timestamp=%!l(MISSING)f"
+ "Accel Update Succeeded = %!d(MISSING) total accel updates= %!z(MISSING)u, at time: %!f(MISSING), RPY OUT: %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f, RPY Delta:  %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f, accel meas = %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f , accel rpy estimate = %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, gyro meas = %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f"
+ "Allow Travel mode hint in 3DoF mode."
+ "Chi SQ Check Failed!"
+ "Declaring moving platform due to frequent SLAM reinit event."
+ "ICDVS: Ignore hint. geo:%!d(MISSING), large-map:%!d(MISSING), 3DoF:%!d(MISSING)"
+ "Increase Chi-Sq Check for Quasi Static Update to %!l(MISSING)f "
+ "InitializeFromStatic at time: %!f(MISSING), RPY OUT: %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f, accel meas = %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f, accel rpy estimate = %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, gyro meas = %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f"
+ "MPC:Suppressed. Low light %!f(MISSING)"
+ "Max elapsed time for valid MCAM lux reading."
+ "Max time span to consider reinit to be recent."
+ "Min MCAM lux reading to use MPC."
+ "Min time enforced in between reinit events in second."
+ "Minimum number of recent reinit to classify hint."
+ "MovingIMUCameraDiscrepancyClassifierConfig.max_elapsed_time_for_valid_mcam_lux_in_sec"
+ "MovingIMUCameraDiscrepancyClassifierConfig.max_time_to_consider_reinit_recent_s"
+ "MovingIMUCameraDiscrepancyClassifierConfig.min_mcam_lux_to_use_mpc"
+ "MovingIMUCameraDiscrepancyClassifierConfig.min_num_recent_reinits_to_classify_hint"
+ "MovingIMUCameraDiscrepancyClassifierConfig.min_time_delta_between_reinits_s"
+ "MovingIMUCameraDiscrepancyClassifierConfig.reinit_timestamps_queue_size"
+ "Number of reinitialization timestamps to be kept in history."
+ "Query state does not exist in the database."
+ "ThreeDOFTracker: LATEST 6DOF SEED STATE timestamp/ YPR=  %!l(MISSING)f / %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, latest accel timestamp / meas = %!l(MISSING)f / %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, accel rpy estimate = %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, latest gyro timestamp/meas = %!l(MISSING)f / %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f"
+ "ThreeDOFTracker: LATEST 6DOF SEED STATE timestamp/ YPR=  %!l(MISSING)f / %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, no imu data"
+ "ThreeDOFTracker: RETURNED State (RollPitchYaw/pos) %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f at timestamp:%!l(MISSING)f, latest accel timestamp / meas = %!l(MISSING)f / %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, accel rpy estimate = %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f, latest gyro timestamp/meas = %!l(MISSING)f / %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f"
+ "Trying to add an anchor to SLAM with an invalid rotation"
+ "Trying to add an anchor to SLAM with invalid rotation elements"
+ "Trying to add an anchor to SLAM with invalid translation elements"
+ "cblas_dger"
+ "filter is recovered from large initial roll pitch errorsRPY %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f -> %!l(MISSING)f, %!l(MISSING)f, %!l(MISSING)f "
+ "latest_reinit_ts > reason_for_reinit_ts_queue_[i]"
+ "latest_reinit_ts: "
+ "readded_variable"
+ "same rotation update is triggered"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/ComputerVisionTypes/src/PlatformType.cpp"
- "Airplane"
- "Boat"
- "Bus"
- "Car"
- "ICDVS: Ignore hint. geo:%!d(MISSING), large-map:%!d(MISSING)"
- "Map spread %!f(MISSING)"
- "Maximum submaps center to consider the map as maybe-created in a movable platform."
- "MovablePlatformMapDescriminatorConfig parameters"
- "MovablePlatformMapDescriminatorConfig.maximum_submaps_center_for_movable_platform_map_in_m"
- "MovingIMUCameraDiscrepancyClassifierConfig.immediatly_allow_travel_mode_hint_in_3dof"
- "NotMovable"
- "ThreeDOFTracker: RETURNED State (RollPitchYaw/pos) %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f %!l(MISSING)f at timestamp:%!l(MISSING)f"
- "Train"
- "opt_spread_from_center.has_value()"

```
