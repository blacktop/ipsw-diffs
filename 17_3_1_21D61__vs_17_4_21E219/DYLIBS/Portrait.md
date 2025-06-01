## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-336.2.0.0.0
-  __TEXT.__text: 0x90054
+339.11.0.0.0
+  __TEXT.__text: 0x902d4
   __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x810c
+  __TEXT.__objc_methlist: 0x813c
   __TEXT.__const: 0x21010
-  __TEXT.__cstring: 0x739a
-  __TEXT.__oslogstring: 0x3a84
+  __TEXT.__cstring: 0x7366
+  __TEXT.__oslogstring: 0x3ac4
   __TEXT.__gcc_except_tab: 0x1ac
   __TEXT.__ustring: 0x30
   __TEXT.__unwind_info: 0x2054
   __TEXT.__objc_classname: 0x1110
-  __TEXT.__objc_methname: 0x17665
+  __TEXT.__objc_methname: 0x177cb
   __TEXT.__objc_methtype: 0x4b9b
-  __TEXT.__objc_stubs: 0xe140
+  __TEXT.__objc_stubs: 0xe1c0
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x670
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15c10
-  __DATA_CONST.__objc_selrefs: 0x46d0
+  __DATA_CONST.__objc_const: 0x15c90
+  __DATA_CONST.__objc_selrefs: 0x46f0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x650
+  __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x5c0
-  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__cfstring: 0x4920
   __AUTH_CONST.__objc_const: 0x38b8
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__objc_intobj: 0x828
+  __AUTH_CONST.__objc_intobj: 0x858
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x8a0
   __AUTH.__objc_data: 0x2e90
   __AUTH.__data: 0xb80
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x650
-  __DATA.__objc_superrefs: 0x438
-  __DATA.__objc_ivar: 0x1424
-  __DATA.__data: 0x6a8
-  __DATA.__bss: 0x1e4
+  __DATA.__objc_ivar: 0x1430
+  __DATA.__data: 0x760
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/FusionTracker.framework/FusionTracker
+  - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/VFX.framework/VFX

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A84FE0AB-E098-35F1-A8C4-12A7D91D7B80
-  Functions: 4022
-  Symbols:   13058
-  CStrings:  6749
+  UUID: 557508F8-5210-3852-B886-6676C462AEBF
+  Functions: 4027
+  Symbols:   13075
+  CStrings:  6759
 
Symbols:
+ +[PTRenderPipeline prewarmForMediaserverd].cold.1
+ -[PTQualitySettings circleOfConfusionLimitBackground]
+ -[PTQualitySettings circleOfConfusionLimitForeground]
+ -[PTQualitySettings setCircleOfConfusionLimitBackground:]
+ -[PTQualitySettings setCircleOfConfusionLimitForeground:]
+ -[PTRaytracingUtils disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipBgFg:]
+ -[PTRaytracingUtils disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipBgFg:].cold.1
+ _OBJC_IVAR_$_PTQualitySettings._circleOfConfusionLimitBackground
+ _OBJC_IVAR_$_PTQualitySettings._circleOfConfusionLimitForeground
+ _OBJC_IVAR_$_PTRaytracingV3001._circleOfConfusionLimitBgFg
+ _OBJC_IVAR_$_PTRaytracingV3001._sourceColorSize
+ _OBJC_IVAR_$_PTRaytracingV3001._sourceDisparitySize
+ __unnamed_array_storage.137
+ _objc_msgSend$circleOfConfusionLimitBackground
+ _objc_msgSend$circleOfConfusionLimitForeground
+ _objc_msgSend$disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipBgFg:
+ _objc_msgSend$setCircleOfConfusionLimitBackground:
+ _objc_msgSend$setCircleOfConfusionLimitForeground:
- -[PTRaytracingUtils disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipMinMax:]
- -[PTRaytracingUtils disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipMinMax:].cold.1
- _OBJC_IVAR_$_PTRaytracingV3001._circleOfConfusionWeightMinMax
- _OBJC_IVAR_$_PTRaytracingV3001._colorSize
- __unnamed_array_storage.135
- _objc_msgSend$disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipMinMax:
CStrings:
+ "\x03\x11!W\x1fR"
+ "Failed to prewarm PTRenderPipeline: latest version not included"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N"
+ "Tf,V_circleOfConfusionLimitBackground"
+ "Tf,V_circleOfConfusionLimitForeground"
+ "_circleOfConfusionLimitBackground"
+ "_circleOfConfusionLimitBgFg"
+ "_circleOfConfusionLimitForeground"
+ "_sourceColorSize"
+ "_sourceDisparitySize"
+ "circleOfConfusionLimitBackground"
+ "circleOfConfusionLimitForeground"
+ "disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipBgFg:"
+ "setCircleOfConfusionLimitBackground:"
+ "setCircleOfConfusionLimitForeground:"
- "\x03\x11!W\x1fB"
- "_circleOfConfusionWeightMinMax"
- "disparityCenterAndClip:inDisparity:outDisparity:centeringValue:clipMinMax:"
- "kSourceColorSize_float2"
- "kSourceDisparitySize_float2"

```
