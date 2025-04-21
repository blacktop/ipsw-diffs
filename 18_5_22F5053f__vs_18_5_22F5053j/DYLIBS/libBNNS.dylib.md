## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

```diff

-1497.120.3.0.0
-  __TEXT.__text: 0xa12944
-  __TEXT.__auth_stubs: 0x1230
-  __TEXT.__gcc_except_tab: 0x2b440
+1497.120.5.0.0
+  __TEXT.__text: 0xa12694
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__gcc_except_tab: 0x2b454
   __TEXT.__const: 0x1526f
-  __TEXT.__cstring: 0x2c4b0
+  __TEXT.__cstring: 0x2c7fe
   __TEXT.__oslogstring: 0x303
   __TEXT.__unwind_info: 0xb868
   __TEXT.__eh_frame: 0xbc48
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x3a40
-  __AUTH_CONST.__auth_got: 0x920
+  __AUTH_CONST.__auth_got: 0x928
   __AUTH_CONST.__auth_ptr: 0x310
   __AUTH_CONST.__const: 0xf820
   __AUTH_CONST.__cfstring: 0x200

   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 11547
-  Symbols:   612
-  CStrings:  4299
+  Functions: 11548
+  Symbols:   614
+  CStrings:  4313
 
Symbols:
+ _BNNSGraphContextMakeWithLogging
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
CStrings:
+ "BNNS Graph: conv op values changed, execution failed (1)"
+ "BNNS Graph: conv op values changed, execution failed (2)"
+ "BNNS Graph: ffn op values changed, execution failed (1)"
+ "BNNS Graph: ffn op values changed, execution failed (2)"
+ "BNNS Graph: ffn op values changed, execution failed (3)"
+ "BNNS Graph: layer norm encountered NaN, execution failed. (1)"
+ "BNNS Graph: layer norm encountered NaN, execution failed. (2)"
+ "BNNS Graph: layer norm op values changed, execution failed. (1)"
+ "BNNS Graph: layer norm op values changed, execution failed. (2)"
+ "BNNS Graph: layer norm op values changed, execution failed. (3)"
+ "BNNS Graph: layer norm op values changed, execution failed. (4)"
+ "BNNS Graph: mha op values changed, execution failed (1)"
+ "BNNS Graph: mha op values changed, execution failed (2)"
+ "BNNS Graph: mha op values changed, execution failed (3)"
+ "BNNS Graph: null pointer not expected"
+ "BNNS Graph: null pointer not expected (1)"
+ "BNNS Graph: null pointer not expected (2)"
+ "BNNS Graph: null pointer not expected (3)"
+ "BNNS: BNNSGraphContextMakeWithLogging failed to allocate memory"
+ "BNNS: BNNSGraphContextMakeWithLogging failed to initialize context"
+ "BNNS: BNNSGraphContextMakeWithLogging passed graph with unsupported ir_version "
+ "BNNS: BNNSGraphContextMakeWithLogging passed invalid graph"
+ "BNNSGraphContextMakeWithLogging"
+ "BasicNeuralNetworkSubroutines-1497.120.5~111"
- "BNNS Graph: conv op values changed, execution failed"
- "BNNS Graph: ffn encountered NaN, execution failed"
- "BNNS Graph: ffn op values changed, execution failed"
- "BNNS Graph: ffn_norm encountered NaN, execution failed"
- "BNNS Graph: layer norm encountered NaN, execution failed."
- "BNNS Graph: layer norm op values changed, execution failed."
- "BNNS Graph: mha encountered NaN, execution failed"
- "BNNS Graph: mha op values changed, execution failed"
- "BNNSGraphContextMake"
- "BasicNeuralNetworkSubroutines-1497.120.3~19"

```
