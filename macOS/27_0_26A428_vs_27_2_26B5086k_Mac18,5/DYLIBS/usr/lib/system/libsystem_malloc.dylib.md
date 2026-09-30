## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-886.0.8.0.0
-  __TEXT.__text: 0x46020
+886.40.15.0.0
+  __TEXT.__text: 0x46340
   __TEXT.__const: 0x6ff
-  __TEXT.__cstring: 0xb9d1
+  __TEXT.__cstring: 0xbb15
   __TEXT.__dof_magmalloc: 0xa96
-  __TEXT.__unwind_info: 0xb98
+  __TEXT.__unwind_info: 0xba0
   __TEXT.__eh_frame: 0x48
   __TEXT.__auth_stubs: 0x7b0
   __DATA_CONST.__const: 0xa28

   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xc0
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x64
+  __DATA.__common: 0x54
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0xb8
-  __DATA_DIRTY.__common: 0x22c
+  __DATA_DIRTY.__common: 0x234
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 977
-  Symbols:   1306
-  CStrings:  1011
+  Functions: 982
+  Symbols:   1310
+  CStrings:  1017
 
Symbols:
+ medium_try_realloc_in_place
+ small_try_realloc_in_place
+ tiny_free_no_lock
+ tiny_try_realloc_in_place
CStrings:
+ "    \"buffer_len\": %u, \n"
+ "    \"max_len\": %u, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:982)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7548)"
+ "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:8331)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7872)"
+ "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7764)"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:1033)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6854)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2603)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7608)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2216)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5356)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:1031)"
+ "Invalid size %zu for ptr %p\n"
+ "medium free list metadata inconsistency (bad next_msize)"
+ "medium free list metadata inconsistency (previous_msize > index)"
+ "small free list metadata inconsistency (bad next_msize)"
+ "small free list metadata inconsistency (previous_msize > index)"
+ "tiny free list metadata inconsistency (bad next_msize)"
- "    \"buffer_len\": %llu, \n"
- "    \"max_len\": %llu, \n"
- "BUG IN LIBMALLOC: malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:981)"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7524)"
- "BUG IN LIBMALLOC: malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:8293)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7834)"
- "BUG IN LIBMALLOC: malloc assertion \"gxz.xz\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7726)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:995)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:6830)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2584)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:7584)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:2197)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_malloc.c:5336)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc/src/xzone_malloc/xzone_introspect.c:993)"
```
