## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

-2.4.0.0.0
-  __TEXT.__text: 0x71388
+2.5.0.0.0
+  __TEXT.__text: 0x710dc
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x50a4
+  __TEXT.__objc_methlist: 0x5084
   __TEXT.__const: 0x620
   __TEXT.__cstring: 0x606e
-  __TEXT.__oslogstring: 0x3369
+  __TEXT.__oslogstring: 0x3340
   __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x1290
-  __TEXT.__objc_classname: 0x6cc
-  __TEXT.__objc_methname: 0x13ca1
-  __TEXT.__objc_methtype: 0x77d3
-  __TEXT.__objc_stubs: 0x7760
+  __TEXT.__unwind_info: 0x1288
+  __TEXT.__objc_classname: 0x6cb
+  __TEXT.__objc_methname: 0x13bdb
+  __TEXT.__objc_methtype: 0x778c
+  __TEXT.__objc_stubs: 0x7740
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0x310
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d8
+  __DATA_CONST.__objc_selrefs: 0x29c0
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x7b8
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__cfstring: 0x3100
-  __AUTH_CONST.__objc_const: 0x11258
+  __AUTH_CONST.__objc_const: 0x111a8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x1514
+  __DATA.__objc_ivar: 0x1500
   __DATA.__data: 0x260
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 047093D9-60B3-3C95-AD22-7E3C19737D7F
-  Functions: 2477
-  Symbols:   8432
-  CStrings:  4665
+  UUID: F119BB44-444D-38F7-A339-2CEE53030299
+  Functions: 2471
+  Symbols:   8410
+  CStrings:  4654
 
Symbols:
+ -[FRNet convertToYUV:attachment:]
+ -[FRNet convertToYUV:attachment:].cold.1
+ _OBJC_IVAR_$_FRNet._lowResolutionNormalizedBufferPool
+ _objc_msgSend$convertToYUV:attachment:
- -[FRNet convertToYUVForSampling:attachment:]
- -[FRNet convertToYUVForSampling:attachment:].cold.1
- -[FRNet cropInput:offset:CMAttachment:]
- -[FRNet cropInput:offset:CMAttachment:].cold.1
- -[FRNet getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:].cold.1
- -[FRNet outputFP16]
- -[FRNet setOutputFP16:]
- _OBJC_IVAR_$_FRNet._lowResolutionCroppedImageBufferPool
- _OBJC_IVAR_$_FRNet._lowResolutionImageBufferPool
- _OBJC_IVAR_$_FRNet._numberOfProcessedFrames
- _OBJC_IVAR_$_FRNet._numberOfRequestedFrames
- _OBJC_IVAR_$_FRNet._outputBufferPool
- _OBJC_IVAR_$_FRNet._outputFP16
- _objc_msgSend$convertToYUVForSampling:attachment:
- _objc_msgSend$cropInput:offset:CMAttachment:
CStrings:
+ "_lowResolutionNormalizedBufferPool"
+ "convertToYUV:attachment:"
- "Error! failed to convert 422 yuv to RGBA"
- "TB,N,V_outputFP16"
- "^{__CVBuffer=}48@0:8^{__CVBuffer=}16{CGPoint=dd}24^{__CFDictionary=}40"
- "_lowResolutionCroppedImageBufferPool"
- "_lowResolutionImageBufferPool"
- "_numberOfProcessedFrames"
- "_numberOfRequestedFrames"
- "_outputBufferPool"
- "_outputFP16"
- "convertToYUVForSampling:attachment:"
- "cropInput:offset:CMAttachment:"
- "outputFP16"
- "setOutputFP16:"

```
