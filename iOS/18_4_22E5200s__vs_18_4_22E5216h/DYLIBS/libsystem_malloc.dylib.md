## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-715.100.17.0.0
-  __TEXT.__text: 0x34b38
+715.100.19.502.1
+  __TEXT.__text: 0x34b80
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x50c
-  __TEXT.__cstring: 0x86ae
+  __TEXT.__cstring: 0x88be
   __TEXT.__dof_magmalloc: 0x912
   __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x48

   - /usr/lib/system/libsystem_pthread.dylib
   Functions: 825
   Symbols:   1106
-  CStrings:  777
+  CStrings:  778
 
CStrings:
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist, client likely has a buffer overflow or use-after-free bug"
+ "BUG IN CLIENT OF LIBMALLOC: failed to allocate malloc metadata, out of virtual address space, client likely has a memory leak"
+ "BUG IN CLIENT OF LIBMALLOC: pointer zone mismatch, client may be passing the wrong malloc zone"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5651)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5026)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5700)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3976)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5786)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6380)"
+ "DeltaForceClient"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - cookie"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - free count"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - inconsistent walk"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny freelist - linkage"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny local freelist"
- "BUG IN CLIENT OF LIBMALLOC: corrupt tiny remote freelist"
- "BUG IN CLIENT OF LIBMALLOC: pointer being reallocated with wrong zone"
- "BUG IN LIBMALLOC: Failed to allocate malloc metadata"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5645)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5020)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5694)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3974)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5780)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6374)"

```
