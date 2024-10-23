## libBNNS.dylib

> `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

```diff

-1361.0.68.0.0
-  __TEXT.__text: 0x55b90c
+1361.60.14.0.1
+  __TEXT.__text: 0x55f98c
   __TEXT.__auth_stubs: 0x7d0
   __TEXT.__gcc_except_tab: 0x1d58
   __TEXT.__const: 0x98a0
-  __TEXT.__cstring: 0x1105a
-  __TEXT.__unwind_info: 0x5178
-  __TEXT.__eh_frame: 0x8210
+  __TEXT.__cstring: 0x11305
+  __TEXT.__unwind_info: 0x51b8
+  __TEXT.__eh_frame: 0x82c8
   __DATA.__auth_got: 0x3f0
   __DATA.__got: 0xb8
   __DATA.__auth_ptr: 0x250

   - /System/ExclaveKit/System/Library/Frameworks/MobileGestalt.framework/MobileGestalt
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
-  Functions: 6703
+  Functions: 6722
   Symbols:   285
-  CStrings:  1400
+  CStrings:  1414
 
CStrings:
+ "BNNS Graph: NULL pointer isn't expected"
+ "BNNS Graph: conv encountered NaN, execution failed"
+ "BNNS Graph: conv op values changed, execution failed"
+ "BNNS Graph: ffn encountered NaN, execution failed"
+ "BNNS Graph: ffn op values changed, execution failed"
+ "BNNS Graph: ffn_norm encountered NaN, execution failed"
+ "BNNS Graph: layer norm encountered NaN, execution failed"
+ "BNNS Graph: layer norm op values changed, execution failed"
+ "BNNS Graph: mha encountered NaN, execution failed"
+ "BNNS Graph: mha op values changed, execution failed"
+ "BasicNeuralNetworkSubroutines_exclavekit-1361.60.14.0.1~175"
+ "KERNEL_TTS_SOUNDSTORM_ENCODER_CROSS_MHA"
+ "KERNEL_TTS_SOUNDSTORM_ENCODER_FFN_MF_SILU"
+ "KERNEL_TTS_SOUNDSTORM_ENCODER_FFN_SILU"
+ "KERNEL_TTS_SOUNDSTORM_ENCODER_ROPE_MHA"
- "BasicNeuralNetworkSubroutines_exclavekit-1361.0.68~1240"

```
