## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-792.40.5.0.0
-  __TEXT.__text: 0x38a04
-  __TEXT.__auth_stubs: 0x740
+792.40.10.0.0
+  __TEXT.__text: 0x3783c
+  __TEXT.__auth_stubs: 0x730
   __TEXT.__const: 0x4fa
-  __TEXT.__cstring: 0x9b98
+  __TEXT.__cstring: 0x99c9
   __TEXT.__dof_magmalloc: 0x912
-  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__unwind_info: 0x878
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x808
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x520
   __AUTH.__data: 0x128
   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xb9
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x216d
-  __DATA.__common: 0x88
+  __DATA.__common: 0x68
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__common: 0x200
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__common: 0x218
+  __DATA_DIRTY.__bss: 0x78
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 6BE0B559-1FC6-36FC-88EE-B9804AD492B3
-  Functions: 842
-  Symbols:   2218
-  CStrings:  874
+  UUID: AB7B254D-C256-3141-8ACA-9DA9A79056E6
+  Functions: 832
+  Symbols:   2188
+  CStrings:  864
 
Symbols:
+ _malloc_zone_register_while_locked.cold.1
+ _malloc_zone_register_while_locked.cold.2
- _NSVersionOfLinkTimeLibrary
- _large_cache_enabled
- _large_deallocate_cache_entry
- _large_destroy_cache
- _large_entry_free_no_lock
- _large_entry_free_no_lock.cold.1
- _large_entry_grow_and_insert_no_lock
- _mvm_deferred_reclaim_init
- _mvm_reclaim_is_available
- _mvm_reclaim_is_available.cold.1
- _mvm_reclaim_mark_free
- _mvm_reclaim_mark_free.cold.1
- _mvm_reclaim_mark_free.cold.2
- _mvm_reclaim_mark_free.cold.3
- _mvm_reclaim_mark_used
- _mvm_reclaim_mark_used.cold.1
- _reclaim_buffer
- _reclaim_buffer_lock
- _remove_from_death_row_no_lock
CStrings:
+ ", madvised"
+ "Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tScribble: %d\n"
- "\tCurrent size:\t\t%y\n\tReserve size:\t\t%y\n\tReserve limit:\t\t%y\n"
- "\nLarge allocator death row cache, %d entries\n\tMax cached size:\t%y\n"
- " (ERROR)"
- "*** can't reset protection for large freed block at %p\n"
- "*** can't vm_purgable_control(..., VM_PURGABLE_SET_STATE) for large freed block at %p\n"
- ", kernel reclaimed"
- "Invalid best: %d\n"
- "Magazine Config:\n\tMax Magazines: %d\n\tMedium Enabled: %d\n\tAggressive Madvise: %d\n\tLarge Cache: %d%s\n\tScribble: %d\n"
- "MallocDeferredReclaim=1"
- "System"
- "Unable to set up reclaim buffer, disabling large cache [%d] %s\n"
- "pointer %p being freed already on death-row\n"

```
