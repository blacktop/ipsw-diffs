## MBHelperService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0x122c4
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0xa4c
+2624.100.67.0.0
+  __TEXT.__text: 0x139a0
+  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__objc_stubs: 0x1f20
+  __TEXT.__objc_methlist: 0xbf4
   __TEXT.__const: 0x220
-  __TEXT.__objc_methname: 0x23f8
-  __TEXT.__cstring: 0x3586
+  __TEXT.__objc_methname: 0x2496
+  __TEXT.__cstring: 0x38f5
   __TEXT.__objc_classname: 0x123
-  __TEXT.__objc_methtype: 0x709
-  __TEXT.__oslogstring: 0x1afe
+  __TEXT.__objc_methtype: 0x74a
+  __TEXT.__oslogstring: 0x1e29
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x380
+  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x548
-  __DATA_CONST.__cfstring: 0x13c0
+  __DATA_CONST.__cfstring: 0x1440
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1150
-  __DATA.__objc_selrefs: 0xa78
+  __DATA.__objc_const: 0xe80
+  __DATA.__objc_selrefs: 0xb20
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x228

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 359
-  Symbols:   273
-  CStrings:  1059
+  Functions: 381
+  Symbols:   281
+  CStrings:  1130
 
Symbols:
+ _OBJC_CLASS_$_MBFileSystemSnapshot
+ _OBJC_METACLASS_$_MBFileSystemSnapshot
+ __DefaultRuneLocale
+ ___maskrune
+ _objc_retain_x27
+ _removefile_state_alloc
+ _removefile_state_free
+ _removefile_state_get
+ _removefile_state_set
+ _removefileat
- _MBDiagnoseGetNumberOfFileExtents
- _MBDiagnoseiCloudBackupFileAtPath
CStrings:
+ "%u%c%u"
+ "%u-%c-%u"
+ "."
+ "=diag=       0x%llx:+%lld (crid %llu)"
+ "=diag=       class:   %#x"
+ "=diag=       exists?  %u"
+ "=diag=       flags:   %#x"
+ "=diag=       len:     %u"
+ "=diag=       os:      %@"
+ "=diag=       payload: %u (trunc? %d)"
+ "=diag=       refcnt:  %u"
+ "=diag=       rev:     %u"
+ "=diag=       version: %u.%u"
+ "=diag=     class:   %#x"
+ "=diag=     exists?  %u"
+ "=diag=     flags:   %#x"
+ "=diag=     len:     %u"
+ "=diag=     os:      %@"
+ "=diag=     payload: %u (trunc? %d)"
+ "=diag=     refcnt:  %u"
+ "=diag=     rev:     %u"
+ "=diag=     version: %u.%u"
+ "=diag=   alloced_size: %llu"
+ "=diag=   default_crid: %llu"
+ "=diag=   num extents:  %u"
+ "=diag=   refcnt:       %u"
+ "=diag=   size:         %llu"
+ "=diag= %{public}s failed with %d at %{public}@"
+ "=diag= Dstream id %llu, dstream size %llu bytes"
+ "=diag= Dumping crypto file info"
+ "=diag= Extent offset %lld and length %lld"
+ "=diag= private_id: %llu"
+ "=diag= prot_class: %llu (explicit? %d)"
+ "B36@0:8i16@20^@28"
+ "B48@0:8@16d24^@32@?40"
+ "B56@0:8@16d24d32^@40@?48"
+ "Cancelled while trying to unmount %@"
+ "Failed to unmount %llu/%llu snapshots"
+ "Retrying unmount for %@ after EBUSY"
+ "Source file is 0 bytes, returning empty 0 byte file at %@"
+ "Timed out trying to unmount %@"
+ "Unmounted %llu mount points"
+ "_deleteSnapshotForVolume:name:error:"
+ "_diagnoseFile"
+ "_getNumberOfFileExtents"
+ "_purgeContentsAt:rPath:error:"
+ "_unmountWithRetry:startTime:timeout:error:cancelationHandler:"
+ "deleteAllSnapshotsAcrossVolumes:withPrefix:error:"
+ "mb_moveToTmpDirThenRemoveItemAtPath:error:"
+ "open_dprotected_np"
+ "removefileat() error"
+ "unmount:timeout:error:cancelationHandler:"
+ "write"
- "=diag= Dstream id %llu, dstream size %llu bytes\n"
- "=diag= Extent offset %lld and length %lld\n"
- "=diag= crypto_id %llu key_class %u, os_vers 0x%x, rev %hu, len %hu"
- "=diag= offset %lld:length %llu, id %lld"
- "Invalid file size (0)"
- "MBDiagnoseFile"
- "MBDiagnoseGetNumberOfFileExtents"
- "No mountpoint specified at which to mount the snapshot"
- "_purgeContentsAt:error:"
- "deleteSnapshotForVolume:name:error:"
- "mountSnapshotForVolume:name:mountPoint:error:"

```
