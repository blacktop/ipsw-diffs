## libsystem_malloc_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-715.102.2.0.0
-  __TEXT.__text: 0x41688
+715.120.10.0.0
+  __TEXT.__text: 0x41800
   __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__cstring: 0xc20f
+  __TEXT.__cstring: 0xc220
   __TEXT.__const: 0x368
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__unwind_info: 0x328
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0x10
   __AUTH_CONST.__auth_got: 0xf8

   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
   Functions: 344
   Symbols:   405
-  CStrings:  393
+  CStrings:  394
 
CStrings:
+ "DefaultXzoneZone"
+ "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7462)"
- "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:7448)"

```
