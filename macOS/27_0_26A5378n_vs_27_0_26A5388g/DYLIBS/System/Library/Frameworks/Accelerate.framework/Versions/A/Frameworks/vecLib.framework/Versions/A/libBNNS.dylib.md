## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib`

### Sections with Same Size but Changed Content

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

-2212.0.4.0.0
-  __TEXT.__text: 0x10f9efc
+2212.0.8.0.0
+  __TEXT.__text: 0x10fb594
   __TEXT.__const: 0x631bc
   __TEXT.__gcc_except_tab: 0x2f29c
-  __TEXT.__cstring: 0x5c27d
+  __TEXT.__cstring: 0x5c301
   __TEXT.__oslogstring: 0x3a6
-  __TEXT.__unwind_info: 0x1c158
+  __TEXT.__unwind_info: 0x1c170
   __TEXT.__eh_frame: 0xdba0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x5608

   - /System/Library/PrivateFrameworks/MIL.framework/Versions/A/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 39477
+  Functions: 39483
   Symbols:   827
-  CStrings:  8675
+  CStrings:  8676
 
CStrings:
+ "BasicNeuralNetworkSubroutines-2212.0.8~23"
+ "ConvertInvokeOp: invoke op passes a token/state argument to its callee, but BNNS only supports tensor arguments in callee functions"
- "BasicNeuralNetworkSubroutines-2212.0.4~21"
```
