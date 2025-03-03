## MBHelperService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

```diff

-2349.80.25.0.0
-  __TEXT.__text: 0x122c4
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0xa4c
+2624.100.98.0.0
+  __TEXT.__text: 0x14000
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0xc4c
   __TEXT.__const: 0x220
-  __TEXT.__objc_methname: 0x23f8
-  __TEXT.__cstring: 0x3586
-  __TEXT.__objc_classname: 0x123
-  __TEXT.__objc_methtype: 0x709
-  __TEXT.__oslogstring: 0x1afe
+  __TEXT.__objc_methname: 0x2569
+  __TEXT.__cstring: 0x3a65
+  __TEXT.__objc_classname: 0x130
+  __TEXT.__objc_methtype: 0x747
+  __TEXT.__oslogstring: 0x1e9c
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x548
-  __DATA_CONST.__cfstring: 0x13c0
+  __TEXT.__unwind_info: 0x3a8
+  __DATA_CONST.__auth_got: 0x5d8
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x588
+  __DATA_CONST.__cfstring: 0x1500
   __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1150
-  __DATA.__objc_selrefs: 0xa78
+  __DATA.__objc_const: 0xec0
+  __DATA.__objc_selrefs: 0xb68
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x228
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1e0
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 359
-  Symbols:   273
-  CStrings:  1059
+  Functions: 391
+  Symbols:   286
+  CStrings:  1156
 
Symbols:
+ _MBSQLiteJournalSuffixes
+ _OBJC_CLASS_$_MBFileSystemSnapshot
+ _OBJC_METACLASS_$_MBFileSystemSnapshot
+ __DefaultRuneLocale
+ ___maskrune
+ _dlopen
+ _dlsym
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_retain_x27
+ _removefile_state_alloc
+ _removefile_state_free
+ _removefile_state_get
+ _removefile_state_set
+ _removefileat
- _MBDiagnoseGetNumberOfFileExtents
- _MBDiagnoseiCloudBackupFileAtPath
CStrings:
+ "%@%@"
+ "%@_CH"
+ "%u%c%u"
+ "%u-%c-%u"
+ "."
+ "/"
+ "/System/Library/Frameworks/IOKit.framework/IOKit"
+ "/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport"
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
+ "=diag= %s does not have associated crypto dstreams"
+ "=diag= %{public}s failed with %d at %{public}@"
+ "=diag= Dstream id %llu, dstream size %llu bytes"
+ "=diag= Dumping crypto file info"
+ "=diag= Extent offset %lld and length %lld"
+ "=diag= private_id: %llu"
+ "=diag= prot_class: %llu (explicit? %d)"
+ "@24@0:8r*16"
+ "AppleBaseband"
+ "B36@0:8i16@20^@28"
+ "B48@0:8@16d24^@32@?40"
+ "B56@0:8@16d24d32^@40@?48"
+ "CH"
+ "CPGetDeviceRegionCode"
+ "Cancelled while trying to unmount %@"
+ "D:"
+ "Failed to set Cx protection class, leaving as C on %@, error:%@"
+ "Failed to unmount %llu/%llu snapshots"
+ "IOServiceGetMatchingService"
+ "IOServiceMatching"
+ "Retrying unmount for %@ after EBUSY"
+ "Source file is 0 bytes, returning empty 0 byte file at %@"
+ "Timed out trying to unmount %@"
+ "Unmounted %llu mount points"
+ "_deleteSnapshotForVolume:name:error:"
+ "_diagnoseFile"
+ "_getNumberOfFileExtents"
+ "_openRawEncryptedWithPathFSR:error:"
+ "_purgeContentsAt:rPath:error:"
+ "_unmountWithRetry:startTime:timeout:error:cancelationHandler:"
+ "containsObject:"
+ "deleteAllSnapshotsAcrossVolumes:withPrefix:error:"
+ "fcntl error setting Cx protection class"
+ "hasSuffix:"
+ "initWithObjects:"
+ "kIOMainPortDefault"
+ "mb_backupIDByAddingCKPrefix"
+ "mb_backupIDByRemovingCKPrefix"
+ "mb_moveToTmpDirThenRemoveItemAtPath:error:"
+ "mb_pathComponentExistsInSet:"
+ "mb_pathHasSQLiteJournalSuffix"
+ "mb_stringByAppendingGreenteaSuffix"
+ "mb_stringByAppendingSlash"
+ "open_dprotected_np"
+ "removefileat() error"
+ "substringFromIndex:"
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
- "finfo->dstream_exists"
- "i32@0:8@16^@24"
- "mountSnapshotForVolume:name:mountPoint:error:"
- "openRawEncryptedWithPath:error:"
- "openRawEncryptedWithPathFSR:error:"

```
