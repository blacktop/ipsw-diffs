## pointeruid

> `/System/Library/PrivateFrameworks/PointerUIServices.framework/Support/pointeruid`

```diff

-163.0.0.0.0
-  __TEXT.__text: 0x26014
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x62e0
-  __TEXT.__objc_methlist: 0x2394
-  __TEXT.__const: 0x380
-  __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__cstring: 0x3142
-  __TEXT.__objc_classname: 0x65e
-  __TEXT.__objc_methname: 0xabed
-  __TEXT.__objc_methtype: 0x1ea2
+163.0.2.0.0
+  __TEXT.__text: 0x274b8
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x6600
+  __TEXT.__objc_methlist: 0x24cc
+  __TEXT.__const: 0x390
+  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0x3494
+  __TEXT.__objc_classname: 0x661
+  __TEXT.__objc_methname: 0xb355
+  __TEXT.__objc_methtype: 0x1edb
   __TEXT.__oslogstring: 0x1546
-  __TEXT.__unwind_info: 0x950
-  __DATA_CONST.__auth_got: 0x650
+  __TEXT.__unwind_info: 0x990
+  __DATA_CONST.__auth_got: 0x658
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__cfstring: 0x2a40
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_doubleobj: 0xb0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_const: 0x62f8
-  __DATA.__objc_selrefs: 0x1db0
-  __DATA.__objc_ivar: 0x474
+  __DATA.__objc_const: 0x6658
+  __DATA.__objc_selrefs: 0x1e88
+  __DATA.__objc_ivar: 0x4c8
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x7e8
   __DATA.__bss: 0x98

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 932D3655-6D98-38D5-B20C-5854CE4FBAA3
-  Functions: 859
-  Symbols:   342
-  CStrings:  2516
+  UUID: 49E04CD3-6305-30CA-8014-440DAA314A98
+  Functions: 891
+  Symbols:   343
+  CStrings:  2616
 
Symbols:
+ _PSPointerVibrantColorMatrixForLuminanceWithPlasmaEnabled
+ _mach_absolute_time
- _PSPointerVibrantColorMatrixForLuminance
CStrings:
+ "Coefficient to convert from wiggles (input) to scale (output)"
+ "Max factor to scale up the pointer size upon gesture detection"
+ "Maximum time between events still considered as one continuous gesture (seconds)"
+ "Maximum variance of slopes between wiggle points allowed to detect a line"
+ "Minimum number of wiggle points for gesture recognition"
+ "Shake To Find Contraction"
+ "Shake To Find Expansion"
+ "Shake to Find"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_shakeToFindContractionAnimationSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_shakeToFindExpansionAnimationSettings"
+ "TQ,N,V_shakeToFindWiggleCount"
+ "Td,N,V_shakeToFindDecayInterval"
+ "Td,N,V_shakeToFindGestureInterval"
+ "Td,N,V_shakeToFindMaxScaleUpFactor"
+ "Td,N,V_shakeToFindPointerSizeMultiplier"
+ "Td,N,V_shakeToFindScaleFactor"
+ "Td,N,V_shakeToFindScaleUpdateInterval"
+ "Td,N,V_shakeToFindSlopeVarianceThreshold"
+ "Td,R,N,V_shakeToFindPointerSizeMultiplier"
+ "Time after last input event at which to begin the decay of cursor size (seconds)"
+ "Time interval between re-evaluation of shake to find scale factor"
+ "_detectShakeToFindGesture"
+ "_getShakeToFindPointerSizeMultiplierAtTime:"
+ "_lastShakeToFindPointerSizeMultiplier"
+ "_performShakeToFindScalingAnimation"
+ "_performShakeToFindWithPointerParentEvent:previousEvent:"
+ "_prevPointerVelocity"
+ "_setupAndUnhidePointerViewForPointerShape:"
+ "_shakeToFindAnimationScheduled"
+ "_shakeToFindAnimationTimer"
+ "_shakeToFindContractionAnimationSettings"
+ "_shakeToFindDecayInterval"
+ "_shakeToFindExpansionAnimationSettings"
+ "_shakeToFindGestureDetected"
+ "_shakeToFindGestureInterval"
+ "_shakeToFindLastWiggleTimestamp"
+ "_shakeToFindMaxScaleUpFactor"
+ "_shakeToFindPointerSizeMultiplier"
+ "_shakeToFindPoints"
+ "_shakeToFindScaleFactor"
+ "_shakeToFindScaleUpdateInterval"
+ "_shakeToFindScalingProperty"
+ "_shakeToFindSlopeVarianceThreshold"
+ "_shakeToFindWiggleCount"
+ "_shakeToFindWiggles"
+ "d24@0:8Q16"
+ "floatValue"
+ "isHidden"
+ "setShakeToFindContractionAnimationSettings:"
+ "setShakeToFindDecayInterval:"
+ "setShakeToFindExpansionAnimationSettings:"
+ "setShakeToFindGestureInterval:"
+ "setShakeToFindMaxScaleUpFactor:"
+ "setShakeToFindPointerSizeMultiplier:"
+ "setShakeToFindScaleFactor:"
+ "setShakeToFindScaleUpdateInterval:"
+ "setShakeToFindSlopeVarianceThreshold:"
+ "setShakeToFindWiggleCount:"
+ "shakeToFindContractionAnimationSettings"
+ "shakeToFindDecayInterval"
+ "shakeToFindExpansionAnimationSettings"
+ "shakeToFindGestureInterval"
+ "shakeToFindMaxScaleUpFactor"
+ "shakeToFindPointerSizeMultiplier"
+ "shakeToFindScaleFactor"
+ "shakeToFindScaleUpdateInterval"
+ "shakeToFindSlopeVarianceThreshold"
+ "shakeToFindWiggleCount"
+ "v32@0:8^{__IOHIDEvent=}16^{__IOHIDEvent=}24"
+ "\xf0\x81"
- "\xf0a"

```
