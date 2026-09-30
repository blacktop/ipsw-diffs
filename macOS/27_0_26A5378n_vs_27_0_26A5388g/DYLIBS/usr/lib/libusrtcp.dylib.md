## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-6681.0.498.501.1
-  __TEXT.__text: 0x5b854
-  __TEXT.__const: 0x254
+6681.0.514.0.4
+  __TEXT.__text: 0x5b988
+  __TEXT.__const: 0x244
   __TEXT.__oslogstring: 0xe6be
   __TEXT.__cstring: 0x1a8e
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x418
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 337
-  Symbols:   666
+  Functions: 338
+  Symbols:   667
   CStrings:  1120
 
Symbols:
+ _nw_protocol_tcp_initialize_failed
Functions:
~ _nw_protocol_tcp_initialize : 4876 -> 5020
+ _nw_protocol_tcp_initialize_failed
```
