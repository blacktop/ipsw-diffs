## AppleCV3D

> `/System/Library/PrivateFrameworks/AppleCV3D.framework/AppleCV3D`

```diff

-8.25.6.11.0
-  __TEXT.__text: 0x1f9576c
+8.25.6.25.1
+  __TEXT.__text: 0x1f8b178
   __TEXT.__auth_stubs: 0x3920
   __TEXT.__init_offsets: 0x8
-  __TEXT.__gcc_except_tab: 0x10ce54
-  __TEXT.__const: 0x16b3bc
-  __TEXT.__cstring: 0xa6519
-  __TEXT.__oslogstring: 0x11895
-  __TEXT.__unwind_info: 0x3ea98
+  __TEXT.__gcc_except_tab: 0x10d2fc
+  __TEXT.__const: 0x16b73c
+  __TEXT.__cstring: 0xa74e1
+  __TEXT.__oslogstring: 0x11b2a
+  __TEXT.__unwind_info: 0x3eb10
   __TEXT.__eh_frame: 0x2328
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x74f
   __TEXT.__objc_stubs: 0xba0
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0x3318
+  __DATA_CONST.__const: 0x3330
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e8
   __AUTH_CONST.__auth_got: 0x1ca0
-  __AUTH_CONST.__const: 0x7ac38
+  __AUTH_CONST.__const: 0x7ac88
   __AUTH_CONST.__cfstring: 0x1980
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x30
-  __DATA.__data: 0x8868
+  __DATA.__data: 0x88c8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x11d88
-  __DATA.__common: 0x2060
+  __DATA.__bss: 0x11e88
+  __DATA.__common: 0x2138
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3F450E4-7E5C-3518-A410-175BF43BDFB3
-  Functions: 47782
+  UUID: D0475B46-AA0F-356B-864C-3AF31DED8DF2
+  Functions: 47841
   Symbols:   2056
-  CStrings:  14626
+  CStrings:  14694
 
CStrings:
+ ", index2: "
+ ". frame_id: "
+ ". match index1: "
+ ". next_track_index: "
+ ". stream_id: "
+ ". track_index: "
+ "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/EstimatorKernels/include/VIO/EstimatorKernels/ComputePose.h"
+ "Active group changing from %s to %s"
+ "Anchors: Can't add a shared or NR anchor in 3DOF with id %{public}s..."
+ "Anchors: Trying to add NR anchor %{public}s from group %s when only group %s is allowed"
+ "Anchors: unable to save NRAnchor %{public}s"
+ "Anchors:Error:Failed to add anchor %{public}s as it was a duplicate"
+ "Anchors:Error:Failed to add anchor %{public}s as there were too many anchors"
+ "Anchors:Msg:Anchor added to the map with ID: %{public}s... and group: %s and has a pose %d and a type %u"
+ "Anchors:NR_anchor_ID: %{public}s added with KF_anchor_ID: %{public}s exist: %d"
+ "Anchors:NR_anchor_ID: %{public}s updated with KF_anchor_ID: %{public}s"
+ "Anchors:NR_anchor_ID: %{public}s... is external | with area_id:%{public}s"
+ "Anchors:RA: Removed anchor with ID %{public}s because %{public}s"
+ "BAFilterConfig.marginalize_only_when_window_sliding"
+ "DeleteBadlyTrackedSubmaps"
+ "DeleteCorruptedStates"
+ "Do marginalization only when the window actuall slides. Enabling this skips marginalization in the first five steps."
+ "Gyroscope bias in rad/sec."
+ "IMUSync"
+ "InsufficientMotion"
+ "Invalid feature_container provided"
+ "MapKeyframe:R:%u|W:%u|S:%u"
+ "MappingIO.Interface.output_mapping_io_analytics_path"
+ "MappingIOInterface::SaveAllToDisk() %f ms of queue size: %zu | context: %{public}s"
+ "MappingIOLoad:LocationArrived|boot:%d|Core| %f [s]"
+ "MappingIOLoad:LocationArrived|boot:%d|Default| %f [s]"
+ "MappingIOLoad:MapLoadingPriorityBump| %f [s]"
+ "MappingIOLoad:MapLoading|boot:%d|Core| %f [s]"
+ "MappingIOPruneErr:Type:ALLOC"
+ "MappingIOPruneErr:Type:FS"
+ "MappingIOPruneErr:Type:RT"
+ "MappingIOSave:NRArrival|sm:%llu|nrarea:%{public}s|created:%llu"
+ "MappingIOSave:NRDuration| %f [s]"
+ "NR:AddNonRemovableAnchor: %{public}s | %d"
+ "NR:AreaInfo: Loc_area:%{public}s Ext_area:%{public}s"
+ "NR:Downgrade|%s: %{public}s"
+ "NR:LocalizedDuration|avg: %f| max: %f"
+ "Odometry"
+ "Output path for mapping IO analytics."
+ "OutsideLimit"
+ "ReceiveSaveBundle|immediate:"
+ "SLAMLinesMLTask"
+ "Solve"
+ "Threshold for cumulative angular velocity norm (in rad/sec) to consider motion significant enough to trigger algorithm."
+ "VerifyAndDeleteCorruptedExternalSubmaps"
+ "Whether to enable or disable running the Lines ML Graphs in Polaris. Disabled by default on visionOS."
+ "Wrong marginalized indices."
+ "Wrong reduced indices."
+ "[lpsba] batched marginalization reduced order: %s (size %u)\n"
+ "[lpsba] estimator kernel marginalization: reducedDoF: %u, norm2: %g, nnz: %u, diag30: %s\n"
+ "[lpsba] marginalization from last frame: reduced order: %s (size %u)\n"
+ "[lpsba] marginalization from last frame: reducedDoF: %u, norm2: %g, nnz: %u, diag30: %s\n"
+ "[lpsba] marginalization from last frame: target order: %s (size %u)\n"
+ "[lpsba] marginalization injected prior: %u x %u norm2: %g, nnz: %u, diag30: %s\n"
+ "[lpsba] successfuly initialized at %.5g\n"
+ "enable_lines_ml_model"
+ "epipolar_algorithm == EpipolarAlgorithm::TwoPoint"
+ "feature_container"
+ "gyro_bias"
+ "lines_ml_output"
+ "num_regular_states_to_remove < submap.NumberOfRegularStates()"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::applecv3d::slam::LinesMLData]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::applecv3d::slam::OpaqueTypeWithSessionID<cv3d::applecv3d::slam::LinesMLData>]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kCoreLocationArrivalDurationAfterBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kCoreLocationArrivalDurationFromBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kDefaultLocationArrivalDurationAfterBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kDefaultLocationArrivalDurationFromBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kMapLoadingLatencyFromCoreLocatedMapAfterBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kMapLoadingLatencyFromCoreLocatedMapFromBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kMapLoadingLatencyFromDefaultLocatedMapAfterBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kMapLoadingLatencyFromDefaultLocatedMapFromBoot]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kMapLoadingLatencyWithPriorityBump]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kNRAnchorSaveDuration]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_io::MappingIOAnalyticsMetricName::kSubmapsSaveDuration]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kLocalizedNonRemovableAreasDuration]"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = cv3d::vio::mapping_types::MapAnalyticsMetricName::kMaxLocalizedNonRemovableAreasDuration]"
+ "std::ranges::equal(offsetsMarg, intermediates.offsetsMarg)"
+ "std::ranges::equal(offsetsRed, intermediates.offsetsRed)"
+ "sufficient_cumulative_angular_motion_threshold_rad_per_sec"
+ "svk != nullptr"
+ "warning: acceleration too big for init."
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/OdometryKernels/src/Shims.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D/library/VIO/Odometry/include/VIO/Odometry/LowPowerEpipolarOutlierRejection.hpp"
- "ALLOC"
- "Active group changing from "
- "Anchors: Can't add a shared or NR anchor in 3DOF with id %s..."
- "Anchors: Trying to add NR anchor %s from group %s when only group %s is allowed"
- "Anchors: unable to save NRAnchor %s"
- "Anchors:Error:Failed to add anchor %s as it was a duplicate"
- "Anchors:Error:Failed to add anchor %s as there were too many anchors"
- "Anchors:Msg:Anchor added to the map with ID: %s... and group: %s and has a pose %d and a type %u"
- "Anchors:NR_anchor_ID: %s added with KF_anchor_ID: %s exist: %d"
- "Anchors:NR_anchor_ID: %s updated with KF_anchor_ID: %s"
- "Anchors:RA: Removed anchor with ID %s because %s"
- "FS"
- "Force to immediate write submap save bundle to disk."
- "MappingIOInterface::SaveAllToDisk() %f ms of queue size: %zu | context: %s"
- "MappingIOPruneErr:Type:%s"
- "MappingManagerConfig.immediately_write_to_disk_on_submap_save_bundle"
- "NR:AddNonRemovableAnchor: %s | %d"
- "NR:AreaInfo: Loc_area:%s Ext_area:%s"
- "NR:Downgrade: %s"
- "RT"
- "ReceiveSaveBundle|immeidate:"
- "[LPS] too many camera models."
- "[lpfg] successfuly initialized at %.g5\n"
- "kMaxNumberOfHypothesesLP >= config.ransac_max_num_hypotheses"
- "num_states_to_remove < submap.NumberOfRegularStates()"
- "std::string_view lacc::function_name() [F = &RunBA]"
- "this->config_.epipolar_algorithm == EpipolarAlgorithm::TwoPoint"
- "warning: motion too big for initialization."

```
