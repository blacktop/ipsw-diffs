## CompanionCamera

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

```diff

-2021.200.3.0.0
-  __TEXT.__text: 0x7b9c
+2021.300.2.0.0
+  __TEXT.__text: 0x7d60
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x53c
+  __TEXT.__objc_methlist: 0x554
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x58
   __TEXT.__cstring: 0x7b5
-  __TEXT.__oslogstring: 0x3e9
+  __TEXT.__oslogstring: 0x3fd
   __TEXT.__unwind_info: 0x1c4
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methname: 0x152f
-  __TEXT.__objc_methtype: 0x4a0
-  __TEXT.__objc_stubs: 0x1300
+  __TEXT.__objc_methname: 0x1594
+  __TEXT.__objc_methtype: 0x4a1
+  __TEXT.__objc_stubs: 0x1360
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xce0
-  __DATA_CONST.__objc_selrefs: 0x5c8
-  __AUTH_CONST.__const: 0x300
+  __DATA_CONST.__objc_const: 0xd00
+  __DATA_CONST.__objc_selrefs: 0x5e8
+  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__cfstring: 0x420

   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 223
-  Symbols:   763
-  CStrings:  400
+  Functions: 227
+  Symbols:   775
+  CStrings:  404
 
Symbols:
+ -[CCCameraConnection _isSpatialCapture]
+ -[CCCameraConnection spatialModeDidChange]
+ ___26-[CCCameraConnection open]_block_invoke.86
+ ___42-[CCCameraConnection spatialModeDidChange]_block_invoke
+ ___42-[CCCameraConnection spatialModeDidChange]_block_invoke.cold.1
+ ___block_literal_global.102
+ ___block_literal_global.104
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.112
+ ___block_literal_global.114
+ ___block_literal_global.116
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.124
+ ___block_literal_global.126
+ ___block_literal_global.128
+ ___block_literal_global.130
+ ___block_literal_global.132
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.95
+ ___block_literal_global.97
+ ___block_literal_global.99
+ _objc_msgSend$_isSpatialCapture
+ _objc_msgSend$cameraConnectionIsSpatialCapture:
+ _objc_msgSend$xpc_spatialCaptureDidChange:
- ___26-[CCCameraConnection open]_block_invoke.84
- ___block_literal_global.101
- ___block_literal_global.103
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.129
- ___block_literal_global.90
- ___block_literal_global.92
- ___block_literal_global.94
- ___block_literal_global.96
- ___block_literal_global.98
CStrings:
+ "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBqB>20"
+ "_isSpatialCapture"
+ "cameraConnectionIsSpatialCapture:"
+ "spatialModeDidChange"
+ "supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnificationSupport:%d minimumZoomMagnification:%f maximumZoomMagnification:%f significantZoomMagnifications:%@ currentZoomMagnification:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d showingLivePreview:%d shallowDepthOfFieldStatus:%@ isSpatialCapture:%d"
+ "xpc_spatialCaptureDidChange:"
- "Vv28@0:8B16@?<v@?@\"NSOrderedSet\"q@\"NSOrderedSet\"qB@\"NSDate\"qBBfBff@\"NSArray\"fqqqqqqqqBBBq>20"
- "supportedCaptureDevices:%@ captureDevice:%@ supportedCaptureModes:%@ captureMode:%@ capturing:%d captureStartDate:%@ orientation:%@ toggleCameraDeviceSupport:%d zoomSupport:%d zoomAmount:%f zoomMagnificationSupport:%d minimumZoomMagnification:%f maximumZoomMagnification:%f significantZoomMagnifications:%@ currentZoomMagnification:%f flashSupport:%@ flashMode:%@ hdrSupport:%@ hdrMode:%@ irisSupport:%@ irisMode:%@ sharedLibrarySupport:%@ sharedLibraryMode:%@ supportsMomentCapture:%d burstSupport:%d showingLivePreview:%d shallowDepthOfFieldStatus:%@"

```
