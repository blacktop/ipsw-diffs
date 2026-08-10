## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-2212.0.8.0.0
-  __TEXT.__text: 0x114095c
+2212.0.11.0.0
+  __TEXT.__text: 0x1140ee8
   __TEXT.__const: 0x6323c
   __TEXT.__gcc_except_tab: 0x2e960
-  __TEXT.__cstring: 0x5fcd4
+  __TEXT.__cstring: 0x5fd52
   __TEXT.__oslogstring: 0x3a6
-  __TEXT.__unwind_info: 0x1c180
+  __TEXT.__unwind_info: 0x1c190
   __TEXT.__eh_frame: 0xdae0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x6da0

   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 39492
+  Functions: 39495
   Symbols:   827
-  CStrings:  8723
+  CStrings:  8726
 
CStrings:
+ "BNNS Fully Connected Sparsify: failed to allocate workspace"
+ "BasicNeuralNetworkSubroutines-2212.0.11~189"
+ "KERNEL_COPY_DYNAMIC_MLA_OR_NEON"
+ "KERNEL_COPY_DYNAMIC_SME_OR_NEON"
- "BasicNeuralNetworkSubroutines-2212.0.8~25"
```
