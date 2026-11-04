## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-575.0.10.0.0
-  __TEXT.__text: 0x5980f4
-  __TEXT.__auth_stubs: 0x35b0
-  __TEXT.__objc_stubs: 0x18480
-  __TEXT.__init_offsets: 0x704
-  __TEXT.__objc_methlist: 0x10104
-  __TEXT.__gcc_except_tab: 0x5798c
-  __TEXT.__const: 0x3fc0d0
-  __TEXT.__cstring: 0x3a461
-  __TEXT.__objc_methname: 0x255e5
-  __TEXT.__oslogstring: 0x68acd
-  __TEXT.__objc_classname: 0x2386
-  __TEXT.__objc_methtype: 0x2445b
+578.0.3.0.0
+  __TEXT.__text: 0x59ed5c
+  __TEXT.__auth_stubs: 0x35c0
+  __TEXT.__objc_stubs: 0x19200
+  __TEXT.__init_offsets: 0x70c
+  __TEXT.__objc_methlist: 0x10a14
+  __TEXT.__gcc_except_tab: 0x585c8
+  __TEXT.__const: 0x3fc1a0
+  __TEXT.__cstring: 0x3a821
+  __TEXT.__objc_methname: 0x26ed5
+  __TEXT.__oslogstring: 0x691cd
+  __TEXT.__objc_classname: 0x2486
+  __TEXT.__objc_methtype: 0x2457b
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0xcec
   __TEXT.__swift5_capture: 0xc54

   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x234c8
+  __TEXT.__unwind_info: 0x23760
   __TEXT.__eh_frame: 0x728
-  __DATA_CONST.__const: 0x21668
-  __DATA_CONST.__cfstring: 0x17d60
-  __DATA_CONST.__objc_classlist: 0x690
+  __DATA_CONST.__const: 0x217d8
+  __DATA_CONST.__cfstring: 0x18320
+  __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x540
+  __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x490
   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_intobj: 0x978
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1af0
-  __DATA_CONST.__got: 0xf38
+  __DATA_CONST.__auth_got: 0x1af8
+  __DATA_CONST.__got: 0xf48
   __DATA_CONST.__auth_ptr: 0x408
-  __DATA.__objc_const: 0x1c948
-  __DATA.__objc_selrefs: 0x7588
-  __DATA.__objc_ivar: 0x1a94
-  __DATA.__objc_data: 0x5890
+  __DATA.__objc_const: 0x1de38
+  __DATA.__objc_selrefs: 0x79b0
+  __DATA.__objc_ivar: 0x1bf4
+  __DATA.__objc_data: 0x5b60
   __DATA.__data: 0x49dc
   __DATA.__common: 0xf98
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24820
-  Symbols:   1442
-  CStrings:  20598
+  Functions: 25041
+  Symbols:   1444
+  CStrings:  20955
 
Symbols:
+ _OBJC_CLASS_$_CLHarvester
+ _objc_retain_x6
CStrings:
+ "#PRRM,No capacity for a new GR session. GR jobs: %zu/%zu, UWB sessions: %zu/%zu"
+ "#nisessmgr,pid %d is gone with %lu live observer sessions. Force-invalidating."
+ "#nisessmgr,pid %d is gone with %lu live sessions. Force-invalidating."
+ "#nrby-eng,#proximityharvest,clock_check, stream,%s, t,%.3f, contNow,%.3f"
+ "#nrby-eng,#proximityharvest,configure, session,%s, configClass,%s, eligible,%d, internal,%d"
+ "#nrby-eng,accessory_motion, id,%s, moving,%d"
+ "#proximityharvest,config, max_harvests_per_day,%ld, source,%s"
+ "#proximityharvest,config, max_session_duration_s,%.1f, source,%s"
+ "#proximityharvest,serialize, error,%s"
+ "#proximityharvest,session_cleanup, id,%s, active,%lu, harvests_today,%lu"
+ "#proximityharvest,session_discarded, id,%s, daily_limit,%ld, dropped,%lu"
+ "#proximityharvest,session_dropped, id,%s, span_s,%.1f, threshold_s,%.1f, reason,exceeded_max_duration"
+ "#proximityharvest,session_end, id,%s, error,serialization_nil"
+ "#proximityharvest,session_end, id,%s, events,%lu, bytes,%lu, range,%lu, vio,%lu, io,%lu, accessory,%lu, pf,%lu, spliced,%lu, status,%s"
+ "#proximityharvest,session_end, id,%s, events,0, action,nothing_to_harvest"
+ "#proximityharvest,session_start, id,%s, active,%lu, source,%s"
+ "#ses-container,Failed to configure specialized session %@. Client is not entitled to camera assistance."
+ "#ses-container,getRangingAuthUWBInfo - all GR job slots are taken reporting UWB as unavailable"
+ "#ses-grResponder,Failed to allocate GR session, current count: %lu, reserved one when PAU is in progress and enabled, return"
+ "#ses-item-loc,Runaway item localizer backstop timeout override: %0.1f s"
+ "#ses-item-loc,Runaway item localizer backstop timer fired — force-invalidating session"
+ "#ses-loc,isBackgroundClient: %d"
+ "%@/%d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "5"
+ "@\"CLHarvester\""
+ "@\"NSUserDefaults\""
+ "B32@?0@\"NSDate\"8Q16^B24"
+ "B40@0:8@16@24d32"
+ "NIPeer"
+ "ProximityHarvestAccessoryMotion"
+ "ProximityHarvestCache"
+ "ProximityHarvestDailyTimestamps"
+ "ProximityHarvestFindingSolution"
+ "ProximityHarvestInertialOdometry"
+ "ProximityHarvestManager"
+ "ProximityHarvestMaxHarvestsPerDay"
+ "ProximityHarvestMaxSessionDurationSeconds"
+ "ProximityHarvestRangeMeasurement"
+ "ProximityHarvestSerializer"
+ "ProximityHarvestSplicedPose"
+ "ProximityHarvestVIOPose"
+ "Proximity_Harvest"
+ "Proximity_Harvest_Internal"
+ "RunawayItemLocalizerBackstopTimeoutOverrideSeconds"
+ "SystemCamera  "
+ "T@\"NSArray\",C,N,V_poseMatrix"
+ "T@\"NSArray\",C,N,V_quaternion"
+ "T@\"NSData\",R,N,V_lastSerializedHarvestForTesting"
+ "T@\"NSNumber\",C,N,V_azimuth_angle_rad"
+ "T@\"NSNumber\",C,N,V_deltaPosX"
+ "T@\"NSNumber\",C,N,V_deltaPosY"
+ "T@\"NSNumber\",C,N,V_deltaPosZ"
+ "T@\"NSNumber\",C,N,V_deltaVx"
+ "T@\"NSNumber\",C,N,V_deltaVy"
+ "T@\"NSNumber\",C,N,V_deltaVz"
+ "T@\"NSNumber\",C,N,V_elevation_angle_rad"
+ "T@\"NSNumber\",C,N,V_multipathProbability"
+ "T@\"NSNumber\",C,N,V_staticFlag"
+ "T@\"NSNumber\",C,N,V_sweepAngleDeg"
+ "T@\"NSNumber\",C,N,V_trackScore"
+ "T@\"NSString\",C,N,V_accessoryMake"
+ "T@\"NSString\",C,N,V_accessoryModel"
+ "T@\"NSString\",C,N,V_accessoryVersion"
+ "T@\"NSString\",C,N,V_pendingClientSource"
+ "T@\"NSString\",R,C,N,V_sessionIdentifier"
+ "T@\"NSUserDefaults\",&,N,V_persistenceStore"
+ "TB,N,V_directionAvailable"
+ "TB,N,V_insufficientDisplacement"
+ "TB,N,V_insufficientHorizontalDiversity"
+ "TB,N,V_insufficientVerticalDiversity"
+ "TB,N,V_majorRelocalization"
+ "TB,N,V_minorRelocalization"
+ "TB,N,V_vioDownsamplingEnabled"
+ "TQ,R,N"
+ "Td,N,V_lightEstimateLumens"
+ "Td,N,V_maxSessionDurationSeconds"
+ "Td,N,V_range_m"
+ "Td,R,N,V_firstEventTime"
+ "Tf,N,V_dirX"
+ "Tf,N,V_dirY"
+ "Tf,N,V_dirZ"
+ "Tf,N,V_horizontalAngleDeg"
+ "Tf,N,V_posX"
+ "Tf,N,V_posY"
+ "Tf,N,V_posZ"
+ "Tf,N,V_quatW"
+ "Tf,N,V_quatX"
+ "Tf,N,V_quatY"
+ "Tf,N,V_quatZ"
+ "Ti,N,V_algorithmSource"
+ "Ti,N,V_algorithmStatus"
+ "Ti,N,V_convergenceState"
+ "Ti,N,V_motionState"
+ "Ti,N,V_odometryAvailability"
+ "Ti,N,V_source"
+ "Ti,N,V_technology"
+ "Ti,N,V_trackingState"
+ "Tq,N,V_maxHarvestsPerDay"
+ "Tq,N,V_maximumAccessoryMotionCount"
+ "Tq,N,V_maximumFindingSolutionCount"
+ "Tq,N,V_maximumInertialOdometryCount"
+ "Tq,N,V_maximumRangeMeasurementCount"
+ "Tq,N,V_maximumSplicedPoseCount"
+ "Tq,N,V_maximumVIOPoseCount"
+ "UWBAccessory"
+ "[PRAppStateMonitor] pid %d initial combinedAppState %@. RunningBoard state: %@"
+ "_accessoryMake"
+ "_accessoryModel"
+ "_accessoryMotions"
+ "_accessoryVersion"
+ "_activeCaches"
+ "_algorithmStatus"
+ "_azimuth_angle_rad"
+ "_cancelRunawayBackstopTimer"
+ "_commitPendingNormalVIOForRangeTimestamp:"
+ "_commitVIOPose:"
+ "_convergenceState"
+ "_currentGRSessionCount"
+ "_deltaPosX"
+ "_deltaPosY"
+ "_deltaPosZ"
+ "_deltaVx"
+ "_deltaVy"
+ "_deltaVz"
+ "_didDropCacheIfMaxDurationReached:forSession:withTimestamp:"
+ "_dirX"
+ "_dirY"
+ "_dirZ"
+ "_directionAvailable"
+ "_elevation_angle_rad"
+ "_findingSolutions"
+ "_firstEventTime"
+ "_harvestClockLoggedMask"
+ "_harvestEligible"
+ "_harvestFeedInertialOdometry:source:"
+ "_harvestRegistered"
+ "_harvestTimestamps"
+ "_harvester"
+ "_horizontalAngleDeg"
+ "_inertialOdometries"
+ "_insufficientDisplacement"
+ "_insufficientHorizontalDiversity"
+ "_insufficientVerticalDiversity"
+ "_isRangingAuthClient"
+ "_lastHarvestedFindingSolutionTimestamp"
+ "_lastHarvestedSplicedTimestamp"
+ "_lastSerializedHarvestForTesting"
+ "_lastVIOCommitTimestamp"
+ "_lastVIOTrackingState"
+ "_lightEstimateLumens"
+ "_loadTimestampsPrunedToToday"
+ "_maxHarvestsPerDay"
+ "_maxSessionDurationSeconds"
+ "_maximumAccessoryMotionCount"
+ "_maximumFindingSolutionCount"
+ "_maximumInertialOdometryCount"
+ "_maximumRangeMeasurementCount"
+ "_maximumSplicedPoseCount"
+ "_maximumVIOPoseCount"
+ "_multipathProbability"
+ "_odometryAvailability"
+ "_pendingClientSource"
+ "_pendingNormalVIOs"
+ "_persistenceStore"
+ "_posX"
+ "_posY"
+ "_posZ"
+ "_poseMatrix"
+ "_proximityHarvestEndIfRegistered"
+ "_prunePendingNormalVIOs"
+ "_pruneTimestampsToTodayAndPersist"
+ "_quatW"
+ "_quatX"
+ "_quatY"
+ "_quatZ"
+ "_rangeMeasurements"
+ "_range_m"
+ "_runawayBackstopTimer"
+ "_source"
+ "_splicedPoses"
+ "_startRunawayBackstopTimer"
+ "_staticFlag"
+ "_sweepAngleDeg"
+ "_technology"
+ "_trackScore"
+ "_trimArray:toCapacity:"
+ "_vioDownsamplingEnabled"
+ "_vioPoses"
+ "accessory"
+ "accessoryMake"
+ "accessoryMeta"
+ "accessoryModel"
+ "accessoryMotions"
+ "accessoryVersion"
+ "activeCacheCountForTesting"
+ "addAccessoryMotion:"
+ "addAccessoryMotionWithTimestamp:motionState:forSession:"
+ "addFindingSolution:"
+ "addFindingSolutionWithTimestamp:dirX:dirY:dirZ:distance:horizontalAngleDeg:convergenceState:directionAvailable:algorithmSource:algorithmStatus:insufficientDisplacement:insufficientHorizontalDiversity:insufficientVerticalDiversity:insufficientLighting:forSession:"
+ "addInertialOdometry:"
+ "addInertialOdometryWithTimestamp:source:deltaPosX:deltaPosY:deltaPosZ:deltaVx:deltaVy:deltaVz:quaternion:staticFlag:forSession:"
+ "addRangeMeasurement:"
+ "addRangeMeasurementWithTimestamp:range_m:azimuthAngleRad:elevationAngleRad:technology:multipathProbability:trackScore:sweepAngleDeg:forSession:"
+ "addSplicedPose:"
+ "addSplicedPoseWithTimestamp:posX:posY:posZ:quatW:quatX:quatY:quatZ:odometryAvailability:trackingState:majorRelocalization:minorRelocalization:forSession:"
+ "addVIOPose:"
+ "addVIOPoseWithTimestamp:poseMatrix:trackingState:lightEstimateLumens:majorRelocalization:minorRelocalization:forSession:"
+ "algorithmStatus"
+ "algorithm_source"
+ "algorithm_status"
+ "allAccessoryMotions"
+ "allFindingSolutions"
+ "allInertialOdometries"
+ "allRangeMeasurements"
+ "allSplicedPoses"
+ "allVIOPoses"
+ "arrayForKey:"
+ "azimuth_angle_rad"
+ "btcs"
+ "com.apple.private.nearbyinteraction.system-camera-assistance"
+ "convergenceState"
+ "convergence_state"
+ "currentStateMatchingDescriptor:"
+ "default"
+ "deltaVx"
+ "deltaVy"
+ "deltaVz"
+ "dirX"
+ "dirY"
+ "dirZ"
+ "dir_x"
+ "dir_y"
+ "dir_z"
+ "directionAvailable"
+ "direction_available"
+ "elevation_angle_rad"
+ "findingSolutions"
+ "firstEventTime"
+ "harvest"
+ "hasReachedDailyHarvestLimit"
+ "horizontalAngleDeg"
+ "horizontal_angle_deg"
+ "indexesOfObjectsPassingTest:"
+ "initWithSessionIdentifier:"
+ "insufficientDisplacement"
+ "insufficientHorizontalDiversity"
+ "insufficientVerticalDiversity"
+ "insufficient_displacement"
+ "insufficient_horizontal_diversity"
+ "insufficient_lighting"
+ "insufficient_vertical_diversity"
+ "io"
+ "isDateInToday:"
+ "lastSerializedHarvestForTesting"
+ "lightEstimateLumens"
+ "major_relocalization"
+ "make"
+ "maxHarvestsPerDay"
+ "maxSessionDurationSeconds"
+ "maximumAccessoryMotionCount"
+ "maximumFindingSolutionCount"
+ "maximumInertialOdometryCount"
+ "maximumRangeMeasurementCount"
+ "maximumSplicedPoseCount"
+ "maximumVIOPoseCount"
+ "minor_relocalization"
+ "multipathProbability"
+ "multipath_probability"
+ "odometryAvailability"
+ "odometry_availability"
+ "ota"
+ "pendingClientSource"
+ "persistenceStore"
+ "posX"
+ "posY"
+ "posZ"
+ "pos_x"
+ "pos_y"
+ "pos_z"
+ "poseMatrix"
+ "quat_w"
+ "quat_x"
+ "quat_y"
+ "quat_z"
+ "rangeMeasurements"
+ "range_m"
+ "reloadDailyHarvestStateForTesting"
+ "removeObjectsAtIndexes:"
+ "resetDailyHarvestState"
+ "seedPersistedHarvestTimestampsForTesting:"
+ "serializeCache:"
+ "sessionDidEndForIdentifier:"
+ "sessionDidStartForIdentifier:clientSource:"
+ "setAccessoryMake:"
+ "setAccessoryMetadataForSession:make:model:version:"
+ "setAccessoryModel:"
+ "setAccessoryVersion:"
+ "setAlgorithmStatus:"
+ "setAzimuth_angle_rad:"
+ "setConvergenceState:"
+ "setDeltaVx:"
+ "setDeltaVy:"
+ "setDeltaVz:"
+ "setDirX:"
+ "setDirY:"
+ "setDirZ:"
+ "setDirectionAvailable:"
+ "setElevation_angle_rad:"
+ "setHorizontalAngleDeg:"
+ "setInsufficientDisplacement:"
+ "setInsufficientHorizontalDiversity:"
+ "setInsufficientVerticalDiversity:"
+ "setLightEstimateLumens:"
+ "setMajorRelocalization:"
+ "setMaxHarvestsPerDay:"
+ "setMaxSessionDurationSeconds:"
+ "setMaximumAccessoryMotionCount:"
+ "setMaximumFindingSolutionCount:"
+ "setMaximumInertialOdometryCount:"
+ "setMaximumRangeMeasurementCount:"
+ "setMaximumSplicedPoseCount:"
+ "setMaximumVIOPoseCount:"
+ "setMinorRelocalization:"
+ "setMultipathProbability:"
+ "setOdometryAvailability:"
+ "setPendingClientSource:"
+ "setPersistenceStore:"
+ "setPosX:"
+ "setPosY:"
+ "setPosZ:"
+ "setPoseMatrix:"
+ "setRange_m:"
+ "setSource:"
+ "setSweepAngleDeg:"
+ "setTechnology:"
+ "setTrackScore:"
+ "setTrackingState:"
+ "setVioDownsamplingEnabled:"
+ "skipped_no_receiver"
+ "splicedPoses"
+ "submitProximityHarvest:sessionIdentifier:"
+ "submitted"
+ "sweepAngleDeg"
+ "sweep_angle_deg"
+ "technology"
+ "totalEventCount"
+ "trackScore"
+ "track_score"
+ "tracking_state"
+ "v100@0:8d16i24@28@36@44@52@60@68@76@84@92"
+ "v28@0:8r^v16i24"
+ "v36@0:8d16i24@28"
+ "v60@0:8d16@24i32d36B44B48@52"
+ "v76@0:8d16f24f28f32f36f40f44f48i52i56B60B64@68"
+ "v84@0:8d16d24@32@40i48@52@60@68@76"
+ "v84@0:8d16f24f28f32f36f40i44B48i52i56B60B64B68B72@76"
+ "vioDownsamplingEnabled"
+ "{array<bool, 13UL>=\"__elems_\"[13B]}"
+ "\xf0\xf0\xa2"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "{array<bool, 12UL>=\"__elems_\"[12B]}"
- "\xf0\xf0r"
```
