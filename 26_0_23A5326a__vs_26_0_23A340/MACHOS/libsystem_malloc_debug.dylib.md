## libsystem_malloc_debug.dylib

> `/System/ExclaveKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

 792.0.2.0.0
-  __TEXT.__text: 0x4602c
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__cstring: 0xd481
+  __TEXT.__text: 0x4c410
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__cstring: 0xd8c4
   __TEXT.__const: 0x228
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__unwind_info: 0x360
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0x1d8
   __AUTH.__data: 0x88
   __DATA.__data: 0x8
   __DATA.__bss: 0x148
-  __DATA.__common: 0x24
+  __DATA.__common: 0x28
   - /System/ExclaveKit/usr/lib/system/liblibc.dylib
   - /System/ExclaveKit/usr/lib/system/liblibc_plat.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_blocks.dylib
-  UUID: 7A34616B-3B5E-39C3-956D-685762AAE6BB
-  Functions: 350
-  Symbols:   406
-  CStrings:  424
+  UUID: 112E79D8-199C-319E-85DE-41009D7E05F2
+  Functions: 359
+  Symbols:   419
+  CStrings:  432
 
Symbols:
+ ____chkstk_darwin
+ ___chkstk_darwin
+ ___chkstk_darwin_probe
+ ___mfm_block_fixup_ptr
+ __xzm_xzone_block_memtag_retag
+ __xzm_xzone_chunk_memtag_init
+ _malloc_has_sec_transition
+ _malloc_sec_transition_policy
+ _memtag_assign_tag
+ _memtag_handle_mismatch
+ _memtag_init_chunk
+ _mfm_memtag_enabled
+ _xrt__has_sec_transition
CStrings:
+ "BUG IN CLIENT OF LIBMALLOC (%llu): MTE tag mismatch"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6807)"
+ "malloc assertion \"memtag_config.max_block_size == XZM_SMALL_BLOCK_SIZE_MAX\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:6808)"
+ "malloc assertion \"memtag_strip_address(ptr) != ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3637)"
+ "malloc assertion \"memtag_strip_address(ptr) == ptr\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:3639)"
+ "malloc assertion \"ptr == memtag_fixup_ptr(ptr)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:2045)"
+ "malloc assertion \"tag != 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:1029)"
+ "malloc assertion \"xz->xz_tagged == chunk->xzc_tagged\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_exclavekit/src/xzone/xzone_malloc.c:4620)"

```
