## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-465.15.2.0.0
-  __TEXT.__text: 0x5c410
+470.16.1.0.0
+  __TEXT.__text: 0x5c0fc
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x3158
+  __TEXT.__objc_methlist: 0x3140
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x20e0
-  __TEXT.__cstring: 0x5934
-  __TEXT.__oslogstring: 0x6e56
+  __TEXT.__gcc_except_tab: 0x20b0
+  __TEXT.__cstring: 0x593e
+  __TEXT.__oslogstring: 0x6e2a
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x1468
+  __TEXT.__unwind_info: 0x1460
   __TEXT.__objc_classname: 0xa62
-  __TEXT.__objc_methname: 0x8e8c
-  __TEXT.__objc_methtype: 0x202d
-  __TEXT.__objc_stubs: 0x6de0
+  __TEXT.__objc_methname: 0x8e86
+  __TEXT.__objc_methtype: 0x205f
+  __TEXT.__objc_stubs: 0x6da0
   __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x1540
+  __DATA_CONST.__const: 0x1548
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x75f0
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_const: 0x7610
+  __DATA_CONST.__objc_selrefs: 0x1fa0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__cfstring: 0x33e0
+  __AUTH_CONST.__cfstring: 0x3400
   __AUTH_CONST.__objc_const: 0x1320
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__objc_intobj: 0x3d8

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x310
   __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x5b8
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0xae0
   __DATA.__bss: 0x158
   __DATA.__common: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1609
-  Symbols:   5818
-  CStrings:  3072
+  Functions: 1607
+  Symbols:   5813
+  CStrings:  3073
 
Symbols:
+ -[CMContinuityCaptureFrameRateManager reportStreamStatus:forConfiguration:forCompanionDeviceType:]
+ GCC_except_table101
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table110
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table99
+ _CMContinuityCaptureFrameRateManagerThrottledKVOKey
+ _OBJC_IVAR_$_CMContinuityCaptureFrameRateManager._currentThermalLevel
+ _OBJC_IVAR_$_ContinuityCaptureRemoteUISystemStatus._callCenterNeighborhoodActivityConduit
+ ___block_literal_global.102
+ ___block_literal_global.70
+ ___block_literal_global.78
+ ___block_literal_global.88
+ _objc_msgSend$incomingCall:data:shouldDisplayNotification:
+ _objc_msgSend$isRingingFaceTimeCallsOnConnectedTVDevice
+ _objc_msgSend$neighborhoodActivityConduit
+ _objc_msgSend$reportStreamStatus:forConfiguration:forCompanionDeviceType:
- -[CMContinuityCaptureFrameRateManager activeControlsForFrameRateThrottle]
- -[CMContinuityCaptureFrameRateManager reportControlStatus:forControlName:]
- -[CMContinuityCaptureFrameRateManager reportStreamStatus:forConfiguration:]
- GCC_except_table105
- GCC_except_table106
- GCC_except_table108
- GCC_except_table4
- GCC_except_table85
- GCC_except_table89
- _OBJC_IVAR_$_CMContinuityCaptureFrameRateManager._activeControlsByNameThrottlingFrameRate
- ___block_literal_global.56
- ___block_literal_global.83
- _objc_msgSend$activeControlsForFrameRateThrottle
- _objc_msgSend$incomingCall:data:
- _objc_msgSend$reportControlStatus:forControlName:
- _objc_msgSend$reportStreamStatus:forConfiguration:
- _objc_msgSend$videoFrameRateRangeForPortraitEffect
- _objc_msgSend$videoFrameRateRangeForStudioLight
CStrings:
+ "\a"
+ "\""
+ "%{public}@ Throttle FPS to %d, Reason: deskview enabled (%d) or LPM enabled (%d)"
+ "%{public}@ Unthrottle/Pick-Up default frameRate (%d,%d)"
+ "%{public}@ Updated maxFrameRate: %u minFrameRate: %u, throttled state: %d"
+ "@\"TUNeighborhoodActivityConduit\""
+ "Center Stage should not be set when docked tracking is enabled. Ignore the request."
+ "Docked tracking is enabled, do not forcefully enable Center Stage as requested"
+ "_callCenterNeighborhoodActivityConduit"
+ "_currentThermalLevel"
+ "incomingCall:data:shouldDisplayNotification:"
+ "isRingingFaceTimeCallsOnConnectedTVDevice"
+ "neighborhoodActivityConduit"
+ "reportStreamStatus:forConfiguration:forCompanionDeviceType:"
+ "v36@0:8B16@20@28"
- "\x06"
- "#"
- "%{public}@ Pickup default frameRate (%d,%d)"
- "%{public}@ Throttle FPS to %d, reason deskview enabled or frame throttle controls enabled"
- "%{public}@ Un-Throttle FPS to (%d,%d), reason deskview disabled or frame throttle controls disabled"
- "%{public}@ current %d range PB supported range %@ for format %@"
- "%{public}@ current %d range SL supported range %@ for format %@"
- "%{public}@ report control status %d for name %{public}@"
- "_activeControlsByNameThrottlingFrameRate"
- "activeControlsForFrameRateThrottle"
- "incomingCall:data:"
- "reportControlStatus:forControlName:"
- "reportStreamStatus:forConfiguration:"
- "videoFrameRateRangeForPortraitEffect"
- "videoFrameRateRangeForStudioLight"

```
