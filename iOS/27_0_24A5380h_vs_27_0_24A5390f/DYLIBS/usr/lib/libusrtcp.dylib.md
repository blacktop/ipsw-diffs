## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-6681.0.498.502.1
-  __TEXT.__text: 0x5b420
+6681.0.514.502.1
+  __TEXT.__text: 0x5b554
   __TEXT.__const: 0x244
   __TEXT.__oslogstring: 0xe6be
   __TEXT.__cstring: 0x1a8e

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 333
-  Symbols:   657
+  Functions: 334
+  Symbols:   658
   CStrings:  1120
 
Symbols:
+ _nw_protocol_tcp_initialize_failed
Functions:
~ _nw_protocol_tcp_initialize : 4876 -> 5020
+ _nw_protocol_tcp_initialize_failed
```
