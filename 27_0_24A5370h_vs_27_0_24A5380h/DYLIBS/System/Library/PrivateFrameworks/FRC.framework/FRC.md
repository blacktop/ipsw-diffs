## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/FRC`

```diff

-  __TEXT.__text: 0x400dc
+  __TEXT.__text: 0x400fc
   __TEXT.__objc_methlist: 0x3a9c
   __TEXT.__const: 0x5a0
   __TEXT.__cstring: 0x65fb

   __AUTH_CONST.__cfstring: 0x3ec0
   __AUTH_CONST.__objc_const: 0xa710
   __AUTH_CONST.__auth_got: 0x7c8
-  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xdb0
   __DATA.__data: 0x140
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
Functions:
~ _saveTextureInterleaved : 324 -> 328
~ _readYUV10bit : 484 -> 480
~ _writeYUV10bit : 476 -> 472
~ -[OpticalFlowAnalyzer processGPUOutputs:blockWidth:blockHeight:faceHandLegBoundingBoxBlocks:] : 2132 -> 2168

```
