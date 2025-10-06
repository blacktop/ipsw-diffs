## CoreOC

> `/System/Library/PrivateFrameworks/CoreOC.framework/CoreOC`

```diff

-9.7.4.0.0
-  __TEXT.__text: 0xdf360
-  __TEXT.__auth_stubs: 0x28b0
+9.8.1.0.0
+  __TEXT.__text: 0xe9e20
+  __TEXT.__auth_stubs: 0x2920
   __TEXT.__objc_methlist: 0x214
-  __TEXT.__const: 0x3108
-  __TEXT.__swift5_typeref: 0x1ebd
-  __TEXT.__cstring: 0xff35
-  __TEXT.__constg_swiftt: 0x3584
-  __TEXT.__swift5_reflstr: 0x329c
-  __TEXT.__swift5_fieldmd: 0x2824
-  __TEXT.__swift5_types: 0x2c8
-  __TEXT.__swift5_builtin: 0x230
-  __TEXT.__swift5_capture: 0x98c
+  __TEXT.__const: 0x3378
+  __TEXT.__swift5_typeref: 0x1f25
+  __TEXT.__cstring: 0x103f5
+  __TEXT.__constg_swiftt: 0x3708
+  __TEXT.__swift5_reflstr: 0x34ec
+  __TEXT.__swift5_fieldmd: 0x2a2c
+  __TEXT.__swift5_types: 0x2f0
+  __TEXT.__swift5_builtin: 0x2e4
+  __TEXT.__swift5_capture: 0x9ac
   __TEXT.__swift5_assocty: 0x240
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_proto: 0x174
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1e78
-  __TEXT.__eh_frame: 0x1060
+  __TEXT.__unwind_info: 0x1f18
+  __TEXT.__eh_frame: 0x1058
   __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methname: 0x5db7
+  __TEXT.__objc_methname: 0x5e09
   __TEXT.__objc_methtype: 0x27dc
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x3d8
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9540
+  __DATA_CONST.__objc_const: 0x9580
   __DATA_CONST.__objc_selrefs: 0x750
-  __AUTH_CONST.__const: 0x4d70
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __AUTH_CONST.__const: 0x51e0
   __AUTH_CONST.__objc_const: 0xd0
-  __AUTH_CONST.__auth_got: 0x1458
+  __AUTH_CONST.__auth_got: 0x1490
   __AUTH.__data: 0x3628
-  __AUTH.__objc_data: 0x11d8
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0xf8
-  __DATA.__data: 0x1350
-  __DATA.__bss: 0x2ef8
-  __DATA.__common: 0x168
+  __AUTH.__objc_data: 0x1218
+  __DATA.__data: 0x14d0
+  __DATA.__bss: 0x3098
+  __DATA.__common: 0x158
   - /System/Library/Frameworks/ARKit.framework/ARKit
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F712ACE0-5FD2-3680-A49B-2720699DB451
-  Functions: 3396
-  Symbols:   526
-  CStrings:  2269
+  UUID: DE172EEB-86D2-3D9B-8CC1-382EC33CC2F2
+  Functions: 3497
+  Symbols:   530
+  CStrings:  2295
 
Symbols:
+ _exp2f
+ _objc_retain_x2
+ _swift_setDeallocating
+ _swift_unknownObjectRetain_n
CStrings:
+ ".voxelhashing.surfacesampling.random_offset_stddev"
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "ObjectCaptureSession.%{private}s: Camera to tap point distance = %{public}fm"
+ "ObjectCaptureSession.%{private}s: Depth confidence threshold scene mode = %{public}f"
+ "ObjectCaptureSession.%{private}s: Failed to start voxel integration at tap point!"
+ "ObjectCaptureSession.%{private}s: Failed to start voxel integration at tap point, tap point in world is nil!"
+ "ObjectCaptureSession.%{private}s: Failed to start voxel integration at tap point, tap point is nil!"
+ "ObjectCaptureSession.%{private}s: Found a new plane under the object after it was removed. Setting should wait for plane = false."
+ "ObjectCaptureSession.%{private}s: Got new tap point, trying to restart voxel integration!"
+ "ObjectCaptureSession.%{private}s: New tap point is too close to the old tap point, not restarting voxel integration!"
+ "ObjectCaptureSession.%{private}s: Plane under the object was removed, cloudn't find another plane close to the old plane. Setting should wait for plane = true."
+ "ObjectCaptureSession.%{private}s: Plane under the object was removed, looking for another plane close to the old plane."
+ "ObjectCaptureSession.%{private}s: Set tap position with image point %{public}s."
+ "ObjectCaptureSession.%{private}s: Successfully restarted voxel integration at tap point."
+ "ObjectCaptureSession.%{private}s: Updated plane with center %s"
+ "ObjectCaptureSession.%{private}s: Voxel dimension scene mode = %{public}fm"
+ "ObjectCaptureSession.%{private}s: Voxel integration is paused till a new plane under the object is available"
+ "ObjectCaptureSession.%{public}s: AutomaticCapture: Take first shot fail!"
+ "ObjectCaptureSession.%{public}s: AutomaticCapture: Take first shot success."
+ "ObjectCaptureSession.%{public}s: BBox and motion manager init take time = %{public}s ms"
+ "ObjectCaptureSession.%{public}s: Called startCapturing() with boundingBox = %{public}s and options = %{public}s"
+ "ObjectCaptureSession.%{public}s: Camera active max exposure duration successfully set to %{public}f seconds"
+ "ObjectCaptureSession.%{public}s: Camera active max exposure duration un-specified, use auto exposure control."
+ "ObjectCaptureSession.%{public}s: Camera auto white balance is locked."
+ "ObjectCaptureSession.%{public}s: Camera control init takes time = %{public}s ms"
+ "ObjectCaptureSession.%{public}s: Camera face driven AF and AE disabled = %{bool,public}d"
+ "ObjectCaptureSession.%{public}s: Depth confidence threshold scanning mode = %{public}f"
+ "ObjectCaptureSession.%{public}s: Failed to start voxel integration!"
+ "ObjectCaptureSession.%{public}s: Init CaptureManager and takes first shot take time = %{public}s ms"
+ "ObjectCaptureSession.%{public}s: Init PGManager if needed takes time = %{public}s ms"
+ "ObjectCaptureSession.%{public}s: Plane filtering is not supported when calling startCapturing from .ready state!"
+ "ObjectCaptureSession.%{public}s: Start capturing expected the state to be .detecting or .ready but got %{public}s.\nNot starting capture!"
+ "ObjectCaptureSession.%{public}s: Voxel integration restart takes time = %{public}s ms"
+ "ObjectCaptureSession.%{public}s: self.arSession.configuration should be non-nil."
+ "ObjectCaptureSession.%{public}s: self.boundingBox should be non-nil."
+ "ObjectCaptureSession.%{public}s: self.referenceTimestamp should be non-nil."
+ "ObjectCaptureSession.%{public}s: startCapturing without boundingBox has not been implemented!"
+ "ObjectCaptureSession.%{public}s: startCapturing() takes time = %{public}s ms"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "TB,?"
+ "TB,?,R,GisClampToHalfBorderSupported"
+ "TB,?,R,GisCustomBorderColorSupported"
+ "TB,?,R,GisQuadDataSharingSupported"
+ "TB,?,R,GisRGB10A2GammaSupported"
+ "TQ,?,R"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "captureOptions"
+ "com.apple.coreoc.coreocmodules"
+ "imageHeightFromLastFrame"
+ "intrinsicsFromLastFrame"
+ "invalid Collection: less than 'count' elements in collection"
+ "logIfDifferent(newPlane:oldPlane:)"
+ "nearestPlaneBelow(tapPosition:)"
+ "proxySurfaceConfig"
+ "proxySurfaceConfigObject(boundingBoxExtent:depthConfidenceThreshold:isCoverageEnabled:isToFSensorTypePeridot:)"
+ "proxySurfaceConfigScene(scanOriginInWorld:voxelDimension:depthConfidenceThreshold:)"
+ "shouldRestartVoxelIntegration"
+ "startCapturing(inside:with:)"
+ "supportsArgumentBuffers"
+ "supportsResourceHeaps"
+ "tryRestartingVoxelIntegrationAtTapPoint(_:)"
+ "voxelHashingRestartTime"
- "\ncom.apple.coreoc.mobilesfm: "
- "\ncom.apple.coreoc.motionblur.depth.filter_point_cloud: "
- "\ncom.apple.coreoc.ocbundle.disable: "
- "\ncom.apple.coreoc.pip.mobilesfm_point_cloud: "
- "\ncom.apple.coreoc.tjf: "
- "ObjectCaptureSession.%{private}s: AutomaticCapture: Take first shot fail!"
- "ObjectCaptureSession.%{private}s: AutomaticCapture: Take first shot success."
- "ObjectCaptureSession.%{private}s: BBox and motion manager init take time = %{public}s ms"
- "ObjectCaptureSession.%{private}s: Called startCapturing() with boundingBox = %{public}s"
- "ObjectCaptureSession.%{private}s: Camera active max exposure duration successfully set to %{public}f seconds"
- "ObjectCaptureSession.%{private}s: Camera active max exposure duration un-specified, use auto exposure control."
- "ObjectCaptureSession.%{private}s: Camera auto white balance is locked."
- "ObjectCaptureSession.%{private}s: Camera control init takes time = %{public}s ms"
- "ObjectCaptureSession.%{private}s: Camera face driven AF and AE disabled = %{bool,public}d"
- "ObjectCaptureSession.%{private}s: Failed to compute nearest plane below tap position because tap position is nil!"
- "ObjectCaptureSession.%{private}s: Failed to recompute a new plane under the object after it was removed by ARKit!"
- "ObjectCaptureSession.%{private}s: Failed to start voxel integration at anchor point!"
- "ObjectCaptureSession.%{private}s: Failed to start, tapPosition is nil!"
- "ObjectCaptureSession.%{private}s: Failed to start, tapPositionWorld is nil!"
- "ObjectCaptureSession.%{private}s: Init CaptureManager and takes first shot take time = %{public}s ms"
- "ObjectCaptureSession.%{private}s: Init PGManager if needed takes time = %{public}s ms"
- "ObjectCaptureSession.%{private}s: Plane is nil after update and cloudn't find another plane close to old plane. Setting should wait for plane = true"
- "ObjectCaptureSession.%{private}s: Plane is nil after update, found another plane close to the old plane."
- "ObjectCaptureSession.%{private}s: Selected the plane with center x=%{public}f, y=%{public}f as the nearest plane below the world tap point x=%{public}f, y=%{public}f, z=%{public}f"
- "ObjectCaptureSession.%{private}s: Set default bounding box around tapPosition."
- "ObjectCaptureSession.%{private}s: Set should wait for new plane = true."
- "ObjectCaptureSession.%{private}s: Set shouldWaitForNewPlane = false"
- "ObjectCaptureSession.%{private}s: Set tap position."
- "ObjectCaptureSession.%{private}s: Set voxel integration depth confidence threshold = %{public}f"
- "ObjectCaptureSession.%{private}s: Successfully restarted voxel integration at anchor point."
- "ObjectCaptureSession.%{private}s: Voxel integration restart takes time = %{public}s ms"
- "ObjectCaptureSession.%{private}s: anchors): ARKit removed the plane under the object!"
- "ObjectCaptureSession.%{private}s: anchors): Found another plane close to the old plane."
- "ObjectCaptureSession.%{private}s: self.arSession.configuration should be non-nil."
- "ObjectCaptureSession.%{private}s: self.referenceTimestamp should be non-nil."
- "ObjectCaptureSession.%{private}s: startCapturing without boundingBox has not been implemented!"
- "ObjectCaptureSession.%{private}s: startCapturing() takes time = %{public}s ms"
- "TB"
- "TB,R,GisClampToHalfBorderSupported"
- "TB,R,GisCustomBorderColorSupported"
- "TB,R,GisQuadDataSharingSupported"
- "TB,R,GisRGB10A2GammaSupported"
- "adaptiveProxySurfaceConfigObject(boundingBoxExtent:isCoverageEnabled:isToFSensorTypePeridot:)"
- "boundingBoxFailCurCount"
- "boundingBoxFailMaxCount"
- "com.apple.coreoc.coreocmodules.voxelhashing.surfacesampling.random_offset_stddev"
- "consecutiveObjectFlippabilityCount"
- "defaultProxySurfaceConfigScene(scanOrigin:isToFSensorTypePeridot:)"
- "minConsecutiveObjectFlippabilityCount"
- "minShotFlippableMapSize"
- "nearestPlaneBelowTapPosition()"
- "numInitialShotsBeforeFlippableDecision"
- "proxySurfaceInputType"
- "startCapturing(inside:)"
- "tryRestartingVoxelIntegrationAtAnchorPoint(_:)"

```
