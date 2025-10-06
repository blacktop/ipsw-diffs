## libsystem_malloc_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-792.40.5.0.0
-  __TEXT.__text: 0xa87ec
-  __TEXT.__auth_stubs: 0x740
+792.40.10.0.0
+  __TEXT.__text: 0xa5c44
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__const: 0x4bc
-  __TEXT.__cstring: 0x1bf5c
+  __TEXT.__cstring: 0x1bd7b
   __TEXT.__dof_magmalloc: 0x8c7
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x118
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x6d0
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0x11c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x21ac
+  __DATA.__bss: 0x219c
   __DATA.__common: 0x248
   - /System/DriverKit/usr/lib/system/libcompiler_rt.dylib
   - /System/DriverKit/usr/lib/system/libcorecrypto.dylib

   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: 40DFCD57-310B-3AB6-B154-06952B5C0597
-  Functions: 1067
-  Symbols:   1367
-  CStrings:  1276
+  UUID: 7588D70A-71BA-3B0C-9B01-6F22A2AE656A
+  Functions: 1057
+  Symbols:   1353
+  CStrings:  1264
 
Symbols:
- _NSVersionOfLinkTimeLibrary
- _large_cache_enabled
- _large_clear_cache_locked
- _large_deallocate_cache_entry
- _large_destroy_cache
- _large_malloc_best_fit_in_cache
- _large_malloc_from_cache
- _mvm_deferred_reclaim_init
- _mvm_reclaim_is_available
- _mvm_reclaim_mark_free
- _mvm_reclaim_mark_used
- _reclaim_buffer
- _reclaim_buffer_lock
- _remove_from_death_row_no_lock
CStrings:
+ ", madvised"
+ "BUG IN LIBMALLOC: malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:8163)"
+ "BUG IN LIBMALLOC: malloc assertion \"rg_idx < main->xzmz_range_group_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:7883)"
+ "BUG IN LIBMALLOC: malloc assertion \"sg->xzsg_id == XZM_SEGMENT_GROUP_POINTER_XZONES\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:7879)"
+ "Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tScribble: %d\n"
- "\tCurrent size:\t\t%y\n\tReserve size:\t\t%y\n\tReserve limit:\t\t%y\n"
- "\nLarge allocator death row cache, %d entries\n\tMax cached size:\t%y\n"
- " (ERROR)"
- "*** can't reset protection for large freed block at %p\n"
- "*** can't vm_purgable_control(..., VM_PURGABLE_SET_STATE) for large freed block at %p\n"
- ", kernel reclaimed"
- "BUG IN LIBMALLOC: malloc assertion \"new_zone != NULL\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:8153)"
- "BUG IN LIBMALLOC: malloc assertion \"rg_idx < main->xzmz_range_group_count\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:7873)"
- "BUG IN LIBMALLOC: malloc assertion \"sg->xzsg_id == XZM_SEGMENT_GROUP_POINTER_XZONES\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc_driverkit/src/xzone/xzone_malloc.c:7869)"
- "Invalid best: %d\n"
- "Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tLarge Cache: %d%s\n\tScribble: %d\n"
- "MallocDeferredReclaim=1"
- "System"
- "Unable to set up reclaim buffer, disabling large cache [%d] %s\n"
- "[newest]"
- "[oldest]"
- "pointer %p being freed already on death-row\n"

```
