## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2317.82.1.0.0
-  __TEXT.__text: 0x333d8
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__cstring: 0x6643
-  __TEXT.__const: 0x338
-  __TEXT.__oslogstring: 0x12b6
-  __TEXT.__unwind_info: 0x628
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x6e0
-  __DATA_CONST.__cfstring: 0xc80
-  __DATA.__data: 0x98
+2332.100.75.502.1
+  __TEXT.__text: 0x36528
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__const: 0x390
+  __TEXT.__cstring: 0x7091
+  __TEXT.__oslogstring: 0x1637
+  __TEXT.__unwind_info: 0x6a0
+  __DATA_CONST.__auth_got: 0x5f8
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__cfstring: 0xda0
+  __DATA.__data: 0x150
   __DATA.__bss: 0x38
   __DATA.__common: 0x64
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 547
-  Symbols:   188
-  CStrings:  777
+  Functions: 598
+  Symbols:   217
+  CStrings:  876
 
Symbols:
+ _CFBooleanGetValue
+ _CFEqual
+ _CFStringGetTypeID
+ _IOObjectRetain
+ _IORegistryEntryGetParentIterator
+ _aio_error
+ _aio_read
+ _aio_return
+ _aio_suspend
+ _cc_clear
+ _ccdigest_init
+ _ccdigest_update
+ _ccsha3_256_di
+ _ccsha3_384_di
+ _ccsha3_512_di
+ _close
+ _fcntl
+ _fstatfs
+ _fsync
+ _fts_close
+ _fts_open
+ _fts_read
+ _getmntinfo_r_np
+ _ioctl
+ _open
+ _os_parse_boot_arg_int
+ _pread
+ _pwrite
+ _strndup
CStrings:
+ "%#16llx %#10llx\n"
+ "%16s %10s\n"
+ "%s/apfs"
+ "%s/apfs_data"
+ "%s/nx"
+ "%s:%d: Couldn't fstat dev_fd (%d), err %d dev_name = %s\n"
+ "%s:%d: Hit an error flushing the cache, %d dev_name = %s\n"
+ "%s:%d: Hit an error flushing the hint list, %d dev_name = %s\n"
+ "%s:%d: blknum %lld size %zu blksize %u invalid, dev_name = %s\n"
+ "%s:%d: blknum 0x%llx size %zu, error %d dev_name = %s\n"
+ "%s:%d: can't get block count (%s)\n"
+ "%s:%d: can't get features for device (%s)\n"
+ "%s:%d: can't get solidstate for device (%s)\n"
+ "%s:%d: can't get the device block size (%s). assuming 512\n"
+ "%s:%d: failed to open apfs/nx special devices ['%s'(%d) / '%s'(%d) / '%s'(%d)] - err %d (%s) dev_name = '%s'\n"
+ "%s:%d: failed to open container device %s: %s\n"
+ "%s:%d: failed to open volume device %s: %s\n"
+ "%s:%d: failed to read blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n"
+ "%s:%d: failed to write blknum 0x%llx size %zu flags 0x%x error %d dev_name = %s\n"
+ "%s:%d: fd %d is type %o rdev %d (%d, %d): I/O registry entry not found\n"
+ "%s:%d: hinting %d blocks from hint_list failed w/: %d (entry %lld:%lld ; %lld:%lld)\n"
+ "%s:%d: open %s hit EBUSY, attempts remaining: %u dev_name = %s\n"
+ "/var/mobile/Library/Caches/com.apple.apfs_iosd.hints.plist"
+ "BSD Major"
+ "BSD Minor"
+ "DEFERRING hint extents activity"
+ "DEFERRING hint extents activity\n"
+ "DONE: Suspending hint extents activity until next interval"
+ "DONE: Suspending hint extents activity until next interval\n"
+ "Device Characteristics"
+ "Failed to initialize dispatch queue for hint extents activity"
+ "Failed to initialize dispatch queue for hint extents activity\n"
+ "IOBlockStorageDevice"
+ "IOMedia"
+ "Internal"
+ "LENGTH"
+ "OFFSET"
+ "Physical Interconnect Location"
+ "Protocol Characteristics"
+ "Removable"
+ "START: Initiating hint extents activity"
+ "START: Initiating hint extents activity\n"
+ "Target Disk Mode"
+ "UNREGISTERING hint extents activity"
+ "UNREGISTERING hint extents activity\n"
+ "Volume: %s Cursor: %llu\n"
+ "_fd_dev_write"
+ "activity is disabled because no volume supports iteration"
+ "activity is disabled because no volume supports iteration\n"
+ "activity is disabled because of level"
+ "activity is disabled because of level\n"
+ "apfs_hint_extents_level"
+ "com.apple.filesystems.apfs_iosd.hint_extents"
+ "com.apple.filesystems.apfs_iosd_hint_extents"
+ "dev_init"
+ "dev_init_common"
+ "failed to create hints plist URL"
+ "failed to create hints plist URL\n"
+ "failed to create new plist"
+ "failed to create new plist\n"
+ "failed to get mount info: %s (%d)\n"
+ "failed to hint extents: %s (%d)\n"
+ "failed to hint purgeable extents: %s (%d)\n"
+ "failed to init device %s: %s (%d)\n"
+ "failed to iterate purgeable extents on %s: %s (%d)\n"
+ "failed to persist hints plist"
+ "failed to persist hints plist\n"
+ "failed to set hint extents activity state to DEFER"
+ "failed to set hint extents activity state to DEFER\n"
+ "failed to set hint extents activity state to DONE"
+ "failed to set hint extents activity state to DONE\n"
+ "fd_dev_close"
+ "fd_dev_hint_flush"
+ "fd_dev_read_extended"
+ "fd_dev_read_helper"
+ "fd_dev_write_extended"
+ "found boot-arg %s=%lld\n"
+ "hints plist did not exist, creating new plist"
+ "hints plist did not exist, creating new plist\n"
+ "i20@?0^{?=QQ}8I16"
+ "ignoring invalid level"
+ "ignoring invalid level\n"
+ "image-format-read-only"
+ "io_get_device_block_size"
+ "io_get_device_features"
+ "io_get_num_device_blocks"
+ "persisted hints plist"
+ "persisted hints plist\n"
+ "spaceman_alloc_iterate_chunks"

```
