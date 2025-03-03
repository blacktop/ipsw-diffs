## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-403.2.0.0.0
-  __TEXT.__text: 0x20aec
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__const: 0x74180
-  __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__cstring: 0x1065
-  __TEXT.__oslogstring: 0x3792
-  __TEXT.__unwind_info: 0x3e8
-  __DATA_CONST.__got: 0x1d8
-  __AUTH_CONST.__auth_got: 0x518
+450.71.0.0.0
+  __TEXT.__text: 0x218ac
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__const: 0x74120
+  __TEXT.__gcc_except_tab: 0x454
+  __TEXT.__cstring: 0x1100
+  __TEXT.__oslogstring: 0x3b83
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x520
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x138
   __AUTH_CONST.__cfstring: 0xc0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 451
-  Symbols:   719
-  CStrings:  341
+  Functions: 464
+  Symbols:   743
+  CStrings:  361
 
Symbols:
+ _CFBooleanGetValue
+ _kCVImageBufferAlphaChannelIsOpaque
+ _kVTDecompressionPropertyKey_Paravirtualized
+ _kVTVideoDecoder_IsParavirtualizationAware
CStrings:
+ "AppleProResHW (0x%x): %s(): Bad RecDecoderHW error, frame %d HWErrorCode=0x%x"
+ "CopyBitstreamToBlockBuffer"
+ "DoubleEncodeFrame"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Bitstream does not have first picture\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Bitstream does not have second picture\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Bitstream does not have valid first picture\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Bitstream does not have valid second picture\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in Double Encode function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in P2Encode function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in ParseFrame function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in PerformAlphaUpscaling function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in PrepareFrame function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error in QueueOutOfOrderFrame function.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): FrameHeader does not meet minimum size\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No encoded alpha when frame is supposed to be non-opaque\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Received invalid bitstream buffer\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): scaleFactor_x %f not equal to scaleFactor_y %f!\n"
+ "P1ParseFrame"
+ "P2Encode"
+ "P2PrepareFrame"
+ "PerformAlphaUpscaling"
+ "QueueOutOfOrderFrame"
+ "depth == 8 || depth == 10 || depth == 12 || depth == 16"
- "AppleProResHW (0x%x): %d: %s(): Warning: scaleFactor_x %zu is not 2/4/8!\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): scaleFactor_x %zu not equal to scaleFactor_y %zu!\n"
- "depth == 8 || depth == 10"

```
