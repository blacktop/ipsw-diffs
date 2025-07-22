## VisualMappingKit

> `/System/Library/PrivateFrameworks/VisualMappingKit.framework/VisualMappingKit`

```diff

-8.25.6.11.0
-  __TEXT.__text: 0x644ccc
-  __TEXT.__auth_stubs: 0x1db0
-  __TEXT.__const: 0x44f00
-  __TEXT.__cstring: 0x107ca
-  __TEXT.__oslogstring: 0x2d6
-  __TEXT.__gcc_except_tab: 0x4240c
-  __TEXT.__unwind_info: 0x11f50
+8.25.6.25.1
+  __TEXT.__text: 0x654d40
+  __TEXT.__auth_stubs: 0x1da0
+  __TEXT.__const: 0x45b10
+  __TEXT.__cstring: 0x10eb5
+  __TEXT.__oslogstring: 0x605
+  __TEXT.__gcc_except_tab: 0x43250
+  __TEXT.__unwind_info: 0x122a8
   __TEXT.__eh_frame: 0xcd4
   __TEXT.__objc_methname: 0x23
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xee8
-  __AUTH_CONST.__const: 0x1eb20
+  __AUTH_CONST.__auth_got: 0xee0
+  __AUTH_CONST.__const: 0x1f250
   __AUTH_CONST.__cfstring: 0x280
   __AUTH.__data: 0x18
-  __DATA.__data: 0x1cc8
+  __DATA.__data: 0x1ca0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xa68
+  __DATA.__bss: 0xad8
   __DATA.__common: 0x2e0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F94FD52-F806-38C9-84E0-17985FCE3D70
-  Functions: 11869
-  Symbols:   683
-  CStrings:  1731
+  UUID: 8FFCDE21-5C8D-3081-AD1F-D5976C04DF36
+  Functions: 12022
+  Symbols:   716
+  CStrings:  1787
 
Symbols:
+ _VMKAnchorCopyIdentifier
+ _VMKAnchorListCopyIdentifiers
+ _VMKDatabaseCopyDatabaseFrame
+ _VMKDatabaseCopyDatabaseFrameIdentifiers
+ _VMKDatabaseCreateDatabaseFrameWithIdentifier
+ _VMKDatabaseCreateDatabaseFrameWithIdentifierKeypointsAndDescriptors
+ _VMKDatabaseFrameCopyIdentifier
+ _VMKDatabaseRemoveDatabaseFrameWithIdentifier
+ _VMKHomeSlamColocationCoordinatesRelease
+ _VMKHomeSlamColocationCoordinatesRetain
+ _VMKHomeSlamColocationCopyCoordinatesIdentifier
+ _VMKHomeSlamColocationGetCoordinatesPosition
+ _VMKIdentifierCreate
+ _VMKIdentifierGetBytes
+ _VMKIdentifierListAppend
+ _VMKIdentifierListCopyIdentifierAt
+ _VMKIdentifierListCreate
+ _VMKIdentifierListRelease
+ _VMKIdentifierListRetain
+ _VMKIdentifierListSize
+ _VMKIdentifierRelease
+ _VMKIdentifierRetain
+ _VMKMappingResultCopyAddDatabaseFrameIdentifiers
+ _VMKMappingResultCopyRemoveDatabaseFrameIdentifiers
+ _VMKPoseEstimationResultCopyQueryIdentifier
+ _VMKPoseEstimationResultCreateWithIdentifier
+ _VMKRelativePoseEstimateCopyReferenceIdentifier
+ _VMKRelativePoseEstimateCreateWithIdentifier
+ _VMKSessionAddAnchorWithIdentifier
+ _VMKSessionAddHomeSlamColocationCoordinates
+ _VMKSessionCopyKeyframeIdentifiers
+ _VMKSessionRemoveAnchorWithIdentifier
+ _VMKSessionRemoveKeyframeWithIdentifier
+ _VMKSessionResetHomeSlamColocationCoordinates
+ _VMKVisualLogFrameWithIdentifier
+ __os_log_pack_fill
+ __os_log_pack_size
- __ZNSt3__14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
- __ZNSt9exceptionD1Ev
- __ZTVSt9exception
- ___cxa_get_exception_ptr
CStrings:
+ " (with port in [0,65535]) but is '"
+ " enableTelemetry=YES "
+ "%s: Config string contains more than one file path; first path: '%s'; following path '%s' ignored"
+ "%s: Config string contains more than one server address; first address: '%s'; following address '%s' ignored"
+ "%s: Enabling log contexts: %s"
+ "%s: Failed to start logging to file at '%s': %s"
+ "%s: Failed to start logging to file at '%s': another file exporter already exists at the same location"
+ "%s: Failed to start logging via network to server at '%s' : %s"
+ "%s: Invalid config string '%s': %s"
+ "%s: Not enabling any log contexts"
+ "%s: Not enabling any log contexts since logger has no destinations"
+ "%s: Starting logging to file at '%s'"
+ "%s: Starting logging via network to server at '%s'"
+ "%s: Stopping logging to file at '%s'"
+ "%s: Stopping logging via network"
+ "'host:port'"
+ "'host[:port]'"
+ ",;"
+ ": failed a TimeframeSync: "
+ "Adding colocation coordinates failed"
+ "Could not find keyframes for HomeSlam colocation check"
+ "Failed to add the camera variable: this should never happen."
+ "Resetting colocation coordinates failed"
+ "VMKDatabaseCreateDatabaseFrame"
+ "VMKDatabaseEstimateRelativePoses"
+ "config_.debug_config.loop_closure_constraint_type == RelativeCameraPoseConstraintType::CameraToCamera5DoFEpipolarCovariance || config_.debug_config.loop_closure_constraint_type == RelativeCameraPoseConstraintType::CameraToCamera5DoFHeuristicCovariance"
+ "cv3d.kit.viz"
+ "eig_values[0] <= eig_values[1]"
+ "eval.external_maps"
+ "eval.map"
+ "given tcp address must be of pattern "
+ "id_iter != state_id_to_variable_id_map_.end()"
+ "index < id_list->uuids.size()"
+ "internal_id"
+ "query_keyframe && candidate_keyframe"
+ "ref_image_id.source == vio::cv_types::CameraSourceID{0}"
+ "ref_keypoints_nsp.size() == num_points * 2"
+ "reloc_info"
+ "ret.second"
+ "session_id"
+ "unknown file"
+ "unknown function"
+ "vuelta::VueltaVisualLogging"
- "Database"
- "Vuelta"

```
