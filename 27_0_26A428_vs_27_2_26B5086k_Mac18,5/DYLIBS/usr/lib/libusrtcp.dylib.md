## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-6681.1.1.0.0
-  __TEXT.__text: 0x5b9d0
+6681.40.80.0.0
+  __TEXT.__text: 0x5bbac
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe6be
-  __TEXT.__cstring: 0x1a8e
+  __TEXT.__oslogstring: 0xe794
+  __TEXT.__cstring: 0x1aab
   __TEXT.__unwind_info: 0x5b8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x268
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x1f0
+  __AUTH.__data: 0x1a0
   __DATA.__data: 0x10
-  __DATA_DIRTY.__data: 0x188
+  __DATA_DIRTY.__data: 0x1d8
   __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 339
   Symbols:   668
-  CStrings:  1120
+  CStrings:  1125
 
Functions:
~ _nw_tcp_destroy_globals : 276 -> 736
~ _tcp_input : 37964 -> 37980
CStrings:
+ "%{public}s called with null globals"
+ "%{public}s called with null globals, backtrace limit exceeded"
+ "%{public}s called with null globals, dumping backtrace:%{public}s"
+ "%{public}s called with null globals, no backtrace"
+ "tcp_heuristics_cache_destroy"
```
