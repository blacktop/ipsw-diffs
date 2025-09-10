## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x346dc
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__cstring: 0x8e50
+2236.102.1.0.0
+  __TEXT.__text: 0x35680
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__cstring: 0x8eee
   __TEXT.__const: 0xf0
-  __TEXT.__unwind_info: 0x668
-  __DATA_CONST.__auth_got: 0x3b0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__unwind_info: 0x6a4
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x290
-  __DATA_CONST.__cfstring: 0x120
-  __DATA.__data: 0x168
-  __DATA.__bss: 0x48
+  __DATA_CONST.__cfstring: 0x140
+  __DATA.__data: 0x160
+  __DATA.__bss: 0x4c
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: A3736E01-D771-3B2B-BF57-1EB31C2485D1
-  Functions: 506
-  Symbols:   129
-  CStrings:  777
+  UUID: ADBEA419-027A-3246-9B55-6D9292C2EB5A
+  Functions: 523
+  Symbols:   138
+  CStrings:  780
 
Symbols:
+ _APFSVolumeLock
+ _APFSVolumeUnlockUnlockRecordWithOptions
+ _CFDataCreate
+ _CFStringCreateWithCString
+ _CFStringGetCString
+ _IOConnectCallStructMethod
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetChildIterator
+ _IOServiceClose
+ _IOServiceOpen
+ _fsctl
+ _kIOMainPortDefault
+ _mach_task_self_
- _ffsctl
- _rmdir
- _unmount
- _uuid_unparse
CStrings:
+ "%s:%d: %s Couldn't find snap_meta for xid %llu: %d\n"
+ "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
+ "%s:%d: Crypto IO enable failed (error %d)\n"
+ "%s:%d: Failed to create password data reference for %s\n"
+ "%s:%d: Failed to dev init for volume %s error: %d\n"
+ "%s:%d: Failed to disable crypto io\n"
+ "%s:%d: Failed to get Container BSD name\n"
+ "%s:%d: Failed to get IO registry entry for given device path %s\n"
+ "%s:%d: Failed to get IOService object associated with %s for dev %s\n"
+ "%s:%d: Failed to unlock volume %s with supplied passphrase error = %d\n"
+ "%s:%d: Get parent object failed (error %d)\n"
+ "%s:%d: Invalid argument: container device is NULL\n"
+ "%s:%d: Invalid argument: device path is NULL\n"
+ "%s:%d: SETBIT for fsindex = %d \n"
+ "%s:%d: Volume %s is already unlocked\n"
+ "%s:%d: Volume lock failed for %s (error %d)\n"
+ "%s:%d: failed to open connection for multikey crypto i/o on device %s: %s\n"
+ "%s:%d: fs %d is FV but no password was given. Since '-U' was set, it will be copied as-is and a password will be required for it to be accessible\n"
+ "%s:%d: fsctl(APFSIOC_IS_VOL_LOCKED, %s) failed, error = %d\n"
+ "/"
+ "/dev/%ss%d"
+ "/dev/r%s"
+ "AppleAPFSContainer"
+ "AppleAPFSMedia"
+ "AppleAPFSSnapshot"
+ "BSD Name"
+ "container_find_and_unlock_encrypted_volumes"
+ "d:o:g:G:O:svtTUp:"
+ "destroy_slurper_context"
+ "extract_container_bsdname"
+ "multiKeyEncryption"
- "%s:%d:   fs %d is FV but no password was given. Since '-U' was set, it will be copied as-is and a password will be required for it to be accessible\n"
- "%s:%d: %s %s%sencrypted fs %d\n"
- "%s:%d: %s Couldn't find snap_meta for xid %llu\n"
- "%s:%d: %s expanded record found on unsupported volume\n"
- "%s:%d: %s failed to update chunk for alloc zone %llu: %d\n"
- "%s:%d: Can't figure out tweak for fext obj_id %lld paddr %lld, err %d\n"
- "%s:%d: failed to create path for apfs mount, error = %d\n"
- "%s:%d: failed to read data (block #%lld, len #%lld), result %lld, err %d\n"
- "%s:%d: failed to set crypto tweak for fext obj_id %lld paddr %lld, error %d\n"
- "%s:%d: find_next_snapshot returned err %d, aborting!\n"
- "%s:%d: mount_apfs failed with error %d (launch error %d)\n"
- "%s:%d: slurper conversion context failed for volume %s (fs %d), error = %d\n"
- "%s:%d: slurper conversion context failed for volume %s (fs %d), error = %d, skipping ...\n"
- "-c"
- "-o"
- "/dev/r"
- "/sbin/mount_apfs"
- "/tmp/%s_%d_mnt"
- "FV-"
- "Slurping metadata of"
- "Transcribing"
- "d:m:o:g:G:O:svtTUp:"
- "jobj_type_from_possibly_large_key"
- "mount_apfs"
- "mount_for_slurper"
- "rdonly"
- "un-"
- "wr_decode_fs_root_iterator"
- "write_decode_enc_fs_file_extents"

```
