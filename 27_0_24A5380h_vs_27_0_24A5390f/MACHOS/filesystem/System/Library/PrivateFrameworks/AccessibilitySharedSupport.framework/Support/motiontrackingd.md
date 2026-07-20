## motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-581.0.0.0.0
-  __TEXT.__text: 0x2a924
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x71e0
-  __TEXT.__objc_methlist: 0x2f84
-  __TEXT.__const: 0x30c
+584.0.0.0.0
+  __TEXT.__text: 0x2b728
+  __TEXT.__auth_stubs: 0xa20
+  __TEXT.__objc_stubs: 0x74a0
+  __TEXT.__objc_methlist: 0x306c
+  __TEXT.__const: 0x3ec
   __TEXT.__dlopen_cstrs: 0x2ef
-  __TEXT.__gcc_except_tab: 0xa5c
-  __TEXT.__cstring: 0x2268
-  __TEXT.__oslogstring: 0x2455
-  __TEXT.__objc_methname: 0x9609
+  __TEXT.__gcc_except_tab: 0xa84
+  __TEXT.__cstring: 0x2278
+  __TEXT.__oslogstring: 0x267e
+  __TEXT.__objc_methname: 0x9a71
   __TEXT.__objc_classname: 0x56c
-  __TEXT.__objc_methtype: 0x1e4c
-  __TEXT.__unwind_info: 0x9f0
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__cfstring: 0x7a0
+  __TEXT.__objc_methtype: 0x1e73
+  __TEXT.__unwind_info: 0xa08
+  __DATA_CONST.__const: 0x998
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__auth_got: 0x520
   __DATA_CONST.__got: 0x420
-  __DATA.__objc_const: 0x4b58
-  __DATA.__objc_selrefs: 0x2120
-  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_const: 0x4cb8
+  __DATA.__objc_selrefs: 0x21d8
+  __DATA.__objc_ivar: 0x3f4
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x850
-  __DATA.__bss: 0x370
+  __DATA.__bss: 0x380
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1053
-  Symbols:   305
-  CStrings:  2221
+  Functions: 1074
+  Symbols:   307
+  CStrings:  2267
 
Symbols:
+ _AXSSDeviceIsViridian
+ _mach_timebase_info
CStrings:
+ "AXMTCameraBasedLookAtPointTracker: active display changed; updated mapper bounds to %@"
+ "AXMTFaceKitFaceTracker: alternate head-tracking seed locked after first successful result"
+ "AXMTVideoCapturer: alternate head-tracking could not set videoRotationAngle 0 (default %.0f) for %@"
+ "AXMTVideoCapturer: alternate head-tracking normalized videoRotationAngle %.0f -> %.0f for %@"
+ "AXMT[AltHeadTrackingPose] holding cursor: confidence %ld < %ld (acquiring)"
+ "AXMT[FaceKitQuality] ignoring low-confidence pose (confidenceLevel=%ld < %ld); unlocking seed to re-acquire"
+ "T@\"NSNumber\",&,N,V__altHeadTrackingLastPitch"
+ "T@\"NSNumber\",&,N,V__altHeadTrackingLastYaw"
+ "TB,N,V__altHeadTrackingSeedLocked"
+ "TQ,N,V__altHeadTrackingLastFrameMachTime"
+ "Tq,N,V__altHeadTrackingConfidenceLevel"
+ "Tq,N,V_confidenceLevel"
+ "T{CGPoint=dd},N,V__altHeadTrackingInterfacePoint"
+ "__altHeadTrackingConfidenceLevel"
+ "__altHeadTrackingInterfacePoint"
+ "__altHeadTrackingLastFrameMachTime"
+ "__altHeadTrackingLastPitch"
+ "__altHeadTrackingLastYaw"
+ "__altHeadTrackingSeedLocked"
+ "_altHeadTrackingConfidenceLevel"
+ "_altHeadTrackingInterfacePoint"
+ "_altHeadTrackingLastFrameMachTime"
+ "_altHeadTrackingLastPitch"
+ "_altHeadTrackingLastYaw"
+ "_altHeadTrackingSeedLocked"
+ "_confidenceLevel"
+ "_handleAltHeadTrackingDetectedFaceWithPose:"
+ "_makeFaceKitFaceTracker"
+ "_resetAltHeadTrackingPoseBaseline"
+ "altHeadTrackingOverride"
+ "confidenceLevel"
+ "confidence_level"
+ "isVideoRotationAngleSupported:"
+ "localizedName"
+ "session:didChangeViewRotationAngle:"
+ "setConfidenceLevel:"
+ "setVideoRotationAngle:"
+ "set_altHeadTrackingConfidenceLevel:"
+ "set_altHeadTrackingInterfacePoint:"
+ "set_altHeadTrackingLastFrameMachTime:"
+ "set_altHeadTrackingLastPitch:"
+ "set_altHeadTrackingLastYaw:"
+ "set_altHeadTrackingSeedLocked:"
+ "v32@0:8@\"ARSession\"16d24"
+ "v32@0:8@16d24"
+ "videoRotationAngle"
```
