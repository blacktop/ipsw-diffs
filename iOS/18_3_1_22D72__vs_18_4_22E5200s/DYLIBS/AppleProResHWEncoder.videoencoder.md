## AppleProResHWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`

```diff

-403.2.0.0.0
-  __TEXT.__text: 0x1c774
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__const: 0x74220
-  __TEXT.__cstring: 0x1148
-  __TEXT.__gcc_except_tab: 0x408
-  __TEXT.__oslogstring: 0x2b27
-  __TEXT.__unwind_info: 0x3b0
-  __DATA_CONST.__got: 0x210
-  __AUTH_CONST.__auth_got: 0x538
+450.71.0.0.0
+  __TEXT.__text: 0x1cf08
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__const: 0x741b0
+  __TEXT.__cstring: 0x11e3
+  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__oslogstring: 0x2d90
+  __TEXT.__unwind_info: 0x3c8
+  __DATA_CONST.__got: 0x228
+  __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x188
   __AUTH_CONST.__cfstring: 0x240

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 399
-  Symbols:   679
-  CStrings:  312
+  Functions: 411
+  Symbols:   701
+  CStrings:  327
 
Symbols:
+ _kCVImageBufferAlphaChannelIsOpaque
+ _kVTCompressionPropertyKey_Paravirtualized
+ _kVTVideoEncoder_IsParavirtualizationAware
+ _memset
CStrings:
+ "AppleProResHW (0x%x): %s(): Bad RecDecoderHW error, frame %d HWErrorCode=0x%x"
+ "CopyBitstreamToBlockBuffer"
+ "DoubleEncodeFrame"
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
