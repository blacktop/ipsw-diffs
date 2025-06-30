## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

```diff

-830.2.1.0.0
-  __TEXT.__text: 0x783f1c
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__gcc_except_tab: 0x14e98
+830.40.9.0.1
+  __TEXT.__text: 0x78615c
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__gcc_except_tab: 0x14ed8
   __TEXT.__const: 0xc500
-  __TEXT.__cstring: 0x22117
+  __TEXT.__cstring: 0x22424
   __TEXT.__oslogstring: 0x1b7
-  __TEXT.__unwind_info: 0x8394
+  __TEXT.__unwind_info: 0x83c0
   __TEXT.__eh_frame: 0x8090
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x2ee8
   __AUTH_CONST.__const: 0xa778
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__auth_got: 0x688
   __DATA.__data: 0x1c
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__data: 0x4e0

   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B39E637E-F466-323A-B81E-09C1DBF6A5E1
-  Functions: 9234
-  Symbols:   507
-  CStrings:  3059
+  UUID: 61691D5E-0F49-3902-A613-4C699F13DF50
+  Functions: 9243
+  Symbols:   514
+  CStrings:  3071
 
Symbols:
+ _BNNSGraphCompileOptionsGetFileWriteFSyncBarrier
+ _BNNSGraphCompileOptionsSetFileWriteFSyncBarrier
+ _BNNSSGemvDWS
+ _BNNSSGemvDiscontiguousDWS
+ _fcntl
+ _fsync
+ _msync
CStrings:
+ "BNNS Graph Compile: failed to write out file with error: %s"
+ "BNNSGraphCompileOptionsGetFileWriteSynchronous"
+ "BNNSGraphCompileOptionsSetFileWriteSynchronous"
+ "BNNSSGemvDWS SPI: Expected input pointers to be non-null"
+ "BNNSSGemvDWS SPI: Expected y buffer to be padded at least 256Bytes multiple"
+ "BNNSSGemvDiscontiguousDWS SPI: Expected N == 32"
+ "BNNSSGemvDiscontiguousDWS SPI: Expected input pointers to be non-null"
+ "BNNSSGemvDiscontiguousDWS SPI: Expected y buffer to be padded at least 256Bytes multiple"
+ "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_AMX1_S32_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_AMX2_S32_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_DEPTHWISE_OW128_IOC448_AMX3"
+ "non_zero op shape deduction resolved to zero in the first axis, which breaks other ops downstream."

```
