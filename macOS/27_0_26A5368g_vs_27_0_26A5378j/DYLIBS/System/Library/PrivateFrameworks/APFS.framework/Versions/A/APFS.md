## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

```diff

-  __TEXT.__text: 0x57d14
-  __TEXT.__const: 0x8580
-  __TEXT.__cstring: 0xebe9
-  __TEXT.__oslogstring: 0x174b
+  __TEXT.__text: 0x56e28
+  __TEXT.__const: 0x8540
+  __TEXT.__cstring: 0xe9f3
+  __TEXT.__oslogstring: 0x1467
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0xa60
+  __TEXT.__unwind_info: 0xa38
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x528
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x14e0
   __AUTH_CONST.__weak_auth_got: 0x8
-  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__auth_got: 0x688
+  __AUTH.__data: 0x148
   __DATA.__data: 0x9c
-  __DATA.__bss: 0x60
-  __DATA.__common: 0x420
-  __DATA_DIRTY.__data: 0x148
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x418
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 942
-  Symbols:   1280
-  CStrings:  1635
+  Functions: 930
+  Symbols:   1257
+  CStrings:  1610
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
Symbols:
- _BC_fetch_omaps_for_all_mounts
- _BC_fetch_omaps_for_mount_cache_entry
- _BC_free_history
- _BC_free_omap_history
- _BC_jettison
- _BC_stop_and_fetch
- _BC_stop_omap_recording_for_all_mounts
- _BC_stop_omap_recording_for_mount_cache_entry
- __clear_apfs_mount_cache_locked
- _bc_log_stream
- _copy_apfs_mount_cache
- _fwrite
- _g_apfs_mount_cache
- _g_apfs_mount_cache_lock
- _g_mountbufs
- _get_volume_uuid
- _getattrlist
- _getmntinfo_r_np
- _notify_post
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _reallocf
- _stop_and_clear_bootcache
CStrings:
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CAjzV9/Sources/apfs_framework/nx/obj.c"
+ "3283.0.9.501.1"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s failed to allocate block from internal pool: %d\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cg4QzQ/Sources/apfs_framework/nx/obj.c"
- "/dev/%s"
- "3283"
- "apfs"
- "com.apple.system.private.bootcache.done"
- "kern.BootCache"
- "libBootCache: Failed to allocate BC_omap_history: %d %s\n"
- "libBootCache: Failed to allocate BC_omap_history: %{errno}d"
- "libBootCache: Failed to allocate bufs for otr records: %d %s\n"
- "libBootCache: Failed to allocate bufs for otr records: %{errno}d"
- "libBootCache: Failed to fetch omaps for mount %s: %d %s\n"
- "libBootCache: Failed to fetch omaps for mount %s: %{errno}d"
- "libBootCache: Unable to realloc more apfs_omap_record_ts"
- "libBootCache: Unable to realloc more apfs_omap_record_ts\n"
- "libBootCache: Unable to realloc more oh_mounts"
- "libBootCache: Unable to realloc more oh_mounts\n"
- "libBootCache: Unable to stop omap recording for %s: %d %s\n"
- "libBootCache: Unable to stop omap recording for %s: %{errno}d"
- "libBootCache: control structure wrong size, version mismatch?"
- "libBootCache: control structure wrong size, version mismatch?\n"
- "libBootCache: could not allocate history mounts memory"
- "libBootCache: could not allocate history mounts memory\n"
- "libBootCache: could not allocate history struct memory"
- "libBootCache: could not allocate history struct memory\n"
- "libBootCache: could not fetch %u and %u bytes of history: %d %s\n"
- "libBootCache: could not fetch %u and %u bytes of history: %{errno}d"
- "libBootCache: could not jettison cache: %d %s\n"
- "libBootCache: could not jettison cache: %{errno}d"
- "libBootCache: could not stop cache: %d %s\n"
- "libBootCache: could not stop cache: %{errno}d"
- "libBootCache: unable to determine uuid for volume %s"
- "libBootCache: unable to determine uuid for volume %s\n"

```
