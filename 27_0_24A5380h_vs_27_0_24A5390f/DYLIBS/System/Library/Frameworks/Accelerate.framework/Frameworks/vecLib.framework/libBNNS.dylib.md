## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib`

### Sections with Same Size but Changed Content

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

-2212.0.4.0.0
-  __TEXT.__text: 0x113f1d4
+2212.0.8.0.0
+  __TEXT.__text: 0x114095c
   __TEXT.__const: 0x6323c
-  __TEXT.__gcc_except_tab: 0x2e95c
-  __TEXT.__cstring: 0x5fc50
+  __TEXT.__gcc_except_tab: 0x2e960
+  __TEXT.__cstring: 0x5fcd4
   __TEXT.__oslogstring: 0x3a6
-  __TEXT.__unwind_info: 0x1c150
+  __TEXT.__unwind_info: 0x1c180
   __TEXT.__eh_frame: 0xdae0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x6da0

   - /System/Library/PrivateFrameworks/MIL.framework/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 39486
+  Functions: 39492
   Symbols:   827
-  CStrings:  8722
+  CStrings:  8723
 
CStrings:
+ "BasicNeuralNetworkSubroutines-2212.0.8~25"
+ "ConvertInvokeOp: invoke op passes a token/state argument to its callee, but BNNS only supports tensor arguments in callee functions"
- "BasicNeuralNetworkSubroutines-2212.0.4~20"
```
