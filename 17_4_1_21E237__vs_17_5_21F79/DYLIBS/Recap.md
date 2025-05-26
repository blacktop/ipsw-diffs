## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

```diff

-135.113.0.0.0
-  __TEXT.__text: 0x1e614
+135.116.0.0.0
+  __TEXT.__text: 0x1ee48
   __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x278c
-  __TEXT.__cstring: 0x1748
-  __TEXT.__const: 0x294
+  __TEXT.__objc_methlist: 0x27d4
+  __TEXT.__cstring: 0x189c
+  __TEXT.__const: 0x2a4
   __TEXT.__oslogstring: 0x37f
   __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x8cc
+  __TEXT.__unwind_info: 0x904
   __TEXT.__objc_classname: 0x658
-  __TEXT.__objc_methname: 0x7205
-  __TEXT.__objc_methtype: 0x15f0
-  __TEXT.__objc_stubs: 0x5180
+  __TEXT.__objc_methname: 0x73cf
+  __TEXT.__objc_methtype: 0x1660
+  __TEXT.__objc_stubs: 0x51e0
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x510
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5118
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_const: 0x51b8
+  __DATA_CONST.__objc_selrefs: 0x1b78
   __DATA_CONST.__objc_classrefs: 0x278
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x448
-  __AUTH_CONST.__cfstring: 0x1d80
+  __AUTH_CONST.__cfstring: 0x1dc0
   __AUTH_CONST.__objc_const: 0x1090
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x700
-  __AUTH.__objc_data: 0x8e8
+  __AUTH.__objc_data: 0x8c0
   __DATA.__objc_ivar: 0x37c
   __DATA.__data: 0x968
   __DATA.__bss: 0x168
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0x438
+  __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 919
-  Symbols:   3635
-  CStrings:  1929
+  Functions: 925
+  Symbols:   3650
+  CStrings:  1946
 
Symbols:
+ -[RCPSyntheticEventStream _squeezeWithPhase:withPage:withUsage:withVersion:withStage:withTransition:withNextThreshold:withPressedThreshold:withReleasedThreshold:withNormalizedForce:withNormalizedForceVelocity:]
+ -[RCPSyntheticEventStream barrelRollAtLocation:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:]
+ -[RCPSyntheticEventStream hover:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:]
+ -[RCPSyntheticEventStream hoverAtLocation:withDuration:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:]
+ -[RCPSyntheticEventStream squeezeAtLocation:]
+ -[RCPSyntheticEventStream squeeze]
+ ___block_literal_global.744
+ _objc_msgSend$_squeezeWithPhase:withPage:withUsage:withVersion:withStage:withTransition:withNextThreshold:withPressedThreshold:withReleasedThreshold:withNormalizedForce:withNormalizedForceVelocity:
+ _objc_msgSend$barrelRollAtLocation:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:
+ _objc_msgSend$hoverAtLocation:withDuration:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:
+ _objc_msgSend$squeeze
- ___block_literal_global.718
- _objc_msgSend$hoverAtLocation:withDuration:withZPosition:
CStrings:
+ "06:34:17"
+ "Apr 13 2024"
+ "Please specify a azimuth angle, altitude angle, and roll angle.\n"
+ "Please specify a roll angle for the barrel roll.\n"
+ "Please specify a start point for the barrel roll.\n"
+ "Please specify a starting z position for the barrel roll.\n"
+ "Please specify an altitude angle for the barrel roll.\n"
+ "Please specify an azimuth angle for the barrel roll.\n"
+ "_squeezeWithPhase:withPage:withUsage:withVersion:withStage:withTransition:withNextThreshold:withPressedThreshold:withReleasedThreshold:withNormalizedForce:withNormalizedForceVelocity:"
+ "barrelRollAtLocation:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:"
+ "br"
+ "hover:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:"
+ "hoverAtLocation:withDuration:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:"
+ "sq"
+ "squeeze"
+ "squeezeAtLocation:"
+ "v64@0:8{CGPoint=dd}16d32d40d48d56"
+ "v72@0:8{CGPoint=dd}16d32d40d48d56d64"
+ "v88@0:8S16@20@28C36I40I44d48d56d64d72d80"
- "00:36:54"
- "Mar  9 2024"

```
