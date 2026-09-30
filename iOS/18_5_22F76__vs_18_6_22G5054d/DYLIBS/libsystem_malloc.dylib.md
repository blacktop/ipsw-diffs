## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-715.120.13.0.0
-  __TEXT.__text: 0x34c50
+715.140.5.0.0
+  __TEXT.__text: 0x34c58
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x50c
   __TEXT.__cstring: 0x8970

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: B6554432-3BBE-3AC9-870D-779DCA3F0CB4
+  UUID: E32F9EEA-02F3-35F3-8E1E-EE7DC2E72BDA
   Functions: 825
   Symbols:   2152
   CStrings:  786
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5655)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5030)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5704)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3980)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5790)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6384)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5651)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5026)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5700)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3976)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5786)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6380)"

```
