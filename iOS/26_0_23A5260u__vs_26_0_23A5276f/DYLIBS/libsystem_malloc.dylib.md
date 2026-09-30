## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-778.0.0.0.0
-  __TEXT.__text: 0x36904
-  __TEXT.__auth_stubs: 0x730
+784.0.0.0.0
+  __TEXT.__text: 0x36a30
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__const: 0x4ea
-  __TEXT.__cstring: 0x96ae
+  __TEXT.__cstring: 0x97b7
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x768
-  __AUTH_CONST.__auth_got: 0x398
+  __DATA_CONST.__const: 0x808
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x520
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: DBC396D5-1594-3CF3-848E-3A6EC5C8831D
-  Functions: 838
-  Symbols:   2183
-  CStrings:  843
+  UUID: 61944DCF-4C9B-324C-8087-C78C385063B1
+  Functions: 837
+  Symbols:   2181
+  CStrings:  853
 
Symbols:
+ __malloc_type_zone_malloc_with_options_outlined
+ __malloc_zone_malloc_with_options_outlined
+ __malloc_zone_malloc_with_options_outlined.cold.1
+ __xzm_free_abort
+ _malloc_type_zone_malloc_with_options
+ _malloc_zone_malloc_with_options
+ _os_security_config_get
+ _sanitizer_malloc_type_malloc_noalign_with_options.cold.2
- __malloc_type_zone_malloc_with_options_np_outlined
- __malloc_zone_malloc_with_options_np_outlined
- __malloc_zone_malloc_with_options_np_outlined.cold.1
- _malloc_type_zone_malloc_with_options_np
- _sanitizer_malloc_type_malloc_with_options.cold.1
- _xzm_malloc_zone_free_definite_size_slow.cold.3
CStrings:
+ "            \"behavior\": %u \n"
+ "    \"tail\": %llu, \n"
+ "BUG IN CLIENT OF LIBMALLOC: free to empty or invalid chunk detected (likely double-free)"
+ "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5918)"
+ "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6116)"
+ "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5269)"
+ "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5975)"
+ "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4207)"
+ "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6063)"
+ "HubbleBlastDoorService"
+ "IMTranscoderAgent"
+ "IMTransferAgent"
+ "MediaAnalysisBlastDoorService"
+ "MobileSMS"
+ "TelephonyBlastDoorService"
+ "WalletBlastDoorService"
+ "managedassetsd"
+ "mobilewifitool"
- "            \"behavior\": %u, \n"
- "    \"tail\": %llu \n"
- "BUG IN LIBMALLOC: malloc assertion \"!chunk->xzc_bits.xzcb_preallocated\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5902)"
- "BUG IN LIBMALLOC: malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6100)"
- "BUG IN LIBMALLOC: malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5253)"
- "BUG IN LIBMALLOC: malloc assertion \"retries < 10\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:5959)"
- "BUG IN LIBMALLOC: malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:4191)"
- "BUG IN LIBMALLOC: malloc assertion \"xz\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_malloc.c:6047)"

```
