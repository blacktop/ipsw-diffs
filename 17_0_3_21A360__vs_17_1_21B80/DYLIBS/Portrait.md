## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-327.0.0.0.0
-  __TEXT.__text: 0x8f478
+330.9.0.0.0
+  __TEXT.__text: 0x8fd54
   __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x80b4
-  __TEXT.__const: 0x20ff0
-  __TEXT.__cstring: 0x73cc
-  __TEXT.__oslogstring: 0x392b
+  __TEXT.__objc_methlist: 0x80ec
+  __TEXT.__const: 0x21010
+  __TEXT.__cstring: 0x739a
+  __TEXT.__oslogstring: 0x39dd
   __TEXT.__gcc_except_tab: 0x1ac
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2028
+  __TEXT.__unwind_info: 0x2048
   __TEXT.__objc_classname: 0x110e
-  __TEXT.__objc_methname: 0x174b5
+  __TEXT.__objc_methname: 0x175ad
   __TEXT.__objc_methtype: 0x4b70
-  __TEXT.__objc_stubs: 0xe040
+  __TEXT.__objc_stubs: 0xe0c0
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x670
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15b48
-  __DATA_CONST.__objc_selrefs: 0x4698
+  __DATA_CONST.__objc_const: 0x15b78
+  __DATA_CONST.__objc_selrefs: 0x46b0
   __DATA_CONST.__objc_arraydata: 0x5c0
-  __AUTH_CONST.__cfstring: 0x4980
+  __AUTH_CONST.__cfstring: 0x4960
   __AUTH_CONST.__objc_const: 0x3900
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_intobj: 0x7f8

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x650
   __DATA.__objc_superrefs: 0x438
-  __DATA.__objc_ivar: 0x1418
+  __DATA.__objc_ivar: 0x141c
   __DATA.__data: 0x6b0
   __DATA.__bss: 0x1f4
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3993
-  Symbols:   12995
-  CStrings:  6143
+  Functions: 4010
+  Symbols:   13034
+  CStrings:  6150
 
Symbols:
+ -[PTDisparityPostProcessing computeOpticalFlow:inRGBA:outDisplacement:]
+ -[PTDisparityPostProcessing computeOpticalFlow:inRGBA:outDisplacement:].cold.1
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:]
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:].cold.1
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:].cold.2
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:].cold.3
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisplacement:inStatePrev:inDisparity:outDisparityFiltered:outState:]
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisplacement:inStatePrev:inDisparity:outDisparityFiltered:outState:].cold.1
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisplacement:inStatePrev:inDisparity:outDisparityFiltered:outState:].cold.2
+ -[PTDisparityPostProcessing temporalDisparityFilter:inDisplacement:inStatePrev:inDisparity:outDisparityFiltered:outState:].cold.3
+ -[PTEffectReactionState setUiTriggeredReaction:]
+ -[PTEffectReactionState uiTriggeredReaction]
+ -[PTMetalContext initWithCommandQueue:bundleClass:].cold.4
+ -[PTMetalContext initWithCommandQueue:bundleClass:].cold.5
+ -[PTMetalContext initWithCommandQueue:bundleClass:].cold.6
+ _OBJC_IVAR_$_PTEffectReactionState._uiTriggeredReaction
+ _objc_msgSend$computeOpticalFlow:inRGBA:outDisplacement:
+ _objc_msgSend$setUiTriggeredReaction:
+ _objc_msgSend$temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:
+ _objc_msgSend$temporalDisparityFilter:inDisplacement:inStatePrev:inDisparity:outDisparityFiltered:outState:
- -[PTDisparityPostProcessing computeOpticalFlow:outDisplacement:].cold.1
- -[PTDisparityPostProcessing initWithCommandQueue:disparitySize:filteredDisparitySize:disparityPixelFormat:colorSize:colorPixelFormat:sensorPort:].cold.3
- -[PTDisparityPostProcessing temporalDisparityFilter:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:].cold.1
- -[PTDisparityPostProcessing temporalDisparityFilter:inStatePrev:inDisparity:outDisparityFiltered:outState:].cold.1
CStrings:
+ "Resolved gpuName: %@"
+ "computeOpticalFlow:inRGBA:outDisplacement:"
+ "disparity size expected (%zu x %zu) was (%zu x %zu)"
+ "g11p"
+ "gpu name: %@"
+ "gpu revision: %@"
+ "inDisplacement size expected (%zu x %zu) was (%zu x %zu)"
+ "outDisparity size expected (%zu x %zu) was (%zu x %zu)"
+ "temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:"
+ "temporalDisparityFilter:inDisplacement:inStatePrev:inDisparity:outDisparityFiltered:outState:"
- "Disparity size must equal color size"
- "Invalid size of inDisparityPrev"
- "Invalid size of inRGBA"

```
