## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-500.71.0.0.0
-  __TEXT.__text: 0x23028
+500.77.0.0.0
+  __TEXT.__text: 0x23060
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__const: 0x74120
-  __TEXT.__gcc_except_tab: 0x454
+  __TEXT.__gcc_except_tab: 0x45c
   __TEXT.__cstring: 0x111b
-  __TEXT.__oslogstring: 0x3d90
+  __TEXT.__oslogstring: 0x3d0c
   __TEXT.__unwind_info: 0x3e8
   __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__auth_got: 0x518

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 796C1000-D487-37F5-9749-75629C91F100
-  Functions: 466
-  Symbols:   1312
-  CStrings:  374
+  UUID: 2C5F2A49-D7AD-3075-8B31-D4521A3541A0
+  Functions: 469
+  Symbols:   1318
+  CStrings:  373
 
Symbols:
+ _OUTLINED_FUNCTION_16
+ __ZL25ProResDecoder_DecodeFrameP20OpaqueVTVideoDecoderP25OpaqueVTVideoDecoderFrameP20opaqueCMSampleBufferjPj.cold.43
+ __ZL25ProResDecoder_DecodeFrameP20OpaqueVTVideoDecoderP25OpaqueVTVideoDecoderFrameP20opaqueCMSampleBufferjPj.cold.44
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): cfa_pattern in frame_header %d does not match with output format CFA/bayer_pattern [0,%d]\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): cfa_pattern in frame_header %d does not match with output format CFA/bayer_pattern [0,%d].\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern [0,3].\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern [0,3]\n"
- "WARNING AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format bayer_pattern [0,3]\n"

```
