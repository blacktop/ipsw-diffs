## AppleProResHWDecoder.videodecoder

> `/System/Library/VideoDecoders/AppleProResHWDecoder.videodecoder`

```diff

-500.55.0.0.0
-  __TEXT.__text: 0x22f24
-  __TEXT.__auth_stubs: 0xa30
+500.71.0.0.0
+  __TEXT.__text: 0x23028
+  __TEXT.__auth_stubs: 0xa20
   __TEXT.__const: 0x74120
-  __TEXT.__gcc_except_tab: 0x448
-  __TEXT.__cstring: 0x1115
-  __TEXT.__oslogstring: 0x3c69
-  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__gcc_except_tab: 0x454
+  __TEXT.__cstring: 0x111b
+  __TEXT.__oslogstring: 0x3d90
+  __TEXT.__unwind_info: 0x3e8
   __DATA_CONST.__got: 0x1f0
-  __AUTH_CONST.__auth_got: 0x520
+  __AUTH_CONST.__auth_got: 0x518
   __AUTH_CONST.__const: 0x138
   __AUTH_CONST.__cfstring: 0xc0
   __DATA.__data: 0xb

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 5DE37830-7DC6-3034-B5FC-CE15727F86A2
-  Functions: 463
-  Symbols:   1305
+  UUID: 796C1000-D487-37F5-9749-75629C91F100
+  Functions: 466
+  Symbols:   1312
   CStrings:  374
 
Symbols:
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table9
+ _OUTLINED_FUNCTION_15
+ __Z16checkFrameHeaderP17ProResFrameHeaderb21ProRes_UserClientTypej.cold.16
+ __Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZL25ProResDecoder_DecodeFrameP20OpaqueVTVideoDecoderP25OpaqueVTVideoDecoderFrameP20opaqueCMSampleBufferjPj.cold.42
+ __ZN19ProResFrameReceiver26getNumFramesOverTargetSizeEv
+ __ZN19ProResFrameReceiver27getSumOfFramesOvershootPercEv
+ ____Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
+ ___block_descriptor_tmp.31
- GCC_except_table10
- GCC_except_table2
- GCC_except_table33
- GCC_except_table39
- GCC_except_table42
- GCC_except_table43
- GCC_except_table47
- GCC_except_table6
- __Z15getHardwareTypePc
- __Z23reportEncodeSessionInfojjjjjhbjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- ____Z23reportEncodeSessionInfojjjjjhbjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
- ___block_descriptor_tmp.36
- _sysctlbyname
CStrings:
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported RAW bayerPattern\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported RAW cfaPattern\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported feature RAW cfaPattern=%d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern 0.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern 1.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern 2.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern 3.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern [0,3].\n"
+ "WARNING AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format CFA/bayer_pattern [0,3]\n"
+ "avgTargetOvershootPercent"
+ "percentFramesOverTarget"
- "AppleTV"
- "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported bayer_pattern %d\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format bayer_pattern 0.\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format bayer_pattern 1.\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format bayer_pattern 2.\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format bayer_pattern 3.\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): bayer_pattern in frame_header %d does not match with output format bayer_pattern [0,3].\n"
- "hardwareType"
- "hw.machine"
- "iPad"
- "iPhone"

```
