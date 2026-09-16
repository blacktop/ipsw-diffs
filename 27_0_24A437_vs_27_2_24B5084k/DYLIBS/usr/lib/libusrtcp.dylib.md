## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-6681.2.2.0.0
-  __TEXT.__text: 0x5b5cc
+6681.40.80.0.0
+  __TEXT.__text: 0x5b798
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe6be
-  __TEXT.__cstring: 0x1a8e
+  __TEXT.__oslogstring: 0xe794
+  __TEXT.__cstring: 0x1aab
   __TEXT.__unwind_info: 0x5c8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x410

   - /usr/lib/libobjc.A.dylib
   Functions: 335
   Symbols:   659
-  CStrings:  1120
+  CStrings:  1125
 
Functions:
~ _nw_tcp_destroy_globals : 276 -> 736
CStrings:
+ "%{public}s called with null globals"
+ "%{public}s called with null globals, backtrace limit exceeded"
+ "%{public}s called with null globals, dumping backtrace:%{public}s"
+ "%{public}s called with null globals, no backtrace"
+ "tcp_heuristics_cache_destroy"
```
