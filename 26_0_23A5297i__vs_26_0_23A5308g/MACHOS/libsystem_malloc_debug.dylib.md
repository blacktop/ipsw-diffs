## libsystem_malloc_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-792.0.0.0.0
-  __TEXT.__text: 0x46028
+792.0.2.0.0
+  __TEXT.__text: 0x4602c
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__cstring: 0xd481
   __TEXT.__const: 0x228

   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc_plat.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
-  UUID: DE4DA50C-AD11-31EE-BCA2-9B60BDBCEFB1
+  UUID: 7A34616B-3B5E-39C3-956D-685762AAE6BB
   Functions: 350
   Symbols:   406
   CStrings:  424
Functions:
~ _xzm_metapool_alloc : 1096 -> 1100
CStrings:
+ "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:8150)"
- "malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:8149)"

```
