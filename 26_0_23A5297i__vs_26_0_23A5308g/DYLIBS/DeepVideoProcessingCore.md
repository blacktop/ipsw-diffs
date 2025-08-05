## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

-2.5.0.0.0
-  __TEXT.__text: 0x710dc
+2.8.0.0.0
+  __TEXT.__text: 0x7134c
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x5084
-  __TEXT.__const: 0x620
-  __TEXT.__cstring: 0x606e
+  __TEXT.__objc_methlist: 0x5094
+  __TEXT.__const: 0x6b0
+  __TEXT.__cstring: 0x609a
   __TEXT.__oslogstring: 0x3340
   __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x1288
+  __TEXT.__unwind_info: 0x1290
   __TEXT.__objc_classname: 0x6cb
-  __TEXT.__objc_methname: 0x13bdb
-  __TEXT.__objc_methtype: 0x778c
-  __TEXT.__objc_stubs: 0x7740
+  __TEXT.__objc_methname: 0x13c2b
+  __TEXT.__objc_methtype: 0x77a0
+  __TEXT.__objc_stubs: 0x7760
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29c0
+  __DATA_CONST.__objc_selrefs: 0x29c8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x3100
+  __AUTH_CONST.__cfstring: 0x3120
   __AUTH_CONST.__objc_const: 0x111a8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B48AF313-DA52-36CC-8EE2-3DA0484F68C4
-  Functions: 2471
-  Symbols:   8410
-  CStrings:  4654
+  UUID: 1CC7BEDE-8C84-39A9-9FAE-0497449431F9
+  Functions: 2475
+  Symbols:   8421
+  CStrings:  4658
 
Symbols:
+ -[Backwarp_Ext encodeUpscaleFlowToCommandBuffer:source:upscaleRatio:destination:]
+ -[FRNet convertToRGB:to:withRGBFormat:rotate:]
+ -[FRNet convertToRGB:to:withRGBFormat:rotate:].cold.1
+ -[Upsampler upscaleFlow:upscaleRatio:destination:]
+ _OBJC_IVAR_$_FRNet._inputIsPortrait
+ _OBJC_IVAR_$_ImageSR._inputIsPortrait
+ _OBJC_IVAR_$_Upsampler._backwarp
+ _isMemoryAvailableForISR
+ _isMemoryAvailableForVSR
+ _memoryUsageTabVSR
+ _objc_msgSend$encodeUpscaleFlowToCommandBuffer:source:upscaleRatio:destination:
+ _objc_msgSend$interestInContentSync:forAssetSelector:
+ _objc_msgSend$upscaleFlow:upscaleRatio:destination:
+ _usageDimensionsTabSR
- -[FRNet convertToRGB:to:withRGBFormat:]
- -[FRNet convertToRGB:to:withRGBFormat:].cold.1
- -[Upsampler upscaleFlowBy4:destination:]
- _OBJC_IVAR_$_FRNet._inputRotation
- _OBJC_IVAR_$_ImageSR._inputRotation
- _OBJC_IVAR_$_Upsampler._flowUpscaleBy4Kernel
- _objc_msgSend$convertToRGB:to:withRGBFormat:
- _objc_msgSend$upscaleFlowBy4:destination:
CStrings:
+ "B36@0:8^{__CVBuffer=}16f24^{__CVBuffer=}28"
+ "_inputIsPortrait"
+ "auto-asset interest in content error:%@"
+ "encodeUpscaleFlowToCommandBuffer:source:upscaleRatio:destination:"
+ "interestInContentSync:forAssetSelector:"
+ "lookForAssetUpdate"
+ "q44@0:8@16@24f32@36"
+ "upscaleFlow:upscaleRatio:destination:"
- "_flowUpscaleBy4Kernel"
- "convertToRGB:to:withRGBFormat:"
- "upscaleFlowBy4"
- "upscaleFlowBy4:destination:"
- "v36@0:8^{__CVBuffer=}16^{__CVBuffer=}24I32"

```
