## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2632.80.1.0.1
-  __TEXT.__text: 0x3a1c8
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__const: 0x3c0
-  __TEXT.__oslogstring: 0x1e12
-  __TEXT.__cstring: 0x74ba
-  __TEXT.__unwind_info: 0x6f8
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x758
-  __DATA_CONST.__cfstring: 0xf00
-  __DATA.__data: 0x150
-  __DATA.__bss: 0x48
-  __DATA.__common: 0x64
+2811.100.177.0.1
+  __TEXT.__text: 0x32e18
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__const: 0x350
+  __TEXT.__cstring: 0x6614
+  __TEXT.__oslogstring: 0x1333
+  __TEXT.__unwind_info: 0x618
+  __DATA_CONST.__auth_got: 0x548
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__cfstring: 0xc80
+  __DATA.__data: 0x9c
+  __DATA.__bss: 0x38
+  __DATA.__common: 0x5c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: 098B2B21-C698-36D4-93ED-F0BBAFEE64D8
-  Functions: 641
-  Symbols:   233
-  CStrings:  1092
+  UUID: C6AED05A-26FE-3330-B44A-AD4648DD149F
+  Functions: 549
+  Symbols:   197
+  CStrings:  875
 
Symbols:
+ __include_codes_in_dsym
+ _unlink
- _CFArrayGetCount
- _CFArrayGetTypeID
- _CFArrayRemoveValueAtIndex
- _CFBooleanGetTypeID
- _CFBooleanGetValue
- _CFEqual
- _CFStringGetTypeID
- _IOObjectRetain
- _IORegistryEntryGetParentIterator
- _XPC_ACTIVITY_INTERVAL
- ___assert_rtn
- _aio_error
- _aio_read
- _aio_return
- _aio_suspend
- _close
- _fcntl
- _ffsctl
- _fstatfs
- _fsync
- _fts_close
- _fts_open
- _fts_read
- _fts_set
- _getmntinfo_r_np
- _ioctl
- _kCFTypeSetCallBacks
- _mkdir
- _open
- _os_parse_boot_arg_int
- _pread
- _pwrite
- _strdup
- _strndup
- _sysctlbyname
- _xpc_activity_copy_criteria
- _xpc_activity_set_completion_status
- _xpc_activity_set_criteria
CStrings:
+ "/Library/Caches/com.apple.xbs/DD28F24C-1931-495A-9115-8546FF886387/TemporaryDirectory.ZQr4xz/Sources/apfs_executables/nx/obj.c"
+ "lookup_jobj_ext"
- "%#16llx %#10llx\n"
- "%16s %10s\n"
- "%s/apfs"
- "%s/apfs_data"
- "%s/nx"
- "%s:%d: %s btree_node_insert_internal failed: %d\n"
- "%s:%d: %s obj_exchange_phys (%llx, %llx) with xid %llu failed: %d\n"
- "%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n"
- "%s:%d: Hit an error flushing the cache, %d dev_name = %s\n"
- "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
- "%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n"
- "%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n"
- "%s:%d: can't get block count (%s)\n"
- "%s:%d: can't get features for device (%s)\n"
- "%s:%d: can't get solidstate for device (%s)\n"
- "%s:%d: can't get the device block size (%s). assuming 512\n"
- "%s:%d: dir %llu no longer has a desired urgency\n"
- "%s:%d: done err = %d\n"
- "%s:%d: expected file %llu but got mode %#o ino %llu\n"
- "%s:%d: expected inode entry but got extent %#llx:+%#llx\n"
- "%s:%d: expected inode entry but got nothing\n"
- "%s:%d: failed get bulk purgeable extents: %s (%d)\n"
- "%s:%d: failed to allocate memory for extent iterator\n"
- "%s:%d: failed to disable rapid-aging vnodes: %s (%d)\n"
- "%s:%d: failed to enable rapid-aging vnodes: %s (%d)\n"
- "%s:%d: failed to fts_read(): %s (%d)\n"
- "%s:%d: failed to get fd for fts: %s (%d)\n"
- "%s:%d: failed to get path for ino %llu: %s (%d)\n"
- "%s:%d: failed to get purgeable extents for file %llu: %s (%d)\n"
- "%s:%d: failed to get purgeable info for ino %llu: %s (%d)\n"
- "%s:%d: failed to iterate purgeable extents of dir %llu: %s (%d)\n"
- "%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n"
- "%s:%d: failed to open container device %s: %s\n"
- "%s:%d: failed to open fts on ino %llu: %s (%d)\n"
- "%s:%d: failed to open volume device %s: %s\n"
- "%s:%d: failed to process purgeable extents of file %llu: %s (%d)\n"
- "%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n"
- "%s:%d: failed to read fd from fts: %s (%d)\n"
- "%s:%d: failed to skip fts for ino %llu: %s (%d)\n"
- "%s:%d: failed to statfs(%s): %s (%d)\n"
- "%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n"
- "%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n"
- "%s:%d: fts_read() returned error: %s (%d)\n"
- "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
- "%s:%d: invalid arguments\n"
- "%s:%d: no stat info requested\n"
- "%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n"
- "%s:%d: ordered iteration must be reset once finished\n"
- "%s:%d: processing dir %llu\n"
- "%s:%d: processing file %llu with %u extents\n"
- "%s:%d: skipping already seen file %llu\n"
- "%s:%d: skipping already seen ino %llu\n"
- "%s:%d: stop iteration requested\n"
- "%s:%d: unexpected mode %#o for ino %llu\n"
- "%s:%d: urgency %#06x done\n"
- "(ent->fts_info == FTS_D) || (ent->fts_info == FTS_F)"
- "/Library/Caches/com.apple.xbs/Sources/apfs_executables/nx/obj.c"
- "/var/mobile/Library/Caches/com.apple.apfs_iosd/"
- "/var/mobile/Library/Caches/com.apple.apfs_iosd/extents_%s_%llu.txt"
- "BSD Major"
- "BSD Minor"
- "Backup"
- "Baseband data"
- "Cache"
- "DONE (PENDING_WORK): Suspending hint extents activity until next interval"
- "DONE (PENDING_WORK): Suspending hint extents activity until next interval\n"
- "DONE: Suspending hint extents activity until next interval"
- "DONE: Suspending hint extents activity until next interval\n"
- "Data"
- "Device Characteristics"
- "Enterprise data"
- "Failed to initialize dispatch queue for hint extents activity"
- "Failed to initialize dispatch queue for hint extents activity\n"
- "Hardware"
- "IOBlockStorageDevice"
- "IOMedia"
- "Installer"
- "Internal"
- "LENGTH"
- "OFFSET"
- "Overprovision"
- "Physical Interconnect Location"
- "Preboot"
- "Protocol Characteristics"
- "Recovery"
- "Removable"
- "START: Initiating hint extents activity"
- "START: Initiating hint extents activity\n"
- "SideCar"
- "System"
- "Target Disk Mode"
- "UNREGISTERING hint extents activity"
- "UNREGISTERING hint extents activity\n"
- "Update"
- "User"
- "VM"
- "Volume: %s Cursor: %llu Urgencies: %#x Ordered: %d\n"
- "_fd_dev_write"
- "a"
- "activity asked to defer, stopping activity"
- "activity asked to defer, stopping activity\n"
- "activity is disabled because no volume supports iteration"
- "activity is disabled because no volume supports iteration\n"
- "activity is disabled because of level"
- "activity is disabled because of level\n"
- "apfs_hint_extents_dump_interval"
- "apfs_hint_extents_level"
- "btree_node_compact"
- "btree_node_copy"
- "com.apple.filesystems.apfs_iosd.hint_extents"
- "com.apple.filesystems.apfs_iosd_hint_extents"
- "cursor"
- "dev_init"
- "dev_init_common"
- "dir"
- "end_state"
- "end_uptime"
- "error_loc"
- "events"
- "extents"
- "failed to append extent to log: %s (%d)\n"
- "failed to create event dictionary"
- "failed to create event dictionary\n"
- "failed to create hints plist URL"
- "failed to create hints plist URL\n"
- "failed to create new plist"
- "failed to create new plist\n"
- "failed to create purgeable extent iterator: %s (%d)\n"
- "failed to create state dictionary"
- "failed to create state dictionary\n"
- "failed to get mount info: %s (%d)\n"
- "failed to hint extents: %s (%d)\n"
- "failed to hint purgeable extents: %s (%d)\n"
- "failed to init device %s: %s (%d)\n"
- "failed to iterate purgeable extents on %s: %s (%d)\n"
- "failed to persist hints plist"
- "failed to persist hints plist\n"
- "failed to record event"
- "failed to record event\n"
- "failed to set hint extents activity state to DONE"
- "failed to set hint extents activity state to DONE\n"
- "failed to set hint extents activity state to DONE (PENDING_WORK)"
- "failed to set hint extents activity state to DONE (PENDING_WORK)\n"
- "failed to set up cache directory: %s (%d)\n"
- "fd_dev_close"
- "fd_dev_hint_flush"
- "fd_dev_read_extended"
- "fd_dev_read_helper"
- "fd_dev_write_extended"
- "found boot-arg %s=%lld\n"
- "fts_openbyid_"
- "fts_read_fd_"
- "hint_extents"
- "hints plist did not exist, creating new plist"
- "hints plist did not exist, creating new plist\n"
- "hit activity timeout, stopping activity"
- "hit activity timeout, stopping activity\n"
- "hit volume timeout, continuing to next volume"
- "hit volume timeout, continuing to next volume\n"
- "i20@?0^{?=QQ}8I16"
- "i8@?0"
- "iDiags"
- "ignoring invalid level"
- "ignoring invalid level\n"
- "image-format-read-only"
- "io_get_device_block_size"
- "io_get_device_features"
- "io_get_num_device_blocks"
- "iterate_purgeable_extents"
- "iterate_purgeable_extents_of_directory"
- "kern.rage_vnode"
- "lookup_jobj_in_snap"
- "make_purgeable_extents_iterator"
- "no boot-arg, defaulting to %s=%u\n"
- "none"
- "ordered"
- "persisted hints plist"
- "persisted hints plist\n"
- "purging_util.c"
- "start_state"
- "start_uptime"
- "state"
- "unknown"
- "urgencies"
- "xART"

```
