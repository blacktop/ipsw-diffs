## libCoreFSCache.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x5a44
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x29a
-  __TEXT.__oslogstring: 0xb9a
-  __TEXT.__unwind_info: 0x230
+404.1.1.0.0
+  __TEXT.__text: 0x5cb4
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x29c
+  __TEXT.__oslogstring: 0xcbd
+  __TEXT.__unwind_info: 0x240
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x58
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 118
+  Functions: 122
   Symbols:   119
-  CStrings:  83
+  CStrings:  88
 
CStrings:
+ "Unexpected: in-memory page-aligned size: %zu is larger than read-only on-disk file size: %zu by more than a page. Page size is %zu."
+ "fopen for resetting cache not permitted on read-only cache file."
+ "r"
+ "read-only cache is invalid or missing; not reinitializing"
+ "refusing to reset a read-only cache"
```
