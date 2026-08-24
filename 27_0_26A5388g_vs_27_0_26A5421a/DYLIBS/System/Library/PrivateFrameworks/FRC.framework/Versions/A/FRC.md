## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/Versions/A/FRC`

```diff

-258.0.0.0.0
-  __TEXT.__text: 0x42948
+259.0.0.0.0
+  __TEXT.__text: 0x42a78
   __TEXT.__objc_methlist: 0x3a9c
   __TEXT.__const: 0x5b0
-  __TEXT.__cstring: 0x658d
+  __TEXT.__cstring: 0x659e
   __TEXT.__oslogstring: 0xec3
   __TEXT.__gcc_except_tab: 0x270
   __TEXT.__unwind_info: 0xcc8

   - /usr/lib/libobjc.A.dylib
   Functions: 1464
   Symbols:   3825
-  CStrings:  839
+  CStrings:  840
 
Functions:
~ -[DualOpticalFlowE5 opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:] : 408 -> 476
~ -[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:] : 2576 -> 2640
~ _getConfigurationName : 792 -> 804
~ sub_2445d08b0 -> sub_244053940 : 64 -> 68
~ -[OpticalFlow opticalFlowFirstFrame:secondFrame:flow:callback:] : 328 -> 372
~ -[OpticalFlow opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:] : 348 -> 416
~ -[NeuFlow opticalFlowFirstFrame:secondFrame:flow:callback:] : 892 -> 936
CStrings:
+ "landscape256x192"
```
