## libCoreFSCache.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib`

```diff

-  __TEXT.__text: 0x5e10
+  __TEXT.__text: 0x6084
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x29a
-  __TEXT.__oslogstring: 0xb9a
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x29c
+  __TEXT.__oslogstring: 0xcbd
+  __TEXT.__unwind_info: 0x138
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x58
   __AUTH_CONST.__auth_got: 0x1a8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 122
-  Symbols:   293
-  CStrings:  84
+  Functions: 127
+  Symbols:   303
+  CStrings:  89
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Symbols:
+ _OUTLINED_FUNCTION_9
CStrings:
+ "Unexpected: in-memory page-aligned size: %zu is larger than read-only on-disk file size: %zu by more than a page. Page size is %zu."
+ "fopen for resetting cache not permitted on read-only cache file."
+ "r"
+ "read-only cache is invalid or missing; not reinitializing"
+ "refusing to reset a read-only cache"

```
