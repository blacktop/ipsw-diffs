## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

 7.1.4.0.0
-  __TEXT.__text: 0xf484
+  __TEXT.__text: 0xf480
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_methlist: 0xb94
   __TEXT.__const: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBA6858E-E469-303B-A43A-B7D303D00D43
-  Functions: 414
-  Symbols:   1770
+  UUID: 0E79D6B4-850A-3FC8-8614-A5680DEC0B06
+  Functions: 415
+  Symbols:   1772
   CStrings:  748
 
Functions:
~ _OUTLINED_FUNCTION_0 : 24 -> 8
~ _OUTLINED_FUNCTION_0 : 32 -> 24
~ _OUTLINED_FUNCTION_0 : 12 -> 32
~ _OUTLINED_FUNCTION_0 : 28 -> 12
~ _OUTLINED_FUNCTION_0 : 96 -> 28
~ _OUTLINED_FUNCTION_0 : 32 -> 96
+ _OUTLINED_FUNCTION_0
~ -[LSSVector2SmoothFilter updateVector:alpha:] : 60 -> 56
~ -[LSSController _resolveFeatures] : 700 -> 696
~ -[LSSMotionBasedLightSource updateTargetDirectionWithOrientation:goToRest:timestamp:] : 1876 -> 1872
~ -[LSSMotionBasedProvider _updateReference:motionLevel:activateLevel:deactivateLevel:] : 716 -> 712
~ -[LSSAccumulator addSample:] : 648 -> 644
~ -[LSSRotationAccumulator update:] : 408 -> 416

```
