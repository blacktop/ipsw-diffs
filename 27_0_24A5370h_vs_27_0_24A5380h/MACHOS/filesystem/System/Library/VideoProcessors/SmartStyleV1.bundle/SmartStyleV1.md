## SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

```diff

-  __TEXT.__text: 0x16320
+  __TEXT.__text: 0x163e0
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x2340
-  __TEXT.__objc_methlist: 0x175c
-  __TEXT.__const: 0xb0
-  __TEXT.__objc_methname: 0x510d
+  __TEXT.__objc_stubs: 0x2360
+  __TEXT.__objc_methlist: 0x1764
+  __TEXT.__const: 0xa0
+  __TEXT.__objc_methname: 0x5133
   __TEXT.__cstring: 0x3c59
-  __TEXT.__oslogstring: 0x2a15
+  __TEXT.__oslogstring: 0x2a09
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methtype: 0x13c4
+  __TEXT.__objc_methtype: 0x13cf
   __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x300

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x28c0
-  __DATA.__objc_selrefs: 0xc10
+  __DATA.__objc_selrefs: 0xc18
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 561
-  Symbols:   1279
-  CStrings:  1213
+  Functions: 562
+  Symbols:   1281
+  CStrings:  1215
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CMISmartStyleProcessorV1 _filteredSRLCurveParameterForCurrent:]
+ _objc_msgSend$_filteredSRLCurveParameterForCurrent:
Functions:
~ -[CMISmartStyleProcessorV1 process] : 9276 -> 9320
+ -[CMISmartStyleProcessorV1 _filteredSRLCurveParameterForCurrent:]
~ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:] : 3356 -> 3352
CStrings:
+ "<<<< CMISmartStyleProcessor >>>> %s: SRL masks missing; holding previous curve parameter %f across the gap"
+ "_filteredSRLCurveParameterForCurrent:"
+ "f20@0:8f16"
- "<<<< CMISmartStyleProcessor >>>> %s: Unexpected SRL state: after receiving valid masks curve parameter must stay valid"

```
