## AppleProResHWEncoder

> `/System/Library/Video/Plug-Ins/AppleProResHWEncoder.bundle/Contents/MacOS/AppleProResHWEncoder`

```diff

-428.3.0.0.0
-  __TEXT.__text: 0x1c298
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__const: 0x741f0
-  __TEXT.__cstring: 0x1148
-  __TEXT.__gcc_except_tab: 0x398
-  __TEXT.__oslogstring: 0x2ad7
-  __TEXT.__unwind_info: 0x398
-  __DATA_CONST.__auth_got: 0x538
-  __DATA_CONST.__got: 0x200
+475.2.0.0.0
+  __TEXT.__text: 0x1ce60
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__const: 0x741b0
+  __TEXT.__cstring: 0x11e3
+  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__oslogstring: 0x2d90
+  __TEXT.__unwind_info: 0x3c8
+  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x188
   __DATA_CONST.__cfstring: 0x240

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 00DD4565-0C1A-3B5B-8644-AEC0A1224CE8
-  Functions: 398
-  Symbols:   237
-  CStrings:  329
+  UUID: 283D5598-BAAC-3A6D-9039-833FB2DA0386
+  Functions: 411
+  Symbols:   243
+  CStrings:  345
 
Symbols:
+ _kCVImageBufferAlphaChannelIsOpaque
+ _kVTCompressionPropertyKey_AverageBitRate
+ _kVTCompressionPropertyKey_ExpectedFrameRate
+ _kVTCompressionPropertyKey_Paravirtualized
+ _kVTVideoEncoder_IsParavirtualizationAware
+ _memset
CStrings:
+ "AppleProResHW (0x%x): %s(): Bad RecDecoderHW error, frame %d HWErrorCode=0x%x"
+ "CopyBitstreamToBlockBuffer"
+ "DoubleEncodeFrame"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW Invalid FrameRate value %f\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in Double Encode function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in P2Encode function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in ParseFrame function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in PerformAlphaUpscaling function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in PrepareFrame function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in QueueOutOfOrderFrame function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): FrameHeader does not meet minimum size\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Illegal combination of numPasses %d, fastPass %d, QpmEn %d, SwrEn %d BsWrDis %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No encoded alpha when frame is supposed to be non-opaque\n"
+ "P1ParseFrame"
+ "P2Encode"
+ "P2PrepareFrame"
+ "PerformAlphaUpscaling"
+ "QueueOutOfOrderFrame"
+ "depth == 8 || depth == 10 || depth == 12 || depth == 16"
- "AppleProResHW (0x%x): %d: %s(): Warning: AppleProResHW Invalid FieldCount value %u\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): Illegal combination of numPasses %d, fastPass %d, QpmEn %d, SwrEn %d\n"
- "depth == 8 || depth == 10"

```
