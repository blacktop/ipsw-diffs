## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2332.120.31.0.2
-  __TEXT.__text: 0x36508
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__const: 0x390
-  __TEXT.__cstring: 0x7091
-  __TEXT.__oslogstring: 0x1637
-  __TEXT.__unwind_info: 0x6a8
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x728
-  __DATA_CONST.__cfstring: 0xda0
+2632.0.15.0.1
+  __TEXT.__text: 0x39c14
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__const: 0x3c0
+  __TEXT.__oslogstring: 0x1e12
+  __TEXT.__cstring: 0x74f9
+  __TEXT.__unwind_info: 0x6e8
+  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__cfstring: 0xf00
   __DATA.__data: 0x150
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   __DATA.__common: 0x64
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: EF0D9506-B8AF-3A66-B136-CA1D0BBF0C9B
-  Functions: 598
-  Symbols:   217
-  CStrings:  985
+  UUID: 4C40D1ED-527A-33C6-BEF1-240BB6245E91
+  Functions: 640
+  Symbols:   232
+  CStrings:  1093
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayRemoveValueAtIndex
+ _CFBooleanGetTypeID
+ _XPC_ACTIVITY_INTERVAL
+ ___assert_rtn
+ __os_log_default
+ _ffsctl
+ _fts_set
+ _kCFTypeSetCallBacks
+ _mkdir
+ _strdup
+ _sysctlbyname
+ _xpc_activity_copy_criteria
+ _xpc_activity_set_completion_status
+ _xpc_activity_set_criteria
- _uuid_is_null
CStrings:
+ "%s:%d: %s entitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
+ "%s:%d: dir %llu no longer has a desired urgency\n"
+ "%s:%d: done err = %d\n"
+ "%s:%d: expected file %llu but got mode %#o ino %llu\n"
+ "%s:%d: expected inode entry but got extent %#llx:+%#llx\n"
+ "%s:%d: expected inode entry but got nothing\n"
+ "%s:%d: failed get bulk purgeable extents: %s (%d)\n"
+ "%s:%d: failed to allocate memory for extent iterator\n"
+ "%s:%d: failed to disable rapid-aging vnodes: %s (%d)\n"
+ "%s:%d: failed to enable rapid-aging vnodes: %s (%d)\n"
+ "%s:%d: failed to fts_read(): %s (%d)\n"
+ "%s:%d: failed to get fd for fts: %s (%d)\n"
+ "%s:%d: failed to get path for ino %llu: %s (%d)\n"
+ "%s:%d: failed to get purgeable extents for file %llu: %s (%d)\n"
+ "%s:%d: failed to get purgeable info for ino %llu: %s (%d)\n"
+ "%s:%d: failed to iterate purgeable extents of dir %llu: %s (%d)\n"
+ "%s:%d: failed to open fts on ino %llu: %s (%d)\n"
+ "%s:%d: failed to process purgeable extents of file %llu: %s (%d)\n"
+ "%s:%d: failed to read fd from fts: %s (%d)\n"
+ "%s:%d: failed to skip fts for ino %llu: %s (%d)\n"
+ "%s:%d: failed to statfs(%s): %s (%d)\n"
+ "%s:%d: failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
+ "%s:%d: fts_read() returned error: %s (%d)\n"
+ "%s:%d: invalid arguments\n"
+ "%s:%d: no stat info requested\n"
+ "%s:%d: ordered iteration must be reset once finished\n"
+ "%s:%d: processing dir %llu\n"
+ "%s:%d: processing file %llu with %u extents\n"
+ "%s:%d: skipping already seen file %llu\n"
+ "%s:%d: skipping already seen ino %llu\n"
+ "%s:%d: stop iteration requested\n"
+ "%s:%d: unexpected mode %#o for ino %llu\n"
+ "%s:%d: urgency %#06x done\n"
+ "(ent->fts_info == FTS_D) || (ent->fts_info == FTS_F)"
+ "/var/mobile/Library/Caches/com.apple.apfs_iosd/"
+ "/var/mobile/Library/Caches/com.apple.apfs_iosd/extents_%s_%llu.txt"
+ "Backup"
+ "Baseband data"
+ "Cache"
+ "DONE (PENDING_WORK): Suspending hint extents activity until next interval"
+ "DONE (PENDING_WORK): Suspending hint extents activity until next interval\n"
+ "Data"
+ "Enterprise data"
+ "Hardware"
+ "Installer"
+ "Overprovision"
+ "Preboot"
+ "Recovery"
+ "SideCar"
+ "System"
+ "Update"
+ "User"
+ "VM"
+ "Volume: %s Cursor: %llu Urgencies: %#x Ordered: %d\n"
+ "a"
+ "activity asked to defer, stopping activity"
+ "activity asked to defer, stopping activity\n"
+ "apfs-clonegroup-lock-mutex"
+ "apfs_hint_extents_dump_interval"
+ "authapfs_validate_node"
+ "cursor"
+ "dir"
+ "end_state"
+ "end_uptime"
+ "error_loc"
+ "events"
+ "extents"
+ "failed to append extent to log: %s (%d)\n"
+ "failed to create event dictionary"
+ "failed to create event dictionary\n"
+ "failed to create purgeable extent iterator: %s (%d)\n"
+ "failed to create state dictionary"
+ "failed to create state dictionary\n"
+ "failed to record event"
+ "failed to record event\n"
+ "failed to set hint extents activity state to DONE (PENDING_WORK)"
+ "failed to set hint extents activity state to DONE (PENDING_WORK)\n"
+ "failed to set up cache directory: %s (%d)\n"
+ "fts_openbyid_"
+ "fts_read_fd_"
+ "hit activity timeout, stopping activity"
+ "hit activity timeout, stopping activity\n"
+ "hit volume timeout, continuing to next volume"
+ "hit volume timeout, continuing to next volume\n"
+ "i8@?0"
+ "iDiags"
+ "iterate_purgeable_extents"
+ "iterate_purgeable_extents_of_directory"
+ "kern.rage_vnode"
+ "make_purgeable_extents_iterator"
+ "no boot-arg, defaulting to %s=%u\n"
+ "none"
+ "nx_reaper_add_ext"
+ "ordered"
+ "purging_util.c"
+ "start_state"
+ "start_uptime"
+ "state"
+ "unknown"
+ "urgencies"
+ "xART"
- "DEFERRING hint extents activity"
- "DEFERRING hint extents activity\n"
- "Volume: %s Cursor: %llu\n"
- "failed to set hint extents activity state to DEFER"
- "failed to set hint extents activity state to DEFER\n"
- "failed to validate node %p (oid:%llu, xid:%llu) of fs %p (%llu) - %d\n"
- "nx-fusion-mt-lock"
- "nx_rc_allocation_lock"
- "nx_reaper_add"

```
