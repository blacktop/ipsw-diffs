## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/FRC`

```diff

-258.0.0.0.0
-  __TEXT.__text: 0x400fc
+259.0.0.0.0
+  __TEXT.__text: 0x40244
   __TEXT.__objc_methlist: 0x3a9c
   __TEXT.__const: 0x5a0
-  __TEXT.__cstring: 0x65fb
+  __TEXT.__cstring: 0x660c
   __TEXT.__oslogstring: 0xec3
   __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__unwind_info: 0xc78

   - /usr/lib/libobjc.A.dylib
   Functions: 1445
   Symbols:   3839
-  CStrings:  842
+  CStrings:  843
 
Functions:
~ sub_261d996ac -> sub_2618526ac : 64 -> 68
~ -[DualOpticalFlowE5 opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:] : 408 -> 476
~ _FRCGetUsageFromSize : 1164 -> 1188
~ -[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:] : 2528 -> 2592
~ _getConfigurationName : 792 -> 804
~ -[OpticalFlow opticalFlowFirstFrame:secondFrame:flow:callback:] : 316 -> 360
~ -[OpticalFlow opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:] : 348 -> 416
~ -[NeuFlow opticalFlowFirstFrame:secondFrame:flow:callback:] : 836 -> 880
CStrings:
+ "landscape256x192"
```
