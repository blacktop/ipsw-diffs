## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-646.0.10.0.0
-  __TEXT.__text: 0x3116c
+646.40.1.0.0
+  __TEXT.__text: 0x31770
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__const: 0x4fc
-  __TEXT.__cstring: 0x76db
+  __TEXT.__cstring: 0x7683
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x6b0

   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xb9
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x415d
+  __DATA.__bss: 0x4155
   __DATA.__common: 0x58
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__common: 0x1e0
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__common: 0x1f0
+  __DATA_DIRTY.__bss: 0xa0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 771
+  Functions: 784
   Symbols:   1010
   CStrings:  704
 
Symbols:
+ _xzm_type_choose_ptr_bucket_4test
CStrings:
+ "\"bucketing_key\": \"%!l(MISSING)lx%!l(MISSING)lx\", \n"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4039)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3472)"
+ "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1114)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4085)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2724)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:805)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4172)"
+ "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4732)"
+ "Corruption of tiny freelist %!p(MISSING): size too small (%!u(MISSING)/%!u(MISSING))\n"
- "\"boot_random\": %!u(MISSING), \n"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3955)"
- "BUG IN LIBMALLOC: malloc assertion \"boothash_prefix_value <= UINT32_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4539)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:3388)"
- "BUG IN LIBMALLOC: malloc assertion \"prev_slot_value == slot_meta.xasa_value\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:1030)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4001)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:2640)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:721)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4088)"
- "BUG IN LIBMALLOC: malloc assertion \"xzone_count <= UINT8_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4638)"

```
